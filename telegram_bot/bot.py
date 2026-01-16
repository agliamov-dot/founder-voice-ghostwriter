import logging
import os
from dataclasses import dataclass, field
from typing import Dict, List

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

(
    TOPIC,
    AUDIENCE,
    THESIS,
    PLATFORM,
    VOICE_SAMPLE_ONE,
    VOICE_SAMPLE_TWO,
    EXPERIENCE,
    SPECIFICS,
    HONESTY,
    STORY,
    REFINEMENT,
) = range(11)


@dataclass
class DraftContext:
    topic: str = ""
    audience: str = ""
    thesis: str = ""
    platform: str = ""
    voice_samples: List[str] = field(default_factory=list)
    experience: str = ""
    specifics: str = ""
    honesty: str = ""
    story: str = ""
    refinement: str = ""


CONTEXT_KEY = "draft_context"


def get_context(user_data: Dict) -> DraftContext:
    if CONTEXT_KEY not in user_data:
        user_data[CONTEXT_KEY] = DraftContext()
    return user_data[CONTEXT_KEY]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data.pop(CONTEXT_KEY, None)
    intro = (
        "Привет! Я помогу превратить твой опыт в аутентичный текст. "
        "Сначала разберёмся с темой.\n\n"
        "1) О чём статья?"
    )
    await update.message.reply_text(intro)
    return TOPIC


async def collect_topic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    draft_context = get_context(context.user_data)
    draft_context.topic = update.message.text.strip()
    await update.message.reply_text("2) Кто целевая аудитория?")
    return AUDIENCE


async def collect_audience(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    draft_context = get_context(context.user_data)
    draft_context.audience = update.message.text.strip()
    await update.message.reply_text("3) Какой главный тезис или угол зрения?")
    return THESIS


async def collect_thesis(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    draft_context = get_context(context.user_data)
    draft_context.thesis = update.message.text.strip()
    await update.message.reply_text("4) Для какой платформы (блог, LinkedIn и т.д.)?")
    return PLATFORM


async def collect_platform(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    draft_context = get_context(context.user_data)
    draft_context.platform = update.message.text.strip()
    prompt = (
        "Теперь нужно откалибровать голос.\n"
        "5) Пришли 1-й пример текста (свой или чужой, который нравится)."
    )
    await update.message.reply_text(prompt)
    return VOICE_SAMPLE_ONE


async def collect_voice_sample_one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    draft_context = get_context(context.user_data)
    draft_context.voice_samples.append(update.message.text.strip())
    await update.message.reply_text("6) Пришли 2-й пример текста (опционально, но желательно).")
    return VOICE_SAMPLE_TWO


async def collect_voice_sample_two(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    draft_context = get_context(context.user_data)
    sample_text = update.message.text.strip()
    if sample_text:
        draft_context.voice_samples.append(sample_text)
    await update.message.reply_text(
        "Переходим к интервью.\n"
        "7) Какой у тебя личный опыт по этой теме?"
    )
    return EXPERIENCE


async def collect_experience(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    draft_context = get_context(context.user_data)
    draft_context.experience = update.message.text.strip()
    await update.message.reply_text("8) Дай конкретику: цифры, даты, проценты, примеры.")
    return SPECIFICS


async def collect_specifics(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    draft_context = get_context(context.user_data)
    draft_context.specifics = update.message.text.strip()
    await update.message.reply_text(
        "9) Где конкуренты сильнее? Какие честные trade-offs?"
    )
    return HONESTY


async def collect_honesty(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    draft_context = get_context(context.user_data)
    draft_context.honesty = update.message.text.strip()
    await update.message.reply_text(
        "10) Расскажи конкретную историю или момент, когда ты понял(а) главное."
    )
    return STORY


async def collect_story(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    draft_context = get_context(context.user_data)
    draft_context.story = update.message.text.strip()
    draft = build_draft_summary(draft_context)
    await update.message.reply_text(
        "Черновик-черновик готов. Посмотри и скажи, что поправить.\n\n"
        f"{draft}",
        parse_mode=ParseMode.MARKDOWN,
    )
    return REFINEMENT


async def collect_refinement(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    draft_context = get_context(context.user_data)
    draft_context.refinement = update.message.text.strip()
    prompt = build_prompt(draft_context)
    await update.message.reply_text(
        "Спасибо! Вот готовый промпт, который можно отправить в LLM, "
        "чтобы получить полноценный текст:\n\n"
        f"```\n{prompt}\n```",
        parse_mode=ParseMode.MARKDOWN,
    )
    return ConversationHandler.END


def build_draft_summary(draft_context: DraftContext) -> str:
    voice_notes = "\n".join(
        f"- Пример {index}: {sample[:200]}" for index, sample in enumerate(draft_context.voice_samples, start=1)
    )
    if not voice_notes:
        voice_notes = "- Примеры не предоставлены"
    summary = (
        "*Сводка по вводным данным*\n"
        f"*Тема:* {draft_context.topic}\n"
        f"*Аудитория:* {draft_context.audience}\n"
        f"*Тезис:* {draft_context.thesis}\n"
        f"*Платформа:* {draft_context.platform}\n\n"
        "*Калибровка голоса:*\n"
        f"{voice_notes}\n\n"
        "*Интервью:*\n"
        f"- Опыт: {draft_context.experience}\n"
        f"- Конкретика: {draft_context.specifics}\n"
        f"- Честность: {draft_context.honesty}\n"
        f"- История: {draft_context.story}\n"
    )
    return summary


def build_prompt(draft_context: DraftContext) -> str:
    voice_section = "\n\n".join(draft_context.voice_samples) if draft_context.voice_samples else ""
    prompt = (
        "Ты пишешь статью в голосе автора.\n"
        "Используй стиль и ритм из примеров, не добавляй клише, начинай с конкретной истории.\n\n"
        f"Тема: {draft_context.topic}\n"
        f"Аудитория: {draft_context.audience}\n"
        f"Тезис: {draft_context.thesis}\n"
        f"Платформа: {draft_context.platform}\n\n"
        f"Опыт автора: {draft_context.experience}\n"
        f"Конкретика: {draft_context.specifics}\n"
        f"Честность: {draft_context.honesty}\n"
        f"Ключевая история: {draft_context.story}\n\n"
        f"Примеры стиля (для калибровки):\n{voice_section}\n\n"
        f"Правки от автора: {draft_context.refinement}\n\n"
        "Сформируй черновик 800-1200 слов. Избегай списков типа '7 способов', "
        "суперлативов и шаблонных CTA. Заверши естественным приглашением к диалогу."
    )
    return prompt


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Диалог остановлен. Если нужно начать заново — /start.")
    return ConversationHandler.END


def main() -> None:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("Set TELEGRAM_BOT_TOKEN environment variable.")

    application = Application.builder().token(token).build()

    conversation = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            TOPIC: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_topic)],
            AUDIENCE: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_audience)],
            THESIS: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_thesis)],
            PLATFORM: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_platform)],
            VOICE_SAMPLE_ONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_voice_sample_one)],
            VOICE_SAMPLE_TWO: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_voice_sample_two)],
            EXPERIENCE: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_experience)],
            SPECIFICS: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_specifics)],
            HONESTY: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_honesty)],
            STORY: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_story)],
            REFINEMENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_refinement)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conversation)
    application.add_handler(CommandHandler("cancel", cancel))

    logger.info("Bot started")
    application.run_polling()


if __name__ == "__main__":
    main()

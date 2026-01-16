# Founder Voice Ghostwriter

An [Agent Skill](https://agentskills.io) for founders who need content but don't want generic SEO agency output.

## The Problem

You know you need to do SEO, write articles, thought leadership. Your options:

1. **Hire an SEO agency** → Get generic "7 Ways to..." articles without your voice
2. **Hire a PR agency** → Expensive, scheduling interviews, waiting for content

## A Third Option

You're browsing LinkedIn late at night. You spot an article that resonates—the voice, the specifics, the honesty. You have your own take on the topic from your experience.

Open Claude Code (or any agent supporting the [Agent Skills standard](https://agentskills.io)), say: "Here's an article I like the style of. I have things to say on this topic. Let's create something."

The interview starts—like with a PR agency, but right now:
- "What's your experience with this?"
- "Give me specific numbers"
- "What didn't work?"

And you can simultaneously:
- Pull data from your analytics
- Research competitors
- Check best practices
- Look up a customer's website for examples

All in the moment. When you have inspiration and things to say—not when a PR manager found a slot in their calendar.

## Installation

```bash
git clone https://github.com/bayramannakov/founder-voice-ghostwriter.git ~/.claude/skills/founder-voice-ghostwriter
```

Works with any agent supporting the Agent Skills standard—Claude Code is just one of them.

## Telegram Bot (guided interview)

You can run the same interview flow as a Telegram bot that collects inputs and produces a ready-to-use prompt.

### Requirements

- Python 3.10+
- A Telegram bot token (from [@BotFather](https://t.me/botfather))

### Setup

```bash
cd telegram_bot
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export TELEGRAM_BOT_TOKEN="your-telegram-token"
python bot.py
```

### Usage

1. Open your bot and run `/start`.
2. Answer the guided questions (topic, audience, voice samples, interview questions).
3. The bot returns a draft summary and a final prompt you can paste into any LLM.

## The Process

```
1. VOICE CALIBRATION
   Share articles you like → AI learns your style

2. INTERVIEW EXTRACTION
   Your stories. Your numbers. Your failures.

3. DRAFTING
   Story-driven, specific, honest
   Matches your calibrated voice

4. REFINEMENT
   Your feedback → targeted edits
```

## What It Won't Do

This won't "10x your SEO" or "revolutionize your content strategy."

What it will do: make it easier to get your voice out there. Maybe even help you find it—because the first step is showing what you like.

## Key Principles

- **Lead with stories** - "I was reviewing logs late one night..." not "AI is transforming..."
- **Real specifics** - "10-15%" not "many"
- **Acknowledge competitors** - Honesty builds trust
- **Dialogue, not sales** - "Find me on LinkedIn" not "Book a demo today!"

## Files

```
founder-voice-ghostwriter/
├── SKILL.md                 # Main skill instructions
├── references/
│   └── voice-guide.md       # Detailed patterns & examples
├── telegram_bot/
│   ├── bot.py               # Telegram bot flow
│   └── requirements.txt     # Bot dependencies
└── README.md
```

## About

Created by [Bayram Annakov](https://linkedin.com/in/bayramannakov) while building [Onsa.ai](https://onsa.ai) - AI agents for B2B sales prospecting.

If you find this useful, say hi on LinkedIn!

## License

MIT

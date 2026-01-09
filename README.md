# Founder Voice Ghostwriter

An [Agent Skill](https://agentskills.io) for collaborative ghostwriting that extracts first-hand founder knowledge and transforms it into authentic, non-AI-sounding content.

## What It Does

This skill guides AI agents through a structured interview process to:

1. **Calibrate to your voice** - Analyzes articles you've written or admire to understand your style
2. **Extract your knowledge** - Asks specific questions to pull out real numbers, stories, and experiences
3. **Draft in your voice** - Writes content that sounds like you, not like AI
4. **Refine together** - Iterates based on your feedback

## Why I Built This

I was working with Claude to write SEO content for [Onsa.ai](https://onsa.ai). The first drafts were... fine. Generic. Obviously AI-generated.

Then something clicked. Instead of asking Claude to write, I had it interview me. Extract the real stories. The specific numbers. The honest tradeoffs.

The result was content that sounded like me—because it was built from my actual experiences.

This skill packages that process so other founders can use it.

## Installation

### For Claude Code users

Add to your `~/.claude/skills/` directory:

```bash
git clone https://github.com/bayramannakov/founder-voice-ghostwriter.git ~/.claude/skills/founder-voice-ghostwriter
```

### For other Agent Skill platforms

Copy `SKILL.md` and the `references/` folder to your skills directory.

## Usage

Just ask Claude to help you write something:

- "Help me write a blog post about [topic]"
- "I need to write a comparison page for my product"
- "Make this draft sound more like me"

The skill will guide you through the interview process.

## The Process

```
┌─────────────────────────────────────────┐
│  1. CONTEXT                             │
│  What are you writing? For whom?        │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│  2. VOICE CALIBRATION                   │
│  Share articles you're proud of         │
│  → AI learns your patterns              │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│  3. INTERVIEW EXTRACTION                │
│  Real numbers. Real stories.            │
│  What surprised you? What failed?       │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│  4. DRAFT                               │
│  Story-driven, specific, honest         │
│  Matches your calibrated voice          │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│  5. REFINE                              │
│  Your feedback → targeted edits         │
└─────────────────────────────────────────┘
```

## Key Principles

- **Lead with stories, not abstractions** - "I was reviewing logs late one night..." not "AI is transforming..."
- **Include real specifics** - "10-15%" not "many", "Swiss salary registry" not "public data"
- **Acknowledge competitor strengths** - Honesty builds trust
- **End with dialogue, not sales** - "Find me on LinkedIn" not "Book a demo today!"

## Files

```
founder-voice-ghostwriter/
├── SKILL.md                 # Main skill instructions
├── references/
│   └── voice-guide.md       # Detailed patterns & examples
└── README.md                # This file
```

## Examples

See the `references/voice-guide.md` for before/after examples showing the transformation from generic AI content to authentic founder voice.

## About

Created by [Bayram Annakov](https://linkedin.com/in/bayramannakov) while building [Onsa.ai](https://onsa.ai) - AI agents for B2B sales prospecting.

If you find this useful, say hi on LinkedIn!

## License

MIT

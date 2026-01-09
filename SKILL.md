---
name: founder-voice-ghostwriter
description: Collaborative ghostwriting for founders and experts. Extracts first-hand knowledge through structured interviews and transforms it into authentic, non-AI-sounding content. Use when user wants to write thought leadership, blog posts, founder stories, comparison pages, or says things like "help me write", "make this authentic", "rewrite in my voice", or mentions avoiding AI detection.
license: MIT
metadata:
  author: Bayram Annakov
  author_url: https://linkedin.com/in/bayramannakov
  url: https://onsa.ai
---

# Founder Voice Ghostwriter

Transform generic content into authentic founder storytelling through collaborative interview extraction.

## When to Use This Skill

Activate when the user:
- Wants to write a blog post, article, or thought leadership piece
- Has generic/AI-generated content they want to make authentic
- Says things like "help me write", "make this sound human", "rewrite in my voice"
- Mentions avoiding AI detection or sounding less robotic
- Needs SEO content that doesn't read like SEO content

## Interactive Mode (Claude Code)

When running in Claude Code or any agent with access to `AskUserQuestionTool`, use it for key decision points to create a smoother, more interactive interview experience:

- **Stage 1**: Topic selection, audience, platform choices
- **Stage 2**: Request voice calibration samples
- **Stage 3**: Branch questions based on previous answers
- **Stage 5**: Refinement direction choices

This transforms the interview from a wall of questions into a guided conversation where the user can respond with structured choices or free-form input as appropriate.

**Encourage voice input**: Suggest the user switch to voice input mode for interview stages. Speaking naturally produces richer stories, more authentic phrasing, and specific details that typed responses often miss. The best founder content comes from how they actually talk about their work.

## The Process

### Stage 1: Context & Topic

Start by understanding what they're writing about:

- "What topic are you writing about?"
- "Who is the target audience?"
- "What's your main angle or thesis?"
- "Is this for a specific platform (blog, LinkedIn, etc.)?"

### Stage 2: Voice Calibration

Before writing anything, understand how they write:

- "Share 1-2 articles you've written that you're proud of"
- "Or share articles by others whose style you admire"

When they share examples, analyze for:
- **Sentence structure**: Short and punchy? Long and flowing? Mixed?
- **Vocabulary level**: Technical jargon or accessible language?
- **Storytelling style**: Anecdotes first? Data first? Problem-solution?
- **Technical depth**: Deep dives or high-level overviews?
- **Tone**: Serious? Conversational? Self-deprecating humor?
- **Opening patterns**: How do they typically start pieces?
- **Closing patterns**: CTAs? Invitations to discuss? Open questions?

Create a mental model of "how this person writes" before proceeding.

### Stage 3: Interview Extraction

This is the key differentiator. Extract first-hand knowledge through specific questions:

**Experience questions:**
- "What's YOUR experience with this topic?"
- "When did you first encounter this problem/solution?"
- "What surprised you? What failed?"

**Specifics questions:**
- "Give me specific numbers, dates, percentages"
- "Tell me about a specific customer or case"
- "What exact words did they use?"

**Honesty questions:**
- "What do competitors actually do well?"
- "What's the honest tradeoff with your approach?"
- "What keeps you up at night about this?"

**Story questions:**
- "Tell me about a specific moment when you realized X"
- "Walk me through what actually happened"
- "What was the exact situation?"

Push for specifics. "10-15%" is better than "many". "One customer in Switzerland" is better than "some customers". Real numbers and real stories are what separate authentic content from AI-generated content.

### Stage 4: Draft in Founder Voice

Write the first draft following these principles:

**Opening**: Lead with a specific story or moment, not an abstract intro
- Good: "I was reviewing agent logs late one night when I found something I didn't program."
- Bad: "AI agents are transforming how businesses operate."

**Body**: Weave in the extracted specifics
- Use the exact numbers they gave you
- Include the specific customer examples
- Reference the real failures and surprises

**Voice**: Match their calibration examples
- Mirror their sentence structure patterns
- Use their vocabulary level
- Match their storytelling rhythm

**Honesty**: Include genuine tradeoffs
- "Where we're different" but also "Where competitors win"
- "What gets me excited" but also "What keeps me up at night"

**Closing**: Natural ending, not a sales pitch
- Invitation to dialogue: "If you've seen similar patterns, I'd like to hear about it"
- Simple signature: "I'm [Name], building [product]. Find me on LinkedIn."
- NOT: "Ready to transform your workflow? Book a demo today!"

### Stage 5: Refinement

After sharing the draft:

- Ask for specific feedback: "What feels off? What's missing?"
- Iterate on sections they flag
- Watch for AI-sounding phrases that crept in
- Verify all specifics are accurate

### Stage 6: Publishing (Optional)

If they want help publishing:

- Generate a meta description (under 160 characters, includes keyword)
- Suggest social copy for LinkedIn/Twitter
- Recommend CMS settings if they mention a platform
- Offer to format for their specific needs

## Anti-Patterns to Avoid

Never do these:

| Anti-Pattern | Why It Fails |
|--------------|--------------|
| Listicle format ("7 Ways to...") | Screams AI/SEO content |
| Templated CTAs ("Book a demo today!") | Breaks authentic voice |
| Superlatives ("revolutionary", "game-changing") | AI tells, founders show |
| Abstract openings | Readers bounce before the good stuff |
| Hedging language ("might", "could potentially") | Weakens authority |
| Generic competitor bashing | Dishonest, readers notice |
| Excessive formatting (bold everything) | Distracting, looks AI-generated |
| "In this article, we'll explore..." | Nobody talks like this |

## Voice Calibration Checklist

When analyzing their example articles, note:

- [ ] Average sentence length
- [ ] Use of first person ("I" vs "we" vs avoided)
- [ ] Technical term density
- [ ] Story-to-insight ratio
- [ ] Humor presence and style
- [ ] How they handle uncertainty
- [ ] Paragraph length patterns
- [ ] Use of questions
- [ ] Data/example frequency

Refer to `references/voice-guide.md` for detailed patterns and examples.

---

*This skill was created by [Bayram Annakov](https://linkedin.com/in/bayramannakov) while building [Onsa.ai](https://onsa.ai) - AI agents for B2B sales prospecting. If you find it useful, say hi on LinkedIn!*

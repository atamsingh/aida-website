# Blog post brief (shared by all posts)

You are drafting ONE blog post for the website of AIDA Consulting Solutions, an AI and
data consultancy in Ottawa, Canada, run by Atam Singh. The post is published under
Atam's name, so write in the first person singular ("I"), as an experienced practitioner
talking to a business owner. Atam will review it before it goes live.

## Reader
An owner, general manager or operations lead at a small or medium-sized business
(roughly 10 to 250 people). Smart, busy, not technical. Has no data team and no AI team.
They use spreadsheets, an accounting package, a CRM, email and shared drives.
Do NOT write sentences that restrict who the advice is for ("this is only for small
businesses"); just use examples such a reader recognises (quotes, invoices, customer
lists, the Monday report, the staff handbook).

## Voice
- Plain, direct, concrete. Short paragraphs (2 to 4 sentences). Canadian spelling.
- Explain any technical term the first time in one short clause, or avoid it.
- No hype, no "in today's fast-paced world", no "game-changer", no emoji, no rhetorical
  question chains. Avoid em dashes; use commas, colons or full stops.
- Give the reader something they can act on this week.
- Honest about limits: say when AI is the wrong tool.

## Facts: what you may and may not use
- Do NOT invent statistics, studies, client names, client stories, prices, timelines or
  quotes. Do NOT do web research. Use only the facts supplied in this brief and in your
  task prompt, plus general, uncontroversial explanations of how the technology works.
- Atam's background (usable, but keep anecdotes UNATTRIBUTED: say "on one project",
  "at a large e-commerce company", "inside a federal department"; never name an
  employer in an anecdote and never claim AIDA client work):
  - 10+ years building data and AI systems.
  - Built an internal retrieval chatbot that gave senior leaders context-specific
    answers from internal information with minimal manual work.
  - Led the build of AI software that interprets lab results for practitioners, using
    retrieval (RAG), agent workflows, human-in-the-loop review and "LLM judges"
    (a second AI model that grades answers); thousands of results processed in production.
  - Built the first dashboard for a government department that replaced weekly funding
    reports which had been printed and mailed.
  - Built a tool monitoring a business's "vital signs": 3.2 million time-series data
    points a day, used by more than 3,500 people.
  - Built an address standardisation pipeline that found duplicate addresses, which
    helped with fraud detection.
  - Built a data quality framework: 200+ automated monitoring rules across 30+ datasets.
  - Re-engineered a critical pipeline (80 million rows an hour) to run 3 times faster.
  - Automated cloud cost auditing that saved roughly $1M.
  - Led an effort to bring 5 petabytes of unstructured data into privacy compliance,
    and built data systems under Canada/US data-residency restrictions.
- Verified statistics you may cite (link the source inline with an <a> tag):
  - Statistics Canada, Canadian Survey on Business Conditions, Q3 2026
    (https://www150.statcan.gc.ca/n1/daily-quotidien/260831/dq260831a-eng.htm):
    25.2% of Canadian businesses plan to use AI in the next 12 months, up from 14.5% a
    year earlier and 10.6% the year before. 52.7% have no plans. Of those with no plans,
    79.1% say AI is not relevant to what they do, 10.8% cite privacy or security
    concerns, 9.9% cite a lack of knowledge about what AI can do.
  - Gartner, Feb 2025
    (https://www.gartner.com/en/newsroom/press-releases/2025-02-26-lack-of-ai-ready-data-puts-ai-projects-at-risk):
    predicts that through 2026 organisations will abandon 60% of AI projects not
    supported by AI-ready data; 63% of organisations do not have, or are unsure they
    have, the right data management practices for AI (survey of 1,203 data leaders).
- Where a real detail from Atam would make the post better (a specific story, a number,
  a tool name he prefers), do not invent it. Insert a visible marker instead:
  `<mark class="todo">[ATAM: what you need from him]</mark>`. Use at most three.

## How AIDA works (you may reference, briefly, near the end only)
Every engagement starts with a conversation, then a short assessment with a fixed scope
and a fixed fee quoted before work starts. No prices or durations are published.

## Output format (strict)
Write ONE file, at the exact path given in your task prompt. It must be an HTML
FRAGMENT, not a full page:
- No <html>, <head>, <body>, <h1>, <style>, <script>, images, tables or inline styles.
  The site template adds the title, author, date and a contact call-to-action.
- Allowed tags only: <p>, <h2>, <h3>, <ul>, <ol>, <li>, <strong>, <em>, <a>,
  <blockquote>, <mark class="todo">.
- First element: `<p class="lead">…</p>`, one or two sentences that state the point.
- Then 4 to 6 sections, each starting with an <h2> (sentence case, no colon-heavy titles).
- Last section: an <h2> such as "What to do this week" with 3 to 5 concrete steps.
- Length: 850 to 1,100 words of body text.
- Internal links (use these exact relative URLs, sparingly, 2 to 4 per post):
  ../../small-business/  ../../ai-consulting/  ../../ai-agents/  ../../data-engineering/
  ../../ai-ready-data/  and other posts at ../SLUG/ using the slugs below.
- External links: only the two source URLs above, with target="_blank" rel="noopener".
- Use real typographic apostrophes and quotes (’ “ ”) or plain ones consistently; escape
  & as &amp;.

## The six posts in this series (slug: title)
- chatbot-that-knows-your-business: A chatbot that actually knows your business
- weekly-report-that-builds-itself: The weekly report that builds itself
- three-versions-of-every-customer: Why you have three versions of every customer
- why-ai-projects-fail: Why most AI projects fail, and the boring fix
- is-your-business-ready-for-ai: Five signs your business is ready for AI, and three signs it isn’t
- is-your-data-safe-with-ai: Is your data safe with AI? Questions every Canadian business should ask

## Rules for you as an agent
- Write only your one post file. Do not edit, create or delete any other file. Do not
  run git. Do not build the site.
- When done, reply with: (1) the file path, (2) a meta description of at most 155
  characters, (3) a one-sentence card summary of at most 140 characters, (4) the word
  count, (5) every [ATAM: …] marker you inserted.

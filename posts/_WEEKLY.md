# Weekly blog post: instructions for the scheduled run

You are running unattended. Your job is to research, write, build, check and publish
ONE new blog post for aidaconsulting.ca, under Atam Singh's name, with nobody reviewing
it first. That is why the checks below are strict: if in doubt, leave it out, and if a
check fails, hold the post instead of publishing it.

All paths are relative to the project root (the folder that contains `build.py`).

## 1. Should a post be written today?
Run `python3 tools/weekly_gate.py`.
- If it prints `SKIP: …`, stop now. Reply with that one line and do nothing else.
- If it prints `POST`, continue.

## 2. Read first
- `posts/_BRIEF.md`: voice, reader, format, and the ONLY facts about Atam you may use.
- `posts/_TOPICS.md`: the topic backlog and the log of what has been published.
- The `POSTS` list in `build.py`: existing titles, so you do not repeat a topic.
- One or two existing posts in `posts/` to match their tone and structure.

## 3. Choose the topic
Use web search to look at the last 10 days of news that matters to a Canadian business
owner who is thinking about AI or struggling with their data: Statistics Canada
releases, Government of Canada announcements and programs, widely reported developments
in AI tools that a business would actually use, privacy or regulatory developments in
Canada, and credible surveys about businesses adopting AI.
- If one item is worth a post, write about what it means in practice for the reader,
  and connect it to the work AIDA does (finding where AI pays off, AI assistants and
  agents, data engineering, getting data ready for AI). Category: `News`.
- If nothing is worth a post this week, take the next unused topic from the backlog in
  `posts/_TOPICS.md`.
- Never write about a topic already published. Never write about politics, a named
  competitor, or a single vendor's product launch as if it were an endorsement.

## 4. Research rules (these override "do not do web research" in the brief)
- Every statistic, date, quotation and news claim must be confirmed by OPENING a
  primary or reputable source during this run: the organisation's own release or page,
  an official government page, or a major news outlet. A search-result snippet is not
  confirmation. If you cannot open a source that confirms it, leave the claim out.
- Link every source inline, with `target="_blank" rel="noopener"`.
- Quote at most one short phrase (under 15 words) per post; summarise everything else in
  your own words.
- No legal, tax, financial or medical advice. On privacy or legal topics, give the
  reader questions to ask and tell them to confirm with their own adviser; do not state
  what a law requires.
- Do not publish prices, timelines or guarantees for AIDA's work.

## 5. Claims about Atam
This post is not reviewed before it goes live, so:
- Use only the background facts listed in `posts/_BRIEF.md`, unattributed ("on one
  project", "inside a federal department"). Never name an employer in the post body.
- Do not invent any first-person experience, opinion presented as experience, client,
  client story or result. If you would need a detail that is not in the brief, write
  the passage without it.
- Do NOT use `<mark class="todo">` markers. A new post must contain none.

## 6. Write the post
- File: `posts/<slug>.html`, an HTML fragment in exactly the format in `posts/_BRIEF.md`
  (lead paragraph, 4 to 6 `<h2>` sections, a final "What to do this week" section,
  850 to 1,100 words, allowed tags only, no em dashes, Canadian spelling with -ize).
- Slug: lowercase words joined by hyphens, 3 to 6 words.
- Do not write sentences that narrow who the advice is for ("this is only for small
  businesses"), and do not list tools as if they were the only ones Atam knows.

## 7. Register it
In `build.py`, add an entry at the TOP of the `POSTS` list:
`{"slug": "…", "tag": "…", "featured": True, "date": "YYYY-MM-DD", "title": "…", "summary": "…", "description": "…"},`
- `date`: today's date. `tag`: exactly one of the `CATEGORIES` in `build.py`.
- `summary`: one sentence, at most 140 characters. `description`: at most 155 characters.
- Then change `"featured": True` to `"featured": False` on the OLDEST featured post, so
  exactly four posts stay featured (the home page shows the four newest featured).
In `posts/_TOPICS.md`, add a line to the log (date, slug, title, source links) and, if
you used a backlog topic, mark it as used.

## 8. Build and check
1. `python3 build.py` must finish with `Built N pages` and no error.
2. `python3 tools/check_site.py --strict-slug <slug>` must print `OK`.
3. Re-read the finished post once more against sections 4 and 5: every number has a
   linked source you opened in this run; nothing about Atam goes beyond the brief.
If something fails, fix it and re-run, at most twice.

## 9. If it still fails: hold, do not publish
Move the post to `posts/_held/<slug>.html`, undo your changes to `build.py` and
`posts/_TOPICS.md` (`git checkout -- build.py posts/_TOPICS.md`), run `python3 build.py`
again, and report what failed. Do not commit.

## 10. Publish
1. `git add -A` then `git commit -m "Blog: <title>"`.
2. If `git remote get-url origin` succeeds, run `git push origin main`.
   - Never force-push, never change branches, remotes, git config or credentials.
   - If there is no remote, or the push is rejected or asks for credentials, stop there:
     the post stays committed locally. Do not try another way to publish.

## 11. Report
Reply with: the title, the category, the live URL
(`https://www.aidaconsulting.ca/blog/<slug>/`), the sources you linked, and one of
"published", "committed locally, not pushed: <reason>" or "held: <reason>". If a
notification tool is available to you, send the same one-line outcome with it.

## Limits
Only create or change: the new file in `posts/`, the `POSTS` list in `build.py`,
`posts/_TOPICS.md`, and the HTML and sitemap that `build.py` generates. Do not change
any other page's wording, the styles, the contact form, `CNAME`, or anything outside
this project. Do not run destructive git commands. Do not send email or post anywhere
other than this repository.

#!/usr/bin/env python3
"""Generates the static pages for aidaconsulting.ca.

Edit the content in this file, then run:  python3 build.py
It rewrites index.html, the landing pages and sitemap.xml. No dependencies.
"""
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://www.aidaconsulting.ca"
# The contact form posts straight into this Google Form, so replies land in its
# existing responses sheet. The entry.* ids below are that form's field ids.
FORM_ID = "1FAIpQLSd4dWFzGbmAxxguMpqVNaVb6ff8SF5sv4adQ7LhOCOJPltsIQ"
FORM = f"https://docs.google.com/forms/d/e/{FORM_ID}/viewform"
FORM_POST = f"https://docs.google.com/forms/d/e/{FORM_ID}/formResponse"
FIELD = {"name": "entry.2005620554", "email": "entry.1045781291", "phone": "entry.1166974658", "comments": "entry.839337160"}
TOPICS = ["AI strategy: where to start", "AI agents and assistants", "Data engineering and pipelines",
          "Data quality and governance", "Public-sector project", "Something else"]
LINKEDIN = "https://www.linkedin.com/in/atamsingh"
LOGO = (ROOT / "partials/logo-mark.svg").read_text().strip()
PIPELINE = (ROOT / "partials/pipeline.svg").read_text().strip()

# Sources for the market figures quoted on the pages.
SRC_STATCAN = "https://www150.statcan.gc.ca/n1/daily-quotidien/260831/dq260831a-eng.htm"
SRC_GARTNER = "https://www.gartner.com/en/newsroom/press-releases/2025-02-26-lack-of-ai-ready-data-puts-ai-projects-at-risk"
SRC_GC_AI = "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/gc-ai-strategy-overview.html"

NAV = [
    ("ai-consulting/", "AI consulting"),
    ("ai-agents/", "AI agents"),
    ("data-engineering/", "Data engineering"),
    ("ai-ready-data/", "AI-ready data"),
    ("public-sector/", "Public sector"),
]

ICONS = {
    "ai": '<circle cx="24" cy="24" r="5"/><circle cx="9" cy="11" r="3"/><circle cx="39" cy="11" r="3"/><circle cx="9" cy="37" r="3"/><circle cx="39" cy="37" r="3"/><path d="M11.5 13l8.5 7.5M36.5 13 28 20.5M11.5 35l8.5-7.5M36.5 35 28 27.500"/>',
    "compass": '<circle cx="24" cy="24" r="18"/><path d="M31 17l-4 10-10 4 4-10z"/>',
    "pipes": '<path d="M6 14h14v8H6zM28 26h14v8H28zM6 30h8M20 18h6a4 4 0 0 1 4 4v4M14 30h14"/>',
    "shield": '<path d="M24 5l15 6v11c0 10-6.5 17-15 21C15.5 39 9 32 9 22V11z"/><path d="M17 24l5 5 9-11"/>',
    "chart": '<path d="M6 40h36M8 34l9-10 8 6 14-18"/><circle cx="17" cy="24" r="2.5" fill="currentColor"/><circle cx="25" cy="30" r="2.5" fill="currentColor"/><circle cx="39" cy="12" r="2.5" fill="currentColor"/>',
    "screen": '<rect x="6" y="8" width="36" height="28" rx="4"/><path d="M18 42h12M14 28v-6M22 28V16M30 28v-9M36 28v-4"/>',
    "chat": '<path d="M8 10h32v22H22l-9 8v-8H8z"/><path d="M16 18h16M16 25h10"/>',
    "check": '<circle cx="24" cy="24" r="18"/><path d="M15 24l6 6 12-13"/>',
    "people": '<circle cx="17" cy="17" r="6"/><circle cx="34" cy="20" r="4.5"/><path d="M5 40c0-7 5-12 12-12s12 5 12 12M31 30c6 0 11 4 11 10"/>',
    "cloud": '<path d="M14 36a9 9 0 0 1-1-18 12 12 0 0 1 23 3 7.500 7.500 0 0 1-1 15z"/><path d="M24 23v9M20 28l4 4 4-4"/>',
}


def icon(name):
    return ('<svg class="card-icon" viewBox="0 0 48 48" aria-hidden="true" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' + ICONS[name].replace(".500", ".5") + "</svg>")


def ul(items, indent="              "):
    return "\n".join(f"{indent}<li>{i}</li>" for i in items)


# ---------------------------------------------------------------- layout

def layout(path, title, description, body, base):
    """path: '' for home or 'slug/'. base: '' for home or '../' for subpages."""
    nav = "\n".join(
        '        <a href="%s%s"%s>%s</a>' % (base, href, ' aria-current="page"' if href == path else "", label)
        for href, label in NAV
    )
    about = "#about" if path == "" else f"{base}#about"
    return f"""<!doctype html>
<html lang="en-CA">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{SITE}/{path}">
  <meta name="theme-color" content="#2a3060">

  <meta property="og:type" content="website">
  <meta property="og:url" content="{SITE}/{path}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{SITE}/assets/og.svg">
  <meta name="twitter:card" content="summary_large_image">

  <link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{base}styles.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "AIDA Consulting Solutions",
    "url": "{SITE}/",
    "description": "AI and data consulting: AI strategy, AI agents and assistants, data engineering and data quality.",
    "founder": {{ "@type": "Person", "name": "Atam Singh", "sameAs": "{LINKEDIN}" }},
    "areaServed": "CA",
    "address": {{ "@type": "PostalAddress", "addressLocality": "Ottawa", "addressRegion": "ON", "addressCountry": "CA" }},
    "knowsAbout": ["Artificial intelligence consulting", "Generative AI", "AI agents", "Retrieval-augmented generation", "Data engineering", "Data quality", "Data governance"]
  }}
  </script>
</head>
<body>
  <a class="skip" href="#main">Skip to main content</a>

  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="{base or './'}" aria-label="AIDA Consulting Solutions, home">
        {LOGO}
        <span>AIDA <span class="brand-sub">Consulting Solutions</span></span>
      </a>
      <nav class="main-nav" aria-label="Primary">
{nav}
        <a href="{about}">About</a>
      </nav>
      <details class="menu">
        <summary>Menu</summary>
        <nav aria-label="Mobile">
{nav}
          <a href="{about}">About</a>
        </nav>
      </details>
      <a class="btn btn-small" href="#contact">Get in touch</a>
    </div>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="site-footer">
    <div class="wrap footer-inner">
      <p>© <span id="year">2026</span> AIDA Consulting Solutions · Ottawa, Canada</p>
      <nav aria-label="Footer">
{nav}
        <a href="{about}">About</a>
      </nav>
    </div>
  </footer>

  <script>document.getElementById('year').textContent = new Date().getFullYear();</script>
  <script src="{base}assets/contact.js" defer></script>
</body>
</html>
"""


def contact(heading="Have an AI or data challenge? Let’s talk it through.",
            text="No pitch deck. Tell us what you are dealing with and we will tell you honestly whether we can help.",
            topic=None, page="Home"):
    options = "\n".join(
        '                <option%s>%s</option>' % (" selected" if t == topic else "", t) for t in TOPICS)
    placeholder = "" if topic else '                <option value="" selected disabled>Choose one</option>\n'
    return f"""    <section class="section contact" id="contact">
      <div class="wrap contact-grid">
        <div class="contact-copy">
          <p class="eyebrow">Get in touch</p>
          <h2>{heading}</h2>
          <p>{text}</p>
          <ol class="next">
            <li><span>1</span>You tell us about your challenge</li>
            <li><span>2</span>We talk it through together</li>
            <li><span>3</span>You get a proposed plan and scope</li>
          </ol>
          <p class="contact-alt">Prefer LinkedIn? <a href="{LINKEDIN}" target="_blank" rel="noopener">Message Atam directly</a>.</p>
        </div>

        <div class="form-card">
          <form class="contact-form" action="{FORM_POST}" method="post" data-page="{page}"
                data-name="{FIELD["name"]}" data-email="{FIELD["email"]}" data-phone="{FIELD["phone"]}" data-comments="{FIELD["comments"]}">
            <div class="field-row">
              <label>Name
                <input type="text" name="name" autocomplete="name" required>
              </label>
              <label>Work email
                <input type="email" name="email" autocomplete="email" required>
              </label>
            </div>
            <div class="field-row">
              <label><span>Organization <span class="optional">optional</span></span>
                <input type="text" name="company" autocomplete="organization">
              </label>
              <label><span>Phone <span class="optional">optional</span></span>
                <input type="tel" name="phone" autocomplete="tel">
              </label>
            </div>
            <label>What do you need help with?
              <select name="topic" required>
{placeholder}{options}
              </select>
            </label>
            <label>Tell us a little about it
              <textarea name="message" rows="5" required placeholder="What are you trying to achieve, and what is getting in the way?"></textarea>
            </label>
            <label class="hp" aria-hidden="true">Leave this field empty
              <input type="text" name="website" tabindex="-1" autocomplete="off">
            </label>
            <button class="btn btn-accent" type="submit">Send message</button>
            <p class="form-note">We only use your details to reply to you.</p>
            <p class="form-error" role="alert" hidden>Something went wrong sending your message. Please try again, or <a href="{LINKEDIN}" target="_blank" rel="noopener">message us on LinkedIn</a>.</p>
          </form>
          <div class="form-done" role="status" tabindex="-1" hidden>
            <svg viewBox="0 0 48 48" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="24" cy="24" r="20"/><path d="M15 24l6 6 12-13"/></svg>
            <h3>Thanks, your message is on its way.</h3>
            <p>We will read it and reply by email.</p>
          </div>
        </div>
      </div>
    </section>"""


def results(items, heading, intro):
    tiles = "\n".join(f"          <div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in items)
    return f"""    <section class="section results" id="results">
      <div class="wrap">
        <p class="eyebrow">Results</p>
        <h2>{heading}</h2>
        <p class="section-intro">{intro}</p>
        <dl class="results-grid">
{tiles}
        </dl>
      </div>
    </section>"""


R = {
    "ai": ("AI in production", "Thousands of results interpreted by AI for practitioners, with human review and automated judges keeping quality in check."),
    "chatbot": ("Answers on demand", "An internal retrieval chatbot giving senior leaders context-specific answers with minimal manual work."),
    "team": ("10-person team", "Data scientists, developers and DevOps engineers led through the build of a tool used by 3,500+ people."),
    "fast": ("3× faster", "A business-critical pipeline processing 80 million rows an hour, re-engineered to run in a third of the time."),
    "saved": ("~$1M saved", "Cloud spend cut through automated cost and usage auditing after an on-prem migration."),
    "pb": ("5 PB", "Of unstructured data brought into privacy compliance, on a fixed regulatory deadline."),
    "rules": ("200+ rules", "Automated data quality checks running across more than 30 datasets."),
    "users": ("3,500+ users", "Serving themselves on a tool that monitors 3.2 million business time series a day."),
    "models": ("~300 models", "An enterprise data repository designed to model an entire programme’s data, with a team mentored to build it."),
    "release": ("2 hours back", "Every release cycle, after deployment preparation for a data team was automated."),
    "trained": ("Team trained", "Architecture documented and developers trained to maintain, test and extend the pipelines after hand-over."),
}

# ---------------------------------------------------------------- home page

HOME_START = [
    ("ai-consulting/", "compass", "AI consulting", "Not sure where AI fits?",
     "Find the use cases that will actually pay off, and get a plan your team can deliver."),
    ("ai-agents/", "chat", "AI agents &amp; assistants", "Stuck at the demo stage?",
     "Assistants, retrieval and agent workflows built and tested for real users."),
    ("data-engineering/", "pipes", "Data engineering", "Pipelines slow or fragile?",
     "Senior data engineering: pipelines, warehouse models, cloud cost and testing."),
    ("ai-ready-data/", "check", "AI-ready data", "Data not ready for AI?",
     "Pipelines, models and quality checks that make your data something AI can rely on."),
    ("public-sector/", "shield", "Public sector", "Working in government?",
     "Data quality, architecture and responsible AI, delivered with public-sector rigour."),
]

HOME_SERVICES = [
    ("AI Strategy &amp; Opportunity", "compass", "Leadership wants an AI plan, and nobody knows where to start.",
     "We look at how your organization actually works and find where AI will save time or make money, and where it won’t.",
     ["A ranked shortlist of AI use cases", "A data-readiness check for each one", "A phased roadmap and budget range", "Clear briefings for senior leadership"], "ai-consulting/"),
    ("AI Agents &amp; Assistants", "ai", "We have an AI demo. We need something we can put in front of customers.",
     "We take AI from prototype to production, with the evaluation and guardrails you need before you can trust what it says.",
     ["Retrieval (RAG) and agent workflows grounded in your data", "Quality measured by human review and LLM judges", "Internal assistants and chatbots", "Monitoring once it is live"], "ai-agents/"),
    ("Data Engineering", "pipes", "Our pipelines are slow, fragile, or cost too much.",
     "We rebuild the foundations: pipelines that finish on time, data models people can reason about, and a cloud bill that matches the value you get.",
     ["Reliable batch and real-time pipelines", "A clean, documented warehouse model", "Automated testing and deployment", "Cloud migration and cost reduction"], "data-engineering/"),
    ("Data Quality &amp; Governance", "shield", "Two dashboards, two different answers. Nobody trusts the numbers.",
     "We find where quality breaks down and put automated checks in place, so problems are caught before your users or your auditors find them.",
     ["Automated quality rules and monitoring", "A testing framework for your pipelines", "Privacy, financial-reporting and data-residency compliance", "Lineage, discovery and master data"], "ai-ready-data/"),
    ("Analytics &amp; Data Science", "chart", "We have plenty of data, but we still can’t see how the business is doing.",
     "We agree on the handful of metrics that matter, then make them visible and monitored, so changes are noticed early and decisions get made.",
     ["Agreed definitions for metrics and KPIs", "Dashboards leaders actually open", "Monitoring of your business’s vital signs", "Customer journey and usage analysis"], None),
    ("Data Products &amp; Platforms", "screen", "Every question sits in the data team’s queue.",
     "We build tools that let people serve themselves, technical or not, so your data team spends its time on the hard problems.",
     ["Self-serve exploration and BI at scale", "Pipeline platforms with GUI, API and CLI", "No-code builders for non-technical users", "Open-source tools adopted securely"], None),
]

ENGAGE = [
    ("Assess", "AI &amp; data assessment", "You want to use AI, but aren’t sure where or whether your data is ready.",
     "We review your processes, data and tools, then tell you plainly where AI will pay off and what has to be fixed first.",
     ["A ranked list of AI opportunities", "Data gaps, risks and quick wins", "A prioritized roadmap"]),
    ("Build", "Project delivery", "You have a defined use case and need it built properly.",
     "We design, build and ship the solution end to end, working alongside your team in small increments.",
     ["A working, tested solution", "Documentation and runbooks", "Your team trained to own it"]),
    ("Advise", "Embedded advisor", "Your team is capable but needs senior AI and data direction.",
     "We join part-time as your senior AI and data lead: reviewing designs, unblocking decisions and mentoring.",
     ["Architecture and design reviews", "Technical leadership on demand", "Mentoring for your engineers"]),
]

WHY = [
    ("AI with a data backbone", "Most AI consultants start at the model. We start at the data it depends on, because that is where AI projects usually fail."),
    ("Senior and hands-on", "You work directly with the principal engineer who does the work. No hand-off to a junior team once the contract is signed."),
    ("Understanding comes first", "We explain what is going on in plain language, so you can make decisions about your own data and AI with confidence."),
    ("Built to hand over", "Everything is documented, tested and taught. The goal is a team that owns the result, not one that depends on us."),
]

STACK = {
    "AI": "LangGraph, LangChain, Pydantic AI, Hugging Face, OpenAI models, PyTorch, TensorFlow",
    "Data": "PySpark, dbt, Airflow, Presto/Trino, BigQuery, PostgreSQL, Tableau, Apache Superset, SAS Viya",
    "Software": "Python, Ruby, Rails, React, GraphQL, TypeScript",
    "Infrastructure": "GCP, AWS, Terraform, Kubernetes",
}

STEPS_HOME = [
    ("Understand", "We start with your business and the questions you need answered, and map the data and AI challenges standing in the way."),
    ("Build", "We deliver in small, working increments, so you see value early and can steer as priorities change."),
    ("Hand over", "We document, explain and train as we go, so your team can run and extend what we leave behind."),
]


def steps(items):
    return "\n".join(f"          <li>\n            <h3>{t}</h3>\n            <p>{p}</p>\n          </li>" for t, p in items)


def card_link(link):
    if not link:
        return ""
    return '\n            <a class="link-arrow card-link" href="%s">Learn more</a>' % link


def home():
    start = "\n".join(f"""          <a class="start-card" href="{href}">
            {icon(ic)}
            <span class="card-label">{label}</span>
            <strong>{q}</strong>
            <span>{text}</span>
          </a>""" for href, ic, label, q, text in HOME_START)

    cards = "\n".join(f"""          <article class="card">
            <div class="card-head">{icon(ic)}<span class="card-label">{name}</span></div>
            <h3 class="pain">“{pain}”</h3>
            <p>{help_}</p>
            <p class="gets-label">What you get</p>
            <ul>
{ul(gets)}
            </ul>{card_link(link)}
          </article>""" for name, ic, pain, help_, gets, link in HOME_SERVICES)

    engage = "\n".join(f"""          <article class="engage-card">
            <p class="engage-kicker">{k}</p>
            <h3>{t}</h3>
            <p class="best"><strong>Best when:</strong> {best}</p>
            <p>{desc}</p>
            <ul>
{ul(li)}
            </ul>
          </article>""" for k, t, best, desc, li in ENGAGE)

    why = "\n".join(f"          <li><h3>{a}</h3><p>{b}</p></li>" for a, b in WHY)
    stack = "\n".join(
        f"          <div><dt>{k}</dt><dd>" + "".join(f"<span>{x}</span>" for x in v.split(", ")) + "</dd></div>"
        for k, v in STACK.items())

    body = f"""    <section class="hero" id="top">
      <div class="wrap hero-grid">
        <div>
          <p class="eyebrow">AI &amp; data consulting · Ottawa, Canada</p>
          <h1>AI that works in production, built on <em>data you can trust.</em></h1>
          <p class="lede">Most AI projects stall because the data underneath them isn’t ready. We are AI consultants with a data engineering backbone: we help Canadian organizations find where AI will pay off, build it properly, and fix the data it depends on.</p>
          <div class="actions">
            <a class="btn" href="#contact">Tell us about your challenge</a>
            <a class="link-arrow" href="#start">See how we can help</a>
          </div>
          <p class="trust">Led by a principal engineer with experience at <strong>Stripe</strong>, <strong>Shopify</strong> and <strong>Fullscript</strong>, and in the federal public sector at <strong>IRCC</strong> and <strong>EDC</strong>.</p>
        </div>

        {PIPELINE}
      </div>
    </section>

    <section class="market" aria-label="The AI market in Canada">
      <div class="wrap market-grid">
        <div>
          <p class="market-num">1 in 4</p>
          <p>Canadian businesses plan to use AI in the next 12 months, up from 1 in 7 a year ago.</p>
          <a href="{SRC_STATCAN}" target="_blank" rel="noopener">Statistics Canada, Q3 2026</a>
        </div>
        <div>
          <p class="market-num">60%</p>
          <p>of AI projects not supported by AI-ready data are predicted to be abandoned through 2026.</p>
          <a href="{SRC_GARTNER}" target="_blank" rel="noopener">Gartner, 2025</a>
        </div>
        <div>
          <p class="market-num">63%</p>
          <p>of organizations don’t have, or aren’t sure they have, the right data practices for AI.</p>
          <a href="{SRC_GARTNER}" target="_blank" rel="noopener">Gartner survey, 2024</a>
        </div>
      </div>
    </section>

    <section class="section" id="start">
      <div class="wrap">
        <p class="eyebrow">Where to start</p>
        <h2>Pick the conversation that sounds like yours.</h2>
        <div class="start">
{start}
        </div>
      </div>
    </section>

    <section class="section section-alt" id="services">
      <div class="wrap">
        <p class="eyebrow">How we can help</p>
        <h2>Sound familiar? These are the problems we solve.</h2>
        <p class="section-intro">AI first, and the data work that makes AI succeed.</p>

        <div class="cards">
{cards}
        </div>
      </div>
    </section>

    <section class="section" id="engage">
      <div class="wrap">
        <p class="eyebrow">How we work</p>
        <h2>Three ways to work with us.</h2>
        <p class="section-intro">Start small or start big. An assessment is the lowest-risk way to begin.</p>
        <div class="engage">
{engage}
        </div>
        <ol class="steps">
{steps(STEPS_HOME)}
        </ol>
      </div>
    </section>

{results([R["ai"], R["fast"], R["saved"], R["pb"], R["rules"], R["users"]],
         "The kind of outcomes you can expect.",
         "Drawn from work our principal has led or delivered over the past decade.")}

    <section class="section" id="why">
      <div class="wrap">
        <p class="eyebrow">Why AIDA</p>
        <h2>A senior practitioner, not a slide deck.</h2>
        <ul class="why">
{why}
        </ul>
      </div>
    </section>

    <section class="section section-alt" id="about">
      <div class="wrap about">
        <div>
          <p class="eyebrow">Who you’ll work with</p>
          <h2>Led by a practitioner.</h2>
          <p class="section-intro">Fluent in the tools below, and comfortable picking up yours.</p>
        </div>
        <article class="person">
          <div class="avatar" aria-hidden="true">AS</div>
          <div>
            <h3>Atam Singh</h3>
            <p class="role">Principal Engineer and Founder</p>
            <p>Atam has spent more than 10 years building data and AI systems. His experience spans Stripe, nearly six years at Shopify, where he went from data engineer to staff data scientist and staff data developer, and production AI work at Fullscript. In the federal public sector he has led data quality and architecture work at Immigration, Refugees and Citizenship Canada (IRCC) and built master data pipelines at Export Development Canada (EDC). He has led multidisciplinary teams of up to ten.</p>
            <a class="link-arrow" href="{LINKEDIN}" target="_blank" rel="noopener">Connect on LinkedIn</a>
          </div>
        </article>
        <dl class="stack">
{stack}
        </dl>
      </div>
    </section>

{contact()}"""
    return layout("", "AI & Data Consulting in Ottawa | AIDA Consulting Solutions",
                  "AI consultants with a data engineering backbone. We help Canadian organizations find where AI pays off, build it for production, and get their data AI-ready.",
                  body, "")


# ---------------------------------------------------------------- landing pages

def bridge(b):
    """Optional call-out linking one service to another."""
    if not b:
        return ""
    source = f' <a class="src" href="{b["src"][1]}" target="_blank" rel="noopener">{b["src"][0]}</a>' if b.get("src") else ""
    return f"""    <section class="bridge">
      <div class="wrap bridge-inner">
        <div>
          <p class="eyebrow">{b["eyebrow"]}</p>
          <h2>{b["heading"]}</h2>
        </div>
        <div>
          <p>{b["text"]}{source}</p>
          <a class="link-arrow" href="../{b["href"]}">{b["link"]}</a>
        </div>
      </div>
    </section>
"""


def landing(p):
    pains = "\n".join(f"          <li>“{x}”</li>" for x in p["pains"])
    offers = "\n".join(f"""          <article class="card">
            <div class="card-head">{icon(ic)}<span class="card-label">{label}</span></div>
            <h3>{title}</h3>
            <p>{text}</p>
            <p class="gets-label">What you get</p>
            <ul>
{ul(gets)}
            </ul>
          </article>""" for ic, label, title, text, gets in p["offers"])
    faq = "\n".join(f"""          <details>
            <summary>{q}</summary>
            <p>{a}</p>
          </details>""" for q, a in p["faq"])
    points = "\n".join(f"            <li>{x}</li>" for x in p["points"])
    fact = p.get("fact")
    fact_html = f"""
        <aside class="fact">
          <p class="market-num">{fact[0]}</p>
          <p>{fact[1]}</p>
          <a href="{fact[3]}"{'' if fact[3].startswith('#') else ' target="_blank" rel="noopener"'}>{fact[2]}</a>
        </aside>""" if fact else ""

    body = f"""    <section class="hero hero-landing" id="top">
      <div class="wrap hero-grid">
        <div>
          <p class="eyebrow">{p["eyebrow"]}</p>
          <h1>{p["h1"]}</h1>
          <p class="lede">{p["lede"]}</p>
          <div class="actions">
            <a class="btn" href="#contact">{p.get("cta", "Tell us about your challenge")}</a>
            <a class="link-arrow" href="#offer">See what you get</a>
          </div>
        </div>
        <ul class="points">
{points}
        </ul>
      </div>
    </section>

    <section class="section section-alt" id="problem">
      <div class="wrap split">
        <div>
          <p class="eyebrow">Sound familiar?</p>
          <h2>{p["pain_heading"]}</h2>{fact_html}
        </div>
        <ul class="pains">
{pains}
        </ul>
      </div>
    </section>

    <section class="section" id="offer">
      <div class="wrap">
        <p class="eyebrow">What we do</p>
        <h2>{p["offer_heading"]}</h2>
        <div class="cards cards-{len(p["offers"])}">
{offers}
        </div>
      </div>
    </section>

    <section class="section section-alt" id="how">
      <div class="wrap">
        <p class="eyebrow">How it works</p>
        <h2>{p["steps_heading"]}</h2>
        <ol class="steps">
{steps(p["steps"])}
        </ol>
      </div>
    </section>

{bridge(p.get("bridge"))}
{results([R[k] for k in p["results"]], p["results_heading"],
         "Drawn from work our principal has led or delivered.")}

    <section class="section" id="faq">
      <div class="wrap split">
        <div>
          <p class="eyebrow">Questions</p>
          <h2>What people ask us first.</h2>
          <p class="section-intro">Led by <a href="../#about">Atam Singh</a>, a principal engineer with 10+ years in data and AI and experience at Stripe, Shopify and Fullscript. You work with him directly.</p>
        </div>
        <div class="faq">
{faq}
        </div>
      </div>
    </section>

{contact(p["contact_heading"], p["contact_text"], p["topic"], p["eyebrow"].replace("&amp;", "&"))}"""
    return layout(p["path"], p["title"], p["description"], body, "../")


PAGES = [
    {
        "path": "ai-consulting/",
        "topic": "AI strategy: where to start",
        "title": "AI Consulting in Ottawa & Across Canada | AIDA Consulting",
        "description": "AI consulting for Canadian organizations. Find the AI use cases that will pay off, prove them with a pilot, and take them to production, with your data ready to support them.",
        "eyebrow": "AI consulting · Ottawa &amp; across Canada",
        "h1": "AI consulting for organizations that want <em>results, not experiments.</em>",
        "lede": "Not sure where AI fits, or stuck after a promising demo? We help you find the use cases that will pay off, build them properly, and make sure your data can support them.",
        "cta": "Book an AI conversation",
        "points": ["Senior consultant, hands-on from day one", "Vendor-neutral advice on tools and models", "Privacy and data residency designed in", "Plain-language findings, not jargon"],
        "pain_heading": "Everyone is talking about AI. Few know what to do on Monday.",
        "fact": ("1 in 4", "Canadian businesses plan to use AI in the next 12 months, up from 1 in 7 a year earlier. Among those with no plans, 79% say they don’t see how it is relevant to them.", "Statistics Canada, Q3 2026", SRC_STATCAN),
        "pains": [
            "Leadership wants an AI plan, and nobody knows where to start.",
            "We bought the licences, but nothing has changed in how we work.",
            "Our pilot works in a demo and nowhere else.",
            "We’re worried about privacy, accuracy, and where our data goes.",
        ],
        "offer_heading": "From “where do we start?” to AI running in your business.",
        "offers": [
            ("compass", "Step 1", "AI opportunity assessment", "We review how your organization works and identify where AI will genuinely save time or grow revenue.",
             ["Use cases ranked by value and feasibility", "A data-readiness check for each", "Risks, costs and a phased roadmap"]),
            ("ai", "Step 2", "Pilot to production", "We build your highest-value use case end to end, with the testing needed to trust it with real users.",
             ["A working, tested AI solution", "Measured accuracy and quality", "Your team trained to run it"]),
            ("people", "Ongoing", "AI advisor", "A senior AI and data lead alongside your team, part-time, for as long as you need direction.",
             ["Tool and vendor decisions", "Design and architecture reviews", "Mentoring for your staff"]),
        ],
        "steps_heading": "Find it. Prove it. Scale it.",
        "steps": [
            ("Find", "We talk to the people doing the work, look at your data, and shortlist the use cases worth pursuing."),
            ("Prove", "We build one use case properly and measure whether it delivers, before you commit to more."),
            ("Scale", "We harden what works, hand it over to your team, and move to the next use case."),
        ],
        "bridge": {
            "eyebrow": "One firm, both halves",
            "heading": "Most AI projects turn into data projects.",
            "text": "Gartner predicts that 60% of AI projects not supported by AI-ready data will be abandoned. When your AI work runs into a pipeline or data quality problem, we fix that too, so you don’t need a second firm.",
            "src": ("Gartner, 2025", SRC_GARTNER),
            "href": "data-engineering/", "link": "See our data engineering work",
        },
        "results": ["ai", "chatbot", "pb"],
        "results_heading": "AI delivered where accuracy matters.",
        "faq": [
            ("We’re a small team. Is AI consulting worth it for us?", "Often the best first project is a small one: a single repetitive process that eats hours every week. The assessment tells you whether there is a real return. If the honest answer is “not yet”, we will say so."),
            ("Does our data need to be in good shape first?", "No. Finding out what state your data is in is part of the assessment. If it needs work before AI will succeed, we will tell you exactly what, and we can do that work too."),
            ("Which AI tools and models do you use?", "We are vendor-neutral. We have built with OpenAI models, open-source models from Hugging Face, and frameworks such as LangGraph, LangChain and Pydantic AI, and we recommend what fits your needs and budget."),
            ("How do you handle privacy and sensitive data?", "Privacy and data-residency requirements are designed in from the start. Our principal has delivered data systems under Canada–US data residency restrictions and large-scale privacy compliance programmes."),
        ],
        "contact_heading": "Wondering where AI fits in your organization?",
        "contact_text": "Tell us what you do and where the time goes. We will tell you honestly whether AI can help.",
    },
    {
        "path": "ai-agents/",
        "topic": "AI agents and assistants",
        "title": "Custom AI Agents, Assistants & RAG Development | AIDA Consulting",
        "description": "Custom AI agents, assistants and RAG systems grounded in your own data, built with the evaluation and guardrails needed for production. Based in Ottawa, serving Canada.",
        "eyebrow": "AI agents, assistants &amp; RAG",
        "h1": "AI assistants and agents that are <em>ready for real users.</em>",
        "lede": "Anyone can build a demo in an afternoon. We build AI assistants, retrieval (RAG) systems and agent workflows grounded in your own data, with the testing and guardrails needed to put them in front of staff and customers.",
        "cta": "Talk about your AI project",
        "points": ["Grounded in your documents and data", "Accuracy measured, not assumed", "Human review where it matters", "Built to be maintained by your team"],
        "pain_heading": "The demo was the easy part.",
        "pains": [
            "It answers confidently, and sometimes wrongly.",
            "It works on ten test questions and fails on the eleventh.",
            "We can’t tell whether a change made it better or worse.",
            "Legal and compliance won’t sign off on it.",
        ],
        "offer_heading": "What we build.",
        "offers": [
            ("chat", "Assistants", "Knowledge assistants", "Chat over your own documents, policies and data, with answers that cite where they came from.",
             ["Retrieval (RAG) tuned to your content", "Source citations on answers", "Access rules respected"]),
            ("ai", "Agents", "Agent workflows", "Multi-step processes automated by AI agents, with a person approving the steps that matter.",
             ["Agents connected to your systems", "Human-in-the-loop approvals", "Clear logs of every action"]),
            ("check", "Quality", "Evaluation &amp; guardrails", "The part most demos skip: proving it is accurate, and keeping it that way after launch.",
             ["Test sets built from real questions", "Human review plus LLM judges", "Monitoring in production"]),
            ("pipes", "Rescue", "Pilot rescue", "Already have a prototype that isn’t good enough to ship? We find out why and fix it.",
             ["A diagnosis of what is failing", "Fixes to retrieval, prompts and data", "A path to production"]),
        ],
        "steps_heading": "Ground it. Test it. Ship it.",
        "steps": [
            ("Ground", "We connect the AI to the right data and documents, so it answers from your facts, not its imagination."),
            ("Test", "We build an evaluation set and measure quality with human reviewers and automated judges, before and after every change."),
            ("Ship", "We deploy with monitoring and guardrails, document everything, and train your team to run it."),
        ],
        "results": ["ai", "chatbot", "team"],
        "results_heading": "AI we have put into production.",
        "faq": [
            ("How do you stop it making things up?", "Three ways: grounding answers in your own data through retrieval, measuring accuracy against a test set built from real questions, and keeping a person in the loop where a wrong answer would be costly."),
            ("Which models and frameworks do you use?", "Whatever fits. We have built with OpenAI models, open-source models from Hugging Face, and frameworks including LangGraph, LangChain and Pydantic AI. We will recommend based on your accuracy, cost and privacy needs."),
            ("Can it work with our existing systems?", "Usually, yes. Assistants and agents are most useful when connected to the databases, documents and APIs you already have. Working out those connections is part of the first conversation."),
            ("We already have a prototype. Can you take it over?", "Yes. We start by measuring how it performs today, then fix what is holding it back, which is often the data and retrieval and not the model."),
        ],
        "contact_heading": "Have an AI idea, or a demo that needs to grow up?",
        "contact_text": "Tell us what you want it to do. We will tell you what it takes to make it reliable.",
    },
    {
        "path": "data-engineering/",
        "topic": "Data engineering and pipelines",
        "title": "Data Engineering Consulting | Pipelines, dbt, Airflow, BigQuery | AIDA Consulting",
        "description": "Senior data engineering consulting in Ottawa, serving Canada. Pipeline build and rescue, warehouse modelling in dbt, cloud migration and cost reduction, testing and CI/CD.",
        "eyebrow": "Data engineering consulting",
        "h1": "Data pipelines that <em>just work.</em>",
        "lede": "Slow jobs, broken dashboards, a cloud bill nobody can explain. We are senior data engineers who fix the unglamorous foundations: pipelines, warehouse models, testing and cost. It is the work everything else depends on, AI included.",
        "cta": "Talk to a data engineer",
        "points": ["dbt, Airflow, PySpark, Trino", "BigQuery, PostgreSQL, GCP, AWS", "Batch and real-time streaming", "Testing, CI/CD and observability"],
        "pain_heading": "The boring work is where the value is.",
        "fact": ("3× faster", "A business-critical pipeline processing 80 million rows an hour, re-engineered by our principal to run in a third of the time.", "More results below", "#results"),
        "pains": [
            "The nightly job takes six hours and fails twice a week.",
            "Nobody dares touch the pipeline the last person built.",
            "Our cloud bill doubled and we can’t say why.",
            "Every release is a manual, nervous afternoon.",
        ],
        "offer_heading": "What we fix and build.",
        "offers": [
            ("pipes", "Pipelines", "Pipeline build &amp; rescue", "New pipelines built properly, or fragile ones rebuilt so they finish on time, every time.",
             ["Batch and real-time ingestion", "Orchestration with Airflow", "Point-in-time and snapshot reporting"]),
            ("screen", "Modelling", "Warehouse &amp; data modelling", "A warehouse people can understand, with one agreed definition for each number that matters.",
             ["Fact and dimension models in dbt", "Documented, tested transformations", "Metrics defined once and reused"]),
            ("cloud", "Cloud", "Migration &amp; cost", "Move from on-prem to the cloud, or get more from the cloud you already pay for.",
             ["Migration planning and delivery", "Automated cost and usage auditing", "Performance tuning of heavy jobs"]),
            ("check", "Reliability", "Testing, CI/CD &amp; monitoring", "Changes that ship safely, and problems that are caught before your users see them.",
             ["Automated tests on every change", "Release pipelines for data", "Data quality rules and alerts"]),
        ],
        "steps_heading": "Diagnose. Rebuild. Automate.",
        "steps": [
            ("Diagnose", "We trace your pipelines end to end and measure where the time, cost and failures actually come from."),
            ("Rebuild", "We fix the highest-impact pieces first, in small increments you can verify against the old results."),
            ("Automate", "We add the tests, deployment and monitoring that keep it working, and train your team to run them."),
        ],
        "bridge": {
            "eyebrow": "Thinking about AI next?",
            "heading": "This is the work that decides whether AI succeeds.",
            "text": "Gartner predicts that 60% of AI projects not supported by AI-ready data will be abandoned, and 63% of organizations are not sure their data practices are up to it. Reliable pipelines and tested data are what make the difference.",
            "src": ("Gartner, 2025", SRC_GARTNER),
            "href": "ai-consulting/", "link": "See our AI consulting",
        },
        "results": ["fast", "saved", "rules", "pb", "users", "release"],
        "results_heading": "Data engineering, measured.",
        "faq": [
            ("Which tools do you work with?", "Most often dbt, Airflow, PySpark, Trino/Presto, BigQuery and PostgreSQL, on GCP or AWS, with Terraform and Kubernetes underneath. We work with the stack you have and only recommend changing it when there is a clear reason."),
            ("Can you fix what we have, or do you always rebuild?", "We start by measuring what you have. Often a few targeted fixes to the worst pipelines deliver most of the benefit. We recommend a rebuild only when patching would cost more."),
            ("We are not doing AI. Is this still for us?", "Yes. Reliable pipelines pay for themselves through time saved, lower cloud costs and numbers people trust. If AI comes later, your data will already be ready for it."),
            ("Do you work with our team or replace it?", "With it. We work alongside your engineers and analysts, and leave documentation, tests and training behind so the work stays maintained."),
        ],
        "contact_heading": "Have a pipeline that keeps you up at night?",
        "contact_text": "Tell us what is slow, broken or expensive. We will tell you what we would look at first.",
    },
    {
        "path": "ai-ready-data/",
        "topic": "Data engineering and pipelines",
        "title": "AI-Ready Data: Data Engineering & Data Quality Consulting | AIDA Consulting",
        "description": "Get your data ready for AI. Data engineering and data quality consulting: reliable pipelines, clean warehouse models and automated quality checks. Ottawa, serving Canada.",
        "eyebrow": "Data engineering &amp; data quality",
        "h1": "Get your data <em>ready for AI.</em>",
        "lede": "AI is only as good as the data behind it. We build the pipelines, models and quality checks that make your data reliable enough for AI, for analytics, and for audit.",
        "cta": "Talk about your data",
        "points": ["Pipelines that finish on time", "Numbers everyone agrees on", "Quality checked automatically", "Lower cloud bills"],
        "pain_heading": "AI projects rarely fail on the model. They fail on the data.",
        "fact": ("60%", "of AI projects not supported by AI-ready data are predicted to be abandoned through 2026. 63% of organizations don’t have, or aren’t sure they have, the right data practices for AI.", "Gartner, 2025", SRC_GARTNER),
        "pains": [
            "Our data is scattered across a dozen systems.",
            "Two dashboards, two different answers.",
            "Pipelines break, and nobody notices until a customer does.",
            "We can’t say where a number came from.",
        ],
        "offer_heading": "The foundations AI needs.",
        "offers": [
            ("compass", "Assess", "Data readiness assessment", "A clear picture of where your data stands and what must change before AI or analytics can depend on it.",
             ["A map of your data and its gaps", "Quality and risk findings", "A prioritized fix list"]),
            ("pipes", "Build", "Pipelines &amp; warehouse", "Batch and real-time pipelines and a warehouse model that people can understand and trust.",
             ["Reliable, tested pipelines", "A documented data model", "Automated deployment (CI/CD)"]),
            ("shield", "Protect", "Data quality framework", "Automated rules that catch bad data before it reaches a dashboard, a model or an auditor.",
             ["Monitoring rules on key datasets", "Unit, sample and UAT testing", "Lineage and ownership"]),
            ("cloud", "Optimize", "Cloud &amp; cost", "Move to the cloud, or get more from the cloud you are already paying for.",
             ["Migration planning and delivery", "Cost and usage auditing", "Faster, cheaper pipelines"]),
        ],
        "steps_heading": "Assess. Fix. Keep it fixed.",
        "steps": [
            ("Assess", "We trace your data from source to use, and show you where it breaks, slows down or can’t be trusted."),
            ("Fix", "We rebuild the pipelines and models that matter most first, in small increments you can verify."),
            ("Keep it fixed", "We leave automated tests and monitoring in place, and a team that knows how to use them."),
        ],
        "results": ["fast", "rules", "saved"],
        "results_heading": "Data foundations, measured.",
        "faq": [
            ("Do we need a data warehouse before we can use AI?", "Not always. Some AI use cases need only a well-organized set of documents. Others need clean, joined-up data. The assessment tells you which you are dealing with, so you don’t build more than you need."),
            ("Which tools do you work with?", "Commonly dbt, Airflow, PySpark, BigQuery, PostgreSQL and Trino, on GCP or AWS. We work with the stack you have and only recommend changing it when there is a clear reason."),
            ("Can you work alongside our existing data team?", "Yes. Most engagements are done with your team, not around it, and include documentation and training so the work stays maintained after we leave."),
        ],
        "contact_heading": "Not sure your data is ready for AI?",
        "contact_text": "Tell us what you are trying to do with it. We will tell you what stands in the way.",
    },
    {
        "path": "public-sector/",
        "topic": "Public-sector project",
        "title": "Data & AI Consulting for the Public Sector | AIDA Consulting, Ottawa",
        "description": "Ottawa-based data and AI consulting for the public sector, with experience at IRCC and EDC: data quality assessment, information architecture, responsible AI pilots and knowledge transfer.",
        "eyebrow": "Public sector · Ottawa",
        "h1": "Data and AI for government, <em>done with rigour.</em>",
        "lede": "Our principal has designed data quality programmes, enterprise data models and AI tools at Immigration, Refugees and Citizenship Canada (IRCC), and built master data pipelines at Export Development Canada (EDC). We understand the governance, privacy and documentation standards that public-sector work demands.",
        "cta": "Start a conversation",
        "points": ["Hands-on experience at IRCC and EDC", "Data quality, architecture and AI", "Documentation and knowledge transfer built in", "Based in Ottawa"],
        "pain_heading": "Responsible AI starts with data you can stand behind.",
        "fact": ("2025–2027", "The AI Strategy for the Federal Public Service sets out to accelerate responsible AI adoption across government. That depends on data that is governed, documented and trusted.", "Government of Canada", SRC_GC_AI),
        "pains": [
            "We need to assess data quality across dozens of datasets, consistently.",
            "We need an information architecture before anyone builds anything.",
            "We want to try generative AI, safely and defensibly.",
            "We need knowledge transfer, not dependency on a contractor.",
        ],
        "offer_heading": "How we support public-sector teams.",
        "offers": [
            ("shield", "Quality", "Data quality assessment", "A repeatable framework to create, validate and run quality rules across your datasets.",
             ["Automated monitoring rules", "Unit, sample and UAT testing", "Standardized onboarding of new datasets"]),
            ("compass", "Architecture", "Information &amp; data architecture", "Scope, requirements, entity models and technology choices, defined before the build begins.",
             ["Business and technical requirements", "Fact and dimension models", "A phased implementation plan"]),
            ("chat", "AI", "Responsible AI pilots", "Retrieval assistants and AI tools built with evaluation, human oversight and clear documentation.",
             ["Assistants grounded in your own data", "Measured accuracy and limits", "Documentation for review and approval"]),
            ("people", "Capacity", "Knowledge transfer", "Your team trained to maintain, test and extend everything we deliver.",
             ["Architecture documentation", "Demos and hands-on training", "Mentoring for developers"]),
        ],
        "steps_heading": "Define. Deliver. Transfer.",
        "steps": [
            ("Define", "We gather requirements, agree on scope with leadership, and recommend the approach and technology with the reasoning written down."),
            ("Deliver", "We build in phases, with testing and documentation at each stage, inside your tools and standards."),
            ("Transfer", "We train your team and leave complete documentation, so the work continues without us."),
        ],
        "results": ["rules", "models", "trained"],
        "results_heading": "Delivered in the federal public sector.",
        "faq": [
            ("Can you work within our existing tools and standards?", "Yes. Our principal has delivered public-sector work using departmental platforms including SAS Viya, as well as dbt and PostgreSQL, and has advised senior leadership on technology selection."),
            ("Will our team be able to maintain what you build?", "That is the aim of every engagement. We document the architecture, run demos, and train your developers to maintain, test and extend the work."),
            ("Do you only work with the federal government?", "No. We also work with private-sector organizations, and bring experience from large-scale e-commerce and health technology to public-sector problems."),
        ],
        "contact_heading": "Have a data or AI initiative to plan?",
        "contact_text": "Tell us what your team is trying to achieve. We will tell you how we can help.",
    },
]


def main():
    (ROOT / "index.html").write_text(home(), encoding="utf-8")
    urls = [f"{SITE}/"]
    for p in PAGES:
        out = ROOT / p["path"]
        out.mkdir(exist_ok=True)
        (out / "index.html").write_text(landing(p), encoding="utf-8")
        urls.append(f"{SITE}/{p['path']}")
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    print(f"Built {len(urls)} pages")


if __name__ == "__main__":
    main()

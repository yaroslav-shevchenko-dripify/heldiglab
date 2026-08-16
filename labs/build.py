import json, os, pathlib

HERE = pathlib.Path(__file__).parent

NICHES = [
    {
        "slug": "ai-visibility",
        "title": "AI Visibility Monitor",
        "tagline": "Find out if ChatGPT recommends you",
        "lede": "Your buyers now ask AI assistants for recommendations instead of searching. AI Visibility Monitor measures how often ChatGPT, Claude, Gemini and Perplexity name your brand — and which sources they pull from when they name a competitor instead.",
        "price": "$99",
        "price_note": "per month, 50 tracked prompts across 4 assistants",
        "problem_title": "You cannot see this traffic in Google Analytics",
        "problems": [
            ("No rank to check", "There is no position 1–10 in an AI answer. Ask the same question five times and you get five different answers, so a single spot-check tells you nothing."),
            ("Competitors get named, you don't", "Assistants recommend a shortlist. If you are not on it, you never enter the buyer's consideration set — and no analytics tool reports the omission."),
            ("You can't fix what you can't attribute", "Models cite specific sources: Reddit threads, review sites, listicles. Without knowing which ones, optimisation is guesswork."),
        ],
        "steps": [
            ("Give us your prompts", "The questions your buyers actually ask — \"best CRM for agencies\", \"alternatives to X\". Start with 50."),
            ("We sample, repeatedly", "Each prompt runs many times per assistant, every day. We report a citation rate with a confidence interval, not a single lucky answer."),
            ("You get the source list", "Every answer is parsed for which pages the model cited. That list is your optimisation backlog."),
        ],
        "gets": [
            "Daily citation rate per prompt, per assistant",
            "Share-of-voice against up to 5 named competitors",
            "The cited-source list behind every answer",
            "Alerts when your rate moves more than 10 points",
            "CSV and API export",
        ],
        "faqs": [
            ("Which assistants do you cover?", "ChatGPT, Claude, Gemini and Perplexity at launch. We add others based on what early users ask for."),
            ("How is this different from an SEO rank tracker?", "Rank trackers read a deterministic list of blue links. Assistants generate a fresh answer each time, so the measurement is statistical — a rate across many samples rather than a position."),
            ("Can you actually improve my visibility?", "Monitoring tells you where you stand and which sources drive the answer. Assistants with live web search respond to source changes within weeks; models answering from training data move far more slowly. We are explicit about which is which rather than promising a fix."),
            ("What do you need from me?", "A domain, a list of prompts and your competitors. Setup takes about ten minutes."),
        ],
    },
    {
        "slug": "local-grid",
        "title": "Local Grid",
        "tagline": "Your Maps rank, street by street",
        "lede": "A single Google Maps ranking is a fiction — you rank differently on every block. Local Grid samples your position across a geographic grid and shows you the exact streets where you disappear.",
        "price": "$79",
        "price_note": "per month, 3 locations, weekly grid scans",
        "problem_title": "One ranking number hides the whole problem",
        "problems": [
            ("Rank is a map, not a number", "You might sit at position 2 outside your shop and position 19 a mile away. Rank trackers report one figure and average away the thing that matters."),
            ("You cannot see your service radius", "Multi-location businesses have no view of where one branch's coverage stops and the next begins — or where neither of them shows up."),
            ("Competitors own specific blocks", "Local visibility is won street by street. Without a grid you cannot tell who beats you where, or whether last month's work moved anything."),
        ],
        "steps": [
            ("Drop a pin", "Give us your business and a radius. We build a sampling grid across it."),
            ("We scan every point", "Each grid point is queried for your target keywords as if a customer were standing there."),
            ("Read the heatmap", "Green where you win, red where you vanish, with week-over-week movement per point."),
        ],
        "gets": [
            "Geo-grid heatmap per keyword and location",
            "Week-over-week change per grid point",
            "Competitor overlay showing who wins each block",
            "Share-of-local-voice across the whole radius",
            "White-label PDF for reporting to clients",
        ],
        "faqs": [
            ("How dense is the grid?", "Configurable — from a 5×5 grid over a neighbourhood to 13×13 across a metro. Denser grids cost more to run, so we let you choose."),
            ("Which keywords should I track?", "The searches that bring buyers: \"plumber near me\", \"emergency dentist\". Start with five per location."),
            ("Does this work outside the US?", "Yes. The grid is coordinates, not postcodes, so it works anywhere Google Maps operates."),
            ("Do you support agencies?", "Multi-location and white-label reporting are in scope. Tell us your client count when you request access."),
        ],
    },
    {
        "slug": "contact-verify",
        "title": "Contact Verify",
        "tagline": "Validate a phone, email or IP in one call",
        "lede": "Bad contact data poisons every downstream system — bounced sends, wasted dials, fraudulent signups. Contact Verify checks phone, email and IP in real time through a single endpoint, so bad records never reach your database.",
        "price": "$0.002",
        "price_note": "per lookup, no monthly minimum",
        "problem_title": "Bad records cost more the later you catch them",
        "problems": [
            ("Bounces wreck sender reputation", "A list with 8% invalid addresses will damage domain reputation faster than any content problem, and recovery takes months."),
            ("Fake signups scale your costs", "Disposable emails and VOIP numbers inflate your user count, your infrastructure bill and your support load simultaneously."),
            ("Three vendors, three integrations", "Most teams buy email validation from one provider, phone from another and IP intelligence from a third — then maintain all three."),
        ],
        "steps": [
            ("One endpoint", "POST a phone, email or IP. You get a verdict, a confidence score and the reason behind it."),
            ("Validate at the boundary", "Call it on signup, on import, before a send. Reject or flag before the record lands."),
            ("Watch the rejection reasons", "The breakdown tells you where bad data enters — a specific ad source, a specific form."),
        ],
        "gets": [
            "Phone: line type, carrier, reachability, VOIP detection",
            "Email: syntax, domain, mailbox existence, disposable detection",
            "IP: proxy, VPN, datacentre and geolocation flags",
            "Bulk endpoint for list cleaning",
            "Sub-300ms responses, 99.9% uptime target",
        ],
        "faqs": [
            ("How accurate is mailbox detection?", "Accuracy varies by provider — some mail servers deliberately accept everything. We return a confidence score rather than a false binary, and we tell you when a domain is catch-all."),
            ("Do you store the data I send?", "Lookups are not retained beyond the request except as aggregate counts for your usage dashboard."),
            ("Is there a free tier?", "Early access includes 5,000 free lookups so you can benchmark us against whatever you use now."),
            ("What about GDPR?", "Validation is processed in the EU with a DPA available. Tell us your jurisdiction when you request access."),
        ],
    },
    {
        "slug": "cart-rescue",
        "title": "Cart Rescue",
        "tagline": "Recover the checkout, prevent the chargeback",
        "lede": "Two leaks drain the same store: shoppers who abandon at checkout and buyers who dispute after delivery. Cart Rescue runs SMS recovery on the first and evidence automation on the second, from one Shopify install.",
        "price": "$0",
        "price_note": "no monthly fee — 9% of recovered revenue only",
        "problem_title": "Both leaks are invisible until you total them",
        "problems": [
            ("Email recovery arrives too late", "Abandonment emails open at around 20% and land hours later. The intent window is measured in minutes, not mornings."),
            ("Chargebacks are lost by default", "Most merchants never respond to disputes because assembling evidence takes 30+ minutes each. Undefended disputes are automatic losses plus a fee."),
            ("Fees escalate quietly", "Cross a processor's dispute threshold and you move to a monitoring programme with higher rates — often before anyone internally notices."),
        ],
        "steps": [
            ("Install on Shopify", "One click. We read checkout and order events, nothing else."),
            ("SMS within minutes", "Abandoned checkouts trigger a compliant SMS while intent is still live, with a direct link back to the filled cart."),
            ("Disputes answered automatically", "When a chargeback lands we assemble the evidence packet — delivery confirmation, device fingerprint, comms history — and submit it inside the processor's window."),
        ],
        "gets": [
            "SMS cart recovery with per-message revenue attribution",
            "Automatic chargeback evidence packets",
            "Dispute win-rate and threshold monitoring",
            "TCPA and GDPR compliant consent capture",
            "Pay only on recovered revenue",
        ],
        "faqs": [
            ("Which platforms do you support?", "Shopify first. WooCommerce is planned — tell us if that is what you run."),
            ("Is SMS marketing legal in my market?", "Rules differ by country. We capture consent at checkout and honour opt-outs, but you remain the sender of record — we will tell you plainly what applies in your market."),
            ("What win rate should I expect on disputes?", "It depends heavily on your category and reason codes. We would rather show you your own numbers in the first month than quote an industry average that may not apply to you."),
            ("How do you charge?", "9% of revenue we recover. No monthly fee, so if it recovers nothing it costs nothing."),
        ],
    },
]

HEAD = """<!DOCTYPE html>
<html class="dark" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title} — Heldig Lab</title>
<meta content="{tagline}. {lede_short}" name="description"/>
<script src="https://cdn.tailwindcss.com?plugins=forms"></script>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;700;800&amp;family=Inter:wght@400;500;600&amp;display=swap" rel="stylesheet"/>
<script>
      tailwind.config = {{
        darkMode: "class",
        theme: {{
          extend: {{
            colors: {{
              "background": "#111318",
              "surface": "#111318",
              "surface-container": "#1e1f25",
              "surface-container-low": "#1a1b21",
              "surface-container-high": "#282a2f",
              "on-surface": "#e2e2e9",
              "on-surface-variant": "#c0c7d4",
              "primary": "#a4c9ff",
              "primary-container": "#4a9eff",
              "on-primary": "#00315d",
              "outline-variant": "#414752"
            }},
            borderRadius: {{ DEFAULT: "0.125rem", lg: "0.25rem", xl: "0.5rem", full: "0.75rem" }},
            fontFamily: {{ headline: ["Manrope"], body: ["Inter"] }}
          }}
        }}
      }}
</script>
<style type="text/tailwindcss">
      .heldig-gradient-text {{ @apply bg-clip-text text-transparent bg-gradient-to-r from-primary to-primary-container; }}
      .heldig-gradient-bg {{ @apply bg-gradient-to-r from-primary to-primary-container; }}
</style>
</head>
<body class="bg-background font-body text-on-surface antialiased">
<header class="border-b border-outline-variant/40">
<div class="max-w-5xl mx-auto px-6 py-5 flex items-center justify-between">
<a class="flex items-center gap-2 font-headline font-extrabold text-lg" href="https://heldiglab.com/">Heldig Lab</a>
<a class="text-sm text-on-surface-variant hover:text-on-surface" href="#request">Request access</a>
</div>
</header>
"""

TPL = """
<main class="max-w-5xl mx-auto px-6">
<section class="py-20 md:py-28">
<span class="text-[10px] uppercase tracking-[0.2em] text-primary-container font-bold mb-6 block">Heldig Lab · Early access</span>
<h1 class="text-4xl md:text-6xl font-extrabold font-headline tracking-tighter mb-6 leading-[1.1]">{title}<br/><span class="heldig-gradient-text">{tagline}</span></h1>
<p class="text-lg text-on-surface-variant max-w-2xl mb-10 leading-relaxed">{lede}</p>
<a class="inline-block px-8 py-4 rounded-full heldig-gradient-bg text-on-primary font-bold active:scale-95 transition-transform" href="#request">Request access</a>
<p class="text-sm text-on-surface-variant mt-4">We are onboarding a small first group and building against their feedback.</p>
</section>

<section class="py-16 border-t border-outline-variant/40">
<h2 class="text-3xl font-bold font-headline mb-10">{problem_title}</h2>
<div class="grid md:grid-cols-3 gap-6">{problems}</div>
</section>

<section class="py-16 border-t border-outline-variant/40">
<h2 class="text-3xl font-bold font-headline mb-10">How it works</h2>
<div class="grid md:grid-cols-3 gap-6">{steps}</div>
</section>

<section class="py-16 border-t border-outline-variant/40 grid md:grid-cols-2 gap-12">
<div>
<h2 class="text-3xl font-bold font-headline mb-8">What you get</h2>
<ul class="space-y-4">{gets}</ul>
</div>
<div class="bg-surface-container rounded-xl p-8 h-fit">
<span class="text-[10px] uppercase tracking-widest font-bold text-primary-container">Early access pricing</span>
<div class="text-5xl font-extrabold font-headline my-4">{price}</div>
<p class="text-on-surface-variant mb-6">{price_note}</p>
<a class="block text-center px-6 py-3 rounded-full heldig-gradient-bg text-on-primary font-bold" href="#request">Request access</a>
<p class="text-xs text-on-surface-variant mt-4">Early access pricing is held for the first year. No card required to request access.</p>
</div>
</section>

<section class="py-16 border-t border-outline-variant/40">
<h2 class="text-3xl font-bold font-headline mb-10">Questions</h2>
<div class="space-y-8 max-w-3xl">{faqs}</div>
</section>

<section class="py-16 border-t border-outline-variant/40" id="request">
<div class="bg-surface-container rounded-xl p-8 md:p-12 max-w-2xl">
<h2 class="text-3xl font-bold font-headline mb-3">Request access</h2>
<p class="text-on-surface-variant mb-8">Tell us a little about your setup. We reply to every request personally, usually within two working days.</p>
<form class="space-y-5" id="request-form">
<div>
<label class="block text-sm font-medium mb-2" for="name">Name</label>
<input class="w-full rounded-lg bg-surface-container-high border-outline-variant/40 text-on-surface" id="name" name="name" required type="text"/>
</div>
<div>
<label class="block text-sm font-medium mb-2" for="email">Work email</label>
<input class="w-full rounded-lg bg-surface-container-high border-outline-variant/40 text-on-surface" id="email" name="email" required type="email"/>
</div>
<div>
<label class="block text-sm font-medium mb-2" for="website">Website</label>
<input class="w-full rounded-lg bg-surface-container-high border-outline-variant/40 text-on-surface" id="website" name="website" placeholder="example.com" type="text"/>
</div>
<div>
<label class="block text-sm font-medium mb-2" for="context">What are you using today?</label>
<textarea class="w-full rounded-lg bg-surface-container-high border-outline-variant/40 text-on-surface" id="context" name="context" rows="3"></textarea>
</div>
<button class="w-full px-6 py-4 rounded-full heldig-gradient-bg text-on-primary font-bold active:scale-95 transition-transform" type="submit">Send request</button>
<p class="text-xs text-on-surface-variant" id="form-note"></p>
</form>
</div>
</section>
</main>

<footer class="border-t border-outline-variant/40 mt-10">
<div class="max-w-5xl mx-auto px-6 py-10 text-sm text-on-surface-variant flex flex-wrap gap-x-6 gap-y-2 justify-between">
<span>{title} is a Heldig Lab product, built and operated in-house.</span>
<a class="hover:text-on-surface" href="https://heldiglab.com/">heldiglab.com</a>
</div>
</footer>

<script>
  const FORM_ENDPOINT = "";
  const CONTACT_EMAIL = "heldig.lab@pm.me";
  const PRODUCT = {product_json};

  document.getElementById("request-form").addEventListener("submit", async (e) => {{
    e.preventDefault();
    const note = document.getElementById("form-note");
    const data = Object.fromEntries(new FormData(e.target).entries());
    data.product = PRODUCT;

    if (FORM_ENDPOINT) {{
      note.textContent = "Sending…";
      try {{
        const res = await fetch(FORM_ENDPOINT, {{
          method: "POST",
          headers: {{ "Content-Type": "application/json", Accept: "application/json" }},
          body: JSON.stringify(data)
        }});
        if (!res.ok) throw new Error(res.status);
        e.target.innerHTML = '<p class="text-lg font-bold">Thank you — request received.</p><p class="text-on-surface-variant mt-2">We reply to every request personally, usually within two working days.</p>';
        return;
      }} catch (err) {{
        note.textContent = "Could not send. Opening your email client instead.";
      }}
    }}

    const body = Object.entries(data).map(([k, v]) => k + ": " + v).join("\\n");
    window.location.href =
      "mailto:" + CONTACT_EMAIL +
      "?subject=" + encodeURIComponent("Access request — " + PRODUCT) +
      "&body=" + encodeURIComponent(body);
  }});
</script>
</body></html>
"""


def card(title, text):
    return (f'<div class="bg-surface-container rounded-xl p-6">'
            f'<h3 class="font-bold mb-3">{title}</h3>'
            f'<p class="text-on-surface-variant text-sm leading-relaxed">{text}</p></div>')


def step(i, title, text):
    return (f'<div class="bg-surface-container rounded-xl p-6">'
            f'<span class="text-[10px] uppercase tracking-widest font-bold text-primary-container">Step {i}</span>'
            f'<h3 class="font-bold mt-3 mb-3">{title}</h3>'
            f'<p class="text-on-surface-variant text-sm leading-relaxed">{text}</p></div>')


def bullet(text):
    return ('<li class="flex gap-3 text-on-surface-variant">'
            '<span class="w-1.5 h-1.5 rounded-full bg-primary-container mt-2 shrink-0"></span>'
            f'<span>{text}</span></li>')


def faq(q, a):
    return (f'<div><h3 class="font-bold mb-2">{q}</h3>'
            f'<p class="text-on-surface-variant leading-relaxed">{a}</p></div>')


for n in NICHES:
    out = HEAD.format(title=n["title"], tagline=n["tagline"], lede_short=n["lede"][:120])
    out += TPL.format(
        title=n["title"],
        tagline=n["tagline"],
        lede=n["lede"],
        problem_title=n["problem_title"],
        problems="".join(card(t, x) for t, x in n["problems"]),
        steps="".join(step(i + 1, t, x) for i, (t, x) in enumerate(n["steps"])),
        gets="".join(bullet(g) for g in n["gets"]),
        price=n["price"],
        price_note=n["price_note"],
        faqs="".join(faq(q, a) for q, a in n["faqs"]),
        product_json=json.dumps(n["title"]),
    )
    d = HERE / n["slug"]
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(out, encoding="utf-8")
    print("wrote", n["slug"], len(out), "bytes")

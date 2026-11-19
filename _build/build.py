"""Builds the Smartech Garage Door Repair website into the parent folder.

Run:  python _build/build.py
GitHub Pages (Jekyll) ignores folders starting with "_", so this script is not published.
"""
import html
import json
from datetime import date
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
SITE_URL = "https://smartechgaragedoor.com"
BRAND = "Smartech Garage Door Repair"
TODAY = date.today().isoformat()

PHONES = {
    "orlando": {"label": "Orlando area", "short": "Orlando", "disp": "(407) 553-9087", "tel": "+14075539087"},
    "tampa": {"label": "Tampa Bay area", "short": "Tampa Bay", "disp": "(813) 519-5168", "tel": "+18135195168"},
}
ORLANDO_CITIES = ["Orlando", "Kissimmee", "Sanford", "Apopka", "Oviedo", "Clermont", "Davenport", "Haines City",
                  "Leesburg", "The Villages", "Ocala", "Deltona", "Daytona Beach", "Ormond Beach", "Port Orange",
                  "New Smyrna Beach", "Titusville", "Cocoa Beach", "Merritt Island", "Melbourne", "Palm Bay"]
TAMPA_CITIES = ["Tampa", "Brandon", "Riverview", "Wesley Chapel", "Land O' Lakes", "Clearwater", "Largo",
                "Pinellas Park", "Palm Harbor", "Tarpon Springs", "Spring Hill", "Brooksville", "Port Richey",
                "Zephyrhills", "Plant City", "Lakeland", "Winter Haven", "Ruskin", "Sun City Center", "Parrish",
                "Bradenton", "Lakewood Ranch", "Sarasota", "Osprey"]

SERVICE_OPTIONS = ["Broken spring", "Opener not working", "Door off track / cable", "$69 tune-up",
                   "New garage door", "Something else"]

e = html.escape


# ---------------------------------------------------------------- services
SERVICES = [
    {
        "slug": "broken-spring-repair", "icon": "&#128297;", "name": "Broken Spring Repair",
        "title": "Broken Garage Door Spring Repair in Orlando & Tampa Bay",
        "desc": "Broken garage door spring? Smartech replaces torsion and extension springs across Orlando and Tampa Bay, often the same day. $100 off any repair.",
        "short": "Torsion and extension spring replacement, balanced and tested.",
        "lead": "Heard a loud bang from the garage and now the door won't lift? That's almost always a broken spring. We replace it fast, often the same day.",
        "body": """
<h2>Signs your garage door spring is broken</h2>
<ul class="tick">
<li>You heard a loud bang from the garage</li>
<li>The door feels extremely heavy or won't open more than a few inches</li>
<li>You can see a gap in the coil above the door</li>
<li>The opener runs but the door doesn't move, or it stops halfway</li>
<li>The door slams down fast when closing</li>
</ul>
<div class="warn"><b>Safety first:</b> garage door springs hold hundreds of pounds of tension. Don't try to adjust or replace one yourself, and avoid running the opener with a broken spring. It can damage the opener and the door.</div>
<h2>What we do</h2>
<p>Most homes have <b>torsion springs</b> mounted above the door, while some older or lighter doors use <b>extension springs</b> along the sides. Our technician will identify your setup, replace the broken spring with one sized to your door's weight, and check the cables, drums and bearings while we're there.</p>
<p>When both springs are the same age, we'll usually recommend replacing them as a pair, since the second one tends to fail soon after the first. We'll explain your options and the price before any work starts.</p>
<p>Before we leave, we balance the door, lubricate the moving parts and test the opener's safety reverse so everything runs smoothly and safely.</p>
""",
        "faq": [("How long does a spring replacement take?", "Most spring replacements are done in about an hour once the technician arrives."),
                ("Can I open the door with a broken spring?", "We don't recommend it. Without the spring, the door is extremely heavy and can fall. If your car is stuck inside, call us and we'll walk you through your options."),
                ("Do you offer a discount?", "Yes. You get $100 off any garage door repair, including spring replacement.")],
    },
    {
        "slug": "garage-door-opener-repair", "icon": "&#9881;&#65039;", "name": "Opener Repair & Replacement",
        "title": "Garage Door Opener Repair & Replacement | Orlando & Tampa Bay",
        "desc": "Garage door opener not working? Smartech repairs and replaces openers, remotes, keypads and safety sensors in Orlando and Tampa Bay.",
        "short": "Openers that won't run, remotes, keypads and safety sensors.",
        "lead": "Opener humming but not lifting? Door reversing for no reason? Remote stopped working? We repair and replace openers of most major brands.",
        "body": """
<h2>Quick checks before you call</h2>
<ul class="tick">
<li>Make sure the opener is plugged in and the outlet has power</li>
<li>Replace the batteries in your remote</li>
<li>Check that the "lock" button on the wall control isn't turned on</li>
<li>Look at the two safety sensors near the floor. Their lights should be on and they should face each other with nothing in between.</li>
</ul>
<p>Still not working? It's time for a technician.</p>
<h2>Opener problems we fix</h2>
<ul class="tick">
<li>Opener hums or clicks but the door doesn't move</li>
<li>Door reverses before it closes all the way</li>
<li>Stripped gears, broken belts or chains</li>
<li>Misaligned or failed safety sensors</li>
<li>Remotes and wall keypads that won't program or respond</li>
<li>Old, loud openers that need to be replaced</li>
</ul>
<p>If a repair makes sense, we'll fix it. If your opener is old and failing, we'll show you replacement options, including quiet belt-drive and smart Wi-Fi openers you can control from your phone.</p>
<div class="warn"><b>Tip:</b> an opener that strains or stops halfway is often a sign of a broken spring or a door that's out of balance, not a bad opener. We'll check the whole system so you only pay for what you need.</div>
""",
        "faq": [("Should I repair or replace my opener?", "If the opener is fairly new, a repair is usually the better value. If it's old, very loud, or the motor is failing, a replacement often costs less in the long run. We'll give you both options."),
                ("Can you install a smart opener?", "Yes. We can install Wi-Fi openers that let you open, close and check your door from your phone."),
                ("Do you program remotes and keypads?", "Yes, we can program new remotes and wall keypads during the visit.")],
    },
    {
        "slug": "cable-off-track-repair", "icon": "&#128736;&#65039;", "name": "Cables & Off-Track Doors",
        "title": "Garage Door Off Track & Broken Cable Repair | Orlando & Tampa Bay",
        "desc": "Garage door off track or cable snapped? Stop using it and call Smartech. We repair cables, rollers and tracks across Orlando and Tampa Bay.",
        "short": "Snapped cables, bent tracks, worn rollers and crooked doors.",
        "lead": "A door hanging crooked or off its track is dangerous. Stop using it, keep people and pets clear, and call us. We'll get it back on track safely.",
        "body": """
<div class="warn"><b>Don't run the opener.</b> If your door is crooked, off track or has a loose cable, using the opener can bend the panels and make the damage much worse.</div>
<h2>Common causes</h2>
<ul class="tick">
<li>A lift cable frayed or snapped</li>
<li>The door was hit by a car</li>
<li>Worn or broken rollers popped out of the track</li>
<li>Bent or loose tracks</li>
<li>A broken spring caused the door to drop unevenly</li>
</ul>
<h2>How we fix it</h2>
<p>Our technician secures the door first, then replaces any damaged cables, rollers or brackets, straightens or replaces bent track sections, and resets the door so it travels smoothly and evenly.</p>
<p>We finish by balancing the door and testing the opener and its safety reverse. You get $100 off any repair.</p>
""",
        "faq": [("Is a door off track an emergency?", "It can be. A door off track can fall. Keep everyone away from it and call us. Same-day service is often available."),
                ("Can you fix a door that was hit by a car?", "Often, yes. Depending on the damage we can replace tracks, rollers or individual panels. If the door is badly damaged, we'll show you replacement options with $500 off a new door.")],
    },
    {
        "slug": "garage-door-tune-up", "icon": "&#10024;", "name": "$69 Tune-Up",
        "title": "$69 Garage Door Tune-Up | Orlando & Tampa Bay",
        "desc": "Keep your garage door safe, quiet and smooth. Smartech's $69 tune-up includes a full safety inspection, spring and cable check, lubrication and hardware tightening.",
        "short": "Full inspection, lubrication and adjustment for just $69.",
        "lead": "Noisy, slow or jerky door? Our $69 tune-up catches small problems before they turn into expensive repairs.",
        "body": """
<h2>What's included</h2>
<ul class="tick">
<li>Full safety inspection of the door and opener</li>
<li>Spring and cable check</li>
<li>Lubrication of hinges, rollers, bearings and springs</li>
<li>Tightening of bolts, brackets and hardware</li>
<li>Door balance check</li>
<li>Safety-reverse and sensor test</li>
</ul>
<h2>Why a tune-up is worth it</h2>
<p>Your garage door is the largest moving part of your home, and it opens and closes thousands of times a year. Florida heat and humidity are hard on springs, rollers and hardware. A yearly tune-up keeps the door quiet, extends the life of the springs and opener, and lets us spot worn parts before they fail.</p>
<p>If we find anything that needs repair, we'll show you and give you the price first. Nothing extra is done without your OK, and you still get $100 off any repair.</p>
""",
        "faq": [("How often should I get a tune-up?", "Once a year is a good rule, or right away if your door gets noisy, slow or jerky."),
                ("How long does it take?", "About 45 minutes to an hour for most doors.")],
    },
    {
        "slug": "new-garage-doors", "icon": "&#127968;", "name": "New Garage Doors",
        "title": "New Garage Door Installation in Orlando & Tampa Bay | $500 Off",
        "desc": "Upgrade your home with a new garage door. Smartech installs steel, insulated and carriage-house style doors across Orlando and Tampa Bay. $500 off a new door.",
        "short": "Steel, insulated and carriage-house styles. $500 off.",
        "lead": "A new garage door can transform the look of your home and fix recurring problems for good. Get $500 off a brand-new door.",
        "body": """
<h2>Styles we install</h2>
<ul class="tick">
<li><b>Steel doors:</b> durable and low-maintenance, in many colors and panel styles</li>
<li><b>Insulated doors:</b> quieter, sturdier and better at keeping Florida heat out of the garage</li>
<li><b>Carriage-house styles:</b> classic look with modern materials</li>
<li><b>Doors with windows:</b> let natural light into the garage</li>
</ul>
<h2>Built for Florida</h2>
<p>Garage doors in Florida need to be rated for local wind requirements. We'll help you choose a door that fits your home, your budget and local code, and we'll handle the removal and haul-away of your old door.</p>
<h2>How it works</h2>
<p>We come out, measure, and walk you through styles and options. Once you pick a door, we schedule the install. Most installs are done in a single visit, including a new opener if you want one.</p>
""",
        "faq": [("How much does a new garage door cost?", "It depends on the size, style and insulation you choose. We'll give you a clear quote after measuring, and you get $500 off."),
                ("Do you remove the old door?", "Yes, removal and haul-away of your old door is part of the install.")],
    },
]


# ---------------------------------------------------------------- building blocks
def rel(depth):
    return "../" * depth


def tel_btn(area, cls="btn"):
    p = PHONES[area]
    return f'<a class="{cls}" href="tel:{p["tel"]}"><small>{p["label"]}</small><b>{p["disp"]}</b></a>'


def quote_form(r, area=None, title="Get a Free Quote", sub="Tell us what's wrong. We'll call you back in minutes."):
    opts_area = "".join(f'<option value="{k}"{" selected" if k == area else ""}>{v["label"]}</option>' for k, v in PHONES.items())
    opts_service = "".join(f"<option>{e(s)}</option>" for s in SERVICE_OPTIONS)
    return f"""<div class="quote-box" id="quote">
<h3>{e(title)}</h3><p class="muted" style="margin:0">{e(sub)}</p>
<form class="quote" data-thanks="{r}thank-you/">
<div class="row"><label>Full name<input name="name" required autocomplete="name"></label>
<label>Phone<input name="phone" type="tel" required autocomplete="tel" inputmode="tel"></label></div>
<div class="row"><label>ZIP code<input name="zip" required inputmode="numeric" pattern="[0-9]{{5}}" maxlength="5" autocomplete="postal-code"></label>
<label>Area<select name="area" required>{'<option value="" disabled selected>Choose your area</option>' if not area else ''}{opts_area}</select></label></div>
<label>What do you need?<select name="service" required><option value="" disabled selected>Choose a service</option>{opts_service}</select></label>
<label>Anything else? (optional)<textarea name="message" rows="2"></textarea></label>
<div class="hp" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></div>
<button class="btn" type="submit">Get My Free Quote</button>
<p class="fine">By submitting, you agree we may call or text you about your request. Msg &amp; data rates may apply. See our <a href="{r}privacy.html">Privacy Policy</a>.</p>
</form></div>"""


def service_cards(r, exclude=None):
    out = []
    for s in SERVICES:
        if s["slug"] == exclude:
            continue
        out.append(f'<a class="card" href="{r}services/#{s["slug"]}"><div class="ic">{s["icon"]}</div>'
                   f'<h3>{e(s["name"])}</h3><p>{e(s["short"])}</p><span class="more">Learn more &rarr;</span></a>')
    return '<div class="cards">' + "".join(out) + "</div>"


def offers():
    return """<div class="offers">
<div class="offer"><div class="big">$69</div><h3>Garage Door Tune-Up</h3><p class="muted">Inspection, spring &amp; cable check, lubrication and hardware tightening.</p></div>
<div class="offer"><div class="big">$100</div><h3>Off Any Repair</h3><p class="muted">Springs, openers, cables, rollers and off-track doors.</p></div>
<div class="offer"><div class="big">$500</div><h3>Off a New Door</h3><p class="muted">Steel, insulated and carriage-house styles, professionally installed.</p></div>
</div>"""


def photo(r, src, alt, badge=True, ratio=None):
    style = f' style="aspect-ratio:{ratio}"' if ratio else ""
    b = (f'<span class="badge"><img src="{r}assets/smartech-icon.png" alt="">Smartech technician</span>' if badge else "")
    return f'<div class="photo"{style}><img src="{r}assets/img/{src}" alt="{e(alt)}" loading="lazy">{b}</div>'


def faq_block(items):
    return '<div class="faq">' + "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in items) + "</div>"


def cta(r):
    return f"""<div class="cta"><div class="wrap"><div><h2>Garage door trouble? We'll fix it fast.</h2>
<p class="muted" style="margin:6px 0 0;color:#C9D5E5">Same-day service often available across Orlando &amp; Tampa Bay.</p></div>
<div class="calls" style="margin:0">{tel_btn("orlando")}{tel_btn("tampa", "btn blue")}</div></div></div>"""


def header(r):
    return f"""<header class="top"><div class="wrap">
<a class="logo" href="{r}" aria-label="{BRAND} home"><img src="{r}assets/smartech-logo.png" alt="{BRAND}" width="226" height="70"></a>
<button class="menu-btn" aria-label="Menu" aria-expanded="false">&#9776;</button>
<nav class="nav"><a href="{r}services/">Services</a><a href="{r}areas/">Service Areas</a>
<a href="{r}contact/">Contact</a><a class="btn" href="{r}contact/#quote">Get a Free Quote</a></nav>
</div></header>"""


def footer(r):
    svc = "".join(f'<li><a href="{r}services/#{s["slug"]}">{e(s["name"])}</a></li>' for s in SERVICES)
    return f"""<footer><div class="wrap"><div class="grid">
<div><a class="logo" href="{r}"><img src="{r}assets/smartech-logo-white.png" alt="{BRAND}"></a>
<p>Fast, reliable garage door repair and installation across Central &amp; West Florida.</p></div>
<div><h4>Services</h4><ul>{svc}</ul></div>
<div><h4>Service Areas</h4><ul><li><a href="{r}areas/#orlando">Orlando area</a></li><li><a href="{r}areas/#tampa-bay">Tampa Bay area</a></li></ul>
<h4 style="margin-top:18px">Company</h4><ul><li><a href="{r}contact/">Contact</a></li><li><a href="{r}privacy.html">Privacy Policy</a></li></ul></div>
<div><h4>Call us</h4><ul><li>Orlando area<br><a href="tel:{PHONES['orlando']['tel']}"><b>{PHONES['orlando']['disp']}</b></a></li>
<li style="margin-top:10px">Tampa Bay area<br><a href="tel:{PHONES['tampa']['tel']}"><b>{PHONES['tampa']['disp']}</b></a></li></ul></div>
</div><div class="bottom"><span>&copy; {date.today().year} {BRAND}. All rights reserved.</span><span><a href="{r}privacy.html">Privacy Policy</a></span></div></div></footer>
<div class="callbar"><a href="tel:{PHONES['orlando']['tel']}"><small>Orlando area</small>Call {PHONES['orlando']['disp']}</a>
<a class="blue" href="tel:{PHONES['tampa']['tel']}"><small>Tampa Bay area</small>Call {PHONES['tampa']['disp']}</a></div>
<script src="{r}assets/site.js" defer></script>"""


def business_schema():
    return {
        "@context": "https://schema.org", "@type": "HomeAndConstructionBusiness", "name": BRAND,
        "url": SITE_URL + "/", "logo": SITE_URL + "/assets/smartech-logo.png",
        "image": SITE_URL + "/assets/img/work-tuneup-1.jpg", "telephone": PHONES["orlando"]["tel"],
        "priceRange": "$$",
        "areaServed": [{"@type": "City", "name": c + ", FL"} for c in ORLANDO_CITIES + TAMPA_CITIES],
        "contactPoint": [{"@type": "ContactPoint", "telephone": p["tel"], "contactType": "customer service",
                          "areaServed": "US-FL", "name": p["label"]} for p in PHONES.values()],
        "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"]}} for s in SERVICES],
    }


SITEMAP = []


def write(path, title, desc, body, depth, noindex=False, schema=None, priority="0.7"):
    r = rel(depth)
    url = SITE_URL + "/" + (path[:-len("index.html")] if path.endswith("index.html") else path)
    schemas = [business_schema()] + ([schema] if schema else [])
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    doc = f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">{'<meta name="robots" content="noindex">' if noindex else ''}
<meta property="og:type" content="website"><meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE_URL}/assets/facebook-profile-1080.png">
<meta name="theme-color" content="#0B1F3A">
<link rel="icon" href="{r}assets/smartech-icon.png"><link rel="apple-touch-icon" href="{r}assets/smartech-icon.png">
<link rel="stylesheet" href="{r}assets/site.css">{ld}
</head><body>
{header(r)}
<main>{body}</main>
{footer(r)}
</body></html>
"""
    f = OUT / path
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(doc, encoding="utf-8")
    if not noindex:
        SITEMAP.append((url, priority))


def hero(r, h1, lead, crumbs=None, pill=None, img="work-tuneup-1.jpg", right=None, small=False):
    bc = ""
    if crumbs:
        bc = '<div class="breadcrumb">' + " / ".join(f'<a href="{u}">{e(t)}</a>' if u else e(t) for t, u in crumbs) + "</div>"
    left = f"""{bc}{f'<span class="pill">{pill}</span>' if pill else ''}<h1>{h1}</h1><p class="lead">{lead}</p>
<div class="calls">{tel_btn("orlando")}{tel_btn("tampa", "btn blue")}</div>
<ul class="checks"><li>Same-day service often available</li><li>Trained local technicians</li><li>Price before work starts</li></ul>"""
    inner = f'<div class="split hero-split">{"<div>" + left + "</div>"}{right}</div>' if right else left
    return (f'<section class="hero{" page-hero" if small else ""}" style="background-image:url({r}assets/img/{img})">'
            f'<div class="wrap">{inner}</div></section>')


def crumb_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE_URL + u}
                                for i, (n, u) in enumerate(items)]}


def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


# ---------------------------------------------------------------- pages
HOME_FAQ = [
    ("How fast can you get here?", "Same-day service is often available in both the Orlando and Tampa Bay areas. Call or send a quote request and we'll give you the earliest time we have."),
    ("How much does a garage door repair cost?", "It depends on the problem and the parts needed. We'll give you the price before any work starts, and you get $100 off any repair."),
    ("Do you work in my city?", "We serve the Orlando area (including Kissimmee, Sanford, Daytona, Melbourne and Ocala) and the Tampa Bay area (including Brandon, Clearwater, Lakeland, Bradenton and Sarasota). See our service areas page for the full list."),
    ("What's included in the $69 tune-up?", "A full safety inspection, spring and cable check, lubrication of all moving parts, hardware tightening and a safety-reverse test."),
    ("Should I fix a broken spring myself?", "No. Garage door springs are under extreme tension and can cause serious injury. Leave spring work to a trained technician."),
]


def build_home():
    r = rel(0)
    body = hero(r, 'Garage Door Repair <span>Done Right.</span>',
                "Broken springs, openers, cables and off-track doors fixed fast by trained local technicians across the Orlando &amp; Tampa Bay areas.",
                pill="NOW SERVING ORLANDO &amp; TAMPA BAY", right=quote_form(r))
    body += f"""<section class="alt"><div class="wrap"><div class="section-head"><h2>Current Specials</h2>
<p class="muted">Mention the offer when you call or book online.</p></div>{offers()}</div></section>
<section id="services"><div class="wrap"><div class="section-head"><h2>Garage Door Services</h2>
<p class="muted">From a quick tune-up to a brand-new door, we handle it all.</p></div>{service_cards(r)}</div></section>
<section class="alt"><div class="wrap split"><div><h2>Why homeowners choose Smartech</h2>
<ul class="tick"><li><b>Fast response.</b> Same-day service is often available, because a stuck garage door can't wait.</li>
<li><b>Clear pricing.</b> You'll know the price before any work starts. No surprises.</li>
<li><b>Done right the first time.</b> We check the whole system (springs, cables, rollers and opener), not just the part that broke.</li>
<li><b>Real savings.</b> $69 tune-ups, $100 off any repair and $500 off new doors.</li>
<li><b>Local to you.</b> Technicians across the Orlando and Tampa Bay areas.</li></ul>
<a class="btn" href="{r}contact/#quote">Get a Free Quote</a></div>
{photo(r, "work-tuneup-2.jpg", "Smartech technician servicing a garage door", ratio="4/3")}</div></section>
<section class="dark"><div class="wrap"><div class="section-head"><h2>How it works</h2><p class="muted">Getting your door fixed is easy.</p></div>
<div class="steps"><div class="step"><h3>Call or request a quote</h3><p class="muted">Tell us what's wrong. It takes less than a minute.</p></div>
<div class="step"><h3>We come to you</h3><p class="muted">A technician arrives, diagnoses the problem and gives you the price first.</p></div>
<div class="step"><h3>Fixed and tested</h3><p class="muted">We repair, balance and safety-test the door before we leave.</p></div></div></div></section>
<section><div class="wrap"><div class="section-head"><h2>Areas We Serve</h2><p class="muted">Call the number for your area for the fastest service.</p></div>
<div class="areas"><div class="area"><h3>Orlando Area</h3><p class="muted">{e(", ".join(ORLANDO_CITIES[:12]))} and nearby cities.</p>
<a class="tel" href="tel:{PHONES['orlando']['tel']}">{PHONES['orlando']['disp']}</a><p style="margin:10px 0 0"><a href="{r}areas/#orlando">See all Orlando-area cities &rarr;</a></p></div>
<div class="area"><h3>Tampa Bay Area</h3><p class="muted">{e(", ".join(TAMPA_CITIES[:12]))} and nearby cities.</p>
<a class="tel" href="tel:{PHONES['tampa']['tel']}">{PHONES['tampa']['disp']}</a><p style="margin:10px 0 0"><a href="{r}areas/#tampa-bay">See all Tampa Bay cities &rarr;</a></p></div></div></div></section>
<section class="alt"><div class="wrap"><div class="section-head"><h2>Our Work</h2><p class="muted">Real jobs from our technicians.</p></div>
<div class="gallery">{photo(r, "work-install-1.jpg", "Garage door installation in progress")}{photo(r, "work-repair-1.jpg", "Technicians repairing a garage door")}{photo(r, "work-tuneup-1.jpg", "Garage door tune-up and inspection")}</div></div></section>
<section><div class="wrap"><div class="section-head"><h2>Frequently Asked Questions</h2></div>{faq_block(HOME_FAQ)}</div></section>
{cta(r)}"""
    write("index.html", f"{BRAND} | Orlando & Tampa Bay Garage Door Repair",
          "Fast garage door repair in Orlando and Tampa Bay: broken springs, openers, cables, off-track doors and new doors. $69 tune-up, $100 off any repair.",
          body, 0, schema=faq_schema(HOME_FAQ), priority="1.0")


def build_services():
    r = rel(1)
    body = hero(r, "Garage Door <span>Services</span>",
                "Everything your garage door needs, from a quick tune-up to a full replacement. Jump to a service below.",
                crumbs=[("Home", r), ("Services", None)], small=True, img="work-repair-1.jpg")
    jump = "".join(f'<a class="btn blue" style="padding:9px 16px;font-size:15px" href="#{s["slug"]}">{e(s["name"])}</a>' for s in SERVICES)
    body += f'<section style="padding:28px 0"><div class="wrap" style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center">{jump}</div></section>'
    imgs = ["work-repair-1.jpg", "work-install-2.jpg", "work-install-1.jpg", "work-tuneup-2.jpg", "work-tuneup-1.jpg"]
    all_faq = []
    for i, s in enumerate(SERVICES):
        cls = "alt" if i % 2 == 0 else ""
        content = s["body"].replace("<h2>", "<h3>").replace("</h2>", "</h3>")
        pic = photo(r, imgs[i], f"Smartech technician: {s['name'].lower()}", ratio="4/3")
        body += f"""<section class="{cls}" id="{s['slug']}" style="scroll-margin-top:80px"><div class="wrap split" style="align-items:start">
<div><span class="pill">{s['icon']} {e(s['name'].upper())}</span><h2>{e(s['title'].split(' | ')[0])}</h2><p class="lead" style="font-size:19px">{s['lead']}</p>{content}
<a class="btn" href="#quote">Get a Free Quote</a></div><div>{pic}</div></div></section>"""
        all_faq += s["faq"]
    body += f"""<section class="dark"><div class="wrap split" style="align-items:start"><div><h2>Service questions</h2>
<p class="muted">Quick answers about repairs, tune-ups and new doors.</p>{faq_block(all_faq).replace('class="faq"', 'class="faq" style="color:#0B1F3A"')}</div>
<div class="stick">{quote_form(r)}</div></div></section>"""
    write("services/index.html", f"Garage Door Repair & Installation Services | {BRAND}",
          "Spring repair, opener repair, cables and off-track doors, $69 garage door tune-ups and new door installation in Orlando and Tampa Bay.",
          body, 1, schema=faq_schema(all_faq), priority="0.9")


def build_areas():
    r = rel(1)
    body = hero(r, "Service <span>Areas</span>",
                "Smartech technicians cover two regions of Florida. Find your city below and call the number for your area for the fastest service.",
                crumbs=[("Home", r), ("Service Areas", None)], small=True, img="work-install-2.jpg")
    for i, (slug, key, name, cities, blurb) in enumerate([
        ("orlando", "orlando", "Orlando Area", ORLANDO_CITIES,
         "From Orlando and Kissimmee out to the Space Coast, Volusia County and Ocala, our Orlando-area team handles springs, openers, cables, tune-ups and new doors."),
        ("tampa-bay", "tampa", "Tampa Bay Area", TAMPA_CITIES,
         "Our Tampa Bay team covers Hillsborough, Pinellas, Pasco, Polk, Manatee and Sarasota counties, from Spring Hill down to Osprey."),
    ]):
        p = PHONES[key]
        body += f"""<section class="{'alt' if i == 0 else ''}" id="{slug}" style="scroll-margin-top:80px"><div class="wrap split" style="align-items:start">
<div><h2>{name}</h2><p>{blurb}</p><ul class="cities">{''.join(f'<li>{e(c)}</li>' for c in cities)}</ul>
<p style="margin-top:22px">Call <a class="tel" style="font-size:24px;font-weight:700;color:var(--orange);text-decoration:none" href="tel:{p['tel']}">{p['disp']}</a></p></div>
<div>{quote_form(r, area=key, title=f"Free Quote: {name}")}</div></div></section>"""
    body += f'<section><div class="wrap center"><h2>Not on the list?</h2><p class="muted">We often cover nearby towns too. Give us a call and ask.</p></div></section>{cta(r)}'
    write("areas/index.html", f"Garage Door Repair Service Areas: Orlando & Tampa Bay | {BRAND}",
          "Smartech serves the Orlando area (Kissimmee, Sanford, Daytona, Melbourne, Ocala) and the Tampa Bay area (Brandon, Clearwater, Lakeland, Bradenton, Sarasota).",
          body, 1, priority="0.8")


def build_simple_pages():
    r = rel(1)
    body = hero(r, "Get a <span>Free Quote</span>",
                "Fill out the form and we'll call you back in minutes, or call the number for your area right now.",
                crumbs=[("Home", r), ("Contact", None)], small=True, right=quote_form(r))
    body += f"""<section><div class="wrap"><div class="areas">
<div class="area"><h3>Orlando Area</h3><a class="tel" href="tel:{PHONES['orlando']['tel']}">{PHONES['orlando']['disp']}</a><p class="muted" style="margin-top:8px">Call or text. Orlando, Kissimmee, Sanford, Daytona, Melbourne, Ocala and nearby.</p></div>
<div class="area"><h3>Tampa Bay Area</h3><a class="tel" href="tel:{PHONES['tampa']['tel']}">{PHONES['tampa']['disp']}</a><p class="muted" style="margin-top:8px">Call or text. Tampa, Brandon, Clearwater, Lakeland, Bradenton, Sarasota and nearby.</p></div>
</div></div></section>
<section class="alt"><div class="wrap split"><div><h2>What happens next</h2><ul class="tick">
<li>We call you back, usually within minutes during business hours</li><li>We ask a few questions about the problem and set a time</li>
<li>A technician arrives, diagnoses the door and gives you the price before starting</li></ul></div>
{photo(r, "work-install-1.jpg", "Smartech technicians at work", ratio="4/3")}</div></section>"""
    write("contact/index.html", f"Contact & Free Quote | {BRAND}",
          "Request a free garage door quote or call Smartech in Orlando (407) 553-9087 or Tampa Bay (813) 519-5168.", body, 1, priority="0.8")

    body = f"""<section class="hero page-hero" style="background-image:url({r}assets/img/work-tuneup-1.jpg)"><div class="wrap">
<span class="pill blue">REQUEST RECEIVED</span><h1>Thanks! We'll call you <span>in a few minutes.</span></h1>
<p class="lead">A Smartech team member will call you shortly to confirm your appointment. Need help right now? Call us:</p>
<div class="calls">{tel_btn("orlando")}{tel_btn("tampa", "btn blue")}</div></div></section>"""
    write("thank-you/index.html", f"Thank You | {BRAND}", "Thanks for your request.", body, 1, noindex=True)

def build_privacy():
    r = rel(0)
    body = f"""<section><div class="wrap" style="max-width:800px"><h1>Privacy Policy</h1><p class="muted">Last updated: November 19, 2026</p>
<p>{BRAND} ("Smartech", "we", "us") respects your privacy. This policy explains what information we collect when you contact us or request service, including through our website and our Facebook and Instagram ads and forms, and how we use it.</p>
<h2>Information we collect</h2><ul><li>Contact details you give us, such as your name, phone number, email address and ZIP code or service address.</li>
<li>Details about your service request, such as the type of garage door problem and your preferred time.</li>
<li>Call and text records when you call or text our phone numbers. Calls may be recorded for quality assurance.</li>
<li>Basic website usage data, such as pages visited, collected through cookies and similar tools.</li></ul>
<h2>How we use your information</h2><ul><li>To contact you by phone, text message or email about your service request, quote or appointment.</li>
<li>To schedule and perform garage door repair, maintenance and installation services.</li><li>To improve our service and measure how our advertising performs.</li></ul>
<h2>How we share your information</h2><p>We share your information only with the technicians and service partners who perform the service you requested, and with service providers that help us run our business (for example, call tracking, scheduling and email tools). <b>We do not sell your personal information.</b></p>
<h2>Text messages</h2><p>If you give us your phone number, you agree that we may call or text you about your request. Message and data rates may apply. Reply <b>STOP</b> to opt out of texts at any time.</p>
<h2>Data retention and your choices</h2><p>We keep your information only as long as needed to provide service and meet legal obligations. You can ask us to access, correct or delete your information, or to stop contacting you, by calling or texting us.</p>
<h2>Contact us</h2><p>{BRAND}<br>Orlando area: <a href="tel:{PHONES['orlando']['tel']}">{PHONES['orlando']['disp']}</a><br>Tampa Bay area: <a href="tel:{PHONES['tampa']['tel']}">{PHONES['tampa']['disp']}</a></p></div></section>"""
    write("privacy.html", f"Privacy Policy | {BRAND}", "How Smartech Garage Door Repair collects and uses your information.", body, 0, priority="0.2")


def build_404():
    # GitHub Pages serves this for any missing path, so links must be absolute from the site root.
    body = f"""<section class="hero page-hero" style="background-image:url(/assets/img/work-tuneup-1.jpg)"><div class="wrap">
<h1>Page not <span>found</span></h1><p class="lead">The page you're looking for doesn't exist. Head back home or call us.</p>
<div class="calls"><a class="btn ghost" href="/">Back to home</a>{tel_btn("orlando")}{tel_btn("tampa", "btn blue")}</div></div></section>"""
    write("404.html", f"Page Not Found | {BRAND}", "Page not found.", body, 0, noindex=True)
    f = OUT / "404.html"
    f.write_text(f.read_text(encoding="utf-8").replace('href="assets/', 'href="/assets/').replace('src="assets/', 'src="/assets/')
                 .replace('href=""', 'href="/"').replace('href="services/', 'href="/services/').replace('href="areas/', 'href="/areas/')
                 .replace('href="contact/', 'href="/contact/').replace('href="privacy.html', 'href="/privacy.html')
                 .replace('data-thanks="thank-you/', 'data-thanks="/thank-you/'), encoding="utf-8")


def build_meta_files():
    urls = "".join(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod><priority>{p}</priority></url>" for u, p in SITEMAP)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n', encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    for old in ("style.css",):
        (OUT / old).unlink(missing_ok=True)
    build_home()
    build_services()
    build_areas()
    build_simple_pages()
    build_privacy()
    build_404()
    build_meta_files()
    print("pages:", len(SITEMAP), "indexed +", "thank-you, 404")

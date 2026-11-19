# Generates the static pages for myhomebistro.in.
# Edit the text below, then run:  python build.py
from pathlib import Path
import time

ROOT = Path(__file__).parent
EMAIL = "myhomebistro.shikha@gmail.com"
PHONE = "+919892386700"
PHONE_SHOW = "+91 98923 86700"
INSTA = "https://www.instagram.com/myhomebistro.shikha"
FB = "https://www.facebook.com/myhomebistro.shikha/"

PAGES = [("index.html", "Home"), ("our-story.html", "Our Story"),
         ("services.html", "Services"), ("gallery.html", "Gallery"),
         ("contact.html", "Contact")]


def layout(file, title, body, desc="Experience fine dining at your home"):
    nav = "".join(
        f'<li><a href="{f}"{" class=\"active\"" if f == file else ""}>{t}</a></li>'
        for f, t in PAGES)
    full_title = "myhomebistro | " + (desc if file == "index.html" else title)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}. Fine dining at home by Chef Shikha.">
<link rel="icon" href="images/cropped-SHIKHA-logo-1-e1523634897971.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css?v={int(time.time())}">
</head>
<body>
<header class="site-header">
  <div class="nav-wrap">
    <a class="logo" href="index.html"><img src="images/SHIKHA-logo1.png" alt="myhomebistro"></a>
    <button class="nav-toggle" aria-label="Menu" onclick="document.querySelector('nav').classList.toggle('open')">&#9776;</button>
    <nav><ul>{nav}</ul></nav>
  </div>
</header>
<main>
{body}
</main>
<footer>Copyright 2026 Myhomebistro.&nbsp;&nbsp; All Rights Reserved.</footer>
</body>
</html>
"""


def card(img, label, text=""):
    cap = f"<strong>{label}</strong>{text}"
    return (f'<figure class="card" data-cat="{label}"><img src="images/{img}" '
            f'alt="{text or label}"><figcaption>{cap}</figcaption></figure>')


HOME_GRID = [
    ("IMG_3293.jpg", "PLAT (Vegetarian)", "Moong gourd with bulgar, onion sauce and coriander pesto"),
    ("IMG_3308.jpg", "POISSON", "Rawas with snap peas"),
    ("IMG_3298.jpg", "SOUP", "Soup verde with coconut milk and sea weed"),
    ("FullSizeRender_2.jpg", "DESSERT", "Entremet au chocolate"),
    ("IMG_3287.jpg", "SALAD", "Plum salad with fruit chutney and goat cheese"),
    ("IMG_4794.jpg", "DESSERT", "Strawberry tart"),
    ("FullSizeRender.jpg", "OEUF", "Free range egg with pea hummus and hollandaise sauce"),
    ("FullSizeRender_3.jpg", "AMUSE BOUCHE", "Parmesan biscuit with avocado mayonnaise, cherry tomato and roquette pesto"),
    ("FullSizeRender_1.jpg", "POISSON", "Shrimps with smoked mango salsa"),
]

GALLERY = [
    ("IMG_3288.jpg", "AMUSE BOUCHE", "Cucumber tartare with four avatars of lemon"),
    ("FullSizeRender12.jpg", "AMUSE BOUCHE", "Antipasto plate (Chicken liver pâté, black olive tapenade, onion jam &amp; sun dried tomato with hot pepper)"),
    ("FullSizeRender10.jpg", "SALAD", "Balsamic vinegar strawberry with mixed leaves, feta and roquette pesto"),
    ("FullSizeRender11.jpg", "SALAD", "Mixed melons with moras leaves and watermelon jus"),
    ("FullSizeRender5.jpg", "SOUP", "Oyster mushroom and butter beans"),
    ("IMG_3336.jpg", "POISSON FISH", "Pomfret with cucumber and tonka beans infused fumet"),
    ("IMG_3337.jpg", "POISSON FISH", "Shrimps with red cabbage gel and celery boule"),
    ("FullSizeRender6.jpg", "OEUF EGG", "Poached organic egg with asparagus and hollandaise"),
    ("FullSizeRender7.jpg", "PLAT VEGETARIAN", "Zucchini fritters with romesco and parmesan crumble"),
    ("FullSizeRender8.jpg", "PLAT VEGETARIAN", "Risotto with portobello mushroom, waterchestnut purée and truffle oil"),
    ("IMG_3317.jpg", "PLAT NON VEGETARIAN", "Turkish spice rubbed chicken with spaghetti aglio olio"),
    ("FullSizeRender9.jpg", "PLAT NON VEGETARIAN", "Coq au vin with mashed potato, bacon crisps and parmesan crumble"),
    ("IMG_3289.jpg", "DESSERT", "Cotton cake with poached peaches and cream anglaise"),
    ("FullSizeRender4.jpg", "DESSERT", "White chocolate and coconut panacotta with mango mousse, passion fruit sauce"),
]

MASONRY_JS = """<script>
// Place each photo in the shortest column, left to right (like the original site).
function layoutMasonry() {
  const box = document.querySelector('.masonry');
  const cards = [...box.querySelectorAll('.card')];
  const n = innerWidth <= 480 ? 1 : innerWidth <= 1000 ? 2 : 3;
  box.innerHTML = '';
  const cols = Array.from({length: n}, () => box.appendChild(Object.assign(document.createElement('div'), {className: 'mcol'})));
  const h = new Array(n).fill(0);
  cards.forEach(c => {
    const img = c.querySelector('img');
    const i = h.indexOf(Math.min(...h));
    cols[i].appendChild(c);
    h[i] += (img.naturalHeight / img.naturalWidth) || 1;
  });
}
addEventListener('load', layoutMasonry);
let rt; addEventListener('resize', () => { clearTimeout(rt); rt = setTimeout(layoutMasonry, 150); });
</script>"""

home = f"""
<div class="home">
  <section class="home-text">
    <h2>Bonjour!</h2>
    <p>With <em>myhomebistro</em> you can enjoy a fine dining experience at your home. Our team will carefully tailor a unique experience for your needs. Book with us to make a memorable meal with your loved ones.</p>
    <p>We curate our menu around seasonal produce. A typical sit-down lunch or dinner will be around 3 to 5 courses. Don’t worry about table linen, cutlery or the right wine glass – we have it covered! You don’t have to do a thing – except to sit back and enjoy our carefully crafted meals.</p>
  </section>
  <div class="masonry">{''.join(card(*c) for c in HOME_GRID)}</div>
</div>
{MASONRY_JS}
"""

story = """
<div class="story">
  <img src="images/IMG_4783.jpg" alt="Chef Shikha in the kitchen">
  <div class="story-text">
    <p>As long as I remember I have loved big family dinners. Food can be a great way to bond with family and friends. It can also be an escape into something exotic and new. I found my true passion for cooking when I started creating exotic food for my family and friends. This interest to cook took me to Paris where I attended a culinary school, Ferrandi and trained to become a professional Chef. My hunger to learn also took me to work at Michelin and Bib Gourmet restaurants like Fäviken in Sweden and Kokoro in Paris.</p>
    <p>In 2017 I started <em>myhomebistro</em> in order to make my passion into my living. With <em>myhomebistro</em> I provide the opportunity for everyone to experience fine dining at your own home. I believe that some of the most exquisite tastes in cooking come from local and seasonal produce. And I am passionate about bringing the natural tastes into my food. This is best described in my favourite movie <em>Burnt.</em></p>
    <p>“It was God who created oysters and apples. And you can’t improve recipes like that. But it’s our job to try.”</p>
    <p>Shikha</p>
  </div>
</div>
"""

services = """
<div class="services">
  <div class="services-photos">
    <img class="small" src="images/IMG_3295.jpg" alt="Table set for a myhomebistro dinner">
    <img src="images/IMG_3301.jpg" alt="Table setting with flowers">
    <img src="images/IMG_3330.jpg" alt="Printed menu at a place setting">
  </div>
  <div class="services-text">
    <p>Our menu is curated around what is available seasonally. A typical sit-down lunch or dinner will be from 3 to 5 courses. We also pair the wine with the courses. A 3 course comes with one glass of wine and a 5 course comes with two glasses of wine.</p>
    <p>We provide table linen, cutlery, glasses, plates and everything else needed on the table to make this experience a memorable one.</p>
  </div>
</div>
"""

cats = []
for _, c, _ in GALLERY:
    if c not in cats:
        cats.append(c)
filters = '<button class="active" data-f="*">Show All</button>' + "".join(
    f'<button data-f="{c}">{c}</button>' for c in cats)
gallery = f"""
<div class="filters">{filters}</div>
<div class="grid gallery-grid">{''.join(card(*c) for c in GALLERY)}</div>
<div class="lightbox" onclick="this.classList.remove('open')"><div><img alt=""><p></p></div></div>
<script>
document.querySelectorAll('.filters button').forEach(b => b.onclick = () => {{
  document.querySelectorAll('.filters button').forEach(x => x.classList.toggle('active', x === b));
  document.querySelectorAll('.card').forEach(c =>
    c.classList.toggle('hidden', b.dataset.f !== '*' && c.dataset.cat !== b.dataset.f));
}});
const lb = document.querySelector('.lightbox');
document.querySelectorAll('.card').forEach(c => c.onclick = () => {{
  lb.querySelector('img').src = c.querySelector('img').src;
  lb.querySelector('p').textContent = c.querySelector('img').alt;
  lb.classList.add('open');
}});
</script>
"""

ICON_MAIL = '<svg viewBox="0 0 24 24" fill="#dd4b39"><path d="M12 11v2.4h3.97c-.16 1.03-1.2 3.02-3.97 3.02-2.39 0-4.34-1.98-4.34-4.42S9.61 7.58 12 7.58c1.36 0 2.27.58 2.79 1.08l1.9-1.83C15.47 5.69 13.89 5 12 5 8.13 5 5 8.13 5 12s3.13 7 7 7c4.04 0 6.72-2.84 6.72-6.84 0-.46-.05-.81-.11-1.16H12z"/><path d="M22 11h-2V9h-1.5v2h-2v1.5h2v2H20v-2h2z"/></svg>'
ICON_IG = '<svg viewBox="0 0 24 24" fill="none" stroke="#c13584" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="#c13584"/></svg>'
ICON_FB = '<svg viewBox="0 0 24 24" fill="#3b5bdb"><path d="M14 8V6.5c0-.8.2-1.5 1.5-1.5H17V2h-2.6C11.6 2 11 4 11 5.8V8H9v3h2v11h3V11h2.5l.5-3z"/></svg>'
ICON_TEL = '<svg viewBox="0 0 24 24" fill="#fff"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>'

contact = f"""
<ul class="contact">
  <li>{ICON_MAIL}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
  <li>{ICON_IG}<a href="{INSTA}" target="_blank" rel="noopener">{INSTA}</a></li>
  <li>{ICON_FB}<a href="{FB}" target="_blank" rel="noopener">{FB}</a></li>
  <li>{ICON_TEL}<a href="tel:{PHONE}">Call Now</a></li>
</ul>
"""

for (f, t), body in zip(PAGES, [home, story, services, gallery, contact]):
    (ROOT / f).write_text(layout(f, t, body), encoding="utf-8")
print("Built", len(PAGES), "pages")

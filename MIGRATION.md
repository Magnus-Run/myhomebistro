# Moving myhomebistro.in to GitHub Pages

Current setup (checked November 2026): WordPress at HostGator, managed by a third party.
GoDaddy holds the domain, but its nameservers point to HostGator, so HostGator controls DNS today.

## 1. Put the site on GitHub (free)
1. Create a GitHub account and a **public** repository, e.g. `myhomebistro`.
2. Upload everything in this `website` folder (drag and drop on github.com works). `build.py` can stay.
3. Repo → Settings → Pages → Source: "Deploy from a branch", branch `main`, folder `/ (root)`.
4. After about a minute the site is live at `https://<username>.github.io/myhomebistro/`. Check it.
5. Settings → Pages → Custom domain: `myhomebistro.in`. (This creates a `CNAME` file.)

## 2. Point the domain (in GoDaddy, no HostGator password needed)
1. GoDaddy → My Products → myhomebistro.in → DNS → **Nameservers → Change → "GoDaddy default"**.
   This takes control of DNS away from HostGator. The old site stops working after this, so do step 1 first.
2. In GoDaddy DNS, add the records:

| Type | Name | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | `<username>.github.io` |

3. Wait up to 24 to 48 hours. Then in GitHub Pages settings tick **Enforce HTTPS**.

## 3. Email on the domain (e.g. shikha@myhomebistro.in)
Pick one, then add the MX/TXT records it gives you in GoDaddy DNS:
- **Zoho Mail Forever Free**: up to 5 mailboxes, web and app. Free.
- **Google Workspace**: Gmail on your own domain, about INR 140 per user per month.
- **Cloudflare / ImprovMX forwarding**: free; forwards to the existing Gmail, no new inbox.

Once it works, change `EMAIL` at the top of `build.py`, run `python build.py`, and upload again.

## 4. Tell the current web person
Ask them for a full backup (files + database) before cancelling HostGator, just in case, and to cancel the hosting after the new site is live.

## Editing the site later
Edit the text in `build.py`, run `python build.py`, upload the changed `.html` files to GitHub.

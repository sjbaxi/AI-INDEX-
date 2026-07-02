# NSE AI Index

A self-updating, market-cap-weighted index of NSE-listed companies where AI
is the core business — a companion to the logistics index, same mechanism:
a scheduled job fetches quotes and commits results **whether or not anyone
is viewing the site**, and a static page displays the latest snapshot.

## Screening criteria — read this first

You asked for companies that are **100% AI, or where AI business lines
exceed 50% of revenue**. Unlike logistics (which NSE tags with clear sector
codes), there is no official "AI company" classification on NSE/SEBI — so
this list is judgment-based, built from public disclosures and press
coverage of each company's revenue mix, not a regulatory field.

Current constituents (`scripts/companies.py`):

| Symbol | Company | Confidence | Why |
|---|---|---|---|
| FRACTAL | Fractal Analytics | **High** | IPO'd Feb 2026, widely reported as India's first pure-play AI listing on NSE/BSE. |
| LATENTVIEW | Latent View Analytics | Borderline | Company commentary (FY26) cited roughly **half** of revenue from AI projects — right at the threshold, not a clean majority. |
| HAPPSTMNDS | Happiest Minds Technologies | Borderline | Self-described "AI-first"; ~97% of revenue is digital/cloud/**AI**-driven combined — bundled, not an AI-only breakout. |
| NETWEB | Netweb Technologies | Borderline | AI/HPC infrastructure manufacturer, often called India's only listed AI-infra pure-play; but its own **AI-systems** product segment was ~43% of revenue (up from 15%) — just under a clean majority by that narrow measure. |

**None of the borderline three have a company-disclosed "AI revenue: >50%"
figure I could verify with confidence** — the underlying numbers are close
to the line, reported inconsistently, and mixed with adjacent categories
(cloud, digital transformation, HPC). I've included them because they're
consistently described in market commentary as AI-core businesses, but
flagged them so you can decide for yourself rather than take that framing
on faith. If your bar is strictly "audited financials show >50% AI revenue,
full stop," you may want to run with FRACTAL alone until more companies
disclose a clean AI-revenue split, or IPO as AI pure-plays (this is a young
and fast-changing list — expect more entrants like Fractal over time).

Edit `scripts/companies.py` to add, remove, or reclassify any company —
each entry has a `note` and `confidence` field designed to be edited.

## How it works

Same architecture as the logistics index:

- `scripts/companies.py` — the master list + screening rationale (above).
- `scripts/establish_base.py` — **run once**. Computes each constituent's
  price on the base date (1 April 2023) and locks in share counts, writing
  `base.json` with a divisor. Since most of these companies IPO'd *after*
  April 2023 (Fractal, Netweb) — this is a young sector — their "base
  price" is a first-trade-day proxy, flagged `baseIsProxy: true`.
- `scripts/fetch_quotes.py` — runs on schedule, computes current prices,
  market cap in ₹ crore, and the index level:
  `index_value = (Σ price × locked_shares) / divisor`.
- `.github/workflows/update-quotes.yml` — runs every 15 minutes during NSE
  trading hours (9:15 AM–3:30 PM IST, Mon–Fri) and commits `data.json`.
- `.github/workflows/establish-base.yml` — manual-only, runs
  `establish_base.py` and commits `base.json`.
- `index.html` — index-value banner up top, compact table below sorted by
  market cap descending, with a confidence badge and screening note per row
  so the judgment call stays visible, not hidden behind the numbers.

## Deploy it (free, ~5 minutes)

1. **Create a new GitHub repository** and push these files:
   ```bash
   cd nse-ai-index-app
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo>.git
   git push -u origin main
   ```

2. **Enable GitHub Pages**: repo → Settings → Pages → Source: "Deploy from a
   branch" → Branch: `main`, folder `/ (root)` → Save.

3. **Allow the workflow to push changes**: repo → Settings → Actions →
   General → "Workflow permissions" → "Read and write permissions" → Save.

4. **Establish the index base**: Actions tab → "Establish index base" →
   "Run workflow". This computes `base.json`.

5. **Kick off the first quote fetch**: Actions tab → "Update NSE AI Index
   quotes" → "Run workflow". After ~30–60 seconds, refresh your Pages URL.

From then on it updates itself every 15 minutes during market hours,
indefinitely, with no server to maintain.

## About the index methodology

Same simplifications as the logistics index — see that project's README for
the full explanation of:
- Total-shares weighting (not free-float)
- Approximated historical share counts
- No auto-rebalancing on constituent changes

## Limits worth knowing

- Public tier GitHub Actions: unlimited scheduled minutes on public repos;
  2,000 free minutes/month on private repos — comfortably enough here.
- Quote source is a public, unauthenticated market-data feed — fine for
  personal reference, not licensed exchange data.
- **This is a small, evolving universe.** Four constituents is a thin index
  by design — there simply aren't many NSE-listed companies that clear a
  strict ">50% AI revenue" bar yet. Revisit `companies.py` periodically as
  more AI-native companies list or disclose cleaner revenue splits.

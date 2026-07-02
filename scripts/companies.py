# Master list of tracked companies for the NSE AI Index.
#
# IMPORTANT -- read before trusting this list blindly:
# Unlike "logistics company," there is no official NSE/SEBI classification
# for "AI company." Screening here is based on public disclosures, investor
# commentary, and press coverage of each company's revenue mix -- not a
# regulatory filing field. Every entry below includes a `note` explaining
# why it's included and a `confidence` flag:
#   - "high"       = company is widely reported as pure-play / near-100% AI
#   - "borderline" = public commentary puts AI-specific revenue at or near
#                    the 50% threshold, or bundles AI with adjacent categories
#                    (e.g. "digital + cloud + AI") without a clean AI-only split
#
# Re-review this list periodically (e.g. after annual reports) and edit
# directly -- remove any company you don't think meets your bar, or add ones
# not covered here. After editing, re-run establish_base.py to rebalance.

COMPANIES = [
    {
        "symbol": "FRACTAL",
        "name": "Fractal Analytics",
        "segment": "AI / Analytics",
        "confidence": "high",
        "note": "IPO'd Feb 2026, widely reported as India's first pure-play AI listing; core business is AI/analytics consulting and products.",
    },
    {
        "symbol": "LATENTVIEW",
        "name": "Latent View Analytics",
        "segment": "AI / Data Analytics",
        "confidence": "borderline",
        "note": "Data analytics and consulting firm; company commentary (FY26) cited roughly half of revenue from AI projects -- near the 50% line, not a clean majority.",
    },
    {
        "symbol": "HAPPSTMNDS",
        "name": "Happiest Minds Technologies",
        "segment": "AI-first IT Services",
        "confidence": "borderline",
        "note": "Self-described 'AI-first' company; ~97% of revenue is from combined digital/cloud/AI-driven services, but that figure bundles AI with cloud and digital transformation rather than isolating AI alone.",
    },
    {
        "symbol": "NETWEB",
        "name": "Netweb Technologies",
        "segment": "AI Infrastructure / HPC",
        "confidence": "borderline",
        "note": "Manufactures AI/HPC computing systems; often called India's only listed 'AI infrastructure pure-play', but the company's own AI-systems product segment was reported at ~43% of revenue (up from 15%) -- just under a clean majority by that narrow measure, though broader AI+HPC+cloud infra framing would exceed 50%.",
    },
]

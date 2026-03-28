# PSF Community Partner Application – Can I Still Code?

> **Submission note:** This document is structured to map onto the PSF Community Partner online form. Copy each section into the corresponding field. Items marked **[FILL IN]** require manual completion before submitting.

---

## Applicant / Organisation Name

Can I Still Code? — A Longitudinal Python Skill Study
PI: Dr Andy Woods, Royal Holloway, University of London
Website: https://canistillcode.org

---

## What is your initiative, and what does it do?

*Can I Still Code?* is a longitudinal citizen-science study asking a question that matters to every working Python developer: does AI-assisted ("vibe") coding quietly erode our unassisted programming skills over time?

Participants register on canistillcode.org and complete a short set of Python coding challenges — with no AI assistance and no web search — once every 28 days over 12 months or more. Before each session they report what proportion of their day-to-day coding is currently AI-assisted. The result is a time-series dataset linking vibe-coding intensity to objective, test-validated Python performance, collected at individual participant level across a full year.

The study is fully open-science: pre-registered hypotheses, analysis code on GitHub, and a fully anonymised dataset released under CC BY 4.0 after a 12-month embargo.

**Tech stack:** Django (Python 3.14), Pyodide (CPython in WebAssembly — code runs in the participant's browser, never on our server), HTMX, Bulma CSS.

---

## Why does this matter for the Python community?

The Python community is living through a rapid shift in how Python is written. GitHub Copilot, Cursor, Claude, and similar tools have moved from novelty to daily infrastructure for many developers. Yet there is almost no empirical evidence on what this shift does to the underlying skills of the people using these tools.

This study exists specifically to generate that evidence — for Python, about Python developers, using Python challenges. The findings will inform:

- Individual developers deciding how much to lean on AI tooling
- Educators designing Python curricula for the AI-assisted era
- Companies setting policy on AI tool use in Python engineering teams
- The broader Python community's understanding of its own skill trajectory

The open dataset will be a permanent community resource: any researcher, educator, or organisation can build on it under CC BY 4.0.

---

## How does the initiative serve the Python community specifically?

- **Participants are Python developers** — any skill level, professional or hobbyist, anywhere in the world
- **Challenges are Python** — drawn from validated research datasets; all tiers from basic syntax (Tier 1) to algorithmic reasoning (Tier 5)
- **The central predictor is Python-specific AI tool use** — not "coding" in general, but vibe-coding Python specifically
- **Results will be published with fully reproducible R analysis** (lme4/brms multilevel models) and open data, so the Python community can interrogate and extend the findings
- **Recruitment targets Python communities** — Reddit (r/Python, r/learnpython), Hacker News, GitHub Discussions, PyPI, developer Discords

---

## Credentials and credibility

- **PI:** Dr Andy Woods, Royal Holloway, University of London (MediaArts / StoryFutures Academy). Background: experimental psychology + 15+ years production Python and JavaScript development. 70+ publications. Royal Holloway profile: https://pure.royalholloway.ac.uk/en/persons/andrew-woods/
- **Co-Investigator:** Dr Alex Reppel, Royal Holloway
- **PhD Researcher:** Chris Chowen, Royal Holloway
- **Institutional affiliation:** Royal Holloway, University of London
- **Funding:** RHUL internal funding
- **Ethics:** Approved by the Royal Holloway Research Ethics Committee (study dates: 21 March 2026 – 31 March 2028)
- **Pre-registration:** OSF (in progress / submitted — **[FILL IN: OSF DOI once live]**)
- **Current participants:** **[FILL IN: number]** registered; **[FILL IN: number]** with at least one completed session

---

## What are you asking the PSF for?

We are requesting **in-kind support only** — no financial grant:

1. **Use of the PSF name and logo** on the canistillcode.org study site, to signal to potential participants that this is a credible, community-endorsed initiative
2. **Promotional posts on PSF social media channels** (Twitter/X, LinkedIn, Mastodon) to support participant recruitment — ideally at launch and again at the 6-month mark

Recruitment is the primary bottleneck for longitudinal citizen-science. An endorsement from the PSF would materially increase participation from exactly the community the study is designed to serve.

---

## Code of Conduct

The study operates under a Code of Conduct drawn from the Contributor Covenant, applied to all participant-facing community spaces (GitHub Discussions, any future events). Reporting contact: andy.woods@rhul.ac.uk. Full text available at: **[FILL IN: direct URL to CoC page on canistillcode.org once published]**

---

## Trademark / logo usage acknowledgement

We acknowledge that use of the PSF name and logo is subject to the PSF Trademark Usage Policy and the Community Partner guidelines. We will not imply PSF endorsement of findings, and will remove all PSF marks on request.

---

## Supporting links

| Resource | URL |
|---|---|
| Study website | https://canistillcode.org |
| PI profile (RHUL) | https://pure.royalholloway.ac.uk/en/persons/andrew-woods/ |
| GitHub (analysis code) | **[FILL IN]** |
| OSF pre-registration | **[FILL IN once live]** |
| PI Google Scholar | https://scholar.google.co.uk/citations?user=p5dUkQIAAAAJ&hl=en |

---

## Items to fill in before submitting

| # | Item | Notes |
|---|---|---|
| 1 | Current registered participant count | From the admin dashboard |
| 2 | Current count with ≥1 completed session | From the admin dashboard |
| 3 | Ethics status | Approved (dates above) — confirm wording you want to use |
| 4 | OSF pre-registration DOI | Once the pre-reg is submitted/published |
| 5 | GitHub repo URL | If you want to link directly to the analysis repo |
| 6 | Code of Conduct URL | Once a CoC page is live on canistillcode.org |
| 7 | Submission timing | PSF asks for ≥6 weeks before your target promotion date — pick a target and back-calculate |

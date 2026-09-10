---
layout: default
title: "Week 6 — Lab 5b: GLM – Regression with Randomization"
parent: Labs
nav_order: 6
permalink: /labs/06/
---

# Week 6 — Lab 5b: GLM – Regression with Randomization

**Module:** Part 3: The General Linear Model – Single Explanatory Variable

Location: CSF BIOL 2218B Computer Lab · Time: 3:00–6:00 PM

> Model verification via randomization. Testing slope null hypotheses through empirical null distribution creation.
{: .objectives }

**Key deliverable:** Resampling scripts & visual overlays
**Software / functions:** `Base R resampling + ggplot2 overlays`


## Starter file

{% assign this_lab = site.data.labs.labs | where: "week", 6 | first %}
{% if this_lab.downloadable %}
[Download lab05b-glm-regression-randomization.Rmd]({{ '/rmd/lab05b-glm-regression-randomization.Rmd' | relative_url }}){: .btn .btn-blue }

Open it in RStudio and knit to HTML (or PDF) to confirm it runs before
editing.
{% else %}
_Materials for this lab will be posted here a few hours before the session._
{% endif %}

[Back to schedule]({{ '/schedule/' | relative_url }})

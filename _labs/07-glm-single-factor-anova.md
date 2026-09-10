---
layout: default
title: "Week 7 — Lab 6a/b: GLM – Single Factor ANOVA"
parent: Labs
nav_order: 7
permalink: /labs/07/
---

# Week 7 — Lab 6a/b: GLM – Single Factor ANOVA

**Module:** Part 3: The General Linear Model – Single Explanatory Variable

Location: CSF BIOL 2218B Computer Lab · Time: 3:00–6:00 PM

> Group comparison models. Factor coding, sum of squares decomposition, variance partitioning, and post-hoc contrasts.
{: .objectives }

**Key deliverable:** ANOVA table with post-hoc contrasts
**Software / functions:** `lm(), anova(), emmeans package`


## Starter file

{% assign this_lab = site.data.labs.labs | where: "week", 7 | first %}
{% if this_lab.downloadable %}
[Download lab06-glm-single-factor-anova.Rmd]({{ '/rmd/lab06-glm-single-factor-anova.Rmd' | relative_url }}){: .btn .btn-blue }

Open it in RStudio and knit to HTML (or PDF) to confirm it runs before
editing.
{% else %}
_Materials for this lab will be posted here a few hours before the session._
{% endif %}

[Back to schedule]({{ '/schedule/' | relative_url }})

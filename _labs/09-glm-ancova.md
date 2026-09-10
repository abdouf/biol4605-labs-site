---
layout: default
title: "Week 9 — Lab 8: GLM – ANCOVA"
parent: Labs
nav_order: 9
permalink: /labs/09/
---

# Week 9 — Lab 8: GLM – ANCOVA

**Module:** Part 4: The General Linear Model – Multiple Explanatory Variables

Location: CSF BIOL 2218B Computer Lab · Time: 3:00–6:00 PM

> Analysis of covariance. Combining continuous covariates with categorical predictors to control for background noise.
{: .objectives }

**Key deliverable:** Homogeneity-of-slopes test & ANCOVA summary
**Software / functions:** `lm(), anova(), car package`


## Starter file

{% assign this_lab = site.data.labs.labs | where: "week", 9 | first %}
{% if this_lab.downloadable %}
[Download lab08-glm-ancova.Rmd]({{ '/rmd/lab08-glm-ancova.Rmd' | relative_url }}){: .btn .btn-blue }

Open it in RStudio and knit to HTML (or PDF) to confirm it runs before
editing.
{% else %}
_Materials for this lab will be posted here a few hours before the session._
{% endif %}

[Back to schedule]({{ '/schedule/' | relative_url }})

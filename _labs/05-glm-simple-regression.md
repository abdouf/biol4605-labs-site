---
layout: default
title: "Week 5 — Lab 5: GLM – Simple Regression"
parent: Labs
nav_order: 5
permalink: /labs/05/
---

# Week 5 — Lab 5: GLM – Simple Regression

**Module:** Part 3: The General Linear Model – Single Explanatory Variable

Location: CSF BIOL 2218B Computer Lab · Time: 3:00–6:00 PM

> Fitting simple linear models. Model formulation (Y = b0 + b1*X + e), parameter estimation, and residual diagnostic plots.
{: .objectives }

**Key deliverable:** Annotated lm() output and diagnostic plots
**Software / functions:** `lm(), summary(), plot() in R`

## Starter file

{% assign this_lab = site.data.labs.labs | where: "week", 5 | first %}
{% if this_lab.downloadable %}
 [Download lab05a-glm-simple-regression.Rmd]({{ '/rmd/lab05a-glm-simple-regression.Rmd' | relative_url }}){: .btn .btn-blue }

 Open it in RStudio and knit to HTML (or PDF) to confirm it runs before
 editing.
{% else %}
_Materials for this lab will be posted here a few hours before the session._
{% endif %}

 [Back to schedule]({{ '/schedule/' | relative_url }})

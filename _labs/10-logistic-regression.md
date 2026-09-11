---
layout: default
title: "Week 10 — Lab 10: Logistic Regression (GLM)"
parent: Labs
nav_order: 10
permalink: /labs/10/
---

# Week 10 — Lab 10: Logistic Regression (GLM)

**Module:** Part 5: The Generalized Linear Model

Location: CSF BIOL 2218B Computer Lab · Time: 3:00–6:00 PM

> Non-Gaussian response variables. Modeling binary/proportional biological outcomes using logit link functions.
{: .objectives }

**Key deliverable:** Fitted logistic model with interpretation
**Software / functions:** `glm(family = binomial)`

 ## Starter file

+{% assign this_lab = site.data.labs.labs | where: "week", 10 | first %}
+{% if this_lab.downloadable %}
 [Download lab10-logistic-regression.Rmd]({{ '/rmd/lab10-logistic-regression.Rmd' | relative_url }}){: .btn .btn-blue }

 Open it in RStudio and knit to HTML (or PDF) to confirm it runs before
 editing.
+{% else %}
+_Materials for this lab will be posted here a few hours before the session._
+{% endif %}

 [Back to schedule]({{ '/schedule/' | relative_url }})

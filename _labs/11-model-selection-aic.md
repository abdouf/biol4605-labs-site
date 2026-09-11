---
layout: default
title: "Week 11 — Lab 11 (new): Model Selection with AIC"
parent: Labs
nav_order: 11
permalink: /labs/11/
---

# Week 11 — Lab 11 (new): Model Selection with AIC

**Module:** Part 6: Extensions of the General Linear Model

Location: CSF BIOL 2218B Computer Lab · Time: 3:00–6:00 PM

> Comparing candidate models rather than testing one at a time. AIC and delta-AIC as a likelihood-based alternative to significance testing for choosing among several plausible models fit to the same data.
{: .objectives }

**Key deliverable:** AIC comparison table across candidate models + written justification of the selected model
**Software / functions:** `AIC(), base R model objects; optional: MuMIn or bbmle package`

 ## Starter file

+{% assign this_lab = site.data.labs.labs | where: "week", 11 | first %}
+{% if this_lab.downloadable %}
 [Download lab11-model-selection-aic.Rmd]({{ '/rmd/lab11-model-selection-aic.Rmd' | relative_url }}){: .btn .btn-blue }

 Open it in RStudio and knit to HTML (or PDF) to confirm it runs before
 editing.
+{% else %}
+_Materials for this lab will be posted here a few hours before the session._
+{% endif %}

 [Back to schedule]({{ '/schedule/' | relative_url }})

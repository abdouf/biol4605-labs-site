---
layout: default
title: "Week 8 — Lab 7: GLM – Multifactor ANOVA"
parent: Labs
nav_order: 8
permalink: /labs/08/
---

# Week 8 — Lab 7: GLM – Multifactor ANOVA

**Module:** Part 4: The General Linear Model – Multiple Explanatory Variables

Location: CSF BIOL 2218B Computer Lab · Time: 3:00–6:00 PM

> Factorial designs & interactions. Main effects, interaction terms, and visual interpretation of non-additive biological responses.
{: .objectives }

**Key deliverable:** Two-way ANOVA & interaction plots
**Software / functions:** `lm(), anova(), interaction.plot() / ggplot2`


## Starter file

{% assign this_lab = site.data.labs.labs | where: "week", 8 | first %}
{% if this_lab.downloadable %}
[Download lab07-glm-multifactor-anova.Rmd]({{ '/rmd/lab07-glm-multifactor-anova.Rmd' | relative_url }}){: .btn .btn-blue }

Open it in RStudio and knit to HTML (or PDF) to confirm it runs before
editing.
{% else %}
_Materials for this lab will be posted here a few hours before the session._
{% endif %}

[Back to schedule]({{ '/schedule/' | relative_url }})

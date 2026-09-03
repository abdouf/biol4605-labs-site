---
title: Labs
layout: default
nav_order: 4
has_children: true
permalink: /labs/
---

# Labs

One page per week. Each links to the downloadable R Markdown starter file
(`rmd/labNN-*.Rmd`) for that lab.
See the [Schedule]({{ '/schedule/' | relative_url }}) for the full table view.

<ul>
{% for lab in site.data.labs.labs %}
  <li><a href="{{ "/labs/" | append: lab.week_padded | append: "/" | relative_url }}">Week {{ lab.week }} — {{ lab.lab_label }}: {{ lab.title }}</a> <span style="color:#586069;">({{ lab.module }})</span></li>
{% endfor %}
</ul>

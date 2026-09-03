---
title: Schedule
layout: default
nav_order: 3
permalink: /schedule/
---

# Lab schedule
{: .no_toc }

All 13 weeks, generated from [`_data/labs.yml`](https://github.com/abdouf/biol4605-labs-site/blob/main/_data/labs.yml).
Edit that file to update dates or content across the whole site.
{: .fs-6 .fw-300 }

| Week | Date | Lab | Module | Focus & learning objectives | Deliverable / software |
|:-----|:-----|:----|:-------|:-----------------------------|:------------------------|
{% for lab in site.data.labs.labs -%}
| {{ lab.week }} | {{ lab.date }} | [{{ lab.lab_label }}: {{ lab.title }}]({{ "/labs/" | append: lab.week_padded | append: "/" | relative_url }}) | {{ lab.module }} | {{ lab.focus }}{% if lab.note and lab.note != "" %} *({{ lab.note }})*{% endif %} | {{ lab.deliverable }} — `{{ lab.software }}` |
{% endfor %}

---

## Quick links to each lab

<ul>
{% for lab in site.data.labs.labs %}
  <li><a href="{{ "/labs/" | append: lab.week_padded | append: "/" | relative_url }}">Week {{ lab.week }} ({{ lab.date }}) — {{ lab.lab_label }}: {{ lab.title }}</a></li>
{% endfor %}
</ul>

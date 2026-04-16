---
permalink: /
title: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a fourth-year PhD candidate at Peking University, working on safety alignment and the development of next-generation large language models.

My research interests include trustworthy AI, adversarial robustness, and generative model safety.

## Publications

{% assign sorted_publications = site.publications | sort: "date" | reverse %}
{% assign current_year = "" %}

{% for post in sorted_publications %}
  {% assign post_year = post.date | default: "1900-01-01" | date: "%Y" %}

  {% if post_year != current_year %}
    {% unless forloop.first %}</ol>{% endunless %}
    <h3 class="publications-year">{{ post_year }}</h3>
    <ol class="publications-list">
    {% assign current_year = post_year %}
  {% endif %}

  <li class="publications-list__item">
    {% include publication-item.html item=post %}
  </li>

  {% if forloop.last %}</ol>{% endif %}
{% endfor %}

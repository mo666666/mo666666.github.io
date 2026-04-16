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
<ul class="publications-list">
{% for post in sorted_publications %}
  <li class="publications-list__item">
    {% include publication-item.html item=post %}
  </li>
{% endfor %}
</ul>

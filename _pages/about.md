---
permalink: /
title: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<div class="homepage-intro">
  <p>I am a fourth-year PhD candidate at Peking University, working on safety alignment and the development of next-generation large language models.</p>
  <p>My research interests include trustworthy AI, adversarial robustness, and generative model safety.</p>
</div>

<h2 class="homepage-section-title">📝 Publications</h2>

{% assign sorted_publications = site.publications | sort: "date" | reverse %}
<div class="publications-list">
{% for post in sorted_publications %}
  <div class="publications-list__item">
    {% include publication-item.html item=post %}
  </div>
{% endfor %}
</div>

<img width="432" height="10" alt="image" src="https://github.com/user-attachments/assets/26a0dfa9-389d-4b3d-bf2e-9f11f22d1ecb" /><img width="432" height="10" alt="image" src="https://github.com/user-attachments/assets/5a474f58-d94f-4c56-87a5-08af6a58ffed" /><img width="432" height="10" alt="image" src="https://github.com/user-attachments/assets/e6190f75-8a8f-4273-9a9b-82fae347175e" />---
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

<h2 class="homepage-section-title"><i class="fa fa-trophy" aria-hidden="true"></i> Seletive Awards</h2>

<p><strong>Undergraduate</strong></p>
<ul>
  <li>2019.10 Merit Student of Shanghai Jiao Tong University</li>
  <li>2019.12 National Scholarship (<strong>Top 1%</strong> in CE Dept.)</li>
  <li>2020.12 National Scholarship (<strong>Top 1%</strong> in CE Dept.)</li>
  <li>2022.6 Outstanding Graduate of Shanghai (<strong>Top 3%</strong>)</li>
  <li>2022.6 Outstanding Undergraduate Thesis, Shanghai Jiao Tong University (<strong>Top 1%</strong>, 1 out of 128 students in the department)</li>
</ul>

<p><strong>Graduate</strong></p>
<ul>
   <li>2023.9 Xiaomi Scholarship (First-Class)</li>
   <li>2023.9 Merit Student of Peking University</li>
   <li>2024.9 Yuehua Luo Scholarship</li>
   <li>2024.9 Outstanding Research Award in Peking University</li>
   <li>2025.4 Nomination for Academic Star（<strong>Five students in AI Dept.</strong>）</li>
  <li>2025.11 Taotian Scholarship (<strong>Eight Graduate students in AI Dept.</strong>)</li>
  <li>2026.4 Optiver AI PhD Scholarship (<strong>Six PhD students in China</strong>)</li>
</ul>

<h2 class="homepage-section-title">📝 Publications</h2>

{% assign sorted_publications = site.publications | sort: "date" | reverse %}
<div class="publications-list">
{% for post in sorted_publications %}
  <div class="publications-list__item">
    {% include publication-item.html item=post %}
  </div>
{% endfor %}
</div>

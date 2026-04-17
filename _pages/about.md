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

<h2 class="homepage-section-title"><i class="fa fa-trophy" aria-hidden="true"></i> Academic Performance</h2>

<p><strong>Undergraduate</strong></p>
<ul>
  <li>GPA: 90.93/100 (or 3.94/4.3), Rank: 2/128 (<strong style="color: #8B0000;">Top 1.6%</strong>)</li>
  <li>Courses: 55.81% above A, 24.42% above A+</li>
</ul>


<p><strong >Graduate</strong></p>
<ul>
  <li>GPA: 3.88/4.0</li>
  <li>Courses: 71.4% above A</li>
</ul>


<h2 class="homepage-section-title"><i class="fa-sharp fa-regular fa-award" style="color: rgb(246, 203, 35);"></i> Seletive Awards</h2>

<p><strong>Undergraduate</strong></p>
<ul>
  <li>2019.10 Merit Student of Shanghai Jiao Tong University</li>
  <li>2019.12 National Scholarship (<strong style="color: #8B0000;">Top 1%</strong> in CE Dept.)</li>
  <li>2020.12 National Scholarship (<strong style="color: #8B0000;">Top 1%</strong> in CE Dept.)</li>
  <li>2021.12 Weichai Power Scholarship</li>
  <li>2022.6 Outstanding Graduate of Shanghai (<strong style="color: #8B0000;">Top 3%</strong>)</li>
  <li>2022.6 Outstanding Undergraduate Thesis, Shanghai Jiao Tong University (<strong style="color: #8B0000;">Top 1%</strong>, 1 out of 128 students in the department)</li>
  
</ul>

<p><strong>Graduate</strong></p>
<ul>
   <li>2023.9 Xiaomi Scholarship (First-Class)</li>
   <li>2023.9 Merit Student of Peking University</li>
   <li>2024.9 Yuehua Luo Scholarship</li>
   <li>2024.9 Outstanding Research Award in Peking University</li>
  <li>2025.4 Nomination for Academic Star（<strong style="color: #8B0000;">Five Graduate students in AI Dept.</strong>）</li>
  <li>2025.11 Taotian Scholarship (<strong style="color: #8B0000;">Eight Graduate students in AI Dept.</strong>)</li>
  <li>2026.4 Optiver AI PhD Scholarship (<strong style="color: #8B0000;">Six PhD students in China</strong>)</li>



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

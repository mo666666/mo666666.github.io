---
permalink: /
title: "Welcome to Yichuan Mo's Homepage! 👏"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<div class="homepage-intro">
  <p>I am a fourth-year PhD candidate at Peking University, working on safety alignment and the development of next-generation large language models.</p>
  <!-- <p>My research interests include trustworthy AI, adversarial robustness, and generative model safety.</p> -->
</div>

<h2 class="homepage-section-title">💯 Academic Performance</h2>

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


<h2 class="homepage-section-title">🏆 Selective Awards</h2>

<p><strong>Undergraduate</strong></p>
<ul>
  <li>2019.10 Merit Student of Shanghai Jiao Tong University</li>
  <li>2019.12 National Scholarship (<strong style="color: #8B0000;">Top 1%</strong> in CE Dept.)</li>
  <li>2020.12 National Scholarship (<strong style="color: #8B0000;">Top 1%</strong> in CE Dept.)</li>
  <li>2021.12 Weichai Power Scholarship</li>
  <li>2022.05 Outstanding Dormitory (D24 401)</li>
  <li>2022.06 Outstanding Graduate of Shanghai (<strong style="color: #8B0000;">Top 3%</strong>)</li>
  <li>2022.06 Outstanding Undergraduate Thesis, Shanghai Jiao Tong University (<strong style="color: #8B0000;">Top 1%</strong>, 1 out of 128 students in CE Dept.)</li>
</ul>

<p><strong>Graduate</strong></p>
<ul>
   <li>2023.12 Sunshine Dormitory</li>
   <li>2023.09 Xiaomi Scholarship (First-Class)</li>
   <li>2023.09 Merit Student of Peking University</li>
   <li>2024.09 Yuehua Luo Scholarship</li>
   <li>2024.09 Outstanding Research Award in Peking University</li>
  <li>2025.04 Nomination for Academic Star（<strong style="color: #8B0000;">Five Graduate students in AI Dept.</strong>）</li>
  <li>2025.11 <a href="https://mp.weixin.qq.com/s/2f75EA4WrAkxEw2N8lQ6zA">Taotian Scholarship</a> (<strong style="color: #8B0000;">Eight Graduate students in AI Dept.</strong>)</li>
  <li>2026.04 <a href="https://mp.weixin.qq.com/s/0o5mH7wNe_JpQ994gPrQZg">Optiver AI PhD Scholarship</a> (<strong style="color: #8B0000;">Six PhD students in China</strong>)</li>



</ul>

<h2 class="homepage-section-title">📝 Papers</h2>
<p class="publications-note">(* Equal Contribution and # Student First Author)</p>

{% assign sorted_publications = site.publications | sort: "date" | reverse %}

<p><strong>Accepted</strong></p>
<ul class="publications-list publications-list--bulleted">
{% for post in sorted_publications %}
  {% unless post.status == "preprint" %}
  <li class="publications-list__item">
    {% include publication-item.html item=post %}
  </li>
  {% endunless %}
{% endfor %}
</ul>

<p><strong>Preprint</strong></p>
<ul class="publications-list publications-list--bulleted">
{% for post in sorted_publications %}
  {% if post.status == "preprint" %}
  <li class="publications-list__item">
    {% include publication-item.html item=post %}
  </li>
  {% endif %}
{% endfor %}
</ul>

<h2 class="homepage-section-title">🤖 Open-source Models</h2>

<ul class="publications-list publications-list--bulleted">
  <li class="publications-list__item">
    <article class="publication-entry">
      <h3 class="publication-entry__title">
        Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making
      </h3>
      <p class="publication-entry__venue"><em>The <span style="color: #cc0000;">toppest medical model</span> in the world (Jan 2026)</em></p>
      <div class="publication-links">
        <a class="publication-links__link" href="https://arxiv.org/pdf/2602.06570" target="_blank" rel="noopener">[PDF]</a>
        <a class="publication-links__link" href="https://github.com/baichuan-inc/Baichuan-M3-235B" target="_blank" rel="noopener">[github]</a>
        <a class="publication-links__link" href="https://huggingface.co/baichuan-inc/Baichuan-M3-235B" target="_blank" rel="noopener">[huggingface]</a>
        <a class="publication-links__link" href="https://www.baichuan-ai.com/blog/baichuan-M3" target="_blank" rel="noopener">[blog]</a>
        <button type="button" class="publication-links__link publication-links__bib-trigger" data-bib="@article{dou2026baichuan,&#10;  title={Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making},&#10;  author={Dou, Chengfeng and Yang, Fan and Li, Fei and Jia, Jiyuan and Ju, Qiang and Wang, Shuai and Li, Tianpeng and Zeng, Xiangrong and Zhou, Yijie and Zhang, Hongda and others},&#10;  journal={arXiv preprint arXiv:2602.06570},&#10;  year={2026}&#10;}" data-bib-title="Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making">[Bib]</button>
      </div>
    </article>
  </li>
  <li class="publications-list__item">
    <article class="publication-entry">
      <h3 class="publication-entry__title">
        Baichuan-M2: Scaling Medical Capability with Large Verifier System
      </h3>
      <p class="publication-entry__venue"><em>The <span style="color: #cc0000;">toppest open-source medical model</span> in the world (Aug 2025)</em></p>
      <div class="publication-links">
        <a class="publication-links__link" href="https://arxiv.org/pdf/2509.02208" target="_blank" rel="noopener">[PDF]</a>
        <a class="publication-links__link" href="https://github.com/baichuan-inc/Baichuan-M2-32B" target="_blank" rel="noopener">[github]</a>
        <a class="publication-links__link" href="https://huggingface.co/baichuan-inc/Baichuan-M2-32B" target="_blank" rel="noopener">[huggingface]</a>
        <a class="publication-links__link" href="https://www.baichuan-ai.com/blog/baichuan-M2" target="_blank" rel="noopener">[blog]</a>
        <button type="button" class="publication-links__link publication-links__bib-trigger" data-bib="@article{dou2025baichuan,&#10;  title={Baichuan-m2: Scaling medical capability with large verifier system},&#10;  author={Dou, Chengfeng and Liu, Chong and Yang, Fan and Li, Fei and Jia, Jiyuan and Chen, Mingyang and Ju, Qiang and Wang, Shuai and Dang, Shunya and Li, Tianpeng and others},&#10;  journal={arXiv preprint arXiv:2509.02208},&#10;  year={2025}&#10;}" data-bib-title="Baichuan-M2: Scaling Medical Capability with Large Verifier System">[Bib]</button>
      </div>
    </article>
  </li>
</ul>

<h2 class="homepage-section-title">🛠️ Academic Service</h2>

<ul>
  <li><strong>Reviewer</strong>: NeurIPS 2023/2024/2025; ICLR 2024/2025/2026; ICML 2024/2025/2026; CVPR 2025/2026; ICCV 2025; IJCAI 2024; AAAI 2025/2026; AISTATS 2025; ECCV 2026</li>
  <li><strong>Top Reviewer</strong> of NeurIPS 2023 (<strong style="color: #8B0000;">Top 10.49%</strong>)</li>
  <li><strong>Top Reviewer</strong> of NeurIPS 2024 (<strong style="color: #8B0000;">Top 8.60%</strong>)</li>
  <li><strong>Top Reviewer</strong> of NeurIPS 2025 (<strong style="color: #8B0000;">Top 8.02%</strong>)</li>
  <li><strong>Notable Reviewer</strong> of ICLR 2025 (<strong style="color: #8B0000;">Top 3%</strong>)</li>
</ul>

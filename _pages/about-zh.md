---
permalink: /zh/
title: "莫易川 - Homepage"
author_profile: true
---

<div class="homepage-intro">
  <p>我是北京大学四年级博士研究生，研究方向为安全对齐以及新一代大语言模型的研发。</p>
  <!-- <p>我的研究兴趣包括可信人工智能、对抗鲁棒性以及生成式模型安全。</p> -->
</div>

{% include base_path %}

<h2 class="homepage-section-title">🎓 教育经历</h2>
<ul class="homepage-education">
  <li class="homepage-education__item">
    <div class="homepage-education__logo">
      <img src="{{ base_path }}/images/pku-seal.svg" alt="北京大学" loading="lazy" decoding="async" />
    </div>
    <div class="homepage-education__body">
      <div class="homepage-education__school">北京大学</div>
      <div class="homepage-education__dates">2022年9月 – 至今</div>
      <div class="homepage-education__degree">博士研究生</div>
      <div class="homepage-education__dept">智能科学与技术学院</div>
    </div>
  </li>
  <li class="homepage-education__item">
    <div class="homepage-education__logo">
      <img src="{{ base_path }}/images/sjtu-seal.png" alt="上海交通大学" loading="lazy" decoding="async" />
    </div>
    <div class="homepage-education__body">
      <div class="homepage-education__school">上海交通大学</div>
      <div class="homepage-education__dates">2018年9月 – 2022年6月</div>
      <div class="homepage-education__degree">工学学士</div>
      <div class="homepage-education__dept">计算机科学与工程学院</div>
    </div>
  </li>
</ul>

<h2 class="homepage-section-title">💯 学业成绩</h2>

<p><strong>本科阶段</strong></p>
<ul>
  <li>GPA：90.93/100（或 3.94/4.3），排名：2/128（<strong style="color: #8B0000;">前 1.6%</strong>）</li>
  <li>课程成绩：55.81% 在 A 以上，24.42% 在 A+ 以上</li>
</ul>


<p><strong>研究生阶段</strong></p>
<ul>
  <li>GPA：3.88/4.0</li>
  <li>课程成绩：71.4% 在 A 以上</li>
</ul>


<h2 class="homepage-section-title">🏆 代表性荣誉</h2>

<p><strong>本科阶段</strong></p>
<ul>
  <li>2019.10 上海交通大学三好学生</li>
  <li>2019.12 国家奖学金（<strong style="color: #8B0000;">前 1%</strong>）</li>
  <li>2020.12 国家奖学金（<strong style="color: #8B0000;">前 1%</strong>）</li>
  <li>2021.12 潍柴动力奖学金</li>
  <li>2022.05 杰出寝室</li>
  <li>2022.06 上海市优秀毕业生（<strong style="color: #8B0000;">前 3%</strong>）</li>
  <li>2022.06 上海交通大学优秀本科毕业论文（<strong style="color: #8B0000;">前 1%</strong>，1/128）</li>
</ul>

<p><strong>博士阶段</strong></p>
<ul>
   <li>2023.12 阳光寝室</li>
   <li>2023.09 小米一等奖学金</li>
   <li>2023.09 北京大学三好学生</li>
   <li>2024.09 ‌罗岳华奖学金</li>
   <li>2024.09 北京大学优秀科研奖</li>
  <li>2025.04 学术智星提名（<strong style="color: #8B0000;">五位研究生/年</strong>）</li>
  <li>2025.11 <a href="https://mp.weixin.qq.com/s/2f75EA4WrAkxEw2N8lQ6zA">淘天奖学金</a>（<strong style="color: #8B0000;">八位研究生/年</strong>）</li>
  <li>2026.04 <a href="https://mp.weixin.qq.com/s/0o5mH7wNe_JpQ994gPrQZg">Optiver AI 博士奖学金</a>（<strong style="color: #8B0000;">全国仅六位博士生/年</strong>）</li>



</ul>

<h2 class="homepage-section-title">📝 学术论文</h2>
<p class="publications-note">（* 共同一作，# 学生一作）</p>

{% assign sorted_publications = site.publications | sort: "date" | reverse %}

<p><strong>已录用</strong></p>
<ul class="publications-list publications-list--bulleted">
{% for post in sorted_publications %}
  {% unless post.status == "preprint" %}
  <li class="publications-list__item">
    {% include publication-item.html item=post %}
  </li>
  {% endunless %}
{% endfor %}
</ul>

<p><strong>预印本</strong></p>
<ul class="publications-list publications-list--bulleted">
{% for post in sorted_publications %}
  {% if post.status == "preprint" %}
  <li class="publications-list__item">
    {% include publication-item.html item=post %}
  </li>
  {% endif %}
{% endfor %}
</ul>

<h2 class="homepage-section-title">🤖 开源模型</h2>

<ul class="publications-list publications-list--bulleted">
  <li class="publications-list__item">
    <article class="publication-entry">
      <h3 class="publication-entry__title">
        Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making
      </h3>
      <p class="publication-entry__venue"><em>世界最强医疗大模型（2026 年 1 月）</em></p>
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
      <p class="publication-entry__venue"><em>世界最强开源医疗大模型（2025 年 8 月）</em></p>
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

<h2 class="homepage-section-title">🛠️ 学术服务</h2>

<ul>
  <li><strong>审稿人</strong>：NeurIPS 2023/2024/2025；ICLR 2024/2025/2026；ICML 2024/2025/2026；CVPR 2025/2026；ICCV 2025；IJCAI 2024；AAAI 2025/2026；AISTATS 2025；ECCV 2026</li>
  <li>NeurIPS 2023 <strong>杰出审稿人</strong>（<strong style="color: #8B0000;">前 10.49%</strong>）</li>
  <li>NeurIPS 2024 <strong>杰出审稿人</strong>（<strong style="color: #8B0000;">前 8.60%</strong>）</li>
  <li>NeurIPS 2025 <strong>杰出审稿人</strong>（<strong style="color: #8B0000;">前 8.02%</strong>）</li>
  <li>ICLR 2025 <strong>优秀审稿人</strong>（<strong style="color: #8B0000;">前 3%</strong>）</li>
</ul>

---
layout: default
title: Blog
permalink: /blog/
---

<style>
  .blog-lang-switch {
    display: inline-flex;
    align-items: center;
    border: 1px solid #13294B;
    border-radius: 3px;
    overflow: hidden;
    font-family: "Source Sans 3", -apple-system, sans-serif;
    font-size: 12.5px;
    line-height: 1;
    vertical-align: middle;
  }
  .blog-lang-switch button {
    background: #ffffff;
    color: #13294B;
    border: none;
    padding: 4px 9px;
    cursor: pointer;
    font-weight: 600;
    font-size: 12px;
  }
  .blog-lang-switch button.active {
    background: #13294B;
    color: #ffffff;
  }
  html[data-blog-lang="en"] .b-zh { display: none !important; }
  html[data-blog-lang="zh"] .b-en { display: none !important; }
  .blog-entry {
    padding: 14px 0 18px;
    border-bottom: 1px solid #e5e5e5;
  }
  .blog-entry-meta {
    font-family: "Ubuntu Mono", monospace;
    font-size: 13px;
    color: #777777;
    margin-bottom: 5px;
  }
  .blog-entry-title {
    font-size: 18.5px;
    font-weight: 600;
    line-height: 1.38;
    margin-bottom: 7px;
  }
  .blog-entry-title a {
    color: #13294B;
    text-decoration: none;
  }
  .blog-entry-title a:hover {
    color: #069;
    text-decoration: underline;
  }
  .blog-entry-desc {
    font-size: 15.5px;
    line-height: 1.62;
    color: #595959;
    margin-bottom: 9px;
  }
  .blog-links a.btn {
    color: #000000;
    border: 1px solid #000000;
    padding: 0.12rem 0.55rem;
    font-size: 12px;
    display: inline-block;
    margin: 0.15rem 0.25rem 0 0;
    text-decoration: none;
  }
  .blog-links a.btn:hover {
    color: #13294B;
    border-color: #13294B;
  }
</style>

<script>
  (function() {
    var saved = localStorage.getItem("xh_blog_lang") || "zh";
    document.documentElement.setAttribute("data-blog-lang", saved);
  })();
  function setBlogListLang(lang) {
    document.documentElement.setAttribute("data-blog-lang", lang);
    localStorage.setItem("xh_blog_lang", lang);
    var bZh = document.getElementById("bl-btn-zh");
    var bEn = document.getElementById("bl-btn-en");
    if (bZh && bEn) {
      bZh.className = lang === "zh" ? "active" : "";
      bEn.className = lang === "en" ? "active" : "";
    }
  }
  document.addEventListener("DOMContentLoaded", function() {
    setBlogListLang(localStorage.getItem("xh_blog_lang") || "zh");
  });
</script>

<h1 id="blog"></h1>

<div style="margin: 60px 0px 8px; display: flex; justify-content: space-between; align-items: center;">
  <h2 style="margin: 0;">Blog</h2>
  <div class="blog-lang-switch" aria-label="Language Switch">
    <button type="button" id="bl-btn-zh" class="active" onclick="setBlogListLang('zh')">中文</button>
    <button type="button" id="bl-btn-en" onclick="setBlogListLang('en')">EN</button>
  </div>
</div>

<div class="blog-entry">
  <div class="blog-entry-meta">
    [Nov. 2026] &nbsp;·&nbsp; Embodied AI · Agentic RL · WAM · MoE · Multi-Agent
  </div>

  <div class="blog-entry-title b-zh">
    <a href="./embodied-agentic-rl-moe/?lang=zh">从 VLA、WAM 到具身智能体：LLM 后训练与 MoE 路由向具身迁移的四条路径</a>
  </div>
  <div class="blog-entry-title b-en">
    <a href="./embodied-agentic-rl-moe/?lang=en">From VLA and WAM to Embodied Agents: Four Paths for Post-Training and MoE Routing</a>
  </div>

  <div class="blog-entry-desc b-zh">
    围绕反应式 VLA、世界-动作模型（WAM）与智能体执行框架三类主流具身基座，梳理 2025–2026 年间交互轨迹进化、动态 Rubric 协同演化、免梯度测试时强化学习以及混合专家与多智能体架构的核心目标、共性挑战、代表作机制与选型边界。
  </div>
  <div class="blog-entry-desc b-en">
    Starting from reactive VLAs, world-action models (WAMs), and agentic robot harnesses, this post surveys four post-training and architectural directions across 2025–2026: trajectory evolution, dynamic rubric co-evolution, training-free test-time RL, and mixture-of-experts versus multi-agent systems.
  </div>

  <div class="blog-links">
    <a class="btn" href="./embodied-agentic-rl-moe/?lang=zh">中文全文</a>
    <a class="btn" href="./embodied-agentic-rl-moe/?lang=en">English Post</a>
  </div>
</div>

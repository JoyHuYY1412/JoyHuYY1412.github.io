<h1 id="publications"></h1>

<h2 class="publications-heading">Publications <span class="publication-index">[<a href="{{ site.google_scholar }}" target="_blank" rel="noopener">Google Scholar</a>] [<a href="https://dblp.org/pid/222/7753.html" target="_blank" rel="noopener">DBLP</a>]</span></h2>


<div class="publications">
<ol class="bibliography">

{% for link in site.data.publications.main %}

<li>
<div class="pub-row">
  <div class="pub-visual">
    {% if link.video %}
    <video class="teaser teaser-video" autoplay muted loop playsinline preload="metadata" poster="{{ link.image }}" aria-label="Animated teaser for {{ link.title | escape }}">
      <source src="{{ link.video }}" type="video/mp4">
    </video>
    {% elsif link.image %}
    <img src="{{ link.image }}" class="teaser" alt="Teaser for {{ link.title | escape }}" loading="lazy">
    {% else %}
    <div class="teaser teaser-placeholder" role="img" aria-label="{{ link.title | escape }}">
      <span>{{ link.conference_short }}</span>
    </div>
    {% endif %}
    <abbr class="badge">{{ link.conference_short }}</abbr>
  </div>
  <div class="pub-details">
      <div class="title"><a href="{{ link.pdf }}" target="_blank" rel="noopener">{{ link.title }}</a></div>
      <div class="author">{{ link.authors }}</div>
      <div class="periodical"><em>{{ link.conference }}</em>
      </div>
    <div class="links">
      {% if link.pdf %} 
      <a href="{{ link.pdf }}" class="btn btn-sm z-depth-0" role="button" target="_blank" rel="noopener">PDF</a>
      {% endif %}
      {% if link.code %} 
      <a href="{{ link.code }}" class="btn btn-sm z-depth-0" role="button" target="_blank" rel="noopener">Code</a>
      {% endif %}
      {% if link.page %} 
      <a href="{{ link.page }}" class="btn btn-sm z-depth-0" role="button" target="_blank" rel="noopener">Project Page</a>
      {% endif %}
      {% if link.data %} 
      <a href="{{ link.data }}" class="btn btn-sm z-depth-0" role="button" target="_blank" rel="noopener">Dataset</a>
      {% endif %}
      {% if link.bibtex %} 
      <a href="{{ link.bibtex }}" class="btn btn-sm z-depth-0" role="button" target="_blank" rel="noopener">BibTeX</a>
      {% endif %}
      {% if link.notes %} 
      <strong> <i style="color:#e74d3c; font-weight:600">{{ link.notes }}</i></strong>
      {% endif %}
      {% if link.others %} 
      {{ link.others }}
      {% endif %}
    </div>
  </div>
</div>
</li>

{% endfor %}

</ol>
</div>

<script>
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('.teaser-video').forEach(function (video) {
      video.removeAttribute('autoplay');
      video.pause();
    });
  }
</script>

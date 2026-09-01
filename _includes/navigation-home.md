{% for link in site.data.navigation.main %}
  {% if link.url contains '://' %}
    {% assign navigation_url = link.url %}
  {% else %}
    {% assign navigation_url = link.url | relative_url %}
  {% endif %}
  {% if link.right %}
    <a class="normal right" href="{{ navigation_url }}">{{ link.title }}</a>
  {% else %}
    <a class="normal" href="{{ navigation_url }}">{{ link.title }}</a>
  {% endif %}
{% endfor %}

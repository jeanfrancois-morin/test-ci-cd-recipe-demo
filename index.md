---
layout: default
title: Ma recette CI/CD
---

{% capture readme_content %}
{% include_relative README.md %}
{% endcapture %}

{{ readme_content | markdownify }}

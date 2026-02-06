"""Configuration for the daily robotics blog post generator."""

# Claude model to use (Sonnet 4.5 for cost efficiency: ~$0.03/day)
MODEL = "claude-sonnet-4-5-20250929"

# RSS feeds to fetch robotics news from
RSS_FEEDS = [
    {
        "name": "IEEE Spectrum Robotics",
        "url": "https://spectrum.ieee.org/feeds/topic/robotics.rss",
    },
    {
        "name": "The Robot Report",
        "url": "https://www.therobotreport.com/feed/",
    },
    {
        "name": "TechCrunch Robotics",
        "url": "https://techcrunch.com/category/robotics/feed/",
    },
    {
        "name": "Heise Online",
        "url": "https://www.heise.de/rss/heise.rdf",
    },
    {
        "name": "Golem.de",
        "url": "https://rss.golem.de/rss.php?feed=RSS2.0",
    },
    {
        "name": "Google News DE - Robotik",
        "url": "https://news.google.com/rss/search?q=Robotik&hl=de&gl=DE&ceid=DE:de",
    },
    {
        "name": "Google News EN - Robotics",
        "url": "https://news.google.com/rss/search?q=robotics&hl=en&gl=US&ceid=US:en",
    },
    {
        "name": "Google News DE - Roboter KI",
        "url": "https://news.google.com/rss/search?q=Roboter+KI&hl=de&gl=DE&ceid=DE:de",
    },
]

# Maximum number of articles to collect per feed
MAX_ARTICLES_PER_FEED = 10

# Maximum total articles to send to Claude for topic selection
MAX_TOTAL_ARTICLES = 50

# RSS fetch timeout in seconds
FETCH_TIMEOUT = 15

# Topic selection prompt
TOPIC_SELECTION_PROMPT = """\
Du bist ein erfahrener Technik-Redakteur für einen deutschen Robotik-Blog.

Unten findest du aktuelle Nachrichten aus verschiedenen Robotik-Quellen. Wähle das EINE Thema aus, \
das sich am besten für einen tiefgehenden Blog-Artikel eignet.

Kriterien für die Auswahl:
- Aktualität und Relevanz für die Robotik-Branche
- Potenzial für eine tiefgehende Analyse (nicht nur eine kurze Meldung)
- Interesse für ein deutschsprachiges technisches Publikum
- Bevorzuge Themen mit Bezug zu Forschung, neuen Technologien oder bedeutenden Industrieentwicklungen

Antworte AUSSCHLIESSLICH im folgenden YAML-Format, ohne zusätzlichen Text:

```yaml
topic: "<Thema in einem Satz>"
angle: "<Dein vorgeschlagener Blickwinkel für den Artikel>"
sources:
  - "<Titel der relevantesten Quelle>"
  - "<Titel einer weiteren relevanten Quelle>"
tags:
  - "<Tag 1>"
  - "<Tag 2>"
  - "<Tag 3>"
category: "<Kategorie: Forschung | Industrie | KI | Humanoide Roboter | Automatisierung | Startups | Politik>"
```

Hier sind die aktuellen Nachrichten:

{news_items}
"""

# Article writing prompt
ARTICLE_WRITING_PROMPT = """\
Du bist ein erfahrener Technik-Journalist, der tiefgehende Artikel über Robotik auf Deutsch schreibt.

Schreibe einen Blog-Artikel zum folgenden Thema:

**Thema**: {topic}
**Blickwinkel**: {angle}
**Quellen-Kontext**: {sources}

Anforderungen:
- Sprache: Deutsch (natürlich, flüssig, nicht übersetzt klingend)
- Länge: 800-1200 Wörter
- Stil: Informativ, analytisch, aber zugänglich – wie ein guter Artikel in der c't oder Spektrum der Wissenschaft
- Struktur: Verwende Markdown-Überschriften (##) um den Artikel zu gliedern
- Beginne mit einer fesselnden Einleitung, die das Thema kontextualisiert
- Erkläre technische Konzepte verständlich, ohne zu vereinfachen
- Schließe mit einem Ausblick oder einer Einordnung ab
- Verwende KEINE Emojis
- Schreibe KEINE Meta-Kommentare über den Artikel selbst
- Der Artikel soll eigenständig sein und nicht auf die Quellen verlinken

Antworte NUR mit dem Artikeltext in Markdown (ohne Frontmatter, ohne Titel-Überschrift).
"""

AUTHOR = 'boinor development team'
SITENAME = 'boinor'
SITEURL = "https://www.boinor.space"

PATH = "content"

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
INDEX_SAVE_AS = "blog/index.html"

# THEME SETTINGS
THEME = './theme/'

# HEAD MENU PAGES
DOCS_PAGE = 'https://docs.boinor.space/en/latest/'
#XXX COMMUNITY_PAGE = 'http://chat.boinor.space/'
#XXX TUTORIALS_PAGE = 'https://beta.mybinder.org/v2/gh/boinor/boinor/main?filepath=index.ipynb'
BLOG_PAGE = 'blog/index.html'
CODE_PAGE = 'https://github.com/boinor/boinor'
ARCHIVES_PAGE = 'archives.html'
ABOUT_PAGE = 'pages/about-boinor.html'
#TWITTER_USERNAME = 'boinor_py'
MASTODON_USERNAME = '@boinor@alteholz.social'
GITHUB_USERNAME = 'boinor'
SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

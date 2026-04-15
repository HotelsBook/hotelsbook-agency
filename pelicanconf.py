# =============================================================================
# CONFIGURAÇÕES GERAIS - HOSPPED BY HOTELSBOK
# =============================================================================

# Identidade da Marca
AUTHOR = 'Hospped'
SITENAME = 'Hospped'
SITESUBTITLE = 'by HotelsBook'

# ⚠️ URL SEM BARRA FINAL + RELATIVE_URLS = True PARA GITHUB PAGES SUBPASTA
SITEURL = 'https://hotelsbook.github.io/hotelsbook-agency'

# Caminhos e Estrutura
PATH = 'content'
OUTPUT_PATH = 'output'
THEME = 'theme'
TIMEZONE = 'America/Fortaleza'
DEFAULT_LANG = 'pt'
MARKUP = ('md',)

# ⚠️ CONFIGURAÇÃO CRÍTICA PARA GITHUB PAGES COM SUBPASTA
RELATIVE_URLS = True  # ← Mude para True (era False)
DISPLAY_PAGES_ON_MENU = False

# Geração de slugs
SLUGIFY_SOURCE = 'title'
SLUGIFY_SUBSTITUTE = {
    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
    'ã': 'a', 'õ': 'o', 'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
    'ç': 'c', ' ': '-', '_': '-',
}

# =============================================================================
# PALETA DE CORES - JADE IMPERIAL
# =============================================================================

COLORS = {
    'primary': '#2A5D5E',
    'primary_hover': '#1f4a4b',
    'accent': '#D4AF37',
    'accent_hover': '#b8962e',
    'bg': '#F0F0E9',
    'text': '#333333',
    'text_light': '#666666',
    'text_on_primary': '#FFFFFF',
    'text_on_accent': '#333333',
}

# =============================================================================
# MENU DE NAVEGAÇÃO
# =============================================================================

MENUITEMS = [
    ('Início', '/'),
    ('Serviços', './servicos.html'),
    ('Sobre', './sobre.html'),
    ('Contato', './contato.html'),
]

# =============================================================================
# ARQUIVOS ESTÁTICOS E METADADOS
# =============================================================================

STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# =============================================================================
# SEO E META TAGS
# =============================================================================

DEFAULT_DESCRIPTION = 'Agência de reservas com atendimento humano e negociação direta. Economia de até 30% em viagens corporativas e acadêmicas em todo o Brasil.'

OG_DEFAULT_IMAGE = 'images/og-hospped.jpg'
OG_DEFAULT_IMAGE_WIDTH = 1200
OG_DEFAULT_IMAGE_HEIGHT = 630

TWITTER_CARD = 'summary_large_image'
TWITTER_SITE = '@hospped'

# =============================================================================
# PLUGINS (Opcional)
# =============================================================================

# PLUGIN_PATHS = ['plugins']
# PLUGINS = ['sitemap']

# SITEMAP = {
#     'format': 'xml',
#     'priorities': {'articles': 0.5, 'indexes': 0.5, 'pages': 1.0},
#     'changefreqs': {'articles': 'monthly', 'indexes': 'daily', 'pages': 'monthly'}
# }

# =============================================================================
# AMBIENTE: DESENVOLVIMENTO vs PRODUÇÃO
# =============================================================================

import os

if os.environ.get('PELICAN_ENV') == 'development':
    SITEURL = 'http://localhost:8000'
    RELATIVE_URLS = True
    DEBUG = True
else:
    DEBUG = False

# =============================================================================
# FEEDS E PAGINAÇÃO
# =============================================================================

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# =============================================================================
# VARIÁVEIS PARA TEMPLATES
# =============================================================================

TEMPLATE_VISIBLE_SETTINGS = {
    'SITENAME': SITENAME,
    'SITESUBTITLE': SITESUBTITLE,
    'SITEURL': SITEURL,
    'AUTHOR': AUTHOR,
    'COLORS': COLORS,
}
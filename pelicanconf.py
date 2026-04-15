# =============================================================================
# CONFIGURAÇÕES GERAIS - HOSPPED BY HOTELSBOK
# =============================================================================

# Identidade da Marca
AUTHOR = 'Hospped'
SITENAME = 'Hospped'
SITESUBTITLE = 'by HotelsBook'  # Usado em meta tags ou rodapé se desejar
SITEURL = 'https://hospped.github.io'  # ⚠️ Ajuste conforme seu domínio real

# Caminhos e Estrutura
PATH = 'content'
OUTPUT_PATH = 'output'
THEME = 'theme'
TIMEZONE = 'America/Fortaleza'
DEFAULT_LANG = 'pt'
MARKUP = ('md',)  # Formatos de conteúdo suportados

# URLs e Estrutura de Links
RELATIVE_URLS = False  # URLs absolutas para SEO e deploy em produção
DISPLAY_PAGES_ON_MENU = False  # Menu controlado manualmente via MENUITEMS
SLUGIFY_SOURCE = 'title'  # Gera slugs amigáveis a partir dos títulos
SLUGIFY_SUBSTITUTE = {  # Remove caracteres especiais dos slugs
    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
    'ã': 'a', 'õ': 'o', 'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
    'ç': 'c', ' ': '-', '_': '-',
}

# =============================================================================
# MENU DE NAVEGAÇÃO
# =============================================================================

MENUITEMS = [
    ('Início', '/'),
    ('Serviços', '/servicos.html'),
    ('Sobre', '/sobre.html'),
    ('Contato', '/contato.html'),
]

# =============================================================================
# ARQUIVOS ESTÁTICOS E METADADOS
# =============================================================================

STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    # 'extra/manifest.json': {'path': 'manifest.json'},  # PWA (opcional)
    # 'extra/sw.js': {'path': 'sw.js'},  # Service Worker (opcional)
}

# =============================================================================
# SEO E META TAGS
# =============================================================================

# Meta description padrão (usado se a página não tiver description própria)
DEFAULT_DESCRIPTION = 'Agência de reservas com atendimento humano e negociação direta. Economia de até 30% em viagens corporativas e acadêmicas em todo o Brasil.'

# Open Graph / Social Sharing (melhora compartilhamento em redes sociais)
OG_DEFAULT_IMAGE = 'images/og-hospped.jpg'  # Imagem padrão para compartilhamento
OG_DEFAULT_IMAGE_WIDTH = 1200
OG_DEFAULT_IMAGE_HEIGHT = 630

# Twitter Cards
TWITTER_CARD = 'summary_large_image'
TWITTER_SITE = '@hospped'  # Substitua pelo handle real se tiver

# =============================================================================
# PLUGINS RECOMENDADOS (Opcionais mas úteis)
# =============================================================================

# Para usar plugins, instale primeiro: pip install pelican-plugins-sitemap pelican-plugins-seo
# Depois, adicione ao PLUGIN_PATHS e PLUGINS abaixo:

# PLUGIN_PATHS = ['plugins']  # Caminho para plugins locais ou submódulos
# PLUGINS = [
#     'sitemap',      # Gera sitemap.xml automaticamente
#     'seo',          # Otimiza meta tags automaticamente
# ]

# Configuração do Plugin Sitemap (se ativado)
# SITEMAP = {
#     'format': 'xml',
#     'priorities': {
#         'articles': 0.5,
#         'indexes': 0.5,
#         'pages': 1.0,
#     },
#     'changefreqs': {
#         'articles': 'monthly',
#         'indexes': 'daily',
#         'pages': 'monthly',
#     }
# }

# =============================================================================
# CONFIGURAÇÕES DE DESENVOLVIMENTO vs PRODUÇÃO
# =============================================================================

# Detecta ambiente para ajustar configurações automaticamente
import os

if os.environ.get('PELICAN_ENV') == 'development':
    # Configurações para desenvolvimento local
    SITEURL = 'http://localhost:8000'
    RELATIVE_URLS = True
    DEBUG = True
else:
    # Configurações para produção (deploy)
    DEBUG = False
    # Minificação pode ser adicionada aqui se usar plugin apropriado

# =============================================================================
# FEEDS (Opcional - se quiser RSS/Atom)
# =============================================================================

FEED_ALL_ATOM = None  # Desativado para site institucional
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# =============================================================================
# PAGINAÇÃO E LISTAGENS
# =============================================================================

DEFAULT_PAGINATION = 10  # Não usado em site sem blog, mas mantido por padrão

# =============================================================================
# CONFIGURAÇÕES ADICIONAIS DE TEMA
# =============================================================================

# Variáveis globais disponíveis em todos os templates
TEMPLATE_VISIBLE_SETTINGS = {
    'SITENAME': SITENAME,
    'SITESUBTITLE': SITESUBTITLE,
    'SITEURL': SITEURL,
    'AUTHOR': AUTHOR,
}

# =============================================================================
# CONFIGURAÇÕES DE ACESSIBILIDADE E PERFORMANCE
# =============================================================================

# Preload de fontes críticas (opcional - pode ser adicionado no base.html também)
# EXTRA_HEADER_HTML = '''
# <link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
# <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap"></noscript>
# '''
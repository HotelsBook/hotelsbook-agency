# HotelsBook Agency Configuration
AUTHOR = 'HotelsBook Agency'
SITENAME = 'HotelsBook Agency'
SITEURL = 'https://hotelsbook.github.io/hotelsbook-agency'

PATH = 'content'
OUTPUT_PATH = 'output'
THEME = 'theme'
TIMEZONE = 'America/Fortaleza'
DEFAULT_LANG = 'pt'
MARKUP = ('md',)

# URLs amigáveis
RELATIVE_URLS = False
DISPLAY_PAGES_ON_MENU = False

# Configuração para encontrar páginas em content/pages/
PAGE_PATHS = ['content/pages']

# Menu de navegação (atualizado)
MENUITEMS = [
    ('Serviços', '/servicos.html'),
    ('Sobre', '/sobre.html'),
    ('Contato', '/contato.html'),
]

# Arquivos estáticos (para robots.txt, favicon, etc.)
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
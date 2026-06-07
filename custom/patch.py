import re

# 1. Patch index.html
print("Patching index.html...")
index_path = "/root/whatsapp-api/custom/index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("<title>Evolution Manager</title>", "<title>W-API v2</title>")
html = html.replace('href="https://evolution-api.com/files/evo/favicon.svg"', 'href="/assets/images/evolution-logo.png"')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html patched.")

# 2. Patch JS file
print("Patching JS file...")
js_path = "/root/whatsapp-api/custom/index-CO3NSIFj.js"
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace product name and header texts
js = js.replace("Evolution Manager - Modern web interface for Evolution API management", "W-API v2 - Seu código produtivo em sua máxima potência.")
js = js.replace("Welcome to Evolution Manager", "Bem-vindo ao Painel de Integração")
js = js.replace("Welcome to Evolution API", "Bem-vindo ao Painel de Integração")
js = js.replace("A powerful, modern dashboard for managing your WhatsApp API instances with Evolution API", "Um painel moderno e intuitivo construído para gerenciar suas instâncias de API do WhatsApp e monitorar webhooks em tempo real.")

# Fallbacks in case of partial replaces or different strings
js = js.replace("Modern web interface for Evolution API management", "Seu código produtivo em sua máxima potência.")
js = js.replace("Access Manager Dashboard", "Entrar no Painel")
js = js.replace("Resources & Support", "Recursos & Suporte")

# Replace card texts (GitHub, Website, Contact)
js = js.replace('children:"GitHub"', 'children:"Documentação"')
js = js.replace('children:"Source code"', 'children:"Consulte nossa referência de API e rotas Postman"')
js = js.replace('href:"https://github.com/EvolutionAPI/evolution-api"', 'href:"http://2.25.183.40:9000"')

js = js.replace('children:"Website"', 'children:"Status do Sistema"')
js = js.replace('children:"Official site"', 'children:"Verifique a estabilidade operacional dos nossos servidores"')
js = js.replace('href:"https://evolution-api.com"', 'href:"http://2.25.183.40:9000"')

js = js.replace('children:"Contact"', 'children:"Suporte Interno"')
js = js.replace('children:"Get support"', 'children:"Abra um chamado com o time de engenharia"')

# Hide footer social/doc links
js = js.replace('o=[{name:"Discord",url:"https://evolution-api.com/discord"},{name:"Postman",url:"https://evolution-api.com/postman"},{name:"GitHub",url:"https://github.com/EvolutionAPI/evolution-api"},{name:"Docs",url:"https://doc.evolution-api.com"}]', 'o=[]')

# Replace copyright
js = js.replace("© 2024 Evolution API", "© 2026 W-API. Todos os direitos reservados. Uso exclusivo interno e homologado.")
js = js.replace("© 2025 Evolution API", "© 2026 W-API. Todos os direitos reservados. Uso exclusivo interno e homologado.")
js = js.replace("Evolution API is an open-source", "W-API é uma interface de uso exclusivo interno.")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("JS file patched.")

# 3. Patch CSS file
print("Patching CSS file...")
css_path = "/root/whatsapp-api/custom/index-DsIrum0U.css"
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Hide top-left Logo, replace it with a styled title, and remove any remaining social links
hide_rules = '\n\n'
# Hide top left evolutionapi logo image/svg completely
hide_rules += 'header img[src*="evolution"], header svg, .logo-container img { display: none !important; }\n'
# Add a custom text "W-API v2" in the header using a pseudo-element
hide_rules += 'header::before { content: "W-API v2"; font-weight: bold; font-size: 1.25rem; color: #10b981; margin-right: auto; padding-left: 10px; }\n'
# Hide the center logo above W-API v2 title on the login card
hide_rules += '.flex.justify-center.mb-8 img, img[src*="evolution-logo"], svg[class*="logo"] { display: none !important; }\n'

css += hide_rules

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("CSS file patched.")

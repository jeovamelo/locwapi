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
print("Patching index-CO3NSIFj.js...")
js_path = "/root/whatsapp-api/custom/index-CO3NSIFj.js"
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Let's do replacements for the brand
js = js.replace("Evolution Manager", "W-API v2")
js = js.replace("Evolution API", "W-API")

# Replace header/landing texts
js = js.replace("Evolution API - Modern web interface...", "Seu código produtivo em sua máxima potência.")
js = js.replace("Modern web interface", "Seu código produtivo em sua máxima potência.")

# Replace welcome texts
js = js.replace("Welcome to Evolution API", "Bem-vindo ao Painel de Integração")
js = js.replace("Welcome to Evolution Manager", "Bem-vindo ao Painel de Integração")

# Replace login description
js = js.replace("Please enter your credentials to continue", "Por favor, insira suas credenciais para continuar")

# Replace button text
js = js.replace("Access Manager Dashboard", "Entrar no Painel")

# Replace resources/support footer section
js = js.replace("Resources & Support", "Recursos & Suporte")

# Replace copyright
js = js.replace("© 2024 Evolution API", "© 2026 W-API. Todos os direitos reservados. Uso exclusivo interno e homologado.")
js = js.replace("© 2025 Evolution API", "© 2026 W-API. Todos os direitos reservados. Uso exclusivo interno e homologado.")
js = js.replace("Evolution API is an open-source", "W-API é uma interface de uso exclusivo interno.")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("JS file patched.")

# 3. Patch CSS file to hide elements and customize style
print("Patching index-DsIrum0U.css...")
css_path = "/root/whatsapp-api/custom/index-DsIrum0U.css"
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Hide Discord, GitHub, Postman, Docs and external links
hide_rules = '\n\na[href*="discord"], a[href*="github"], a[href*="postman"], a[href*="docs"], a[href*="evolution-api.com"] { display: none !important; }\n'
# Hide Evolution logo and replace with title placeholder
hide_rules += '.logo-container img, img[src*="evolution-logo"], svg[class*="logo"] { content: url("/assets/images/evolution-logo.png"); max-height: 50px; }\n'

css += hide_rules

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("CSS file patched.")

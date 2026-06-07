import re
with open('/root/whatsapp-api/docker-compose.yml', 'r') as f:
    content = f.read()
api_key = re.search(r'AUTHENTICATION_API_KEY=([^\s]+)', content).group(1)
db_pass = re.search(r'POSTGRES_PASSWORD:\s*([^\s]+)', content).group(1)
print(f"{api_key}|||{db_pass}")

import os
from dotenv import load_dotenv
from azure.identity import EnvironmentCredential
from azure.keyvault.secrets import SecretClient

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
key_vault_name = os.getenv('KEY_VAULT_NAME')
kv_url = f"https://{key_vault_name}.vault.azure.net/"

# Autenticação com Azure usando EnvironmentCredential
credential = EnvironmentCredential()
client = SecretClient(vault_url=kv_url, credential=credential)

# Recuperar um segredo do Key Vault
secret_key_name = "KEY"
retrieved_secret = client.get_secret(secret_key_name)
print(f"Valor do segredo '{secret_key_name}': {retrieved_secret.value}")

secret_region_name = "REGION"
retrieved_secret = client.get_secret(secret_region_name)
print(f"Valor do segredo '{secret_region_name}': {retrieved_secret.value}")


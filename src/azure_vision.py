## src/azure_vision.py
# Este módulo contém funções para interagir com a API de Visão Computacional da Azure
import os
import time
from dotenv import load_dotenv
from azure.keyvault.secrets import SecretClient
from azure.identity import EnvironmentCredential
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# Carrega variáveis de ambiente
load_dotenv()

# Função para obter as credenciais de visão computacional
def get_vision_credentials():
    # Tenta obter do Key Vault
    key_vault_name = os.getenv('KEY_VAULT_NAME')
    if key_vault_name:
        kv_url = f"https://{key_vault_name}.vault.azure.net/"
        credential = EnvironmentCredential()
        secret_client = SecretClient(vault_url=kv_url, credential=credential)
        key = secret_client.get_secret("KEY").value
        endpoint = secret_client.get_secret("ENDPOINT").value
    else:
        # Fallback para variáveis de ambiente locais
        key = os.getenv("VISION_KEY")
        endpoint = os.getenv("VISION_ENDPOINT")
    return endpoint, key

def detectar_textos(img_path):
    endpoint, key = get_vision_credentials()
    client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))

    # Verifica se o caminho da imagem é válido
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Imagem não encontrada: {img_path}")
    # Lê a imagem do caminho fornecido
    # O método read_in_stream é usado para enviar a imagem para análise . O parâmetro raw=True é usado para obter a resposta bruta da operação
    if not img_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        raise ValueError("O arquivo deve ser uma imagem PNG ou JPG.")
    # Abre a imagem em modo binário
    with open(img_path, "rb") as img:
        # Usa o método correto para leitura de texto
        read_response = client.read_in_stream(img, raw=True)
        # Obtém o ID da operação
        operation_location = read_response.headers["Operation-Location"]
        operation_id = operation_location.split("/")[-1]

    # Aguarda o resultado da operação .O status pode ser 'notStarted', 'running' ou 'succeeded'
    while True:
        # Obtém o resultado da operação. O método get_read_result é usado para verificar o status da operação
        result = client.get_read_result(operation_id)
        if result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    # Extrai os textos detectados
    # Se o status for 'succeeded', extrai os textos das linhas detectadas
    componentes = []
    if result.status == 'succeeded':
        for page in result.analyze_result.read_results:
            for line in page.lines:
                componentes.append(line.text)
    return componentes
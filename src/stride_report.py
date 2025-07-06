## src/stride_report.py
# Este módulo contém funções para gerar relatórios de ameaças e contramedidas usando o modelo
# STRIDE e buscar vulnerabilidades associadas a componentes de software.
# Ele utiliza um mapeamento de ameaças e contramedidas predefinido, 
# além de uma função para buscar vulnerabilidades de um módulo externo.

# Importa as bibliotecas necessárias
import json
import os
from vulnerabilidades import buscar_vulnerabilidades

# Carrega o mapeamento de ameaças e contramedidas do arquivo JSON
# O mapeamento é usado para associar componentes a ameaças específicas
stride_map_path = os.path.join(os.path.dirname(__file__), "stride_map.json")
with open(stride_map_path) as f:
    stride_map = json.load(f)

# Define as contramedidas para cada tipo de ameaça
contramedidas = {
    "Spoofing": "Autenticação forte",
    "Tampering": "Criptografia e integridade",
    "Repudiation": "Logs auditáveis",
    "Information Disclosure": "Criptografia TLS, RBAC",
    "DoS": "Rate limiting",
    "Elevation of Privilege": "Menor privilégio"
}

# Função para gerar um relatório de ameaças e contramedidas para os componentes fornecidos
# A função itera sobre os componentes, busca as ameaças associadas e gera um relatório
def gerar_relatorio(componentes):
    relatorio = []
    for componente in componentes:
        # Procura o componente na lista stride_map
        info = next((item for item in stride_map if item["componente"].lower() == componente.lower()), None)
        if info:
            relatorio.append({
                "componente": componente,
                "ameacas": info.get("ameacas", []),
                "contramedidas": info.get("contramedidas", []),
                "vulnerabilidades": buscar_vulnerabilidades(componente.lower())
            })
        else:
            relatorio.append({
                "componente": componente,
                "ameacas": [],
                "contramedidas": [],
                "vulnerabilidades": buscar_vulnerabilidades(componente.lower())
            })
    return relatorio

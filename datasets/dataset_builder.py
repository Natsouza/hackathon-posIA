import os
import json
from pathlib import Path
from turtle import st

# Função para construir o dataset de imagens
# Busca todas as imagens em uma pasta específica e retorna uma lista de caminhos
def construir_dataset(pasta_imagens="datasets/images"):
    extensoes_validas = [".jpg", ".jpeg", ".png"]
    return [str(p) for p in Path(pasta_imagens).rglob("*") if p.suffix.lower() in extensoes_validas]


# Função para anotar os componentes detectados nas imagens
# Essa função utiliza a API de visão da Azure para detectar textos nas imagens e salva as anotações em um arquivo JSON
def anotar_componentes(imagens, saida_json="datasets/anotacoes.json"):
    from azure_vision import detectar_textos
    anotacoes = []
    # Itera sobre cada imagem, detecta os textos e salva as anotações
    if not imagens:
        st.warning("Nenhuma imagem encontrada. Certifique-se de que a pasta contém imagens válidas.")
        return
    st.info(f"Encontradas {len(imagens)} imagens para análise.")
  
    # Verifica se o diretório de saída existe, se não, cria o diretório de saída se não existir
    if not os.path.exists(os.path.dirname(saida_json)):
        os.makedirs(os.path.dirname(saida_json))
    for img in imagens:
        st.write(f" Analisando imagem: {img}")
        componentes = detectar_textos(img)
        anotacoes.append({
            "imagem": img,
            "componentes_detectados": componentes
        })
        st.write(f" Componentes detectados: {componentes}")
        st.info(f" Análise concluída. {len(anotacoes)} imagens processadas.")
   
   # Salva as anotações em um arquivo JSON
    if not anotacoes:
        st.warning("Nenhum componente detectado nas imagens.")
        return
    os.makedirs(os.path.dirname(saida_json), exist_ok=True)
    with open(saida_json, "w") as f:
        json.dump(anotacoes, f, indent=4)
    st.success(f" Anotações salvas em {saida_json}")
# app.py - Interface Streamlit para análise STRIDE com Azure Vision

import streamlit as st
from azure_vision import detectar_textos
from stride_report import gerar_relatorio
from vulnerabilidades import vulnerabilidades_dict
import os
import json
from pathlib import Path

# Verifica se o arquivo de mapeamento STRIDE existe
stride_map_path = os.path.join(os.path.dirname(__file__), "stride_map.json")
with open(stride_map_path) as f:
    stride_map = json.load(f)
st.set_page_config(page_title="Analisador STRIDE com Azure Vision")
st.title("Analisador de Ameaças STRIDE a partir de Diagrama de Arquitetura")

if not os.path.exists(stride_map_path):
    st.error(f"Arquivo de mapeamento STRIDE não encontrado: {stride_map_path}")
    st.stop()
imagem = st.file_uploader("Envie a imagem do diagrama (PNG ou JPG)", type=["png", "jpg", "jpeg"])

# Verifica se a imagem foi carregada. Se a imagem não for carregada, exibe uma mensagem de aviso e encerra a execução
if not imagem:  
    st.warning("Por favor, carregue uma imagem do diagrama de arquitetura.")
    st.stop()
if imagem:
    # Salva a imagem temporariamente para análise
    # O caminho temporário é usado para evitar problemas de leitura direta do objeto de arquivo
    temp_path = "temp_img.jpg"
    with open(temp_path, "wb") as f:
        # Lê o conteúdo da imagem carregada e escreve no arquivo temporário
        # Isso garante que a imagem esteja disponível para a API de Visão Computacional da Azure
        f.write(imagem.read())

    st.image(temp_path, caption="Imagem carregada", use_container_width=True)
    with st.spinner("Analisando a imagem com Azure Computer Vision..."):
        componentes = detectar_textos(temp_path)

    st.success(f" {len(componentes)} componentes detectados:")
    st.write(componentes)

    # Gera o relatório de ameaças e contramedidas usando o modelo STRIDE
    relatorio = gerar_relatorio(componentes)

    st.header("Relatório STRIDE")
    for item in relatorio:
        componentes = item["componente"].lower()
        vulnerabilidades = vulnerabilidades_dict.get(componentes, [])
        st.write(f"**Componente:** {item['componente']}")
        st.write(f"**Ameaças:** {', '.join(item['ameacas']) if item['ameacas'] else 'Nenhuma'}")
        st.write(f"**Contramedidas:** {', '.join(item['contramedidas']) if item['contramedidas'] else 'Nenhuma'}")
        st.write(f"**Vulnerabilidades:** {', '.join(vulnerabilidades) if vulnerabilidades else 'Nenhuma encontrada'}")
        st.markdown("---")
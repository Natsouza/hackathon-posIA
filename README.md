# hackathon-posIA
Hackathon referente a pós IA
Projeto: Análise de Diagramas de Arquitetura com Azure Computer Vision + STRIDE

Este projeto utiliza o serviço Azure Computer Vision para identificar automaticamente componentes em diagramas de arquitetura de software (AWS e Azure), gerar um relatório de ameaças baseado na metodologia STRIDE, e apresentar as vulnerabilidades e contramedidas por componente.

🔧 Tecnologias Utilizadas

Python 3.10+

Streamlit (interface web)

Azure Cognitive Services (Computer Vision)

OpenCV (leitura/edição de imagem)

Pillow (manipulação de imagem)

JSON (armazenamento de ameaças)


▶️ Como Executar o Projeto Localmente

1. Clone o repositório

git clone https://github.com/seuusuario/hackathon-posIA.git
cd hackathon-posIA

2. Crie o ambiente virtual (opcional mas recomendado)

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Instale as dependências

pip install -r requirements.txt

4. Configure variáveis de ambiente

Crie um arquivo .env com as seguintes variáveis:

AZURE_CV_ENDPOINT=https://<seu-endpoint>.cognitiveservices.azure.com/
AZURE_CV_KEY=<sua-chave-de-api>

5. Execute a aplicação

streamlit run src/app.py

📸 Como Usar

Faça upload de um diagrama de arquitetura (PNG, JPG, etc.)

A aplicação analisará os componentes com o Azure Computer Vision

Será exibido:

Lista de componentes identificados

Ameaças STRIDE por componente

Vulnerabilidades e contramedidas

📌 Possíveis Melhorias

Treinar modelo próprio com dataset anotado para detectar ícones de arquitetura

Integração com CV de outras nuvens (Google Vision API)

Exportação de relatório em PDF ou DOCX

🧠 Metodologia STRIDE

STRIDE é um modelo de modelagem de ameaças que representa:

Spoofing

Tampering

Repudiation

Information Disclosure

Denial of Service

Elevation of Privilege

👨‍💻 Autoria

Projeto desenvolvido para Hackathon 3IADT - Inteligência Artificial para Devs
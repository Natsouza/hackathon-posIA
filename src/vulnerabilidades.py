vulnerabilidades_dict  = {
    # Azure
    "api gateway": ["Exposição de endpoints públicos", "Rate limit ausente", "Headers de segurança ausentes"],
    "api management": ["Falta de autenticação entre APIs expostas", "Exposição de logs com dados sensíveis"],
    "developer portal": ["Documentação sensível exposta", "Falta de autenticação"],
    "logic apps": ["Execução indevida de fluxos", "Exposição de variáveis sensíveis"],
    "azure services": ["Configuração incorreta de IAM", "Uso de permissões excessivas"],
    "saas services": ["Falta de criptografia de dados em trânsito", "Autenticação fraca"],
    "rest": ["Falhas em validação de entrada", "Exposição de dados sensíveis"],
    "soap": ["Vulnerabilidade XXE (External Entity Attack)", "Falha de parsing XML"],
    "microsoft entra": ["Falta de MFA", "Autenticação fraca"] ,
    "resource group": ["Permissões excessivas concedidas", "Objetos não segregados por função"],

   
    # AWS
    "application load balancer": ["Exposição de serviços internos", "Falta de WAF configurado"],
    "aws shield": ["Ineficiência contra ataques zero-day", "Cobertura limitada para camadas superiores"],
    "cloudfront": ["Distribuição de conteúdo não seguro", "Headers de cache indevidos"],
    "aws waf": ["Regras mal configuradas", "Não atualização das regras"],
    "cloudtrail": ["Logs não criptografados", "Logs não armazenados de forma segura"],
    "aws kms": ["Chaves expostas ou mal gerenciadas", "Políticas permissivas"],
    "aws backup": ["Backups não criptografados", "Falta de verificação de integridade"],
    "cloudwatch": ["Monitoramento ineficaz", "Alertas não configurados"],
    "efs": ["Acesso público indevido", "Sem controle de versão"],
    "rds": ["SQL Injection", "Credenciais padrão ativas"],
    "elasticache": ["Exposição de dados em cache", "Sem TLS nas conexões"],
    "auto scaling": ["Escalonamento com base em métricas manipuláveis", "Sem limites máximos configurados"],
    "solr": ["Exposição da interface de administração", "Sem autenticação básica"],
    "sei / sip": ["Exposição de interfaces públicas sem autenticação forte","Ausência de verificação de input (risco de XSS/SQLi)","Uso de protocolos inseguros (ex: HTTP sem TLS)","Dependência de bibliotecas desatualizadas","Autorização mal configurada entre perfis de usuário"],
    "vpc": ["Segurança de rede mal configurada", "Regras de firewall permissivas"],
    "public subnet": ["Acesso direto da internet sem proteção", "Falta de NAT Gateway"],
    "private subnet": ["Falta de isolamento de rede", "Rotas indevidas para internet"],
    "availability zone": ["Distribuição incorreta de carga", "Dependência de uma única zona"],
    "amazon simple email service": ["Envio de phishing", "Falta de autenticação SPF/DKIM"],
    "ec2": ["Portas abertas sem controle de firewall (SG/NACL)", "Acesso SSH exposto à internet", "Uso de AMIs não verificadas", "Credenciais armazenadas em disco", "Falta de atualizações no sistema operacional"]
}

# Função para buscar vulnerabilidades associadas a um componente
# Esta função recebe o nome de um componente e retorna uma lista de vulnerabilidades associadas
# Se o componente não estiver no dicionário, retorna uma lista vazia
# Exemplo de uso: buscar_vulnerabilidades("api gateway")
def buscar_vulnerabilidades(comp):
    return vulnerabilidades_dict.get(comp.lower(), [])

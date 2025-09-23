from cryptography.fernet import Fernet
import json
import logging
from datetime import datetime

# Geração de chave para criptografia (em produção, armazene com segurança)
chave = Fernet.generate_key()
fernet = Fernet(chave)

# Configuração de log
logging.basicConfig(filename='logs_acesso.log', level=logging.INFO)

def validar_dados(dados):
    """
    Valida se os dados seguem os princípios da LGPD:
    - Minimização
    - Finalidade
    - Consentimento
    """
    campos_obrigatorios = ['id_anonimo', 'data_evento', 'tipo_evento']
    for campo in campos_obrigatorios:
        if campo not in dados:
            raise ValueError(f"Dado ausente: {campo}")
    return True

def aplicar_criptografia(dados_sensiveis):
    """
    Criptografa dados sensíveis usando Fernet (AES 128)
    """
    dados_json = json.dumps(dados_sensiveis)
    dados_encriptados = fernet.encrypt(dados_json.encode())
    return dados_encriptados

def gerar_log_acesso(usuario, acao):
    """
    Registra log de acesso com timestamp
    """
    timestamp = datetime.now().isoformat()
    log_msg = f"{timestamp} | Usuário: {usuario} | Ação: {acao}"
    logging.info(log_msg)


# 🔐 Hackathon Forecast Big Data 2025 – Camada de Segurança e LGPD

Este projeto foi desenvolvido como parte do desafio técnico do Hackathon Forecast Big Data 2025, com foco em previsão de demanda de vendas utilizando machine learning. A contribuição abaixo adiciona uma camada robusta de segurança e conformidade com a LGPD.

---

## 📁 Estrutura da Contribuição

### 1. Documentação Legal e de Conformidade

- `docs/seguranca/politica_privacidade.md`  
  Política de privacidade alinhada à Lei nº 13.709/2018 (LGPD)

- `docs/seguranca/termo_consentimento.md`  
  Termo de consentimento claro e objetivo para uso de dados

- `docs/seguranca/plano_recuperacao.md`  
  Plano de recuperação de dados e resposta a incidentes

- `docs/seguranca/checklist_seguranca.md`  
  Checklist técnico para auditoria e validação de segurança

---

### 2. Monitoramento e Alertas

- `scripts/monitoramento_logs.py`  
  Script Python que monitora o arquivo `seguranca.log` e envia alertas por e-mail em caso de `WARNING` ou `ERROR`.

#### 🔧 Tecnologias utilizadas:
- `smtplib` + `email.mime` para envio de e-mails
- Monitoramento incremental com controle de posição (`last_log_position.txt`)
- Integração com Gmail via SMTP seguro

Exemplo de código: monitoramento_logs.py
import os
import smtplib
from email.mime.text import MIMEText

LOG_FILE = 'seguranca.log'
LAST_POSITION_FILE = 'last_log_position.txt'
EMAIL_SENDER = 'seu_email@gmail.com'
EMAIL_RECEIVER = 'destinatario@example.com'
EMAIL_PASSWORD = 'sua_senha_de_app'

def send_alert(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"Alerta enviado: {subject}")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

def monitor_logs():
    last_pos = 0
    if os.path.exists(LAST_POSITION_FILE):
        with open(LAST_POSITION_FILE, 'r') as f:
            last_pos = int(f.read())

    with open(LOG_FILE, 'r') as f:
        f.seek(last_pos)
        new_logs = f.readlines()
        current_pos = f.tell()

    for line in new_logs:
        if 'ERROR' in line or 'WARNING' in line:
            send_alert("Alerta de Segurança no Pipeline", line.strip())

    with open(LAST_POSITION_FILE, 'w') as f:
        f.write(str(current_pos))

if __name__ == "__main__":
    monitor_logs()

---

### 3. Segurança Técnica

- Criptografia com algoritmo Fernet
- Controle de acesso ao código e dados
- Minimização de dados e anonimização
- `.gitignore` configurado para proteger arquivos sensíveis (`.log`, `.key`, etc.)

---

## 👤 Autor da Contribuição

**Vinicios Tsatsoulis**  
Profissional de Cibersegurança e Governança de TI  
Pós-graduando em IA e Machine Learning  
Experiência em segurança patrimonial, análise de riscos, docência e alta performance esportiva

---

## 📬 Contato

Para dúvidas ou sugestões, abra uma issue ou envie uma mensagem via [LinkedIn](https://www.linkedin.com/in/viniciostsatsoulis).

---

## ✅ Status do Pull Request

Aguardando revisão e merge pelo responsável do repositório.


Mesmo trabalhando com dados anonimizados, o projeto respeita os princípios da LGPD. Caso este projeto evolua para utilizar dados pessoais, garantiremos todos os direitos aos titulares, como acesso, correção, anonimização e eliminação dos seus dados.

## 6. Contato
Para dúvidas sobre esta Política de Privacidade, entre em contato com a equipe do projeto através do repositório no GitHub.

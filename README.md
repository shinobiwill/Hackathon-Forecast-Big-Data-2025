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

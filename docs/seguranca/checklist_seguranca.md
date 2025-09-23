# Checklist de Segurança — Projeto Forecast Big Data 2025


| Item                      | Status | Observações |
|---------------------------|--------|-------------|
| **1. Criptografia**       |        |             |
| Criptografia em repouso   | ✅     | Implementada com `cryptography.fernet` para os dados processados. |
| Criptografia em trânsito  | N/A    | O projeto não envolve a transmissão de dados em rede. |
| Gerenciamento de chaves   | ✅     | Chave armazenada em `chave.key` e carregada em tempo de execução. **Não deve ser commitada.** |

| **2. Validação e Sanitização** |        |             |
| Validação de esquema       | ✅     | Script Python (`pipeline_seguro.py`) verifica a presença de colunas obrigatórias. |
| Tratamento de nulos        | ✅     | Remoção de linhas com valores ausentes (`dropna()`). |

| **3. Controle de Acesso**  |        |             |
| Acesso ao repositório      | ✅     | Permissões de acesso gerenciadas via configurações do GitHub. |
| Proteção de branches       | ✅     | Branch `main` protegida contra pushes diretos via GitHub Settings. |

| **4. Monitoramento e Logs**|        |             |
| Logs de auditoria          | ✅     | Arquivo `seguranca.log` registra eventos importantes do pipeline. |
| Alertas de segurança       | ✅     | Logs configurados para registrar falhas críticas; recomendação de integração futura com GitHub Actions. |

| **5. Recuperação de Desastres** |        |             |
| Plano de backup            | ✅     | Estratégia definida no `plano_recuperacao.md`. |
| Teste de recuperação       | ✅     | Teste realizado com restauração de dados criptografados usando `chave.key`. |


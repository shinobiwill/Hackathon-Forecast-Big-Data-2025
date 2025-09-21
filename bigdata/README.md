# Guia de Execução do Pipeline de Previsão de Vendas

## 1. Visão Geral

Este documento descreve o passo a passo para executar o pipeline de Machine Learning contido no notebook `cat_xgboost_lightgbm_3.ipynb`. O objetivo do projeto é prever a demanda de vendas agregada para os próximos 7 dias por produto e loja, utilizando um ensemble de modelos de Gradient Boosting (LightGBM, XGBoost, CatBoost).

## 2. Pré-requisitos

Antes de iniciar, garanta que você tenha o seguinte ambiente configurado:

1.  **Python:** Versão 3.9 ou superior (o notebook foi desenvolvido com Python 3.13).
2.  **Gerenciador de Pacotes:** `pip` instalado e atualizado.
3.  **Ambiente Virtual (Recomendado):** Para isolar as dependências do projeto.
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Linux/macOS
    .venv\Scripts\activate      # No Windows
    ```
4.  **Hardware Recomendado:**
    *   **RAM:** Mínimo de **32 GB**
    *   **Processador:** Mínimo de **8 núcleos**

    > ***Observação Importante:*** *O pipeline processa um volume considerável de dados (milhões de linhas) e executa tarefas computacionalmente intensivas, como engenharia de features em larga escala e otimização de hiperparâmetros. Em máquinas com especificações inferiores, a execução (especialmente nas Células 3, 5 e 6) pode ser extremamente lenta ou falhar por falta de memória.*

## 3. Estrutura de Diretórios

Para que o notebook funcione corretamente, os arquivos de dados devem estar organizados na seguinte estrutura de pastas, relativa à localização do seu notebook:

```
/seu_projeto/
├── cat_xgboost_lightgbm_3.ipynb         # O seu notebook
└── data_parquet/                        # Pasta contendo os arquivos de dados brutos
    ├── part-00000-tid-27790...parquet   # Dados dos pontos de venda (PDV)
    ├── part-00000-tid-51965...parquet   # Dados de vendas (sales)
    └── part-00000-tid-71732...parquet   # Dados dos produtos (products)
```

**Importante:** Se seus dados estiverem em outro local, você precisará ajustar os caminhos na Célula 2.

## 4. Passo a Passo da Execução

Execute as células do notebook na ordem sequencial. Abaixo estão as instruções e o que esperar de cada passo.

---

### Passo 1: Instalação e Configuração (Célula 1)

**O que faz:** Instala todas as bibliotecas necessárias, importa os módulos e define funções de utilidade (como a métrica customizada `wmate` e o monitoramento de memória).

**Ação:**
1.  Execute a **Célula 1**.
2.  Aguarde a conclusão da instalação das bibliotecas.

**Saída Esperada:**
*   Mensagens de instalação do `pip`.
*   A versão do XGBoost instalada.
*   A mensagem `✅ Instalações e importações concluídas!`.
*   O uso inicial de memória RAM.

---

### Passo 2: Carregamento e Pré-processamento dos Dados (Célula 2)

**O que faz:** Carrega os três arquivos Parquet, os une em um único DataFrame, trata valores nulos e agrega os dados transacionais para um formato de série temporal diária (produto-loja-dia).

**Ação:**
1.  **Verifique a variável `base_path`:**
    *   Se você seguiu a estrutura de diretórios recomendada, o valor `base_path = './'` está correto.
    *   Se seus dados estão em outro lugar, ajuste o caminho. Ex: `base_path = '/caminho/para/meus/dados/'`.
2.  Execute a **Célula 2**.

**Saída Esperada:**
*   Mensagens indicando o progresso: "Iniciando carregamento...", "Dados carregados.", "Agregando dados...".
*   Ao final, a mensagem `Agregação concluída.` com o `shape` do DataFrame e o uso de RAM.

---

### Passo 3: Engenharia de Features (Célula 3)

**O que faz:** Cria um conjunto robusto de features para os modelos, incluindo features de calendário, lags de vendas, médias móveis (com média e desvio padrão) e uma variável de preço simulada. Ao final, salva um "checkpoint" do DataFrame processado.

**Ação:**
1.  Execute a **Célula 3**. Esta célula pode levar alguns minutos para ser concluída, dependendo do poder de processamento da sua máquina.

**Saída Esperada:**
*   Mensagens de progresso: "Criando features...", "Calculando features...".
*   Ao final, a confirmação de que o checkpoint foi salvo: `Checkpoint com features avançadas salvo em: ./df_model_ready_final_v2.parquet`.

> **Dica:** O arquivo `df_model_ready_final_v2.parquet` é muito útil. Se você precisar reiniciar o kernel, pode pular as Células 2 e 3 e ir direto para a Célula 4, carregando este arquivo.

---

### Passo 4: Preparação para Modelagem (Célula 4)

**O que faz:** Carrega o DataFrame do checkpoint, separa os dados em features (`X`) e alvo (`y`), codifica as variáveis categóricas para formato numérico e define a estratégia de validação cruzada para séries temporais (`TimeSeriesSplit`).

**Ação:**
1.  **Verifique o caminho do `read_parquet`:** Certifique-se de que o caminho para `df_model_ready_final_v2.parquet` está correto.
2.  Execute a **Célula 4**.

**Saída Esperada:**
*   A mensagem `Pronto para treinar com 3 folds.` e o `shape` da matriz `X`.

---

### Passo 5: Otimização de Hiperparâmetros (Célula 5)

**O que faz:** Utiliza a biblioteca Optuna para encontrar os melhores hiperparâmetros para LightGBM, XGBoost e CatBoost. Este processo é fundamental para extrair a máxima performance dos modelos.

**Ação:**
1.  Execute a **Célula 5**.
2.  **Seja paciente:** Esta é a etapa **mais demorada** do pipeline. Ela treina múltiplos modelos com diferentes configurações e é altamente intensiva em CPU e RAM.

> **Para agilizar (opcional):** Você pode reduzir o valor de `n_trials` (ex: de `15` para `5`) em cada estudo para uma execução mais rápida, com o custo de uma otimização potencialmente menos precisa.

**Saída Esperada:**
*   Logs de progresso do Optuna para cada modelo.
*   No final, as mensagens com os melhores parâmetros encontrados para LightGBM, XGBoost e CatBoost.

---

### Passo 6: Treinamento Final com Validação Cruzada (Célula 6)

**O que faz:** Treina os três modelos usando os melhores hiperparâmetros encontrados no passo anterior, aplicando a validação cruzada (`TimeSeriesSplit`). As previsões de validação (OOF) e de teste são salvas para a etapa de ensemble.

**Ação:**
1.  Execute a **Célula 6**.

**Saída Esperada:**
*   Logs de progresso para cada fold e cada modelo, mostrando o score `WMATE` de validação.
*   Ao final, a mensagem `✅ Treinamento de todos os modelos concluído.`.

---

### Passo 7: Ensemble e Avaliação Final (Célula 7)

**O que faz:** Combina as previsões dos três modelos usando uma técnica de *stacking*, onde um meta-modelo (LGBM) aprende a ponderar as previsões dos modelos base. Em seguida, avalia o desempenho final do ensemble no conjunto de teste.

**Ação:**
1.  Execute a **Célula 7**.

**Saída Esperada:**
*   Scores OOF para cada modelo individual.
*   A seção `RESULTADOS FINAIS DO STACKING ENSEMBLE` com as métricas `WMATE`, `MAE` e `R²`.
*   Uma tabela mostrando a importância de cada modelo base no ensemble.
*   Um gráfico de análise de resíduos.

---

### Passo 8: Geração do Arquivo de Submissão (Célula 8)

**O que faz:** Formata as previsões finais do ensemble no layout exigido para submissão, garantindo uma previsão única por `internal_product_id` e `internal_store_id`.

**Ação:**
1.  **Verifique os caminhos:** Confirme que `base_path` e `checkpoint_path` estão corretos.
2.  Execute a **Célula 8**.

**Saída Esperada:**
*   A mensagem `✅ Arquivo de submissão criado...`.
*   O caminho onde o arquivo `submission.csv` foi salvo.
*   Uma pré-visualização (`.head()`) do arquivo de submissão gerado.

---

## 5. Resultados Esperados

Ao final da execução completa do notebook, você terá:

1.  **`df_model_ready_final_v2.parquet`:** Um arquivo intermediário com os dados processados e todas as features criadas.
2.  **`submission.csv`:** O arquivo final com as previsões de demanda para ser submetido. Ele conterá três colunas: `internal_product_id`, `internal_store_id`, e `target`.
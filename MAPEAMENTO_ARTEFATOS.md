# Mapeamento de Artefatos - Análise TRI (Teoria de Resposta ao Item)

Este documento apresenta um mapeamento completo de todos os artefatos gerados pelos scripts do projeto de Análise TRI, utilizando o Modelo Logístico de 3 Parâmetros (3PL) aplicado aos dados do ENEM dos estados do **Paraná (PR)** e **Pará (PA)**.

---

## 📊 Parâmetros TRI Gerados

Os scripts geram os seguintes parâmetros da Teoria de Resposta ao Item:

| Parâmetro | Descrição | Símbolo | Arquivo de Origem |
|-----------|-----------|---------|-------------------|
| **Habilidade (θ)** | Proficiência estimada do estudante | θ (theta) | `habil_*.csv` |
| **Dificuldade (b)** | Dificuldade do item | b | `dif_*.csv` |
| **Discriminação (a)** | Capacidade do item discriminar alunos | a | `dif_*.csv` |
| **Acerto ao Acaso (c)** | Probabilidade de chute | c | `dif_*.csv` |

---

## 🗂️ Estrutura de Artefatos

### 1. Dados de Entrada (Pré-processamento)

#### 1.1 Matrizes Binárias
**Local:** `pre-processamento/matrizes_binarias/`

Matrizes de respostas binárias (0 = erro, 1 = acerto) para cada área de conhecimento:

**Prova Amarela (utilizada nas análises TRI):**

| Arquivo | Área de Conhecimento | Estado |
|---------|----------------------|--------|
| `MATRIZ_CH_BINARIA_PA_amarela.csv` | Ciências Humanas | Pará |
| `MATRIZ_CH_BINARIA_PR_amarela.csv` | Ciências Humanas | Paraná |
| `MATRIZ_CN_BINARIA_PA_amarela.csv` | Ciências da Natureza | Pará |
| `MATRIZ_CN_BINARIA_PR_amarela.csv` | Ciências da Natureza | Paraná |
| `MATRIZ_LC_BINARIA_PA_amarela.csv` | Linguagens e Códigos | Pará |
| `MATRIZ_LC_BINARIA_PR_amarela.csv` | Linguagens e Códigos | Paraná |
| `MATRIZ_MT_BINARIA_PA_amarela.csv` | Matemática | Pará |
| `MATRIZ_MT_BINARIA_PR_amarela.csv` | Matemática | Paraná |

**Prova Azul (disponível para referência):**

| Arquivo | Área de Conhecimento | Estado |
|---------|----------------------|--------|
| `MATRIZ_CH_BINARIA_PA_azul.csv` | Ciências Humanas | Pará |
| `MATRIZ_CH_BINARIA_PR_azul.csv` | Ciências Humanas | Paraná |
| `MATRIZ_CN_BINARIA_PA_azul.csv` | Ciências da Natureza | Pará |
| `MATRIZ_CN_BINARIA_PR_azul.csv` | Ciências da Natureza | Paraná |
| `MATRIZ_LC_BINARIA_PA_azul.csv` | Linguagens e Códigos | Pará |
| `MATRIZ_LC_BINARIA_PR_azul.csv` | Linguagens e Códigos | Paraná |
| `MATRIZ_MT_BINARIA_PA_azul.csv` | Matemática | Pará |
| `MATRIZ_MT_BINARIA_PR_azul.csv` | Matemática | Paraná |

**Colunas presentes:**
- `matricula`: Identificador único do aluno
- `Q1` a `Q45`: Respostas binárias para cada questão
- `raw_score`: Escore bruto (total de acertos)

---

### 2. Artefatos do Modelo ERM (1PL - Modelo de Rasch)

**Local:** `codigos_R/ERM/`

#### 2.1 Dificuldades dos Itens (1PL)
**Local:** `codigos_R/ERM/dificuldades/`

| Arquivo | Área | Estado | Colunas |
|---------|------|--------|---------|
| `dif_modelo_ERM_CH_PA.csv` | Ciências Humanas | Pará | questao, dificuldade_item |
| `dif_modelo_ERM_CH_PR.csv` | Ciências Humanas | Paraná | questao, dificuldade_item |
| `dif_modelo_ERM_CN_PA.csv` | Ciências da Natureza | Pará | questao, dificuldade_item |
| `dif_modelo_ERM_CN_PR.csv` | Ciências da Natureza | Paraná | questao, dificuldade_item |
| `dif_modelo_ERM_LC_PA.csv` | Linguagens e Códigos | Pará | questao, dificuldade_item |
| `dif_modelo_ERM_LC_PR.csv` | Linguagens e Códigos | Paraná | questao, dificuldade_item |
| `dif_modelo_ERM_MT_PA.csv` | Matemática | Pará | questao, dificuldade_item |
| `dif_modelo_ERM_MT_PR.csv` | Matemática | Paraná | questao, dificuldade_item |

#### 2.2 Habilidades dos Alunos (1PL)
**Local:** `codigos_R/ERM/habilidades/`

| Arquivo | Área | Estado | Colunas |
|---------|------|--------|---------|
| `habil_modelo_ERM_CH_PA.csv` | Ciências Humanas | Pará | raw_score, habilidade_estimada |
| `habil_modelo_ERM_CH_PR.csv` | Ciências Humanas | Paraná | raw_score, habilidade_estimada |
| `habil_modelo_ERM_CN_PA.csv` | Ciências da Natureza | Pará | raw_score, habilidade_estimada |
| `habil_modelo_ERM_CN_PR.csv` | Ciências da Natureza | Paraná | raw_score, habilidade_estimada |
| `habil_modelo_ERM_LC_PA.csv` | Linguagens e Códigos | Pará | raw_score, habilidade_estimada |
| `habil_modelo_ERM_LC_PR.csv` | Linguagens e Códigos | Paraná | raw_score, habilidade_estimada |
| `habil_modelo_ERM_MT_PA.csv` | Matemática | Pará | raw_score, habilidade_estimada |
| `habil_modelo_ERM_MT_PR.csv` | Matemática | Paraná | raw_score, habilidade_estimada |

#### 2.3 Probabilidades de Acerto (1PL)
**Local:** `codigos_R/ERM/probabilidades/`

| Arquivo | Área | Estado |
|---------|------|--------|
| `prob_ERM_1PL_CH_PA.csv` | Ciências Humanas | Pará |
| `prob_ERM_1PL_CH_PR.csv` | Ciências Humanas | Paraná |
| `prob_ERM_1PL_CN_PA.csv` | Ciências da Natureza | Pará |
| `prob_ERM_1PL_CN_PR.csv` | Ciências da Natureza | Paraná |
| `prob_ERM_1PL_LC_PA.csv` | Linguagens e Códigos | Pará |
| `prob_ERM_1PL_LC_PR.csv` | Linguagens e Códigos | Paraná |
| `prob_ERM_1PL_MT_PA.csv` | Matemática | Pará |
| `prob_ERM_1PL_MT_PR.csv` | Matemática | Paraná |

#### 2.4 Gráficos CCI (1PL)
**Local:** `codigos_R/ERM/graficos/` e `codigos_R/ERM/graficos_python/`

| Arquivo | Descrição |
|---------|-----------|
| `grafico_CCI.pdf` | Curva Característica do Item geral |
| `grafico_ERM_LC_PA.pdf` | CCI Linguagens e Códigos - Pará |
| `grafico_ERM_LC_PR.pdf` | CCI Linguagens e Códigos - Paraná |
| `grafico_ERM_MT_PA.pdf` | CCI Matemática - Pará |
| `grafico_ERM_MT_PR.pdf` | CCI Matemática - Paraná |

---

### 3. Artefatos do Modelo LTM 2PL (Dois Parâmetros)

**Local:** `codigos_R/LTM_2PL/`

#### 3.1 Dificuldades dos Itens (2PL)
**Local:** `codigos_R/LTM_2PL/dificuldades/`

| Arquivo | Área | Estado | Colunas |
|---------|------|--------|---------|
| `dif_2PLM_LTM_CH_PA.csv` | Ciências Humanas | Pará | dificuldade_item, discriminacao_item, questao |
| `dif_2PLM_LTM_CH_PR.csv` | Ciências Humanas | Paraná | dificuldade_item, discriminacao_item, questao |
| `dif_2PLM_LTM_CN_PA.csv` | Ciências da Natureza | Pará | dificuldade_item, discriminacao_item, questao |
| `dif_2PLM_LTM_CN_PR.csv` | Ciências da Natureza | Paraná | dificuldade_item, discriminacao_item, questao |
| `dif_2PLM_LTM_LC_PA.csv` | Linguagens e Códigos | Pará | dificuldade_item, discriminacao_item, questao |
| `dif_2PLM_LTM_LC_PR.csv` | Linguagens e Códigos | Paraná | dificuldade_item, discriminacao_item, questao |
| `dif_2PLM_LTM_MT_PA.csv` | Matemática | Pará | dificuldade_item, discriminacao_item, questao |
| `dif_2PLM_LTM_MT_PR.csv` | Matemática | Paraná | dificuldade_item, discriminacao_item, questao |

#### 3.2 Habilidades dos Alunos (2PL)
**Local:** `codigos_R/LTM_2PL/habilidades/`

| Arquivo | Área | Estado |
|---------|------|--------|
| `habil_modelo_2PLM_LTM_CH_PA.csv` | Ciências Humanas | Pará |
| `habil_modelo_2PLM_LTM_CH_PR.csv` | Ciências Humanas | Paraná |
| `habil_modelo_2PLM_LTM_CN_PA.csv` | Ciências da Natureza | Pará |
| `habil_modelo_2PLM_LTM_CN_PR.csv` | Ciências da Natureza | Paraná |
| `habil_modelo_2PLM_LTM_LC_PA.csv` | Linguagens e Códigos | Pará |
| `habil_modelo_2PLM_LTM_LC_PR.csv` | Linguagens e Códigos | Paraná |
| `habil_modelo_2PLM_LTM_MT_PA.csv` | Matemática | Pará |
| `habil_modelo_2PLM_LTM_MT_PR.csv` | Matemática | Paraná |

#### 3.3 Probabilidades de Acerto (2PL)
**Local:** `codigos_R/LTM_2PL/probabilidades/`

| Arquivo | Área | Estado |
|---------|------|--------|
| `df_prob_2PL_LTM_CH_PA.csv` | Ciências Humanas | Pará |
| `df_prob_2PL_LTM_CH_PR.csv` | Ciências Humanas | Paraná |
| `df_prob_2PL_LTM_CN_PA.csv` | Ciências da Natureza | Pará |
| `df_prob_2PL_LTM_CN_PR.csv` | Ciências da Natureza | Paraná |
| `df_prob_2PL_LTM_LC_PA.csv` | Linguagens e Códigos | Pará |
| `df_prob_2PL_LTM_LC_PR.csv` | Linguagens e Códigos | Paraná |
| `df_prob_2PL_LTM_MT_PA.csv` | Matemática | Pará |
| `df_prob_2PL_LTM_MT_PR.csv` | Matemática | Paraná |

#### 3.4 Gráficos CCI (2PL)
**Local:** `codigos_R/LTM_2PL/graficos/` e `codigos_R/LTM_2PL/graficos_python/`

| Arquivo | Descrição |
|---------|-----------|
| `grafico_2PL_LTM_CH_PA.pdf` | CCI Ciências Humanas - Pará |
| `grafico_2PL_LTM_CH_PR.pdf` | CCI Ciências Humanas - Paraná |
| `grafico_2PL_LTM_CN_PA.pdf` | CCI Ciências da Natureza - Pará |
| `grafico_2PL_LTM_CN_PR.pdf` | CCI Ciências da Natureza - Paraná |
| `grafico_2PL_LTM_LC_PA.pdf` | CCI Linguagens e Códigos - Pará |
| `grafico_2PL_LTM_LC_PR.pdf` | CCI Linguagens e Códigos - Paraná |
| `grafico_2PL_LTM_MT_PA.pdf` | CCI Matemática - Pará |
| `grafico_2PL_LTM_MT_PR.pdf` | CCI Matemática - Paraná |

---

### 4. Artefatos do Modelo LTM 3PL (Três Parâmetros) ⭐ PRINCIPAL

**Local:** `codigos_R/LTM_3PL/`

Este é o modelo principal utilizado nas análises, incluindo o parâmetro de chute (c).

#### 4.1 Dificuldades dos Itens (3PL)
**Local:** `codigos_R/LTM_3PL/dificuldades/`

| Arquivo | Área | Estado | Colunas |
|---------|------|--------|---------|
| `dif_modelo_3PL_ltm_CH_PA.csv` | Ciências Humanas | Pará | acerto_acaso_item, dificuldade_item, discriminacao_item, questao |
| `dif_modelo_3PL_ltm_CH_PR.csv` | Ciências Humanas | Paraná | acerto_acaso_item, dificuldade_item, discriminacao_item, questao |
| `dif_modelo_3PL_ltm_CN_PA.csv` | Ciências da Natureza | Pará | acerto_acaso_item, dificuldade_item, discriminacao_item, questao |
| `dif_modelo_3PL_ltm_CN_PR.csv` | Ciências da Natureza | Paraná | acerto_acaso_item, dificuldade_item, discriminacao_item, questao |
| `dif_modelo_3PL_ltm_LC_PA.csv` | Linguagens e Códigos | Pará | acerto_acaso_item, dificuldade_item, discriminacao_item, questao |
| `dif_modelo_3PL_ltm_LC_PR.csv` | Linguagens e Códigos | Paraná | acerto_acaso_item, dificuldade_item, discriminacao_item, questao |
| `dif_modelo_3PL_ltm_MT_PA.csv` | Matemática | Pará | acerto_acaso_item, dificuldade_item, discriminacao_item, questao |
| `dif_modelo_3PL_ltm_MT_PR.csv` | Matemática | Paraná | acerto_acaso_item, dificuldade_item, discriminacao_item, questao |

**Estrutura do arquivo de dificuldades (3PL):**
```csv
"acerto_acaso_item","dificuldade_item","discriminacao_item","questao"
"Q1",0.149664,1.886558,3.709187,1
"Q2",0.210946,0.914660,2.361208,2
...
```

#### 4.2 Habilidades dos Alunos (3PL)
**Local:** `codigos_R/LTM_3PL/habilidades/`

| Arquivo | Área | Estado |
|---------|------|--------|
| `habil_3PL_ltm_CH_PA.csv` | Ciências Humanas | Pará |
| `habil_3PL_ltm_CH_PR.csv` | Ciências Humanas | Paraná |
| `habil_3PL_ltm_CN_PA.csv` | Ciências da Natureza | Pará |
| `habil_3PL_ltm_CN_PR.csv` | Ciências da Natureza | Paraná |
| `habil_3PL_ltm_LC_PA.csv` | Linguagens e Códigos | Pará |
| `habil_3PL_ltm_LC_PR.csv` | Linguagens e Códigos | Paraná |
| `habil_3PL_ltm_MT_PA.csv` | Matemática | Pará |
| `habil_3PL_ltm_MT_PR.csv` | Matemática | Paraná |

**Colunas presentes:**
- `Q1` a `Q45`: Padrão de respostas (0/1)
- `Obs`: Observações
- `Exp`: Esperado
- `habilidade`: Habilidade estimada (θ)
- `se.z1`: Erro padrão
- `respostas`: String binária do padrão de respostas
- `Ocorrência`: Frequência do padrão
- `alunos_id_string`: IDs dos alunos com este padrão

#### 4.3 Probabilidades de Acerto (3PL)
**Local:** `codigos_R/LTM_3PL/probabilidades/`

| Arquivo | Área | Estado |
|---------|------|--------|
| `df_prob_3PL_LTM_CH_PA.csv` | Ciências Humanas | Pará |
| `df_prob_3PL_LTM_CH_PR.csv` | Ciências Humanas | Paraná |
| `df_prob_3PL_LTM_CN_PA.csv` | Ciências da Natureza | Pará |
| `df_prob_3PL_LTM_CN_PR.csv` | Ciências da Natureza | Paraná |
| `df_prob_3PL_LTM_LC_PA.csv` | Linguagens e Códigos | Pará |
| `df_prob_3PL_LTM_LC_PR.csv` | Linguagens e Códigos | Paraná |
| `df_prob_3PL_LTM_MT_PA.csv` | Matemática | Pará |
| `df_prob_3PL_LTM_MT_PR.csv` | Matemática | Paraná |

**Estrutura:** Matriz com valores de theta (-5 a 5) e probabilidade de acerto para cada item (Item 1 a Item 45).

#### 4.4 Gráficos CCI (3PL)
**Local:** `codigos_R/LTM_3PL/graficos/` e `codigos_R/LTM_3PL/graficos_python/`

| Arquivo | Descrição |
|---------|-----------|
| `grafico_3PL_LTM_CH_PA.pdf` | CCI Ciências Humanas - Pará |
| `grafico_3PL_LTM_CH_PR.pdf` | CCI Ciências Humanas - Paraná |
| `grafico_3PL_LTM_CN_PA.pdf` | CCI Ciências da Natureza - Pará |
| `grafico_3PL_LTM_CN_PR.pdf` | CCI Ciências da Natureza - Paraná |
| `grafico_3PL_LTM_LC_PA.pdf` | CCI Linguagens e Códigos - Pará |
| `grafico_3PL_LTM_LC_PR.pdf` | CCI Linguagens e Códigos - Paraná |
| `grafico_3PL_LTM_MT_PA.pdf` | CCI Matemática - Pará |
| `grafico_3PL_LTM_MT_PR.pdf` | CCI Matemática - Paraná |
| `grafico_3PL_CCI_Negativa.pdf` | Exemplo de item com discriminação negativa |
| `item_4_disc_negativa.pdf` | Análise de item com discriminação negativa |

---

### 5. Dados Normalizados

**Local:** `report/normalized_data/`

#### 5.1 Dificuldades Normalizadas
**Local:** `report/normalized_data/dificuldades/`

| Arquivo | Área | Estado | Colunas |
|---------|------|--------|---------|
| `dif_CH_PA.csv` | Ciências Humanas | Pará | dificuldade_item_normalizada, classificacao_dificuldade |
| `dif_CH_PR.csv` | Ciências Humanas | Paraná | dificuldade_item_normalizada, classificacao_dificuldade |
| `dif_CN_PA.csv` | Ciências da Natureza | Pará | dificuldade_item_normalizada, classificacao_dificuldade |
| `dif_CN_PR.csv` | Ciências da Natureza | Paraná | dificuldade_item_normalizada, classificacao_dificuldade |
| `dif_LC_PA.csv` | Linguagens e Códigos | Pará | dificuldade_item_normalizada, classificacao_dificuldade |
| `dif_LC_PR.csv` | Linguagens e Códigos | Paraná | dificuldade_item_normalizada, classificacao_dificuldade |
| `dif_MT_PA.csv` | Matemática | Pará | dificuldade_item_normalizada, classificacao_dificuldade |
| `dif_MT_PR.csv` | Matemática | Paraná | dificuldade_item_normalizada, classificacao_dificuldade |

**Escala normalizada:** 200-1000 (escala similar ao ENEM)

#### 5.2 Habilidades Normalizadas
**Local:** `report/normalized_data/habilidades/`

| Arquivo | Área | Estado | Colunas |
|---------|------|--------|---------|
| `habil_CH_PA.csv` | Ciências Humanas | Pará | habilidade_normalizada |
| `habil_CH_PR.csv` | Ciências Humanas | Paraná | habilidade_normalizada |
| `habil_CN_PA.csv` | Ciências da Natureza | Pará | habilidade_normalizada |
| `habil_CN_PR.csv` | Ciências da Natureza | Paraná | habilidade_normalizada |
| `habil_LC_PA.csv` | Linguagens e Códigos | Pará | habilidade_normalizada |
| `habil_LC_PR.csv` | Linguagens e Códigos | Paraná | habilidade_normalizada |
| `habil_MT_PA.csv` | Matemática | Pará | habilidade_normalizada |
| `habil_MT_PR.csv` | Matemática | Paraná | habilidade_normalizada |

---

### 6. Artefatos de Relatórios e Feedback

#### 6.1 Relatórios HTML para Alunos (sem LLM)
**Local:** `report/report_html_no_llm/`

**Padrão de nomenclatura:** `report_{matricula}_{estado}_{area}_{questao}.html`

Exemplos:
- `report_210054478563_PA_CH_13.html` - Relatório do aluno 210054478563, Pará, Ciências Humanas, questão 13
- `report_210055501428_PR_LC_7.html` - Relatório do aluno 210055501428, Paraná, Linguagens, questão 7

**Conteúdo dos relatórios:**
- Habilidade do aluno (normalizada)
- Probabilidade de acerto
- Gabarito da questão
- Dificuldade do item
- Classificação de dificuldade
- Probabilidade de chute
- Se acertou ou errou
- Competência e habilidade da questão
- Feedback personalizado
- Gráfico CCI interativo

#### 6.2 Relatórios PDF para Alunos
**Local:** `report/report_html_no_llm/`

**Padrão de nomenclatura:** `report_{matricula}_{estado}_{area}_{questao}.pdf`

#### 6.3 Relatórios para Professores
**Local:** `report/report_html_no_llm/`

| Arquivo | Descrição |
|---------|-----------|
| `prof_report_PA.pdf` | Relatório geral para professores - Pará |
| `prof_report_PR.pdf` | Relatório geral para professores - Paraná |

#### 6.4 Artefatos de Relatórios (CCI individuais)
**Local:** `report/artefatos/`

**Gráficos CCI por aluno/questão:**
- `cci_{matricula}_{estado}_{area}_{questao}.html`

**Relatórios individuais:**
- `report_{matricula}_{estado}_{area}_{questao}.html`

---

### 7. Gráficos de Análise Comparativa

**Local:** `report/plots/`

#### 7.1 Histogramas de Distribuição de Habilidades
| Arquivo | Descrição |
|---------|-----------|
| `histograma_habilidades_CH.png/pdf` | Distribuição de habilidades - Ciências Humanas (ambos estados) |
| `histograma_habilidades_CN.png/pdf` | Distribuição de habilidades - Ciências da Natureza (ambos estados) |
| `histograma_habilidades_LC.png/pdf` | Distribuição de habilidades - Linguagens (ambos estados) |
| `histograma_habilidades_MT.png/pdf` | Distribuição de habilidades - Matemática (ambos estados) |
| `histograma_habilidades_PA_CH.png` | Distribuição de habilidades - Ciências Humanas - Pará |
| `histograma_habilidades_PA_CN.png` | Distribuição de habilidades - Ciências da Natureza - Pará |
| `histograma_habilidades_PA_LC.png` | Distribuição de habilidades - Linguagens - Pará |
| `histograma_habilidades_PA_MT.png` | Distribuição de habilidades - Matemática - Pará |
| `histograma_habilidades_PR_CH.png` | Distribuição de habilidades - Ciências Humanas - Paraná |
| `histograma_habilidades_PR_CN.png` | Distribuição de habilidades - Ciências da Natureza - Paraná |
| `histograma_habilidades_PR_LC.png` | Distribuição de habilidades - Linguagens - Paraná |
| `histograma_habilidades_PR_MT.png` | Distribuição de habilidades - Matemática - Paraná |

#### 7.2 Boxplots de Comparação
| Arquivo | Descrição |
|---------|-----------|
| `boxplot_habilidades_CH.png` | Comparação PA vs PR - Ciências Humanas |
| `boxplot_habilidades_CN.png` | Comparação PA vs PR - Ciências da Natureza |
| `boxplot_habilidades_LC.png` | Comparação PA vs PR - Linguagens |
| `boxplot_habilidades_MT.png` | Comparação PA vs PR - Matemática |

#### 7.3 Gráficos para Professores
| Arquivo | Descrição |
|---------|-----------|
| `prof_plot_PA_CH.png` | Análise geral Ciências Humanas - Pará |
| `prof_plot_PA_CN.png` | Análise geral Ciências da Natureza - Pará |
| `prof_plot_PA_LC.png` | Análise geral Linguagens - Pará |
| `prof_plot_PA_MT.png` | Análise geral Matemática - Pará |
| `prof_plot_PR_CH.png` | Análise geral Ciências Humanas - Paraná |
| `prof_plot_PR_CN.png` | Análise geral Ciências da Natureza - Paraná |
| `prof_plot_PR_LC.png` | Análise geral Linguagens - Paraná |
| `prof_plot_PR_MT.png` | Análise geral Matemática - Paraná |
| `professor_tabela_ch_pa.png` | Tabela de análise - Ciências Humanas - Pará |
| `professor_tabela_ch_pr.png` | Tabela de análise - Ciências Humanas - Paraná |

#### 7.4 Gráficos de CCI Individuais por Aluno
| Padrão | Descrição |
|--------|-----------|
| `cci_{matricula}_{estado}_{area}_{questao}.html` | CCI interativo para análise individual |
| `plot_{matricula}_{estado}_{area}_{questao}.png` | CCI estático para análise individual |

---

## 🔍 Análises Possíveis com os Artefatos

### Análise de Desempenho dos Estudantes

#### 1. Identificação de Acertos por Chute
**Artefatos utilizados:**
- `dif_modelo_3PL_ltm_{area}_{estado}.csv` (coluna `acerto_acaso_item`)
- `df_prob_3PL_LTM_{area}_{estado}.csv`
- `habil_3PL_ltm_{area}_{estado}.csv`

**Critério:** Aluno com probabilidade de acerto próxima ao parâmetro `c` (acerto ao acaso) provavelmente acertou por chute.

#### 2. Acertos Acima do Esperado
**Descrição:** Alunos com baixa habilidade que acertaram itens de alta dificuldade.

**Critério:** `habilidade_aluno < dificuldade_item AND acertou = 1`

**Artefatos utilizados:**
- `habil_3PL_ltm_{area}_{estado}.csv`
- `dif_modelo_3PL_ltm_{area}_{estado}.csv`

#### 3. Erros Inesperados
**Descrição:** Alunos com alta habilidade que erraram itens fáceis.

**Critério:** `habilidade_aluno > dificuldade_item AND acertou = 0`

#### 4. Comparação entre Estados (PR vs PA)
**Artefatos utilizados:**
- `boxplot_habilidades_{area}.png`
- `histograma_habilidades_{area}.png/pdf`

---

## 📈 Fluxo de Geração dos Artefatos

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DADOS BRUTOS DO ENEM                            │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Pré-processamento (Jupyter Notebooks)                              │
│  - Itens_prova_geral_2022.ipynb                                     │
│  - tratamento_geracao_matriz_binaria.ipynb                          │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  MATRIZES BINÁRIAS                                                  │
│  pre-processamento/matrizes_binarias/MATRIZ_{area}_BINARIA_{est}.csv│
└──────────────────────────────┬──────────────────────────────────────┘
                               │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
            ▼                  ▼                  ▼
┌───────────────────┐ ┌───────────────────┐ ┌───────────────────┐
│    MODELO 1PL     │ │    MODELO 2PL     │ │    MODELO 3PL     │
│     (ERM)         │ │   (LTM 2PL)       │ │   (LTM 3PL)       │
│                   │ │                   │ │                   │
│ - Dificuldade (b) │ │ - Dificuldade (b) │ │ - Dificuldade (b) │
│ - Habilidade (θ)  │ │ - Discriminação(a)│ │ - Discriminação(a)│
│                   │ │ - Habilidade (θ)  │ │ - Chute (c)       │
│                   │ │                   │ │ - Habilidade (θ)  │
└─────────┬─────────┘ └─────────┬─────────┘ └─────────┬─────────┘
          │                     │                     │
          ▼                     ▼                     ▼
┌─────────────────────────────────────────────────────────────────────┐
│  PROBABILIDADES DE ACERTO POR ITEM                                  │
│  codigos_R/{modelo}/probabilidades/                                 │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  NORMALIZAÇÃO DOS DADOS (escala 200-1000)                           │
│  report/normalize_data.py                                           │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
┌───────────────────────────────────┐ ┌───────────────────────────────────┐
│  RELATÓRIOS PARA ALUNOS           │ │  RELATÓRIOS PARA PROFESSORES      │
│  - report_html_no_llm/            │ │  - prof_report_{estado}.pdf       │
│  - report/artefatos/              │ │  - Análises comparativas          │
│  - CCI individuais                │ │  - Histogramas e Boxplots         │
└───────────────────────────────────┘ └───────────────────────────────────┘
```

---

## 📋 Resumo Quantitativo de Artefatos

| Categoria | Quantidade | Localização Principal |
|-----------|------------|----------------------|
| Matrizes Binárias | 16 (8 amarela + 8 azul) | `pre-processamento/matrizes_binarias/` |
| Dificuldades (todos modelos) | 24 | `codigos_R/*/dificuldades/` |
| Habilidades (todos modelos) | 24 | `codigos_R/*/habilidades/` |
| Probabilidades | 24 | `codigos_R/*/probabilidades/` |
| Dados Normalizados | 16 | `report/normalized_data/` |
| Gráficos CCI | ~60+ | `codigos_R/*/graficos*/` |
| Relatórios HTML/PDF (alunos) | 100+ | `report/report_html_no_llm/` |
| Relatórios Professores | 2 | `report/report_html_no_llm/` |
| Gráficos Comparativos | 20+ | `report/plots/` |

---

## 🎯 Usos dos Artefatos para o Artigo

### Para Análise de Desempenho dos Estudantes:
1. **Identificar acertos por chute:** Usar `acerto_acaso_item` do modelo 3PL
2. **Identificar alunos que acertaram acima do esperado:** Comparar θ com b
3. **Comparar estados:** Usar boxplots e histogramas

### Para Feedback Formativo:
1. **Para Alunos:** Relatórios HTML/PDF individuais com CCI e recomendações
2. **Para Professores:** Relatórios gerais por estado com visão macro do desempenho

### Para Comparação PR vs PA:
1. **Distribuição de habilidades:** `histograma_habilidades_{area}.png`
2. **Comparação direta:** `boxplot_habilidades_{area}.png`
3. **Análise por área:** Relatórios de professor por estado

---

## 📚 Referências Técnicas

- **Modelo 1PL (Rasch):** `P(θ) = 1 / (1 + exp(-(θ - b)))`
- **Modelo 2PL:** `P(θ) = 1 / (1 + exp(-a(θ - b)))`
- **Modelo 3PL:** `P(θ) = c + (1 - c) * 1 / (1 + exp(-a(θ - b)))`

Onde:
- θ = habilidade do examinando
- b = dificuldade do item
- a = discriminação do item
- c = probabilidade de acerto ao acaso (chute)

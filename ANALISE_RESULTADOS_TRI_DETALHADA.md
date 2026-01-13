# Análise Detalhada de Resultados - Teoria de Resposta ao Item (TRI)

## Modelo Logístico de 3 Parâmetros (3PL) - ENEM 2022

**Estados analisados:** Pará (PA - pior ranking IDEB) vs Paraná (PR - melhor ranking IDEB)

> **IMPORTANTE:** Todas as análises deste documento utilizam **exclusivamente** os dados do modelo 3PL gerados pelos scripts em `codigos_R/LTM_3PL/`.

---

## 📋 Fontes de Dados Utilizadas

### Arquivos de Habilidades (por aluno)
- `codigos_R/LTM_3PL/habilidades/habil_3PL_ltm_{AREA}_{ESTADO}.csv`
- **Colunas principais:**
  - `Q1` a `Q45`: Respostas binárias (0=erro, 1=acerto)
  - `habilidade`: Valor de θ estimado (escala -5 a 5)
  - `alunos_id_string`: Identificador único do aluno
  - `Obs`: Total de acertos observados

### Arquivos de Dificuldade (por item)
- `codigos_R/LTM_3PL/dificuldades/dif_modelo_3PL_ltm_{AREA}_{ESTADO}.csv`
- **Colunas principais:**
  - `questao`: Número da questão
  - `dificuldade_item` (b): Dificuldade do item
  - `discriminacao_item` (a): Discriminação do item
  - `acerto_acaso_item` (c): Probabilidade de acerto ao acaso (chute)

### Arquivos Normalizados (escala 200-1000)
- `report/normalized_data/habilidades/habil_{AREA}_{ESTADO}.csv`
- `report/normalized_data/dificuldades/dif_{AREA}_{ESTADO}.csv`

---

## 📐 Metodologia de Cálculos

### Modelo 3PL - Fórmula Base

A probabilidade de acerto é calculada por:

```
P(θ) = c + (1 - c) / (1 + exp(-a(θ - b)))
```

Onde:
- **θ (theta)**: Habilidade do examinando
- **a**: Discriminação do item
- **b**: Dificuldade do item
- **c**: Probabilidade de acerto ao acaso (chute)

### Conversão para Escala 200-1000

```python
habilidade_normalizada = 500 + (100 * θ)
```

### Critérios de Identificação

| Fenômeno | Critério | Fórmula |
|----------|----------|---------|
| **Acerto por Chute** | Aluno acertou item muito acima de sua habilidade | `θ < b - 1` AND `acertou = 1` AND `c > 0.10` |
| **Erro Inesperado** | Aluno errou item muito abaixo de sua habilidade | `θ > b + 1` AND `acertou = 0` |
| **Item Problemático** | Item com discriminação negativa | `a < 0` |
| **Item com Alto Chute** | Item favorável ao chute | `c > 0.25` |

---

## 1. Exemplos de Alunos em Diferentes Perfis de Desempenho

### 1.1 Matemática (MT)

#### PARÁ (PA)

| Perfil | ID do Aluno | Habilidade (θ) | Habilidade Normalizada |
|--------|-------------|----------------|------------------------|
| **Menor habilidade** | 210057715141 | -1,4406 | ~356 |
| **Percentil 10** | 210054598180 | -0,7920 | ~421 |
| **Mediano** | 210057224411 | 0,0488 | ~505 |
| **Percentil 90** | 210056743790 | 1,2861 | ~629 |
| **Maior habilidade** | 210057073469 | 3,3545 | ~835 |

#### PARANÁ (PR)

| Perfil | ID do Aluno | Habilidade (θ) | Habilidade Normalizada |
|--------|-------------|----------------|------------------------|
| **Menor habilidade** | 210055668415 | -1,6622 | ~334 |
| **Percentil 10** | 210055560487 | -0,9440 | ~406 |
| **Mediano** | 210057764540 | 0,0244 | ~502 |
| **Percentil 90** | 210055319824 | 1,2652 | ~627 |
| **Maior habilidade** | 210056808237 | 3,1175 | ~812 |

#### Comparação Entre Estados - Mesma Faixa de Habilidade

**Faixa de Baixa Habilidade (θ entre -1,0 e -0,5):**

| Estado | Alunos na Faixa | Exemplo de ID | θ |
|--------|-----------------|---------------|---|
| PA | 1.212 | 210057651046 | -0,9954 |
| PA | | 210054769323 | -0,9950 |
| PA | | 210054883849 | -0,9948 |
| PR | 1.589 | 210057806673 | -0,9991 |
| PR | | 210056899892 | -0,9987 |
| PR | | 210055283269 | -0,9983 |

> **Insight:** O PR tem 31% mais alunos na faixa de baixa habilidade em Matemática (1.589 vs 1.212), apesar de ser o estado melhor ranqueado no IDEB.

---

## 2. Análise de Acertos Suspeitos por Chute

### 2.1 Metodologia

**Critério utilizado:**
```python
acerto_suspeito = (θ_aluno < b_item - 1) AND (acertou == 1) AND (c_item > 0.10) AND (a_item > 0)
```

**Interpretação:** Um aluno com habilidade muito inferior à dificuldade do item que acertou a questão provavelmente o fez por chute, especialmente se o parâmetro c (acerto ao acaso) do item for significativo.

### 2.2 Exemplos Específicos - Matemática

#### PARÁ (PA)

| # | ID do Aluno | θ | Questão | Dificuldade (b) | Diferença (b-θ) | Chute (c) |
|---|-------------|---|---------|-----------------|-----------------|-----------|
| 1 | **210056753271** | -1,2987 | Q32 | 3,1566 | **4,46** | 19,83% |
| 2 | **210056753271** | -1,2987 | Q42 | 2,8114 | **4,11** | 20,23% |
| 3 | **210057638944** | -1,3073 | Q25 | 2,7613 | **4,07** | 23,62% |
| 4 | **210054579943** | -1,2577 | Q25 | 2,7613 | **4,02** | 23,62% |
| 5 | **210056753271** | -1,2987 | Q20 | 2,5745 | **3,87** | 11,57% |

> **Análise do Aluno 210056753271 (PA):** Este aluno apresenta habilidade θ = -1,2987 (muito baixa) mas acertou 3 questões de alta dificuldade (Q32, Q42, Q20). A diferença entre a dificuldade das questões e sua habilidade varia de 3,87 a 4,46 pontos na escala θ. Probabilidade muito alta de que esses acertos sejam por chute.

#### PARANÁ (PR)

| # | ID do Aluno | θ | Questão | Dificuldade (b) | Diferença (b-θ) | Chute (c) |
|---|-------------|---|---------|-----------------|-----------------|-----------|
| 1 | **210055515774** | -1,6379 | Q39 | 2,7942 | **4,43** | 13,39% |
| 2 | **210055515774** | -1,6379 | Q26 | 2,6907 | **4,33** | 17,68% |
| 3 | **210055668415** | -1,6622 | Q42 | 2,3888 | **4,05** | 20,81% |
| 4 | **210057376930** | -1,5968 | Q42 | 2,3888 | **3,99** | 20,81% |
| 5 | **210055515774** | -1,6379 | Q34 | 2,1848 | **3,82** | 13,83% |

> **Análise do Aluno 210055515774 (PR):** Com θ = -1,6379 (uma das menores habilidades do estado), este aluno acertou 3 questões muito difíceis (Q39, Q26, Q34). Estas questões têm dificuldade entre 2,18 e 2,79, resultando em diferenças de 3,82 a 4,43 pontos. Forte indicativo de acertos por chute.

### 2.3 Exemplos Específicos - Ciências da Natureza

#### PARÁ (PA)

| # | ID do Aluno | θ | Questão | Dificuldade (b) | Diferença (b-θ) | Chute (c) |
|---|-------------|---|---------|-----------------|-----------------|-----------|
| 1 | **210054896020** | -1,3475 | Q36 | 10,5603 | **11,91** | 17,36% |
| 2 | **210055042997** | -1,3456 | Q17 | 4,3190 | **5,66** | 12,24% |
| 3 | **210054509366** | -1,3772 | Q16 | 2,9009 | **4,28** | 12,32% |
| 4 | **210054509366** | -1,3772 | Q3 | 2,8797 | **4,26** | 19,33% |
| 5 | **210054896020** | -1,3475 | Q16 | 2,9009 | **4,25** | 12,32% |

> **CASO EXTREMO - Aluno 210054896020:** Acertou a questão Q36 que tem dificuldade b = 10,5603 (extremamente difícil). Com habilidade θ = -1,3475, a diferença é de **11,91 pontos**! Praticamente impossível acertar por conhecimento - claramente um acerto ao acaso.

#### PARANÁ (PR)

| # | ID do Aluno | θ | Questão | Dificuldade (b) | Diferença (b-θ) | Chute (c) |
|---|-------------|---|---------|-----------------|-----------------|-----------|
| 1 | **210057879963** | -2,2432 | Q21 | 3,7938 | **6,04** | 30,12% |
| 2 | **210055416405** | -2,1122 | Q3 | 3,5942 | **5,71** | 18,77% |
| 3 | **210057759026** | -2,1159 | Q17 | 3,0615 | **5,18** | 13,32% |
| 4 | **210057879963** | -2,2432 | Q45 | 2,7866 | **5,03** | 25,47% |
| 5 | **210055416405** | -2,1122 | Q22 | 2,6146 | **4,73** | **44,92%** |

> **DESTAQUE - Questão Q22:** O aluno 210055416405 acertou esta questão que tem **c = 44,92%** de probabilidade de chute. Com θ = -2,1122 e b = 2,6146, a diferença é de 4,73 pontos. A altíssima probabilidade de acerto ao acaso do item (quase 50%) combinada com a baixa habilidade do aluno indica forte evidência de acerto por chute.

---

## 3. Análise de Erros Inesperados

### 3.1 Metodologia

**Critério utilizado:**
```python
erro_inesperado = (θ_aluno > b_item + 1) AND (acertou == 0) AND (a_item > 0)
```

**Interpretação:** Um aluno com habilidade muito superior à dificuldade do item que errou a questão pode ter sido vítima de desatenção, interpretação equivocada, ou possui uma lacuna de conhecimento específica naquele tópico.

### 3.2 Exemplos Específicos - Matemática

#### PARÁ (PA)

| # | ID do Aluno | θ | Questão | Dificuldade (b) | Diferença (θ-b) | Interpretação |
|---|-------------|---|---------|-----------------|-----------------|---------------|
| 1 | **210054561200** | 2,7021 | Q6 | 0,5279 | **2,17** | Desatenção provável |
| 2 | **210057386329** | 3,1049 | Q30 | 1,0962 | **2,01** | Lacuna específica |
| 3 | **210054527854** | 2,9275 | Q31 | 0,9942 | **1,93** | Desatenção provável |
| 4 | **210054600139** | 2,7845 | Q8 | 1,1462 | **1,64** | Lacuna específica |
| 5 | **210056695320** | 2,7291 | Q30 | 1,0962 | **1,63** | Desatenção provável |

> **Análise do Aluno 210054561200:** Este é um aluno de alta habilidade (θ = 2,7021 ≈ 770 na escala normalizada) que errou a questão Q6, uma questão relativamente fácil (b = 0,5279). A diferença de 2,17 pontos indica que deveria ter acertado com alta probabilidade. Possíveis causas: desatenção, erro de leitura, ou confusão com alternativas.

#### PARANÁ (PR)

| # | ID do Aluno | θ | Questão | Dificuldade (b) | Diferença (θ-b) | Interpretação |
|---|-------------|---|---------|-----------------|-----------------|---------------|
| 1 | **210056820621** | 2,3436 | Q9 | -0,8396 | **3,18** | Erro extremo |
| 2 | **210057757548** | 2,4308 | Q11 | -0,5407 | **2,97** | Erro extremo |
| 3 | **210056620875** | 2,5233 | Q6 | 0,0902 | **2,43** | Desatenção |
| 4 | **210056714914** | 2,4390 | Q6 | 0,0902 | **2,35** | Desatenção |
| 5 | **210057727514** | 2,4158 | Q6 | 0,0902 | **2,33** | Desatenção |

> **CASO EXTREMO - Aluno 210056820621:** Com θ = 2,3436, errou a Q9 que tem dificuldade b = -0,8396 (questão muito fácil). A diferença de **3,18 pontos** é a maior encontrada. Este é um caso clássico de erro por desatenção ou problema na interpretação do enunciado. **Recomendação de feedback:** Revisar estratégias de gestão de tempo e atenção durante a prova.

### 3.3 Exemplos Específicos - Ciências da Natureza

#### PARÁ (PA)

| # | ID do Aluno | θ | Questão | Dificuldade (b) | Diferença (θ-b) |
|---|-------------|---|---------|-----------------|-----------------|
| 1 | **210054541614** | 2,8159 | Q12 | 0,3960 | **2,42** |
| 2 | **210054907526** | 2,7400 | Q12 | 0,3960 | **2,34** |
| 3 | **210054649030** | 2,7006 | Q12 | 0,3960 | **2,30** |
| 4 | **210057073469** | 2,8516 | Q22 | 0,6629 | **2,19** |
| 5 | **210057170236** | 2,8932 | Q14 | 0,7132 | **2,18** |

> **Padrão identificado:** A questão Q12 aparece 3 vezes na lista de erros inesperados. Isso pode indicar que o item tem algum problema de formulação que confunde alunos de alta habilidade.

#### PARANÁ (PR)

| # | ID do Aluno | θ | Questão | Dificuldade (b) | Diferença (θ-b) |
|---|-------------|---|---------|-----------------|-----------------|
| 1 | **210057755513** | 3,1677 | Q14 | -0,1908 | **3,36** |
| 2 | **210057367956** | 3,0575 | Q14 | -0,1908 | **3,25** |
| 3 | **210057236472** | 2,9675 | Q14 | -0,1908 | **3,16** |
| 4 | **210055352085** | 2,9672 | Q11 | 1,0079 | **1,96** |
| 5 | **210056808237** | 3,3922 | Q6 | 1,6109 | **1,78** |

> **ITEM PROBLEMÁTICO - Q14:** Três alunos com habilidades entre θ = 2,97 e θ = 3,17 erraram esta questão, que tem dificuldade b = -0,1908 (muito fácil). A diferença média é de ~3,26 pontos. **Recomendação:** Este item deve ser revisado qualitativamente para identificar possíveis problemas no enunciado ou nas alternativas.

---

## 4. Comparação Direta de Alunos PA vs PR

### 4.1 Metodologia

Para comparar alunos de diferentes estados de forma justa, selecionamos alunos com habilidades similares (mesmo intervalo de θ) e analisamos seus padrões de resposta.

### 4.2 Faixa de Alta Habilidade (θ entre 1,0 e 1,5) - Matemática

#### Alunos Selecionados

**PARÁ:**
| ID | θ | Posição |
|----|---|---------|
| 210057152381 | 1,0001 | ~2.500 de 6.268 |
| 210054558434 | 1,0003 | |
| 210056504560 | 1,0004 | |

**PARANÁ:**
| ID | θ | Posição |
|----|---|---------|
| 210055453027 | 1,0013 | ~3.500 de 8.912 |
| 210055316565 | 1,0015 | |
| 210057768296 | 1,0016 | |

**Estatísticas da Faixa:**
- PA: 495 alunos (7,9% do total)
- PR: 725 alunos (8,1% do total)

> **Insight:** Proporcionalmente, PR e PA têm percentuais similares de alunos de alta habilidade nesta faixa (~8%). Isto contradiz a expectativa de que o estado melhor ranqueado no IDEB teria mais alunos de alta performance.

### 4.3 Faixa de Baixa Habilidade (θ entre -1,0 e -0,5) - Matemática

**PARÁ:**
| ID | θ |
|----|---|
| 210057651046 | -0,9954 |
| 210054769323 | -0,9950 |
| 210054883849 | -0,9948 |

**PARANÁ:**
| ID | θ |
|----|---|
| 210057806673 | -0,9991 |
| 210056899892 | -0,9987 |
| 210055283269 | -0,9983 |

**Estatísticas da Faixa:**
- PA: 1.212 alunos (19,3% do total)
- PR: 1.589 alunos (17,8% do total)

> **Insight:** O PA tem proporcionalmente mais alunos na faixa de baixa habilidade (19,3% vs 17,8%). Entretanto, em números absolutos, o PR tem mais alunos nesta faixa (1.589 vs 1.212).

---

## 5. Estatísticas Consolidadas

### 5.1 Taxa de Acertos Suspeitos (Chute) por Área e Estado

| Área | PA - Suspeitos | PA - Total | PA - Taxa | PR - Suspeitos | PR - Total | PR - Taxa |
|------|----------------|------------|-----------|----------------|------------|-----------|
| **Matemática** | 33.372 | 74.240 | **44,95%** | 44.697 | 122.461 | **36,50%** |
| **Linguagens** | 18.146 | 113.125 | 16,04% | 21.004 | 186.401 | 11,27% |
| **Ciências Humanas** | 23.356 | 107.090 | 21,81% | 23.779 | 171.040 | 13,90% |
| **Ciências da Natureza** | 34.812 | 71.309 | **48,82%** | 51.055 | 114.274 | **44,68%** |

### 5.2 Taxa de Erros Inesperados por Área e Estado

| Área | PA - Erros Inesp. | PA - Total Erros | PA - Taxa | PR - Erros Inesp. | PR - Total Erros | PR - Taxa |
|------|-------------------|------------------|-----------|-------------------|------------------|-----------|
| **Matemática** | 11.037 | 201.552 | 5,48% | 15.805 | 269.667 | 5,86% |
| **Linguagens** | 14.810 | 169.520 | 8,74% | 13.002 | 210.319 | 6,18% |
| **Ciências Humanas** | 5.379 | 175.285 | 3,07% | 10.773 | 225.680 | 4,77% |
| **Ciências da Natureza** | 19.222 | 210.841 | 9,12% | 35.164 | 286.676 | **12,27%** |

---

## 6. Implicações para Feedback Formativo

### 6.1 Para Alunos Específicos

#### Modelo de Feedback para Aluno com Possíveis Acertos por Chute

**Exemplo - Aluno 210055515774 (PR, Matemática):**

> *"Você acertou as questões Q39, Q26 e Q34, que são questões de alta dificuldade. Parabéns! No entanto, sua habilidade estimada (θ = -1,64) indica que você pode ter tido sorte nessas questões. Sugerimos que você revise os conteúdos relacionados a essas questões para consolidar o aprendizado:*
> - *Q39: [Conteúdo específico]*
> - *Q26: [Conteúdo específico]*
> - *Q34: [Conteúdo específico]*
> 
> *Continue estudando para transformar esses acertos em conhecimento sólido!"*

#### Modelo de Feedback para Aluno com Erros Inesperados

**Exemplo - Aluno 210056820621 (PR, Matemática):**

> *"Você demonstrou alta habilidade (θ = 2,34, equivalente a ~734 na escala ENEM), mas errou a questão Q9, que é relativamente fácil (b = -0,84). Isso pode ter ocorrido por desatenção ou interpretação equivocada do enunciado.*
> 
> *Dicas para evitar erros similares:*
> - *Leia o enunciado pelo menos duas vezes*
> - *Marque as informações-chave*
> - *Revise suas respostas antes de finalizar*
> 
> *Você tem potencial para acertar questões como essa! Pratique exercícios de atenção."*

### 6.2 Para Professores

#### Identificação de Itens Problemáticos

**Recomendação - Questão Q14 de Ciências da Natureza (PR):**

> *"A Q14 apresenta um padrão atípico: alunos de alta habilidade (θ > 2,9) estão errando esta questão que tem baixa dificuldade (b = -0,19). Sugerimos:*
> - *Revisar o enunciado para identificar possíveis ambiguidades*
> - *Verificar se as alternativas são claras*
> - *Analisar se o conteúdo está alinhado com o currículo*
> 
> *Esta questão pode não estar medindo adequadamente o conhecimento dos alunos."*

#### Identificação de Áreas com Alto Índice de Chute

**Recomendação - Ciências da Natureza:**

> *"A área de CN apresenta taxa de acertos suspeitos de ~48% no PA e ~45% no PR. Isso indica que:*
> - *Muitos alunos não dominam o conteúdo*
> - *Estão usando estratégia de chute*
> 
> *Sugestões:*
> - *Revisar metodologia de ensino dos tópicos com maior taxa de chute*
> - *Implementar avaliações formativas durante o ano*
> - *Trabalhar habilidades metacognitivas com os alunos"*

---

## 7. Reprodutibilidade - Código Python

### 7.1 Carregamento dos Dados

```python
import pandas as pd
import numpy as np
from scipy import stats

# Carregar habilidades
df_hab = pd.read_csv('codigos_R/LTM_3PL/habilidades/habil_3PL_ltm_MT_PA.csv')

# Carregar dificuldades
df_dif = pd.read_csv('codigos_R/LTM_3PL/dificuldades/dif_modelo_3PL_ltm_MT_PA.csv')

# Carregar dados normalizados
df_norm = pd.read_csv('report/normalized_data/habilidades/habil_MT_PA.csv')
```

### 7.2 Identificação de Acertos por Chute

```python
def identificar_acertos_chute(df_hab, df_dif, area):
    """
    Identifica acertos suspeitos por chute.
    Critério: θ < b - 1 AND acertou = 1 AND c > 0.10 AND a > 0
    """
    if area == 'MT':
        q_cols = [f'Q{i}' for i in range(1, 40)] + [f'Q{i}' for i in range(41, 46)]
    else:
        q_cols = [f'Q{i}' for i in range(1, 46)]
    
    acertos_suspeitos = []
    
    for _, aluno in df_hab.iterrows():
        theta = aluno['habilidade']
        aluno_id = aluno['alunos_id_string']
        
        for q in q_cols:
            if q in df_hab.columns and aluno[q] == 1:
                q_num = int(q.replace('Q', ''))
                dif_row = df_dif[df_dif['questao'] == q_num]
                
                if len(dif_row) > 0:
                    b = dif_row['dificuldade_item'].values[0]
                    c = dif_row['acerto_acaso_item'].values[0]
                    a = dif_row['discriminacao_item'].values[0]
                    
                    if theta < (b - 1) and c > 0.10 and a > 0:
                        acertos_suspeitos.append({
                            'aluno_id': aluno_id,
                            'theta': theta,
                            'questao': q,
                            'dificuldade': b,
                            'chute': c,
                            'diferenca': b - theta
                        })
    
    return pd.DataFrame(acertos_suspeitos)
```

### 7.3 Identificação de Erros Inesperados

```python
def identificar_erros_inesperados(df_hab, df_dif, area):
    """
    Identifica erros inesperados.
    Critério: θ > b + 1 AND acertou = 0 AND a > 0
    """
    if area == 'MT':
        q_cols = [f'Q{i}' for i in range(1, 40)] + [f'Q{i}' for i in range(41, 46)]
    else:
        q_cols = [f'Q{i}' for i in range(1, 46)]
    
    erros_inesperados = []
    
    for _, aluno in df_hab.iterrows():
        theta = aluno['habilidade']
        aluno_id = aluno['alunos_id_string']
        
        for q in q_cols:
            if q in df_hab.columns and aluno[q] == 0:
                q_num = int(q.replace('Q', ''))
                dif_row = df_dif[df_dif['questao'] == q_num]
                
                if len(dif_row) > 0:
                    b = dif_row['dificuldade_item'].values[0]
                    a = dif_row['discriminacao_item'].values[0]
                    
                    if theta > (b + 1) and a > 0:
                        erros_inesperados.append({
                            'aluno_id': aluno_id,
                            'theta': theta,
                            'questao': q,
                            'dificuldade': b,
                            'diferenca': theta - b
                        })
    
    return pd.DataFrame(erros_inesperados)
```

### 7.4 Cálculo de Estatísticas Descritivas

```python
def calcular_estatisticas(df_hab):
    """
    Calcula estatísticas descritivas das habilidades.
    """
    return {
        'n': len(df_hab),
        'media_theta': df_hab['habilidade'].mean(),
        'mediana_theta': df_hab['habilidade'].median(),
        'dp_theta': df_hab['habilidade'].std(),
        'min_theta': df_hab['habilidade'].min(),
        'max_theta': df_hab['habilidade'].max(),
        'p25': df_hab['habilidade'].quantile(0.25),
        'p75': df_hab['habilidade'].quantile(0.75)
    }
```

---

## 8. Conclusões

### Principais Descobertas com Evidências de Alunos

1. **Desempenho Similar entre Estados:** Alunos de estados diferentes com habilidades na mesma faixa (ex: aluno 210057651046 do PA com θ = -0,9954 vs aluno 210057806673 do PR com θ = -0,9991) apresentam proficiências praticamente idênticas.

2. **Alta Taxa de Chute em CN e MT:** O aluno 210054896020 (PA) acertou a Q36 de CN com diferença de 11,91 pontos entre sua habilidade e a dificuldade do item - caso extremo de provável chute.

3. **Padrão de Erros Inesperados:** A Q14 de CN no PR foi erroneamente respondida por 3 alunos de altíssima habilidade (θ > 2,9), indicando possível problema no item.

4. **Itens com Alto Parâmetro de Chute:** A Q22 de CN no PR tem c = 44,92%, fazendo com que alunos sem conhecimento tenham quase 50% de chance de acertar ao acaso.

---

*Documento gerado com dados exclusivamente do modelo 3PL*
*Arquivos fonte: `codigos_R/LTM_3PL/`*

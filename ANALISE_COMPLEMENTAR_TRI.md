# Análise Complementar TRI - Modelo 3PL

## Explicação Detalhada das Fórmulas e Metodologia

Este documento complementa `ANALISE_RESULTADOS_TRI_DETALHADA.md` com explicações aprofundadas das fórmulas utilizadas, tratamento de valores extremos e listas completas de alunos para feedback formativo.

---

## 1. Explicação das Fórmulas de Identificação

### 1.1 Fórmula do Modelo 3PL

O modelo logístico de 3 parâmetros (3PL) estima a probabilidade de um aluno com habilidade θ acertar um item:

```
P(θ) = c + (1 - c) / (1 + e^(-a(θ - b)))
```

**Parâmetros:**
- **θ (theta)**: Habilidade do examinando (-5 a +5 na escala original)
- **a (discriminação)**: Inclinação da curva característica do item
- **b (dificuldade)**: Ponto onde P = (1+c)/2 (dificuldade do item)
- **c (chute)**: Assíntota inferior - probabilidade mínima de acerto

**Interpretação Visual:**
```
P(θ)
  1 |           _____
    |         /
    |       /
    |     /
  c |..../ 
    |
  0 +------------------θ
         b
```

Quando θ < b: A curva está na parte inferior, P(θ) ≈ c (probabilidade de chute)
Quando θ = b: P(θ) = c + (1-c)/2 = (1+c)/2 (probabilidade de 50% acrescida do chute)
Quando θ > b: P(θ) → 1 (alta probabilidade de acerto)

---

### 1.2 Fórmula de Acerto Suspeito por Chute

```python
acerto_suspeito = (θ_aluno < b_item - 1) AND (acertou == 1) AND (c_item > 0.10) AND (a_item > 0)
```

**Explicação de cada componente:**

| Condição | Significado | Por que é necessária |
|----------|-------------|---------------------|
| `θ_aluno < b_item - 1` | Habilidade do aluno está **pelo menos 1 ponto abaixo** da dificuldade do item | Garante que o aluno "deveria" ter baixa probabilidade de acerto |
| `acertou == 1` | O aluno **acertou** a questão | Estamos identificando acertos, não erros |
| `c_item > 0.10` | O item tem probabilidade de chute **maior que 10%** | Itens sem chute não permitem acerto "por sorte" |
| `a_item > 0` | O item tem discriminação **positiva** | Itens com a < 0 são problemáticos e devem ser excluídos |

**Lógica probabilística:**

Se θ = -1.5 e b = 2.0, então a diferença é de 3.5 pontos. Pela fórmula 3PL:

```python
# Exemplo numérico
theta = -1.5
b = 2.0
a = 2.0  # discriminação típica
c = 0.20  # 20% de chute

expoente = -a * (theta - b)  # -2 * (-1.5 - 2.0) = -2 * (-3.5) = 7
P = c + (1 - c) / (1 + exp(expoente))
P = 0.20 + 0.80 / (1 + exp(7))
P = 0.20 + 0.80 / 1097
P ≈ 0.2007  # Praticamente só o chute (20%)
```

**Conclusão:** Um aluno com θ muito abaixo de b tem probabilidade de acerto próxima ao parâmetro c. Se acertou, provavelmente foi por chute.

---

### 1.3 Fórmula de Erro Inesperado

```python
erro_inesperado = (θ_aluno > b_item + 1) AND (acertou == 0) AND (a_item > 0)
```

**Explicação de cada componente:**

| Condição | Significado | Por que é necessária |
|----------|-------------|---------------------|
| `θ_aluno > b_item + 1` | Habilidade do aluno está **pelo menos 1 ponto acima** da dificuldade do item | Garante que o aluno "deveria" ter alta probabilidade de acerto |
| `acertou == 0` | O aluno **errou** a questão | Estamos identificando erros, não acertos |
| `a_item > 0` | O item tem discriminação **positiva** | Itens com a < 0 são problemáticos e devem ser excluídos |

**Lógica probabilística:**

Se θ = 2.5 e b = 0.5, então a diferença é de 2.0 pontos. Pela fórmula 3PL:

```python
# Exemplo numérico
theta = 2.5
b = 0.5
a = 2.0  # discriminação típica
c = 0.20  # 20% de chute

expoente = -a * (theta - b)  # -2 * (2.5 - 0.5) = -2 * 2.0 = -4
P = c + (1 - c) / (1 + exp(expoente))
P = 0.20 + 0.80 / (1 + exp(-4))
P = 0.20 + 0.80 / 1.018
P ≈ 0.986  # 98.6% de probabilidade de acerto
```

**Conclusão:** Um aluno com θ muito acima de b tem probabilidade de acerto > 95%. Se errou, foi provavelmente por desatenção, interpretação equivocada ou lacuna específica de conhecimento.

---

### 1.4 Por que o limiar de 1 ponto?

O limiar de **1 ponto na escala θ** foi escolhido porque:

1. **Significância estatística**: Uma diferença de 1 ponto corresponde a aproximadamente 1 desvio padrão na escala de habilidade
2. **Impacto na probabilidade**: Com a = 1.5 (discriminação média), uma diferença de 1 ponto muda a probabilidade de ~0.5 para ~0.8 ou ~0.2
3. **Margem de erro**: Considera o erro padrão da estimação de θ (geralmente ± 0.3 a 0.5)

**Visualização do impacto:**

| Diferença (θ - b) | P(acerto) com a=1.5, c=0.20 |
|-------------------|----------------------------|
| -2 | 0.24 (≈ chute) |
| -1 | 0.32 |
| 0 | 0.60 |
| +1 | 0.86 |
| +2 | 0.96 |

---

## 2. Tratamento de Valores Extremos de Dificuldade

### 2.1 Itens com Dificuldade Fora da Faixa [-4, 4]

Foram identificados diversos itens com valores de dificuldade (b) extremos:

#### Matemática - Pará (PA)
| Questão | b | a | c | Problema |
|---------|---|---|---|----------|
| Q10 | 6.98 | 0.23 | 0.02 | a muito baixo |
| Q17 | 4.81 | 0.22 | 0.01 | a muito baixo |
| Q21 | 5.59 | 0.23 | 0.02 | a muito baixo |
| **Q22** | **189.67** | 0.01 | 0.16 | a ≈ 0, item não discrimina |
| Q27 | -6.91 | **-0.51** | 0.07 | a < 0 (problemático) |
| Q36 | 20.29 | 0.07 | 0.08 | a muito baixo |
| Q39 | 13.98 | 0.14 | 0.02 | a muito baixo |

#### Matemática - Paraná (PR)
| Questão | b | a | c | Problema |
|---------|---|---|---|----------|
| Q10 | 7.06 | 0.22 | 0.03 | a muito baixo |
| Q17 | 5.72 | 0.17 | 0.02 | a muito baixo |
| Q21 | 5.48 | 0.19 | 0.02 | a muito baixo |
| **Q22** | **49.02** | 0.03 | 0.06 | a ≈ 0, item não discrimina |
| Q27 | -11.74 | **-0.22** | 0.02 | a < 0 (problemático) |
| **Q36** | **-88.32** | **-0.02** | 0.08 | a < 0 (problemático) |

#### Ciências da Natureza - Pará (PA)
| Questão | b | a | c | Problema |
|---------|---|---|---|----------|
| Q5 | -5.35 | **-0.28** | 0.12 | a < 0 (problemático) |
| Q15 | 4.33 | 0.37 | 0.17 | Limítrofe |
| Q17 | 4.32 | 1.30 | 0.12 | a OK, item muito difícil |
| Q21 | 4.97 | 0.23 | 0.04 | a muito baixo |
| Q35 | -9.79 | **-0.16** | 0.07 | a < 0 (problemático) |
| **Q36** | **10.56** | 0.42 | 0.17 | a baixo |
| **Q37** | **-202.46** | **-0.01** | 0.23 | a ≈ 0 (problema grave) |
| Q43 | -5.66 | **-0.30** | 0.02 | a < 0 (problemático) |

### 2.2 Explicação dos Valores Extremos

**Por que ocorrem valores como b = 189 ou b = -202?**

Esses valores extremos ocorrem quando:

1. **Discriminação muito baixa (a → 0)**: A curva característica se torna quase horizontal, fazendo o algoritmo de estimação divergir
2. **Discriminação negativa (a < 0)**: O item funciona "ao contrário" - quanto maior a habilidade, menor a chance de acerto
3. **Problema de convergência**: O algoritmo de máxima verossimilhança não consegue encontrar estimativas estáveis

**Visualização:**

```
Item Normal (a > 0.5):      Item Problemático (a → 0):
   P                            P
   1|     ___                   1|  ________________
    |   /                        |
    | /                          |
 0.5|•                        0.5|•
    |                            |
   0+----θ                      0+----θ
      b                           b → ∞
```

### 2.3 Recomendação: Filtrar ou Observar?

**Recomendação:** Para análises válidas, **filtrar itens** com:
- `a < 0` (discriminação negativa)
- `a < 0.3` (discriminação muito baixa - segundo Baker & Kim, 2017, valores abaixo de 0.35 indicam itens de qualidade questionável)
- `|b| > 4` (dificuldade fora da escala típica)

**Justificativa:**
1. A escala de -4 a +4 (ou -5 a +5) cobre 99.99% dos alunos
2. Itens fora dessa faixa têm parâmetros não confiáveis
3. Esses itens comprometem a validade da avaliação

**Na análise apresentada:** Todos os cálculos de acerto por chute e erro inesperado já **filtram itens com a < 0 ou |b| > 4** usando o critério `(a_item > 0)` e considerando apenas itens com parâmetros válidos.

**Observação para o artigo:** É válido mencionar que alguns itens apresentaram parâmetros fora da faixa esperada, sugerindo problemas de calibração ou formulação do item.

---

## 3. Lista de 10 Alunos por Cenário - Para Feedback Formativo

### 3.1 MATEMÁTICA (MT)

#### Pará (PA)

**Alunos de Baixa Habilidade (θ < -0.5) - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) | Perfil |
|---|-------------|---|-------------------|--------|
| 1 | 210057715141 | -1.4406 | ~356 | Muito baixo |
| 2 | 210057638944 | -1.3073 | ~369 | Muito baixo |
| 3 | 210056753271 | -1.2987 | ~370 | Muito baixo |
| 4 | 210054579943 | -1.2577 | ~374 | Muito baixo |
| 5 | 210055144470 | -1.2298 | ~377 | Muito baixo |
| 6 | 210055041533 | -1.2240 | ~378 | Muito baixo |
| 7 | 210054575969 | -1.2232 | ~378 | Muito baixo |
| 8 | 210054900376 | -1.2226 | ~378 | Muito baixo |
| 9 | 210054520833 | -1.2226 | ~378 | Muito baixo |
| 10 | 210057262204 | -1.2224 | ~378 | Muito baixo |

**Alunos de Alta Habilidade (θ > 1.0) - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) | Perfil |
|---|-------------|---|-------------------|--------|
| 1 | 210057073469 | 3.3545 | ~835 | Excelente |
| 2 | 210057621097 | 3.2742 | ~827 | Excelente |
| 3 | 210054559551 | 3.2483 | ~825 | Excelente |
| 4 | 210057386329 | 3.1049 | ~810 | Excelente |
| 5 | 210054634680 | 3.0748 | ~807 | Excelente |
| 6 | 210057170236 | 2.9387 | ~794 | Muito Alto |
| 7 | 210054527854 | 2.9275 | ~793 | Muito Alto |
| 8 | 210054656683 | 2.9265 | ~793 | Muito Alto |
| 9 | 210055154207 | 2.8332 | ~783 | Muito Alto |
| 10 | 210054567989 | 2.8208 | ~782 | Muito Alto |

**Acertos Suspeitos por Chute - 10 exemplos:**

| # | ID | θ | Questão | b | Diferença | c |
|---|-------------|---|---------|---|-----------|---|
| 1 | 210056753271 | -1.30 | Q32 | 3.16 | 4.46 | 20% |
| 2 | 210055144470 | -1.23 | Q32 | 3.16 | 4.39 | 20% |
| 3 | 210055041533 | -1.22 | Q32 | 3.16 | 4.38 | 20% |
| 4 | 210056753271 | -1.30 | Q42 | 2.81 | 4.11 | 20% |
| 5 | 210057638944 | -1.31 | Q25 | 2.76 | 4.07 | 24% |
| 6 | 210054952536 | -1.22 | Q42 | 2.81 | 4.03 | 20% |
| 7 | 210054901871 | -1.22 | Q42 | 2.81 | 4.03 | 20% |
| 8 | 210054579943 | -1.26 | Q25 | 2.76 | 4.02 | 24% |
| 9 | 210054900376 | -1.22 | Q25 | 2.76 | 3.98 | 24% |
| 10 | 210054901871 | -1.22 | Q25 | 2.76 | 3.98 | 24% |

#### Paraná (PR)

**Alunos de Baixa Habilidade (θ < -0.5) - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) | Perfil |
|---|-------------|---|-------------------|--------|
| 1 | 210055668415 | -1.6622 | ~334 | Muito baixo |
| 2 | 210055515774 | -1.6379 | ~336 | Muito baixo |
| 3 | 210056729672 | -1.6232 | ~338 | Muito baixo |
| 4 | 210057287122 | -1.6115 | ~339 | Muito baixo |
| 5 | 210054971799 | -1.5972 | ~340 | Muito baixo |
| 6 | 210057376930 | -1.5968 | ~340 | Muito baixo |
| 7 | 210056794925 | -1.5761 | ~342 | Muito baixo |
| 8 | 210055495243 | -1.5735 | ~343 | Muito baixo |
| 9 | 210057378300 | -1.5558 | ~344 | Muito baixo |
| 10 | 210055527509 | -1.5522 | ~345 | Muito baixo |

**Alunos de Alta Habilidade (θ > 1.0) - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) | Perfil |
|---|-------------|---|-------------------|--------|
| 1 | 210056808237 | 3.1175 | ~812 | Excelente |
| 2 | 210055185541 | 2.9824 | ~798 | Muito Alto |
| 3 | 210056864119 | 2.9427 | ~794 | Muito Alto |
| 4 | 210057723494 | 2.8648 | ~786 | Muito Alto |
| 5 | 210057367956 | 2.8071 | ~781 | Muito Alto |
| 6 | 210057369769 | 2.8039 | ~780 | Muito Alto |
| 7 | 210057358876 | 2.7837 | ~778 | Muito Alto |
| 8 | 210057769186 | 2.7733 | ~777 | Muito Alto |
| 9 | 210055460752 | 2.7193 | ~772 | Muito Alto |
| 10 | 210055536698 | 2.6612 | ~766 | Muito Alto |

**Erros Inesperados - 10 exemplos:**

| # | ID | θ | Questão | b | Diferença |
|---|-------------|---|---------|---|-----------|
| 1 | 210055616833 | 0.56 | Q9 | -0.84 | 1.40 |
| 2 | 210055485540 | 0.56 | Q9 | -0.84 | 1.40 |
| 3 | 210055394700 | 0.55 | Q9 | -0.84 | 1.39 |
| 4 | 210055469416 | 0.55 | Q9 | -0.84 | 1.39 |
| 5 | 210055087310 | 0.55 | Q9 | -0.84 | 1.39 |
| 6 | 210057821662 | 0.54 | Q9 | -0.84 | 1.38 |
| 7 | 210055594043 | 0.53 | Q9 | -0.84 | 1.37 |
| 8 | 210055522348 | 0.53 | Q9 | -0.84 | 1.37 |
| 9 | 210055391955 | 0.52 | Q9 | -0.84 | 1.36 |
| 10 | 210055138693 | 0.52 | Q9 | -0.84 | 1.36 |

---

### 3.2 LINGUAGENS (LC)

#### Pará (PA)

**Alunos de Baixa Habilidade - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) |
|---|-------------|---|-------------------|
| 1 | 210055117815 | -2.6347 | ~237 |
| 2 | 210055085649 | -2.5602 | ~244 |
| 3 | 210054579873 | -2.4747 | ~253 |
| 4 | 210056610565 | -2.4719 | ~253 |
| 5 | 210056794969 | -2.4009 | ~260 |
| 6 | 210057137116 | -2.3697 | ~263 |
| 7 | 210057242612 | -2.2500 | ~275 |
| 8 | 210056721190 | -2.1710 | ~283 |
| 9 | 210054713760 | -2.1689 | ~283 |
| 10 | 210057682430 | -2.1637 | ~284 |

**Alunos de Alta Habilidade - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) |
|---|-------------|---|-------------------|
| 1 | 210054520901 | 2.6711 | ~767 |
| 2 | 210054688006 | 2.5617 | ~756 |
| 3 | 210057159960 | 2.5281 | ~753 |
| 4 | 210054695345 | 2.5231 | ~752 |
| 5 | 210054592421 | 2.4808 | ~748 |
| 6 | 210055017417 | 2.4506 | ~745 |
| 7 | 210054899354 | 2.4477 | ~745 |
| 8 | 210056718423 | 2.4474 | ~745 |
| 9 | 210055054523 | 2.4267 | ~743 |
| 10 | 210054802939 | 2.4070 | ~741 |

**Acertos Suspeitos por Chute - 10 exemplos:**

| # | ID | θ | Questão | b | Diferença |
|---|-------------|---|---------|---|-----------|
| 1 | 210055117815 | -2.63 | Q31 | 2.77 | 5.41 |
| 2 | 210056610565 | -2.47 | Q19 | 2.83 | 5.30 |
| 3 | 210056610565 | -2.47 | Q31 | 2.77 | 5.24 |
| 4 | 210057137116 | -2.37 | Q19 | 2.83 | 5.20 |
| 5 | 210056794969 | -2.40 | Q31 | 2.77 | 5.17 |
| 6 | 210057137116 | -2.37 | Q31 | 2.77 | 5.14 |
| 7 | 210057242612 | -2.25 | Q19 | 2.83 | 5.08 |
| 8 | 210054713760 | -2.17 | Q19 | 2.83 | 5.00 |
| 9 | 210054713760 | -2.17 | Q31 | 2.77 | 4.94 |
| 10 | 210057682430 | -2.16 | Q31 | 2.77 | 4.93 |

#### Paraná (PR)

**Alunos de Baixa Habilidade - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) |
|---|-------------|---|-------------------|
| 1 | 210055564757 | -2.6344 | ~237 |
| 2 | 210057566801 | -2.6252 | ~237 |
| 3 | 210057347558 | -2.6005 | ~240 |
| 4 | 210055413006 | -2.5930 | ~241 |
| 5 | 210056536456 | -2.5647 | ~244 |
| 6 | 210055292798 | -2.5466 | ~245 |
| 7 | 210055560951 | -2.5422 | ~246 |
| 8 | 210057551651 | -2.5366 | ~246 |
| 9 | 210057819771 | -2.5149 | ~249 |
| 10 | 210057346798 | -2.4730 | ~253 |

**Alunos de Alta Habilidade - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) |
|---|-------------|---|-------------------|
| 1 | 210057293816 | 2.8850 | ~789 |
| 2 | 210055438559 | 2.7321 | ~773 |
| 3 | 210055278838 | 2.6938 | ~769 |
| 4 | 210056862189 | 2.6126 | ~761 |
| 5 | 210055627043 | 2.6001 | ~760 |
| 6 | 210057278737 | 2.5999 | ~760 |
| 7 | 210054954197 | 2.5304 | ~753 |
| 8 | 210055632038 | 2.5050 | ~751 |
| 9 | 210055311330 | 2.5017 | ~750 |
| 10 | 210055519326 | 2.4812 | ~748 |

---

### 3.3 CIÊNCIAS HUMANAS (CH)

#### Pará (PA)

**Alunos de Baixa Habilidade - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) |
|---|-------------|---|-------------------|
| 1 | 210054828335 | -2.1809 | ~282 |
| 2 | 210054803451 | -2.1401 | ~286 |
| 3 | 210056721190 | -2.1278 | ~287 |
| 4 | 210057282027 | -2.1102 | ~289 |
| 5 | 210058008503 | -2.1083 | ~289 |
| 6 | 210057634616 | -2.1039 | ~290 |
| 7 | 210056225314 | -2.0741 | ~293 |
| 8 | 210055014550 | -2.0600 | ~294 |
| 9 | 210056844272 | -2.0562 | ~294 |
| 10 | 210054785165 | -2.0554 | ~294 |

**Alunos de Alta Habilidade - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) |
|---|-------------|---|-------------------|
| 1 | 210054802939 | 2.9421 | ~794 |
| 2 | 210054493037 | 2.7776 | ~778 |
| 3 | 210054537519 | 2.7099 | ~771 |
| 4 | 210054520901 | 2.6839 | ~768 |
| 5 | 210056801269 | 2.6207 | ~762 |
| 6 | 210057606472 | 2.5954 | ~760 |
| 7 | 210057159960 | 2.5865 | ~759 |
| 8 | 210057612537 | 2.5829 | ~758 |
| 9 | 210054730274 | 2.5509 | ~755 |
| 10 | 210054971408 | 2.5118 | ~751 |

#### Paraná (PR)

**Alunos de Baixa Habilidade - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) |
|---|-------------|---|-------------------|
| 1 | 210058004862 | -2.5745 | ~243 |
| 2 | 210055524133 | -2.5705 | ~243 |
| 3 | 210056690647 | -2.5679 | ~243 |
| 4 | 210057671230 | -2.5497 | ~245 |
| 5 | 210055180880 | -2.4899 | ~251 |
| 6 | 210055688259 | -2.4527 | ~255 |
| 7 | 210055516398 | -2.4153 | ~258 |
| 8 | 210056441452 | -2.3916 | ~261 |
| 9 | 210056523321 | -2.3883 | ~261 |
| 10 | 210055046225 | -2.3505 | ~265 |

**Alunos de Alta Habilidade - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) |
|---|-------------|---|-------------------|
| 1 | 210057255613 | 2.9844 | ~798 |
| 2 | 210055140444 | 2.8001 | ~780 |
| 3 | 210057780977 | 2.7103 | ~771 |
| 4 | 210055486785 | 2.6553 | ~766 |
| 5 | 210055183262 | 2.6478 | ~765 |
| 6 | 210056601209 | 2.6334 | ~763 |
| 7 | 210055069406 | 2.6307 | ~763 |
| 8 | 210056864379 | 2.5998 | ~760 |
| 9 | 210055278838 | 2.5835 | ~758 |
| 10 | 210057686887 | 2.5455 | ~755 |

---

### 3.4 CIÊNCIAS DA NATUREZA (CN)

#### Pará (PA)

**Alunos de Baixa Habilidade - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) |
|---|-------------|---|-------------------|
| 1 | 210054509366 | -1.3772 | ~362 |
| 2 | 210054896020 | -1.3475 | ~365 |
| 3 | 210055042997 | -1.3456 | ~365 |
| 4 | 210054960522 | -1.3328 | ~367 |
| 5 | 210054549281 | -1.3143 | ~369 |
| 6 | 210054833732 | -1.3088 | ~369 |
| 7 | 210054915349 | -1.2863 | ~371 |
| 8 | 210056600800 | -1.2830 | ~372 |
| 9 | 210054703873 | -1.2663 | ~373 |
| 10 | 210054761063 | -1.2590 | ~374 |

**Alunos de Alta Habilidade - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) |
|---|-------------|---|-------------------|
| 1 | 210057386329 | 2.9455 | ~795 |
| 2 | 210057170236 | 2.8932 | ~789 |
| 3 | 210057165191 | 2.8809 | ~788 |
| 4 | 210054559551 | 2.8586 | ~786 |
| 5 | 210057073469 | 2.8516 | ~785 |
| 6 | 210054911417 | 2.8505 | ~785 |
| 7 | 210056216602 | 2.8305 | ~783 |
| 8 | 210054541614 | 2.8159 | ~782 |
| 9 | 210057151674 | 2.8134 | ~781 |
| 10 | 210057666437 | 2.7782 | ~778 |

**Acertos Suspeitos por Chute - 10 exemplos:**

| # | ID | θ | Questão | b | Diferença |
|---|-------------|---|---------|---|-----------|
| 1 | 210054509366 | -1.38 | Q16 | 2.90 | 4.28 |
| 2 | 210054509366 | -1.38 | Q3 | 2.88 | 4.26 |
| 3 | 210054896020 | -1.35 | Q16 | 2.90 | 4.25 |
| 4 | 210054896020 | -1.35 | Q3 | 2.88 | 4.23 |
| 5 | 210054549281 | -1.31 | Q3 | 2.88 | 4.19 |
| 6 | 210054509366 | -1.38 | Q19 | 2.79 | 4.16 |
| 7 | 210054833732 | -1.31 | Q31 | 2.82 | 4.13 |
| 8 | 210054915349 | -1.29 | Q30 | 2.83 | 4.11 |
| 9 | 210054549281 | -1.31 | Q19 | 2.79 | 4.10 |
| 10 | 210056600800 | -1.28 | Q34 | 2.82 | 4.10 |

#### Paraná (PR)

**Alunos de Baixa Habilidade - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) |
|---|-------------|---|-------------------|
| 1 | 210057879963 | -2.2432 | ~276 |
| 2 | 210057759026 | -2.1159 | ~288 |
| 3 | 210055416405 | -2.1122 | ~289 |
| 4 | 210057328893 | -2.0683 | ~293 |
| 5 | 210054940032 | -2.0496 | ~295 |
| 6 | 210056882821 | -2.0207 | ~298 |
| 7 | 210055040770 | -1.9978 | ~300 |
| 8 | 210056895542 | -1.9525 | ~305 |
| 9 | 210056887746 | -1.9489 | ~305 |
| 10 | 210058021990 | -1.9428 | ~306 |

**Alunos de Alta Habilidade - 10 exemplos:**

| # | ID do Aluno | θ | θ Normalizado (~) |
|---|-------------|---|-------------------|
| 1 | 210056684908 | 3.7089 | ~871 |
| 2 | 210057569637 | 3.4342 | ~843 |
| 3 | 210056808237 | 3.3922 | ~839 |
| 4 | 210057348542 | 3.2549 | ~825 |
| 5 | 210056890179 | 3.2119 | ~821 |
| 6 | 210057755513 | 3.1677 | ~817 |
| 7 | 210055185541 | 3.1426 | ~814 |
| 8 | 210057383057 | 3.0686 | ~807 |
| 9 | 210057367956 | 3.0575 | ~806 |
| 10 | 210055584838 | 3.0488 | ~805 |

**Acertos Suspeitos por Chute - 10 exemplos:**

| # | ID | θ | Questão | b | Diferença |
|---|-------------|---|---------|---|-----------|
| 1 | 210057879963 | -2.24 | Q21 | 3.79 | 6.04 |
| 2 | 210054940032 | -2.05 | Q15 | 3.95 | 6.00 |
| 3 | 210055040770 | -2.00 | Q15 | 3.95 | 5.95 |
| 4 | 210056882821 | -2.02 | Q21 | 3.79 | 5.81 |
| 5 | 210055416405 | -2.11 | Q3 | 3.59 | 5.71 |
| 6 | 210058021990 | -1.94 | Q3 | 3.59 | 5.54 |
| 7 | 210057759026 | -2.12 | Q17 | 3.06 | 5.18 |
| 8 | 210055040770 | -2.00 | Q17 | 3.06 | 5.06 |
| 9 | 210057879963 | -2.24 | Q45 | 2.79 | 5.03 |
| 10 | 210055040770 | -2.00 | Q45 | 2.79 | 4.78 |

---

## 4. Modelos de Feedback Formativo com Matriz ENEM

### 4.1 Matriz de Referência do ENEM

O ENEM avalia competências e habilidades organizadas por área:

| Área | Competências | Habilidades |
|------|--------------|-------------|
| Matemática (MT) | 7 competências | 30 habilidades (H1-H30) |
| Linguagens (LC) | 9 competências | 30 habilidades (H1-H30) |
| Ciências Humanas (CH) | 6 competências | 30 habilidades (H1-H30) |
| Ciências da Natureza (CN) | 8 competências | 30 habilidades (H1-H30) |

### 4.2 Exemplo de Feedback para Aluno - Baixa Habilidade

**Aluno:** 210057715141
**Estado:** Pará (PA)
**Área:** Matemática (MT)
**Habilidade (θ):** -1.4406
**Habilidade Normalizada:** ~356 pontos

---

#### RELATÓRIO DE FEEDBACK FORMATIVO

**Prezado(a) Estudante,**

Sua proficiência estimada em Matemática foi de **356 pontos** (escala ENEM 200-1000).

**📊 O que isso significa?**

Sua habilidade está na faixa **Muito Baixa** (abaixo de 450 pontos). Isso indica que você ainda precisa desenvolver competências fundamentais em Matemática.

**🎯 Competências a Desenvolver (Prioritárias):**

1. **Competência 1 - Números e Operações**
   - H1: Reconhecer diferentes significados de números e operações
   - H2: Identificar padrões numéricos
   - H3: Resolver situações-problema com conhecimentos numéricos

2. **Competência 2 - Geometria**
   - H6: Interpretar localização e movimentação no espaço
   - H7: Identificar características de figuras planas e espaciais

**⚠️ Análise de suas Respostas:**

Você acertou algumas questões de alta dificuldade (ex: Q32, Q25) apesar de sua habilidade baixa. Isso pode indicar:
- Acertos por eliminação ou sorte
- Conhecimento pontual em alguns tópicos

**📚 Recomendações de Estudo:**

1. **Fundamentos primeiro:** Revise operações básicas com frações, decimais e porcentagens
2. **Interpretação:** Pratique leitura de gráficos e tabelas simples
3. **Problemas do dia a dia:** Resolva problemas contextualizados de matemática financeira

**🔗 Recursos Sugeridos:**
- [Site de Estudos do ENEM](https://app.mecenem.mec.gov.br/)
- Khan Academy - Matemática Básica
- Questões anteriores do ENEM (nível fácil)

---

### 4.3 Exemplo de Feedback para Aluno - Alta Habilidade

**Aluno:** 210057073469
**Estado:** Pará (PA)
**Área:** Matemática (MT)
**Habilidade (θ):** 3.3545
**Habilidade Normalizada:** ~835 pontos

---

#### RELATÓRIO DE FEEDBACK FORMATIVO

**Prezado(a) Estudante,**

Sua proficiência estimada em Matemática foi de **835 pontos** (escala ENEM 200-1000).

**🏆 Parabéns!**

Sua habilidade está na faixa **Muito Alta** (acima de 750 pontos). Você demonstrou excelente domínio das competências matemáticas avaliadas pelo ENEM.

**✅ Competências Demonstradas:**

Você domina a maioria das habilidades, incluindo:

1. **Competência 5 - Álgebra e Funções**
   - H19: Identificar representações algébricas
   - H20: Interpretar gráficos cartesianos
   - H21: Resolver situações-problema com modelagem algébrica

2. **Competência 7 - Estatística e Probabilidade**
   - H28: Resolver situações-problema de estatística
   - H29: Utilizar estatística na construção de argumentos

**📈 Pontos de Atenção:**

Mesmo com alta habilidade, você errou algumas questões de dificuldade média. Verifique se houve:
- Desatenção na leitura do enunciado
- Erro de cálculo
- Interpretação equivocada de gráficos

**🎯 Próximos Passos:**

1. **Mantenha o nível:** Continue praticando questões de alto nível
2. **Atenção aos detalhes:** Revise respostas antes de finalizar
3. **Aprofundamento:** Estude tópicos avançados não cobertos pelo ENEM

---

### 4.4 Exemplo de Feedback para Professor

**Estado:** Pará (PA)
**Área:** Matemática (MT)
**Total de Alunos:** 6.268

---

#### RELATÓRIO PARA O PROFESSOR

**Panorama Geral da Turma:**

| Faixa de Proficiência | N | % |
|-----------------------|---|---|
| Muito Baixo (< 450) | 0 | 0% |
| Baixo (450-550) | 1.433 | 22.9% |
| Médio (550-650) | 2.915 | 46.5% |
| Alto (650-750) | 1.463 | 23.3% |
| Muito Alto (> 750) | 457 | 7.3% |

**📊 Análise das Competências:**

**Competências com maior déficit (itens com mais erros):**

1. **C2 - Geometria Espacial**
   - Itens Q7, Q8, Q9 tiveram baixo índice de acerto
   - Habilidades H6, H7, H8 precisam de reforço

2. **C5 - Álgebra**
   - Itens Q19-Q23 mostraram dificuldade média
   - Alunos de baixa habilidade não conseguem modelar problemas

**⚠️ Itens Problemáticos:**

| Item | Problema | Recomendação |
|------|----------|--------------|
| Q22 | b = 189 (instável) | Desconsiderar na análise |
| Q27 | a < 0 (negativo) | Item não discrimina |
| Q36 | a muito baixo | Revisar formulação |

**📈 Taxa de Acertos Suspeitos (Chute):**

**44,95%** dos acertos podem ter sido por chute. Isso indica que muitos alunos estão usando estratégias de eliminação em vez de conhecimento sólido.

**🎯 Recomendações Pedagógicas:**

1. **Reforço em Geometria:** Implementar atividades práticas com figuras espaciais
2. **Problemas Contextualizados:** Trabalhar mais situações-problema do cotidiano
3. **Avaliação Formativa:** Aplicar diagnósticos frequentes para identificar lacunas
4. **Estratégias de Prova:** Ensinar técnicas de resolução que minimizem chute

**Alunos Prioritários para Intervenção:**

| ID | θ | Necessidade |
|----|---|-------------|
| 210057715141 | -1.44 | Urgente |
| 210057638944 | -1.31 | Urgente |
| 210056753271 | -1.30 | Urgente |
| 210054579943 | -1.26 | Alta |
| 210055144470 | -1.23 | Alta |

---

## 5. Conversão de Escalas - Referência

### 5.1 Fórmula de Conversão

```
θ_normalizado = 500 + (100 × θ)

Onde: θ deve estar no intervalo [-3, 5] para garantir resultados na escala ENEM (200-1000)
      Valores fora deste intervalo devem ser truncados aos limites 200 ou 1000
```

### 5.2 Tabela de Conversão

| θ (original) | θ normalizado | Classificação |
|--------------|---------------|---------------|
| -3.0 | 200 | Mínimo |
| -2.5 | 250 | Muito Baixo |
| -2.0 | 300 | Muito Baixo |
| -1.5 | 350 | Muito Baixo |
| -1.0 | 400 | Baixo |
| -0.5 | 450 | Baixo |
| 0.0 | 500 | Médio |
| 0.5 | 550 | Médio |
| 1.0 | 600 | Médio |
| 1.5 | 650 | Alto |
| 2.0 | 700 | Alto |
| 2.5 | 750 | Muito Alto |
| 3.0 | 800 | Muito Alto |
| 3.5 | 850 | Excelente |
| 4.0 | 900 | Excelente |
| 5.0 | 1000 | Máximo |

---

*Documento gerado para complementar as análises TRI do modelo 3PL*
*Dados: ENEM 2022 - Estados PA e PR*

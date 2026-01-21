# Prompt para Análise TRI - Modelo 3PL

## Instruções de Uso

Este documento contém um prompt estruturado que pode ser usado com qualquer agente de IA para realizar análises similares às apresentadas em `ANALISE_RESULTADOS_TRI_DETALHADA.md`.

**Para usar:**
1. Copie o prompt abaixo
2. Substitua os placeholders `{...}` pelos seus dados
3. Cole no agente de IA de sua preferência

---

## Prompt Completo

```
# TAREFA: Análise de Dados da Teoria de Resposta ao Item (TRI) - Modelo 3PL

## CONTEXTO

Você é um especialista em psicometria e análise de dados educacionais. Recebi dados do ENEM processados com o modelo logístico de 3 parâmetros (3PL) da Teoria de Resposta ao Item.

O modelo 3PL estima três parâmetros para cada item:
- **a (discriminação)**: Capacidade do item de diferenciar alunos
- **b (dificuldade)**: Nível de habilidade necessário para 50% de chance de acerto
- **c (chute)**: Probabilidade de acerto ao acaso

E um parâmetro para cada aluno:
- **θ (theta/habilidade)**: Proficiência estimada do aluno

A fórmula do modelo 3PL é:
P(θ) = c + (1 - c) / (1 + exp(-a(θ - b)))

## DADOS DISPONÍVEIS

### Estrutura dos Arquivos de Habilidade (por aluno)
Arquivo: habil_3PL_ltm_{AREA}_{ESTADO}.csv

Colunas:
- Q1 a Q45: Respostas binárias (0=erro, 1=acerto)
- habilidade: Valor de θ (escala -5 a 5)
- alunos_id_string: ID único do aluno
- Obs: Total de acertos

Exemplo de dados:
{COLE_AQUI_PRIMEIRAS_LINHAS_DO_ARQUIVO_DE_HABILIDADES}

### Estrutura dos Arquivos de Dificuldade (por item)
Arquivo: dif_modelo_3PL_ltm_{AREA}_{ESTADO}.csv

Colunas:
- questao: Número da questão
- dificuldade_item (b): Dificuldade
- discriminacao_item (a): Discriminação
- acerto_acaso_item (c): Probabilidade de chute

Exemplo de dados:
{COLE_AQUI_PRIMEIRAS_LINHAS_DO_ARQUIVO_DE_DIFICULDADES}

## ANÁLISES SOLICITADAS

Por favor, realize as seguintes análises:

### 1. PERFIS DE ALUNOS
- Identifique alunos nos extremos (menor e maior habilidade)
- Identifique alunos nos percentis 10, 50 e 90
- Para cada aluno, liste: ID, θ, total de acertos

### 2. ACERTOS POR CHUTE
Critério: θ_aluno < b_item - 1 AND acertou = 1 AND c > 0.10

Para cada caso encontrado, mostre:
- ID do aluno
- Habilidade (θ)
- Questão acertada
- Dificuldade do item (b)
- Diferença (b - θ)
- Probabilidade de chute (c)

### 3. ERROS INESPERADOS
Critério: θ_aluno > b_item + 1 AND acertou = 0

Para cada caso encontrado, mostre:
- ID do aluno
- Habilidade (θ)
- Questão errada
- Dificuldade do item (b)
- Diferença (θ - b)

### 4. COMPARAÇÃO ENTRE ESTADOS (se aplicável)
- Compare alunos com habilidades similares em diferentes estados
- Calcule estatísticas por faixa de habilidade
- Identifique padrões diferenciados

### 5. ITENS PROBLEMÁTICOS
Identifique itens com:
- Discriminação negativa (a < 0)
- Alto parâmetro de chute (c > 0.25)
- Padrão de erros inesperados frequentes

### 6. RECOMENDAÇÕES DE FEEDBACK

#### Para Alunos:
- Modelos de mensagens para alunos com possíveis acertos por chute
- Modelos de mensagens para alunos com erros inesperados

#### Para Professores:
- Identificação de itens problemáticos
- Áreas com alto índice de chute
- Recomendações pedagógicas

## FORMATO DE SAÍDA

Apresente os resultados em:
1. Tabelas markdown organizadas
2. Insights numerados e destacados
3. Exemplos específicos com IDs de alunos
4. Código Python reproduzível para cada análise

## ÁREAS E ESTADOS DISPONÍVEIS

Áreas: {LISTE_AS_AREAS: MT, LC, CH, CN}
Estados: {LISTE_OS_ESTADOS: PA, PR}
```

---

## Prompt Simplificado (Versão Curta)

```
Analise os dados TRI do modelo 3PL abaixo.

DADOS DE HABILIDADE (por aluno):
{COLE_DADOS_DE_HABILIDADE}

DADOS DE DIFICULDADE (por item):
{COLE_DADOS_DE_DIFICULDADE}

ANÁLISES SOLICITADAS:
1. Identifique alunos com habilidades extremas (mínimo, máximo, percentis)
2. Encontre acertos suspeitos por chute (θ < b-1 e acertou)
3. Encontre erros inesperados (θ > b+1 e errou)
4. Liste itens problemáticos (a<0 ou c>0.25)
5. Sugira feedback para alunos e professores

Use IDs específicos de alunos nos exemplos.
Mostre os cálculos usados.
Apresente em tabelas markdown.
```

---

## Exemplo de Dados para Teste

### Exemplo - Habilidades (primeiras 5 linhas)

```csv
"Q1","Q2","Q3","Q4","Q5","Q6",...,"habilidade","alunos_id_string"
0,1,1,0,0,0,...,-1.4406,"210057715141"
0,0,1,0,0,0,...,-1.3073,"210057638944"
0,0,1,0,0,0,...,-1.2987,"210056753271"
0,0,1,0,1,0,...,-1.2577,"210054579943"
```

### Exemplo - Dificuldades (primeiras 5 linhas)

```csv
"acerto_acaso_item","dificuldade_item","discriminacao_item","questao"
0.1781,2.4017,4.1924,1
0.2058,1.6354,2.1110,2
0.1040,2.1728,2.2668,3
0.1649,1.5906,1.1340,4
```

---

## Parâmetros Importantes

| Parâmetro | Descrição | Faixa Típica |
|-----------|-----------|--------------|
| θ (theta) | Habilidade do aluno | -3 a 3 (raramente ±5) |
| a | Discriminação do item | 0.5 a 2.5 (bom item) |
| b | Dificuldade do item | -2 a 2 (típico) |
| c | Chute | 0.0 a 0.25 (típico) |

### Critérios de Qualidade de Item

| Critério | Valor | Interpretação |
|----------|-------|---------------|
| a < 0 | Negativo | Item problemático - discrimina inversamente |
| a < 0.5 | Muito baixo | Item não diferencia bem os alunos |
| 0.5 ≤ a ≤ 2.5 | Adequado | Item de boa qualidade |
| a > 2.5 | Alto | Item muito discriminativo |
| c > 0.35 | Alto | Item muito favorável ao chute |

---

## Scripts Python Prontos para Uso

### Script 1: Carregar e Analisar Dados

```python
import pandas as pd
import numpy as np

# Parâmetros
AREA = 'MT'  # Altere para: MT, LC, CH, CN
ESTADO = 'PA'  # Altere para: PA, PR

# Carregar dados
df_hab = pd.read_csv(f'codigos_R/LTM_3PL/habilidades/habil_3PL_ltm_{AREA}_{ESTADO}.csv')
df_dif = pd.read_csv(f'codigos_R/LTM_3PL/dificuldades/dif_modelo_3PL_ltm_{AREA}_{ESTADO}.csv')

# Estatísticas básicas
print(f"Total de alunos: {len(df_hab)}")
print(f"Total de itens: {len(df_dif)}")
print(f"\nDistribuição de habilidades:")
print(df_hab['habilidade'].describe())

# Alunos extremos
print(f"\nAluno com MENOR habilidade:")
aluno_min = df_hab.loc[df_hab['habilidade'].idxmin()]
print(f"  ID: {aluno_min['alunos_id_string']}, θ: {aluno_min['habilidade']:.4f}")

print(f"\nAluno com MAIOR habilidade:")
aluno_max = df_hab.loc[df_hab['habilidade'].idxmax()]
print(f"  ID: {aluno_max['alunos_id_string']}, θ: {aluno_max['habilidade']:.4f}")
```

### Script 2: Encontrar Acertos por Chute

```python
def encontrar_acertos_chute(df_hab, df_dif, area, limiar_diferenca=1, limiar_chute=0.10):
    """
    Encontra acertos suspeitos por chute.
    """
    if area == 'MT':
        q_cols = [f'Q{i}' for i in range(1, 40)] + [f'Q{i}' for i in range(41, 46)]
    else:
        q_cols = [f'Q{i}' for i in range(1, 46)]
    
    resultados = []
    
    for _, aluno in df_hab.iterrows():
        theta = aluno['habilidade']
        
        for q in q_cols:
            if q in df_hab.columns and aluno[q] == 1:
                q_num = int(q.replace('Q', ''))
                item = df_dif[df_dif['questao'] == q_num]
                
                if len(item) > 0:
                    b = item['dificuldade_item'].values[0]
                    c = item['acerto_acaso_item'].values[0]
                    a = item['discriminacao_item'].values[0]
                    
                    if theta < (b - limiar_diferenca) and c > limiar_chute and a > 0:
                        resultados.append({
                            'aluno_id': aluno['alunos_id_string'],
                            'theta': theta,
                            'questao': q,
                            'dificuldade_b': b,
                            'chute_c': c,
                            'diferenca': b - theta
                        })
    
    return pd.DataFrame(resultados).sort_values('diferenca', ascending=False)

# Executar
resultado = encontrar_acertos_chute(df_hab, df_dif, AREA)
print(f"\nEncontrados {len(resultado)} acertos suspeitos")
print(resultado.head(10))
```

### Script 3: Encontrar Erros Inesperados

```python
def encontrar_erros_inesperados(df_hab, df_dif, area, limiar_diferenca=1):
    """
    Encontra erros inesperados (aluno deveria ter acertado).
    """
    if area == 'MT':
        q_cols = [f'Q{i}' for i in range(1, 40)] + [f'Q{i}' for i in range(41, 46)]
    else:
        q_cols = [f'Q{i}' for i in range(1, 46)]
    
    resultados = []
    
    for _, aluno in df_hab.iterrows():
        theta = aluno['habilidade']
        
        for q in q_cols:
            if q in df_hab.columns and aluno[q] == 0:
                q_num = int(q.replace('Q', ''))
                item = df_dif[df_dif['questao'] == q_num]
                
                if len(item) > 0:
                    b = item['dificuldade_item'].values[0]
                    a = item['discriminacao_item'].values[0]
                    
                    if theta > (b + limiar_diferenca) and a > 0:
                        resultados.append({
                            'aluno_id': aluno['alunos_id_string'],
                            'theta': theta,
                            'questao': q,
                            'dificuldade_b': b,
                            'diferenca': theta - b
                        })
    
    return pd.DataFrame(resultados).sort_values('diferenca', ascending=False)

# Executar
resultado = encontrar_erros_inesperados(df_hab, df_dif, AREA)
print(f"\nEncontrados {len(resultado)} erros inesperados")
print(resultado.head(10))
```

### Script 4: Analisar Itens Problemáticos

```python
def analisar_itens_problematicos(df_dif):
    """
    Identifica itens com parâmetros problemáticos.
    """
    problemas = []
    
    # Discriminação negativa
    neg = df_dif[df_dif['discriminacao_item'] < 0]
    for _, item in neg.iterrows():
        problemas.append({
            'questao': f"Q{int(item['questao'])}",
            'problema': 'Discriminação negativa',
            'valor': item['discriminacao_item']
        })
    
    # Discriminação muito baixa
    baixa = df_dif[(df_dif['discriminacao_item'] >= 0) & (df_dif['discriminacao_item'] < 0.5)]
    for _, item in baixa.iterrows():
        problemas.append({
            'questao': f"Q{int(item['questao'])}",
            'problema': 'Discriminação baixa',
            'valor': item['discriminacao_item']
        })
    
    # Chute alto
    chute_alto = df_dif[df_dif['acerto_acaso_item'] > 0.25]
    for _, item in chute_alto.iterrows():
        problemas.append({
            'questao': f"Q{int(item['questao'])}",
            'problema': 'Chute alto',
            'valor': item['acerto_acaso_item']
        })
    
    return pd.DataFrame(problemas)

# Executar
problemas = analisar_itens_problematicos(df_dif)
print(f"\nEncontrados {len(problemas)} itens problemáticos")
print(problemas)
```

---

## Checklist de Análise

- [ ] Dados carregados corretamente
- [ ] Estatísticas descritivas calculadas
- [ ] Alunos extremos identificados
- [ ] Acertos por chute encontrados
- [ ] Erros inesperados encontrados
- [ ] Itens problemáticos listados
- [ ] Comparação entre estados (se aplicável)
- [ ] Feedback para alunos elaborado
- [ ] Feedback para professores elaborado
- [ ] Código reproduzível documentado

---

*Prompt criado para facilitar análises TRI com qualquer agente de IA*
*Baseado no modelo 3PL aplicado aos dados do ENEM 2022*

import pandas as pd

INPUT_FILE = "template_prompt_aluno.txt"
OUTPUT_FILE = "prompt_aluno.txt"

def get_class_dif(area_conhecimento, estado, item):
  df = pd.read_csv(f"../normalized_data/dificuldades/dif_{area_conhecimento}_{estado}.csv")
  df = df[df["questao"] == item]
  return df["classificacao_dificuldade"].values[0]

def get_dificuldade_item(estado, area_conhecimento, item):
  df_dificuldade = pd.read_csv(f"../../codigos_R/LTM_3PL/dificuldades/dif_modelo_3PL_ltm_{area_conhecimento}_{estado}.csv")
  df_dificuldade = df_dificuldade[df_dificuldade["questao"] == item]
  
  chute = df_dificuldade["acerto_acaso_item"].values[0]
  chute = 100*chute
  dificuldade_item = df_dificuldade["dificuldade_item"].values[0]

  dificuldade_normalizada = dificuldade_item

  if dificuldade_item > 4:
    dificuldade_normalizada = 4.00
  elif dificuldade_item < -4:
    dificuldade_normalizada = -4.00
  
  dificuldade_normalizada = ((dificuldade_normalizada + 4)/8) * 800 + 200
  
  return round(chute, 2), round(dificuldade_normalizada, 2)

def get_habilidade_item(area, habilidade):
  matriz_hab = pd.read_csv("../../pre-processamento/microdados_enem_2022/DADOS/matriz_referencia_enem_habilidades_2019.csv")
  matriz_hab = matriz_hab[matriz_hab["SG_AREA"] == area]
  
  matriz_hab = matriz_hab[matriz_hab["CO_HABILIDADE"] == habilidade]
  
  hab_desc = matriz_hab["INF_HABILIDADE"].values[0]
  competencia = matriz_hab["CO_COMPETENCIA"].values[0]
  
  return hab_desc, competencia

def get_competencia(area, competencia):
  matriz_comp = pd.read_csv("../../pre-processamento/microdados_enem_2022/DADOS/matriz_referencia_enem_competencias_2019.csv")
  matriz_comp = matriz_comp[matriz_comp["SG_AREA"] == area]
  matriz_comp = matriz_comp[matriz_comp["CO_COMPETENCIA"] == competencia]
  
  comp_desc = matriz_comp["INF_COMPETENCIA"].values[0]
  
  return comp_desc

def get_question(area, item):
  prova_amarela = pd.read_csv(f'../../pre-processamento/Itens_provas_amarela/dt_itens_{area}_amarela.csv')
  prova_amarela = prova_amarela.drop(columns=["Unnamed: 0"])
  
  if area == "MT":
    questao = prova_amarela[prova_amarela["CO_POSICAO"] == item+135]
  elif area == "CN":
    questao = prova_amarela[prova_amarela["CO_POSICAO"] == item+90]
  elif area == "CH":
    questao = prova_amarela[prova_amarela["CO_POSICAO"] == item+45]
  elif area == "LC":
    questao = prova_amarela[prova_amarela["CO_POSICAO"] == item]
  else:
    return 0
  
  return questao

def get_question_information(area, item):
  questao = get_question(area, item)

  item_prova = questao["CO_POSICAO"].values[0]
  
  gabarito = questao["TX_GABARITO"].values[0]
  
  habilidade_item = questao["CO_HABILIDADE"].values[0]
  
  hab_desc, competencia = get_habilidade_item(area, habilidade_item)
  
  comp_desc = get_competencia(area, competencia)

  # Deixa apenas o texto da descrição da String
  item_comp_desc_partes = comp_desc.split()
  item_comp_desc_corrijido = ' '.join(item_comp_desc_partes[5:])

  # Deixa apenas o texto da descrição da String
  item_hab_desc_partes = hab_desc.split()
  item_hab_desc_corrijido = ' '.join(item_hab_desc_partes[2:])
  
  return gabarito, item_hab_desc_corrijido, item_comp_desc_corrijido, item_prova

def get_prob_acerto(area_conhecimento, estado, theta, item):
  df_probabilidade = pd.read_csv(f"../../codigos_R/LTM_3PL/probabilidades/df_prob_3PL_LTM_{area_conhecimento}_{estado}.csv")

  prob_acerto = df_probabilidade[round(df_probabilidade["theta"], 4) == theta]
  prob_acerto = prob_acerto[f'Item  {item}'].values[0]

  prob_acerto = round(100*prob_acerto, 2)
  
  return prob_acerto

def get_habilidade_aluno(matricula, questao, estado, area_conhecimento):
  df_habil_3PL = pd.read_csv(f"../../codigos_R/LTM_3PL/habilidades/habil_3PL_ltm_{area_conhecimento}_{estado}.csv")
  df_habil_3PL["alunos_id_string"] = df_habil_3PL["alunos_id_string"].astype(str)
  habil_examinando = df_habil_3PL[df_habil_3PL["alunos_id_string"] == matricula]
  
  acertou_questao = habil_examinando[f"Q{questao}"].values[0]

  habil_examinando = habil_examinando["habilidade"].values[0]
  if habil_examinando > 4:
    habil_examinando = 4.00
  elif habil_examinando < -4:
    habil_examinando = -4.00
  
  habil_examinando_normalizada = ((habil_examinando + 4)/8) * 800 + 200
  
  return round(habil_examinando, 4), round(habil_examinando_normalizada, 2), bool(acertou_questao)

def gera_prompt(mat, item, estado, area, cci_file):
  habilidade_aluno, habilidade_aluno_normalizada, acertou_questao = get_habilidade_aluno(mat, item, estado, area)
  prob_acerto = get_prob_acerto(area, estado, habilidade_aluno, item)
  gabarito, habilidade_exigida, competencia_exigida, item_prova = get_question_information(area, item)
  acerto_acaso, dificuldade_item = get_dificuldade_item(estado, area, item)
  classificacao_dificuldade = get_class_dif(area, estado, item)

  dados = {
    "matricula": mat,
    "item": item_prova,
    "habilidade_estimada": habilidade_aluno_normalizada,
    "probabilidade_acerto": prob_acerto,
    "gabarito": gabarito,
    "dificuldade_item": dificuldade_item,
    "classificacao_item": classificacao_dificuldade,
    "probabilidade_acerto_acaso": acerto_acaso,
    "acertou": acertou_questao,
    "competencia_exigida_item": competencia_exigida,
    "habilidade_exigida_item": habilidade_exigida,
    "cci_file": cci_file
  }

  with open(INPUT_FILE, "r", encoding="utf-8") as f:
        template = f.read()

  # substitui os valores no texto
  for key, value in dados.items():
      template = template.replace(f"%%{key}%%", str(value))

  # grava por cima do mesmo arquivo
  with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
      f.write(template)

  print("Arquivo atualizado com sucesso!")
  return dados


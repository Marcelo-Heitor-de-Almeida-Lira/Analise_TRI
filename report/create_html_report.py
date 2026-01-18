import re
import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from gera_cci import gera_cci_aluno_no_llm as gera_cci


def get_question(area, item):
  prova_amarela = pd.read_csv(f'../pre-processamento/Itens_provas_amarela/dt_itens_{area}_amarela.csv')
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

def get_habilidade_item(area, habilidade):
  matriz_hab = pd.read_csv("../pre-processamento/microdados_enem_2022/DADOS/matriz_referencia_enem_habilidades_2019.csv")
  matriz_hab = matriz_hab[matriz_hab["SG_AREA"] == area]
  
  matriz_hab = matriz_hab[matriz_hab["CO_HABILIDADE"] == habilidade]
  
  hab_desc = matriz_hab["INF_HABILIDADE"].values[0]
  competencia = matriz_hab["CO_COMPETENCIA"].values[0]
  
  return hab_desc, competencia

def get_competencia(area, competencia):
  matriz_comp = pd.read_csv("../pre-processamento/microdados_enem_2022/DADOS/matriz_referencia_enem_competencias_2019.csv")
  matriz_comp = matriz_comp[matriz_comp["SG_AREA"] == area]
  matriz_comp = matriz_comp[matriz_comp["CO_COMPETENCIA"] == competencia]
  
  comp_desc = matriz_comp["INF_COMPETENCIA"].values[0]
  
  return comp_desc

def get_question_information(area, item):
  questao = get_question(area, item)

  item_prova = questao["CO_POSICAO"].values[0]
  
  gabarito = questao["TX_GABARITO"].values[0]
  
  habilidade_item = questao["CO_HABILIDADE"].values[0]
  
  hab_desc, competencia = get_habilidade_item(area, habilidade_item)
  
  comp_desc = get_competencia(area, competencia)
  
  return gabarito, hab_desc, comp_desc, item_prova
  

def get_habilidade_aluno(matricula, estado, area_conhecimento, questao):
  df_habil_3PL = pd.read_csv(f"../codigos_R/LTM_3PL/habilidades/habil_3PL_ltm_{area_conhecimento}_{estado}.csv")
  df_habil_3PL["alunos_id_string"] = df_habil_3PL["alunos_id_string"].astype(str)
  examinando = df_habil_3PL[df_habil_3PL["alunos_id_string"] == matricula]
  habilidade_examinando = examinando["habilidade"].values[0]
  
  acertou_questao = examinando[f"Q{questao}"].values[0]

  df_normalizado = pd.read_csv(f"normalized_data/habilidades/habil_{area_conhecimento}_{estado}.csv")
  df_normalizado["alunos_id_string"] = df_normalizado["alunos_id_string"].astype(str)
  df_normalizado = df_normalizado[df_normalizado["alunos_id_string"] == matricula]

  habilidade_normalizada = df_normalizado["habilidade_normalizada"].values[0]

  if habilidade_normalizada > 1000:
    habilidade_normalizada = 1000
  elif habilidade_normalizada < 200:
    habilidade_normalizada = 200
  
  return habilidade_examinando, habilidade_normalizada, acertou_questao

def get_dificuldade_item(estado, area_conhecimento, item):
  df_dificuldade = pd.read_csv(f"normalized_data/dificuldades/dif_{area_conhecimento}_{estado}.csv")
  df_dificuldade = df_dificuldade[df_dificuldade["questao"] == item]
  
  chute = df_dificuldade["acerto_acaso_item"].values[0]
  dificuldade = df_dificuldade["dificuldade_item_normalizado"].values[0]
  discriminacao = df_dificuldade["discriminacao_item"].values[0]
  classificacao_dificuldade = df_dificuldade["classificacao_dificuldade"].values[0]

  if dificuldade > 1000:
    dificuldade = 1000
  elif dificuldade < 200:
    dificuldade = 200
  
  return chute, dificuldade, discriminacao, classificacao_dificuldade

def get_prob_acerto(area_conhecimento, estado, theta, item):
  df_probabilidade = pd.read_csv(f"../codigos_R/LTM_3PL/probabilidades/df_prob_3PL_LTM_{area_conhecimento}_{estado}.csv")
  prob_acerto = df_probabilidade[round(df_probabilidade["theta"], 4) == theta]
  prob_acerto = prob_acerto[f'Item  {item}'].values[0]
  
  return prob_acerto
  
  
def get_report_informations(matricula, questao, area_conhecimento, estado):
  gabarito, item_hab_desc, item_comp_desc, item_prova = get_question_information(area_conhecimento, questao)

  habilidade_examinando, habilidade_normalizada, acertou_questao = get_habilidade_aluno(matricula, estado, area_conhecimento, questao)
  habilidade_examinando = round(habilidade_examinando, 4)

  acerto_acaso_item, dificuldade_item, discriminacao_item, classificacao_dificuldade = get_dificuldade_item(estado, area_conhecimento, questao)

  prob_acerto = get_prob_acerto(area_conhecimento, estado, habilidade_examinando, questao)
  
  return gabarito, item_hab_desc, item_comp_desc, item_prova, habilidade_normalizada, acerto_acaso_item, dificuldade_item, discriminacao_item, classificacao_dificuldade, prob_acerto, acertou_questao

def calculate_feedback(habilidade, item_hab_desc_corrijido, dificuldade, acerto_acaso, acertou, prob_acerto):
  if habilidade < dificuldade and acertou:
      feedback = (
          f"Você acertou uma questão acima do seu nível atual (habilidade = {habilidade}, dificuldade = {dificuldade}). "
          f"Isso pode indicar um bom raciocínio pontual ou sorte. Vale a pena revisar esse conteúdo ({item_hab_desc_corrijido}) para consolidar o conhecimento."
      )
  elif abs(habilidade - dificuldade) <= 0.3 and acertou:
      feedback = (
          f"Você acertou uma questão compatível com seu nível (habilidade = {habilidade}, dificuldade = {dificuldade}). "
          "Isso mostra domínio consistente sobre o conteúdo."
      )
  elif habilidade > dificuldade and acertou:
      feedback = (
          f"Você acertou uma questão mais fácil para o seu nível (habilidade = {habilidade}, dificuldade = {dificuldade}). "
          "Esse conteúdo está bem consolidado para você."
      )
  elif habilidade > dificuldade and not acertou:
      feedback = (
          f"Você errou uma questão que, em média, está abaixo do seu nível (habilidade = {habilidade}, dificuldade = {dificuldade}). "
          f"Talvez tenha sido um erro de atenção ou falta de revisão. Vale a pena revisar o tema ({item_hab_desc_corrijido})."
      )
  elif habilidade < dificuldade and not acertou:
      feedback = (
          f"Essa questão estava acima do seu nível atual (habilidade = {habilidade}, dificuldade = {dificuldade}). "
          f"É natural ter dificuldade aqui. Reforçar o conteúdo ({item_hab_desc_corrijido}) pode ajudar você a avançar."
      )

  # Análise do chute
  if acertou and prob_acerto - acerto_acaso < 0.15:
      feedback += f" A chance de ter acertado por sorte é significativa (probabilidade de acerto do aluno = {(prob_acerto*100):.2f}%, probabilidade de acerto por chute da questão = {(acerto_acaso*100):.2f}%). Considere revisar esse tópico para garantir o entendimento."
    
  return feedback

def get_area_nome(area):
  if area == "CN":
    area_conhecimento = "Ciências da Natureza e suas Tecnologias"
  elif area == "CH":
    area_conhecimento = "Ciências Humanas e suas Tecnologias"
  elif area == "MT":
    area_conhecimento = "Matemática e suas Tecnologias"
  elif area == "LC":
    area_conhecimento = "Linguagens, Códigos e suas Tecnologias"
  
  return area_conhecimento

def create_html_report(matricula, area_conhecimento, estado, questao, gabarito, item_hab_desc, item_comp_desc, item_prova, habil_examinando, acerto_acaso_item, dificuldade_item, class_dificuldade, prob_acerto, acertou_questao, feedback):
  TEMPLATE_FILE = "report_aluno_template_teste.txt"
  OUTPUT_FILE = f"report_html_no_llm/exemplo_{matricula}_{estado}_{area_conhecimento}_{questao}.html"

  if acertou_questao == 1:
    acertou_questao = "acertou"
  else:
    acertou_questao = "errou"
  
  area_nome = get_area_nome(area_conhecimento)

  cci_file = gera_cci(matricula, questao, area_conhecimento, estado)

  dados = {
    "matricula": matricula,
    "area_conhecimento": area_nome,
    "item": item_prova,
    "habilidade_aluno": habil_examinando,
    "probabilidade_acerto": round(100*prob_acerto, 2),
    "gabarito": gabarito,
    "dificuldade_item": dificuldade_item,
    "classificacao_item": class_dificuldade,
    "chute": round(acerto_acaso_item*100, 2),
    "acertou_errou": acertou_questao,
    "competencia_questao": item_comp_desc,
    "habilidade_questao": item_hab_desc,
    "feedback": feedback,
    "cci_file": cci_file
  }
  with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
    template = f.read()
  
  for key, value in dados.items():
    template = template.replace(f"%%{key}%%", str(value))
  
  with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(template)

  print(f"Report gerado e salvo em {OUTPUT_FILE}")
  return


# Transforma reports pdf em html - não mais necessário
def iterar_pasta():
  padrao = re.compile(r"report_(\d+)_(\w{2})_(\w{2})_(\d+)\.pdf$")
  PASTA = "report_html_no_llm"

  for name in os.listdir(PASTA):
    match = padrao.match(name)

    if match:
      matricula, estado, area_conhecimento, questao = match.groups()

      questao = int(questao)

      gabarito, item_hab_desc, item_comp_desc, item_prova, habil_examinando, acerto_acaso_item, dificuldade_item, discriminacao_item, class_dificuldade, prob_acerto, acertou_questao = get_report_informations(matricula, questao, area_conhecimento, estado)
      # Deixa apenas o texto da descrição da String
      item_comp_desc_partes = item_comp_desc.split()
      item_comp_desc_corrijido = ' '.join(item_comp_desc_partes[5:])

      # Deixa apenas o texto da descrição da String
      item_hab_desc_partes = item_hab_desc.split()
      item_hab_desc_corrijido = ' '.join(item_hab_desc_partes[2:])

      habil_examinando = round(habil_examinando, 2)
      dificuldade_item = round(dificuldade_item, 2)
      acerto_acaso_item = round(acerto_acaso_item, 4)
      prob_acerto = round(prob_acerto, 4)

      feedback = calculate_feedback(habil_examinando, item_hab_desc_corrijido, dificuldade_item, acerto_acaso_item, acertou_questao, prob_acerto)

      create_html_report(matricula, area_conhecimento, estado, questao, gabarito, item_hab_desc_corrijido, item_comp_desc_corrijido, item_prova, habil_examinando, acerto_acaso_item, dificuldade_item, class_dificuldade, prob_acerto, acertou_questao, feedback)
      print(f"Report html criado para {matricula} na questão {questao}")


def generate_report(matricula, estado, area_conhecimento, questao):
  TEMPLATE_FILE = "report_aluno_template.txt"
  OUTPUT_FILE = f"report_html_no_llm/report_{matricula}_{estado}_{area_conhecimento}_{questao}.html"


  gabarito, item_hab_desc, item_comp_desc, item_prova, habil_examinando, acerto_acaso_item, dificuldade_item, discriminacao_item, class_dificuldade, prob_acerto, acertou_questao = get_report_informations(matricula, questao, area_conhecimento, estado)

  # Deixa apenas o texto da descrição da String
  item_comp_desc_partes = item_comp_desc.split()
  item_comp_desc_corrijido = ' '.join(item_comp_desc_partes[5:])

  # Deixa apenas o texto da descrição da String
  item_hab_desc_partes = item_hab_desc.split()
  item_hab_desc_corrijido = ' '.join(item_hab_desc_partes[2:])

  habil_examinando = round(habil_examinando, 2)
  dificuldade_item = round(dificuldade_item, 2)
  acerto_acaso_item = round(acerto_acaso_item, 4)
  prob_acerto = round(prob_acerto, 4)

  feedback = calculate_feedback(habil_examinando, item_hab_desc_corrijido, dificuldade_item, acerto_acaso_item, acertou_questao, prob_acerto)

  create_html_report(matricula, area_conhecimento, estado, questao, gabarito, item_hab_desc_corrijido, item_comp_desc_corrijido, item_prova, habil_examinando, acerto_acaso_item, dificuldade_item, class_dificuldade, prob_acerto, acertou_questao, feedback)


def gerar_artefatos():
  # Multiplas instâncias de uma vez
  dados = [
    {"mat": "210055059725", "item": 5, "area": "CH", "estado": "PA"},
    {"mat": "210055059725", "item": 6, "area": "CH", "estado": "PA"},
    {"mat": "210054537519", "item": 5, "area": "CH", "estado": "PA"},
    {"mat": "210054537519", "item": 6, "area": "CH", "estado": "PA"},
    {"mat": "210055516398", "item": 5, "area": "CH", "estado": "PR"},
    {"mat": "210055516398", "item": 6, "area": "CH", "estado": "PR"},
    {"mat": "210055486785", "item": 5, "area": "CH", "estado": "PR"},
    {"mat": "210055486785", "item": 6, "area": "CH", "estado": "PR"},
    {"mat": "210054915349", "item": 37, "area": "CN", "estado": "PA"},
    {"mat": "210054915349", "item": 25, "area": "CN", "estado": "PA"},
    {"mat": "210054559551", "item": 37, "area": "CN", "estado": "PA"},
    {"mat": "210054559551", "item": 25, "area": "CN", "estado": "PA"},
    {"mat": "210055416405", "item": 37, "area": "CN", "estado": "PR"},
    {"mat": "210055416405", "item": 25, "area": "CN", "estado": "PR"},
    {"mat": "210057569637", "item": 37, "area": "CN", "estado": "PR"},
    {"mat": "210057569637", "item": 25, "area": "CN", "estado": "PR"},
    {"mat": "210054579873", "item": 32, "area": "LC", "estado": "PA"},
    {"mat": "210054579873", "item": 24, "area": "LC", "estado": "PA"},
    {"mat": "210054688006", "item": 32, "area": "LC", "estado": "PA"},
    {"mat": "210054688006", "item": 24, "area": "LC", "estado": "PA"},
    {"mat": "210057347558", "item": 32, "area": "LC", "estado": "PR"},
    {"mat": "210057347558", "item": 24, "area": "LC", "estado": "PR"},
    {"mat": "210055278838", "item": 32, "area": "LC", "estado": "PR"},
    {"mat": "210055278838", "item": 24, "area": "LC", "estado": "PR"},
    {"mat": "210056753271", "item": 9, "area": "MT", "estado": "PA"},
    {"mat": "210056753271", "item": 32, "area": "MT", "estado": "PA"},
    {"mat": "210054559551", "item": 9, "area": "MT", "estado": "PA"},
    {"mat": "210054559551", "item": 32, "area": "MT", "estado": "PA"},
    {"mat": "210057287122", "item": 9, "area": "MT", "estado": "PR"},
    {"mat": "210057287122", "item": 32, "area": "MT", "estado": "PR"},
    {"mat": "210056864119", "item": 9, "area": "MT", "estado": "PR"},
    {"mat": "210056864119", "item": 32, "area": "MT", "estado": "PR"},
  ]

  for dado in dados:
    generate_report(dado["mat"], dado["estado"], dado["area"], dado["item"])
    print(f"Report gerado para {dado['mat']} do estado de {dado['estado']} na área {dado['area']}, item {dado['item']}")
    print("-------------------------------------------------------------------\n")

def main():
  aluno_id = str(input("Digite o id do aluno: "))
  estado = str(input("Digite o estado (PA/PR): "))
  area = str(input("Digite a área de conhecimento (MT/CN/CH/LC): "))
  item = int(input("Digite o número da questão: "))

  generate_report(aluno_id, estado, area, item)
  print(f"Report gerado para {aluno_id} do estado de {estado} na área {area}, item {item}")
  

if __name__ == '__main__':
  main()

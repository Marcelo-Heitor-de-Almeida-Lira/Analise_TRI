# Vou precisar de:
# Matricula - Errou a questao? - Alternativa correta - Habilidade latente
# Questao - Eixo/area abordada.?

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm

def scatter_plot(df, item, aluno, habilidade, dificuldade, examinando="", titulo=""):
    coluna_y = item
    
    scatter = go.Figure()

    if area_conhecimento == "MT" and item > 40:
      scatter.add_trace(go.Scatter(
          x=df['theta'],
          y=df[f"Item  {coluna_y}"],
          name=df.columns[coluna_y-1],
          mode='lines'
      ))
    else:
      scatter.add_trace(go.Scatter(
          x=df['theta'],
          y=df[f"Item  {coluna_y}"],
          name=df.columns[coluna_y],
          mode='lines'
      ))

    # Layout do gráfico
    scatter.update_layout(
        title=titulo,
        xaxis=dict(
            title='Habilidade θ',
            zeroline=False
        ),
        yaxis=dict(
            title='Probabilidade P(θ)',
            zeroline=False
        )
    )

    # Anotação
    scatter.add_annotation(
        x=aluno['theta'],
        y=aluno['probabilidade'],
        text=f"{examinando}<br>Habilidade (θ): {np.round(aluno['theta'], 2)} ({habilidade:.2f})"
             f"<br>Discriminação do Item: {np.round(aluno['discriminacao'], 2)}"
             f"<br>Dificuldade do Item: {np.round(aluno['dificuldade'], 2)} ({dificuldade:.2f})"
             f"<br>Probabilidade de chute: {np.round(aluno['prob_chute'] * 100, 2)}%"
             f"<br>Probabilidade P(θ): {np.round(aluno['probabilidade'] * 100, 2)}%",
        showarrow=True,
        arrowhead=7,
        arrowwidth=2,
        ax=aluno['theta'] - 100,
        ay=-100,
        arrowcolor="#636363",
        bordercolor="#c7c7c7",
        bgcolor="#2CA02C",
        font=dict(color="white")
    )
    
    return scatter

def get_class_dif(area_conhecimento, estado, item):
  df = pd.read_csv(f"normalized_data/dificuldades/dif_{area_conhecimento}_{estado}.csv")
  df = df[df["questao"] == item]
  return df["classificacao_dificuldade"].values[0]


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
  habil_examinando = df_habil_3PL[df_habil_3PL["alunos_id_string"] == matricula]
  
  acertou_questao = habil_examinando[f"Q{questao}"].values[0]
  
  return habil_examinando, acertou_questao

def get_dificuldade_item(estado, area_conhecimento, item):
  df_dificuldade = pd.read_csv(f"../codigos_R/LTM_3PL/dificuldades/dif_modelo_3PL_ltm_{area_conhecimento}_{estado}.csv")
  df_dificuldade = df_dificuldade[df_dificuldade["questao"] == item]
  
  chute = df_dificuldade["acerto_acaso_item"].values[0]
  dificuldade = df_dificuldade["dificuldade_item"].values[0]
  discriminacao = df_dificuldade["discriminacao_item"].values[0]
  
  return chute, dificuldade, discriminacao

def get_prob_acerto(area_conhecimento, estado, theta, item):
  df_probabilidade = pd.read_csv(f"../codigos_R/LTM_3PL/probabilidades/df_prob_3PL_LTM_{area_conhecimento}_{estado}.csv")
  
  return df_probabilidade
  
  
def get_report_informations(matricula, questao, area_conhecimento, estado):
  gabarito, item_hab_desc, item_comp_desc, item_prova = get_question_information(area_conhecimento, questao)

  habil_examinando, acertou_questao = get_habilidade_aluno(matricula, estado, area_conhecimento, questao)
  habil_examinando = habil_examinando["habilidade"].values[0]
  if habil_examinando > 4:
    habil_examinando = 4.00
  elif habil_examinando < -4:
    habil_examinando = -4.00
  
  habil_examinando_normalizada = ((habil_examinando + 4)/8) * 800 + 200
  habil_examinando = round(habil_examinando, 4)

  acerto_acaso_item, dificuldade_item, discriminacao_item = get_dificuldade_item(estado, area_conhecimento, questao)
  
  dificuldade_normalizada = dificuldade_item

  if dificuldade_item > 4:
    dificuldade_normalizada = 4.00
  elif dificuldade_item < -4:
    dificuldade_normalizada = -4.00
  
  dificuldade_normalizada = ((dificuldade_normalizada + 4)/8) * 800 + 200

  df_probabilidade = get_prob_acerto(area_conhecimento, estado, habil_examinando, questao)

  prob_acerto = df_probabilidade[round(df_probabilidade["theta"], 4) == habil_examinando]
  prob_acerto = prob_acerto[f'Item  {questao}'].values[0]

  dados_examinando = {
    "theta": habil_examinando,
    "probabilidade": prob_acerto,
    "prob_chute": acerto_acaso_item,
    "discriminacao": discriminacao_item,
    "dificuldade": dificuldade_item
  }


  cci = scatter_plot(df_probabilidade, questao, dados_examinando, habil_examinando_normalizada, dificuldade_normalizada, f"Examinando {matricula}", f"CCI para o item {questao} da prova de {area_conhecimento}")

  cci.write_image(f"plots/plot_{matricula}_{estado}_{area_conhecimento}_{questao}.png")
  
  return gabarito, item_hab_desc, item_comp_desc, item_prova, habil_examinando_normalizada, acerto_acaso_item, dificuldade_normalizada, discriminacao_item, prob_acerto, acertou_questao

def calculate_feedback(habilidade, dificuldade, acerto_acaso, acertou, prob_acerto):
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
      feedback += f" A chance de ter acertado por sorte é significativa (probabilidade de chute = {(prob_acerto*100):.2f}%, chute = {(acerto_acaso*100):.2f}%). Considere revisar esse tópico para garantir o entendimento."
    
  return feedback

def create_pdf_report(gabarito, item_hab_desc, item_comp_desc, item_prova, habil_examinando, acerto_acaso_item, dificuldade_item, class_dificuldade, discriminacao_item, prob_acerto, acertou_questao, feedback):
  doc = SimpleDocTemplate(f"report_pdf/report_{matricula}_{estado}_{area_conhecimento}_{questao}.pdf", pagesize=A4)
  styles = getSampleStyleSheet()

  title = styles["Heading1"]
  title.alignment = 1

  header = styles["Heading3"]
  header.alignment = 0

  text = styles["Bullet"]
  text.alignment = 4

  conteudo = []

  conteudo.append(Paragraph("Relatório de Análise pós-prova do ENEM", title))
  conteudo.append(Spacer(1, 12))
  
  conteudo.append(Paragraph(f"Matricula do examinando: {matricula}", header))
  conteudo.append(Spacer(1, 12))

  conteudo.append(Paragraph(f"O examinando teve habilidade estimada {round(habil_examinando, 2)}, de uma escala de 200 a 1.000", text))
  conteudo.append(Spacer(1, 12))

  conteudo.append(Paragraph(f"O examinando tinha uma probabilidade de acerto estimada em {round(prob_acerto*100, 2)}%", text))
  conteudo.append(Spacer(1, 12))

  conteudo.append(Paragraph(f"Item avaliado: {item_prova}", header))
  conteudo.append(Spacer(1, 12))
  
  conteudo.append(Paragraph(f"Gabarito do item: {gabarito}", text))
  conteudo.append(Spacer(1, 12))

  conteudo.append(Paragraph(f"Dificuldade estimada: {round(dificuldade_item, 4)} (200 - 1.000). É considerada uma questão {class_dificuldade}", text))
  conteudo.append(Spacer(1, 12))

  conteudo.append(Paragraph(f"Probabilidade de chute: {round(acerto_acaso_item*100, 2)}%", text))
  conteudo.append(Spacer(1, 12))

  if acertou_questao:
    conteudo.append(Paragraph("O examinando acertou a questão", text))
    conteudo.append(Spacer(1, 12))
  else:
    conteudo.append(Paragraph("O examinando errou a questão", text))
    conteudo.append(Spacer(1, 12))

  conteudo.append(Paragraph(f"Competência exigida: {item_comp_desc}", text))
  conteudo.append(Spacer(1, 12))

  conteudo.append(Paragraph(f"Habilidade exigida: {item_hab_desc}", text))
  conteudo.append(Spacer(1, 20))

  conteudo.append(Paragraph("Feedback", header))
  conteudo.append(Spacer(1, 12))

  conteudo.append(Paragraph(feedback, text))
  conteudo.append(Spacer(1, 12))

  img = Image(f"plots/plot_{matricula}_{estado}_{area_conhecimento}_{questao}.png", width=20*cm, height=14*cm)
  img.hAlign = 'CENTER'

  conteudo.append(img)

  doc.build(conteudo)
  
  

matricula = "210054695880"
questao = 7
area_conhecimento = "MT"
estado = "PA"


gabarito, item_hab_desc, item_comp_desc, item_prova, habil_examinando, acerto_acaso_item, dificuldade_item, discriminacao_item, prob_acerto, acertou_questao = get_report_informations(matricula, questao, area_conhecimento, estado)

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

class_dificuldade = get_class_dif(area_conhecimento, estado, questao)

feedback = calculate_feedback(habil_examinando, dificuldade_item, acerto_acaso_item, acertou_questao, prob_acerto)

create_pdf_report(gabarito, item_hab_desc_corrijido, item_comp_desc_corrijido, item_prova, habil_examinando, acerto_acaso_item, dificuldade_item, class_dificuldade, discriminacao_item, prob_acerto, acertou_questao, feedback)

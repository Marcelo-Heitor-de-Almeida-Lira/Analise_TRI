import pandas as pd
import numpy as np
import gera_cci
from gera_prompt_prof import gera_prompt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from ollama import chat
from ollama import ChatResponse


prompt_file = "prompt_prof.txt"
report_output_file_html = "report_examples/report_professor_v9.html"
report_raw_output = "report_examples/report_raw_professor_9.txt"

def create_bar_chart(distribuicao_marcacoes):
  # Dados fornecidos
  dados = {
      "Alternativa": ["A", "B", "C", "D", "E"],
      "Percentual": distribuicao_marcacoes
  }

  df = pd.DataFrame(dados)

  # Criar gráfico de barras
  fig = px.bar(
      df,
      x="Alternativa",
      y="Percentual",
      text="Percentual",
      title="Distribuição de Marcações por Alternativa",
  )

  # Ajustar exibição do texto e layout
  fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
  fig.update_layout(yaxis_title="Percentual (%)", xaxis_title="Alternativas")

  chart_html = fig.to_html(include_plotlyjs="cdn", full_html=False)

  with open("dist_respostas.html", "w", encoding="utf-8") as f:
      f.write(chart_html)


def grafico_acertos_alunos(estatistica_acertos):
    # Estrutura dos dados
    data = {
        "Categoria": [
            "Acertos (acima da dificuldade)",
            "Erros (acima da dificuldade)",
            "Acertos (abaixo da dificuldade)",
            "Erros (abaixo da dificuldade)"
        ],
        "Grupo": [
            "Acima da dificuldade",
            "Acima da dificuldade",
            "Abaixo da dificuldade",
            "Abaixo da dificuldade"
        ],
        "Percentual": estatistica_acertos
    }

    df = pd.DataFrame(data)

    colors = {
        "Acertos (acima da dificuldade)": "#2ecc71",
        "Erros (acima da dificuldade)": "#e74c3c",
        "Acertos (abaixo da dificuldade)": "#2ecc71",
        "Erros (abaixo da dificuldade)": "#e74c3c"
    }


    fig = make_subplots(
        rows=1,
        cols=2,
        specs=[
            [{"type": "domain"}, {"type": "domain"}]
        ],
        subplot_titles=["Alunos mais Habilidosos", "Alunos menos Habilidosos"]
    )

    # Pie chart para "Acima da dificuldade"
    acima = df[df["Grupo"] == "Acima da dificuldade"]
    fig.add_trace(
        go.Pie(
            labels=acima["Categoria"],
            values=acima["Percentual"],
            marker_colors=[colors[c] for c in acima["Categoria"]],
            textinfo='percent'
        ),
        row=1, col=1
    )

    # Pie chart para "Abaixo da dificuldade"
    abaixo = df[df["Grupo"] == "Abaixo da dificuldade"]
    fig.add_trace(
        go.Pie(
            labels=abaixo["Categoria"],
            values=abaixo["Percentual"],
            marker_colors=[colors[c] for c in abaixo["Categoria"]],
            textinfo='percent'
        ),
        row=1, col=2
    )

    fig.update_layout(
        title_text="Distribuição de acertos e erros pelo nível de habilidade",
        title_x=0.5
    )

    # Salvar HTML
    chart_html = fig.to_html(include_plotlyjs="cdn", full_html=False)
    with open("acertos_por_habilidade.html", "w", encoding="utf-8") as f:
        f.write(chart_html)



def gera_relatorio_deepseek():
    with open(prompt_file, "r", encoding="utf-8") as file:
        prompt = file.read()

    response: ChatResponse = chat(
        model="deepseek-r1:14b", 
        messages = [{'role': 'user', 'content': prompt}],
    )

    report_txt = response['message']['content']

    with open(report_raw_output, "w", encoding="utf-8") as f:
        f.write(report_txt)
    
    print("Report gerado e salvo em ", report_raw_output)

    report_html = report_txt.split("===INICIO_HTML===")[1].split("===FIM_HTML===")[0].strip()

    with open(report_output_file_html, "w", encoding="utf-8") as f:
        f.write(report_html)


ITEM = 29
AREA_CONHECIMENTO = "MT"
ESTADO = "PR"

item_data = gera_prompt(AREA_CONHECIMENTO, ESTADO, ITEM)
print("Novo prompt gerado")
print("Dados da questão recolhidos")

alternativas = ['a', 'b', 'c', 'd', 'e']
classes_alunos = ["acertos_acima", "erros_acima", "acertos_abaixo", "erros_abaixo"]

distribuicao_marcacoes = [item_data[key] for key in alternativas]
estatistica_acertos = [item_data[key] for key in classes_alunos]

total_acertos = item_data["acertos_acima"] + item_data["acertos_abaixo"]
total_erros = item_data["erros_acima"] + item_data["erros_abaixo"]

total_acertos_percent = 100*(total_acertos/item_data["total_respostas"])
total_erros_percent = 100*(total_erros/item_data["total_respostas"])

create_bar_chart(distribuicao_marcacoes)
print("Bar chart created")
grafico_acertos_alunos(estatistica_acertos)
print("Plot de acertos por habilidade criado")
gera_cci.gera_cci_prof(ITEM, AREA_CONHECIMENTO, ESTADO)
print("CCI gerada")
gera_relatorio_deepseek()
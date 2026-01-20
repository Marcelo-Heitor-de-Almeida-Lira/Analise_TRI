import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, PageBreak, Spacer, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib import colors


def theta_to_enem(habilidade_tri):
   habilidade_enem = ((habilidade_tri + 4) / 8) * 800 + 200
   return habilidade_enem

def gera_scatter(df, vetor_itens, titulo, area_conhecimento):
    fig = go.Figure()

    habilidade_enem = theta_to_enem(df['theta'])

    # Adiciona o primeiro item
    fig.add_trace(go.Scatter(
        x=habilidade_enem,
        y=df.iloc[:, vetor_itens[0]],
        name=df.columns[vetor_itens[0]],
        mode='lines'
    ))

    # Adiciona os demais itens
    for i in range(1, len(vetor_itens)):
        # No DataFrame de Matematica, a questao 40 foi excluida, tornando necessario ajuste de indices
        if area_conhecimento == "MT" and vetor_itens[i] > 40:    
            fig.add_trace(go.Scatter(
                x=habilidade_enem,
                y=df.iloc[:, vetor_itens[i]-1],
                name=df.columns[vetor_itens[i]-1],
                mode='lines'
            ))
        else:
            fig.add_trace(go.Scatter(
                x=habilidade_enem,
                y=df.iloc[:, vetor_itens[i]],
                name=df.columns[vetor_itens[i]],
                mode='lines'
            ))

    # Layout
    fig.update_layout(
        title=titulo,
        xaxis=dict(title='Habilidade θ', range=[200, 1000], zeroline=False),
        yaxis=dict(title='Probabilidade P(θ)', range=[0, 1.0], zeroline=False)
    )

    return fig


def get_items(area_conhecimento, estado):
    df = pd.read_csv(f"../codigos_R/LTM_3PL/dificuldades/dif_modelo_3PL_ltm_{area_conhecimento}_{estado}.csv")

    df = df.sort_values(by="dificuldade_item")
    
    items = df["questao"].values[:]

    selected_items = items[[5, 6, int((items.size/2)-1), int(items.size/2), items.size-7, items.size-6]]

    print(f"{estado} - {area_conhecimento}: {selected_items}")

    return selected_items


def create_histograms(estado, area_conhecimento):
    df_pa = pd.read_csv(f"normalized_data/habilidades/habil_{area_conhecimento}_PA.csv")
    df_pr = pd.read_csv(f"normalized_data/habilidades/habil_{area_conhecimento}_PR.csv")

    # Improved Histogram with clear labels including area: Ciências da Natureza
    plt.figure(figsize=(10,6))

    bins = np.linspace(
        min(df_pa["habilidade_normalizada"].min(), df_pr["habilidade_normalizada"].min()),
        max(df_pa["habilidade_normalizada"].max(), df_pr["habilidade_normalizada"].max()),
        45
    )

    plt.hist(df_pr['habilidade_normalizada'], bins=bins, alpha=0.6, label='PR', color='#4A90E2', edgecolor='black')
    plt.hist(df_pa['habilidade_normalizada'], bins=bins, alpha=0.6, label='PA', color='#F5A623', edgecolor='black')

    plt.xlabel(f'Habilidade normalizada (escala ENEM) — {area_conhecimento}')
    plt.ylabel('Frequência de estudantes')
    plt.title(f'Histograma das Habilidades em {area_conhecimento} — PA vs PR')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    hist_path = f"plots/histograma_habilidades_{area_conhecimento}.png"
    plt.savefig(hist_path, dpi=300, bbox_inches='tight')
    print(f"Histograma saalvo em {hist_path}")
    plt.close()

def create_boxplot(area_conhecimento):
    pa = pd.read_csv(f"normalized_data/habilidades/habil_{area_conhecimento}_PA.csv")
    pr = pd.read_csv(f"normalized_data/habilidades/habil_{area_conhecimento}_PR.csv")

    # Improved Boxplot with proper Y label
    plt.figure(figsize=(8,6))

    data = [pa['habilidade_normalizada'], pr['habilidade_normalizada']]
    labels = ['PA', 'PR']

    box = plt.boxplot(data, labels=labels, patch_artist=True)

    colors = ['#F5A623', '#4A90E2']
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)

    plt.ylabel('Habilidade normalizada (escala ENEM) — Ciências da Natureza')
    plt.title('Boxplot das Habilidades em Ciências da Natureza — PA vs PR')
    plt.grid(True, linestyle='--', alpha=0.5)

    box_path = f"plots/boxplot_habilidades_{area_conhecimento}.png"
    plt.savefig(box_path, dpi=300, bbox_inches='tight')
    plt.close()


def create_plots(areas_conhecimento, estados):
    for area_conhecimento in areas_conhecimento:
        for estado in estados:
            cci_file = f'plots/cci_{area_conhecimento}_{estado}_prof.png'
            create_histograms(estado, area_conhecimento)
            create_boxplot(area_conhecimento)
            df = pd.read_csv(f'../codigos_R/LTM_3PL/probabilidades/df_prob_3PL_LTM_{area_conhecimento}_{estado}.csv')

            items = get_items(area_conhecimento, estado)

            if area_conhecimento == "MT" and estado == "PR":
                title = "CCI de Matemática e suas Tecnologias do estado do Paraná"
            elif area_conhecimento == "MT" and estado == "PA":
                title = "CCI de Matemática e suas Tecnologias do estado do Pará"
            elif area_conhecimento == "CH" and estado == "PR":
                title = "CCI de Ciências Humanas e suas Tecnologias do estado do Paraná"
            elif area_conhecimento == "CH" and estado == "PA":
                title = "CCI de Ciências Humanas e suas Tecnologias do estado do Pará"
            elif area_conhecimento == "CN" and estado == "PR":
                title = "CCI de Ciências da Natureza e suas Tecnologias do estado do Paraná"
            elif area_conhecimento == "CN" and estado == "PA":
                title = "CCI de Ciências da Natureza e suas Tecnologias do estado do Pará"
            elif area_conhecimento == "LC" and estado == "PR":
                title = "CCI de Linguagens e Códigos e suas Tecnologias do estado do Paraná"
            elif area_conhecimento == "LC" and estado == "PA":
                title = "CCI de Linguagens e Códigos e suas Tecnologias do estado do Pará"

            cci = gera_scatter(df, items, title, area_conhecimento)

            cci.write_image(cci_file)



def get_num_erros(area_conhecimento, estado, questao):
    df = pd.read_csv(f"../pre-processamento/matrizes_binarias/MATRIZ_{area_conhecimento}_BINARIA_{estado}_amarela.csv")
    df = df.drop(columns=["Unnamed: 0"])

    soma_acertos = df[f"Q{questao}"].sum()

    total_alunos = df.shape[0]

    total_acertos_percent = (soma_acertos/total_alunos)*100
    
    return soma_acertos, total_acertos_percent

def get_item_prova(area, questao):
    prova_amarela = pd.read_csv(f'../pre-processamento/Itens_provas_amarela/dt_itens_{area}_amarela.csv')
    prova_amarela = prova_amarela.drop(columns=["Unnamed: 0"])
  
    if area == "MT":
        item = prova_amarela[prova_amarela["CO_POSICAO"] == questao+135]
    elif area == "CN":
        item = prova_amarela[prova_amarela["CO_POSICAO"] == questao+90]
    elif area == "CH":
        item = prova_amarela[prova_amarela["CO_POSICAO"] == questao+45]
    elif area == "LC":
        item = prova_amarela[prova_amarela["CO_POSICAO"] == questao]
    else:
        return 0
    
    return item["CO_POSICAO"].values[0]


def get_info_table_dif(area_conhecimento, estado):
    table = [["Item", "Dificuldade (200 - 1000)", "Classificação", "Acertos (%)"]]

    df = pd.read_csv(f"normalized_data/dificuldades/dif_{area_conhecimento}_{estado}.csv")
    df.sort_values(by="dificuldade_item_normalizado", inplace=True)

    for _, row in df.iterrows():
        questao = row["questao"]
        item_prova = get_item_prova(area_conhecimento, questao)
        dificuldade_escala_ENEM = round(row["dificuldade_item_normalizado"], 2)
        if dificuldade_escala_ENEM < 200:
            dificuldade_escala_ENEM = 200.00
        elif dificuldade_escala_ENEM > 1000:
            dificuldade_escala_ENEM = 1000.00
        
        classificacao = row["classificacao_dificuldade"]
        _, acertos_percent = get_num_erros(area_conhecimento, estado, questao)
        table.append([item_prova, dificuldade_escala_ENEM, classificacao, f"{round(acertos_percent, 2)}%"])

    return table

def create_pdf_report(estado):
  doc = SimpleDocTemplate(f"report_examples/prof_report_{estado}.pdf", pagesize=A4)
  styles = getSampleStyleSheet()

  title = styles["Heading1"]
  title.alignment = 1

  header = styles["Heading2"]
  header.alignment = 1

  text = styles["Bullet"]
  text.alignment = 4

  conteudo = []

  conteudo.append(Paragraph("Relatório de Questões do ENEM 2022", title))
  conteudo.append(Spacer(1, 12))

  for area_conhecimento in areas_conhecimento:
    conteudo.append(Paragraph(f"Relatório da Área {area_conhecimento}", header))
    conteudo.append(Spacer(1, 12))

    img = Image(f"plots/cci_{area_conhecimento}_{estado}_prof.png", width=20*cm, height=14*cm)
    img.hAlign = 'CENTER'

    conteudo.append(img)

    table = get_info_table_dif(area_conhecimento, estado)

    tabela = Table(table)

    estilo = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Cabeçalho com fundo cinza
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Texto branco no cabeçalho
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centralizar tudo
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Cabeçalho em negrito
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Espaçamento extra no cabeçalho
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),  # Fundo bege no restante
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grade nas células
    ])

    tabela.setStyle(estilo)


    conteudo.append(tabela)

    img = Image(f"plots/histograma_habilidades_{area_conhecimento}.png", width=20*cm, height=14*cm)
    img.hAlign = 'CENTER'

    conteudo.append(img)

    boxplot = Image(f"plots/boxplot_habilidades_{area_conhecimento}.png", width=20*cm, height=14*cm)
    boxplot.hAlign = 'CENTER'

    conteudo.append(boxplot)

    conteudo.append(PageBreak())

  doc.build(conteudo)


areas_conhecimento = ["CN", "CH", "LC", "MT"]
estados = ["PR", "PA"]

create_plots(areas_conhecimento, estados)

for estado in estados:
    create_pdf_report(estado)


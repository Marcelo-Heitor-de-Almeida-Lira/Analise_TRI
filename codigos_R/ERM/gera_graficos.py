import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

def gera_scatter_curva_unica(df, vetor_itens, titulo):
    fig = go.Figure()

    # Adiciona a primeira linha (sem legendas múltiplas como no R)
    fig.add_trace(go.Scatter(
        x=df['theta'],
        y=df.iloc[:, vetor_itens[0]],
        name=df.columns[vetor_itens[0]],
        mode='lines'
    ))

    fig.update_layout(
        title=titulo,
        xaxis=dict(
            title='Habilidade θ',
            zeroline=False
        ),
        yaxis=dict(
            title='Probabilidade de acerto P(θ)',
            zeroline=False
        )
    )

    return fig


def gera_scatter_pers(df, vetor_itens, titulo):
    fig = go.Figure()

    # Adiciona o primeiro item
    fig.add_trace(go.Scatter(
        x=df['theta'],
        y=df.iloc[:, vetor_itens[0]],
        name=df.columns[vetor_itens[0]],
        mode='lines'
    ))

    # Adiciona os demais itens
    for i in range(1, len(vetor_itens)):
        fig.add_trace(go.Scatter(
            x=df['theta'],
            y=df.iloc[:, vetor_itens[i]],
            name=df.columns[vetor_itens[i]],
            mode='lines'
        ))

    # Layout
    fig.update_layout(
        title=titulo,
        xaxis=dict(title='Habilidade θ', zeroline=False),
        yaxis=dict(title='Probabilidade P(θ)', zeroline=False)
    )

    return fig



def gera_scatter_comp(df, vetor_itens, valor1, valor2, examinando_A="", examinando_B="", titulo=""):
    fig = go.Figure()

    # Adiciona o primeiro item
    fig.add_trace(go.Scatter(
        x=df['theta'],
        y=df.iloc[:, vetor_itens[0]],
        name=df.columns[vetor_itens[0]],
        mode='lines'
    ))

    # Adiciona os demais itens
    for i in range(1, len(vetor_itens)):
        fig.add_trace(go.Scatter(
            x=df['theta'],
            y=df.iloc[:, vetor_itens[i]],
            name=df.columns[vetor_itens[i]],
            mode='lines'
        ))

    # Layout
    fig.update_layout(
        title=titulo,
        xaxis=dict(title='Habilidade θ', zeroline=False),
        yaxis=dict(title='Probabilidade P(θ)', zeroline=False)
    )

    # Adiciona anotação para o examinando A (valor2)
    fig.add_annotation(
        x=valor2['theta'],
        y=valor2['probabilidade'],
        text=f"{examinando_A}<br>Habilidade θ: {round(valor2['theta'], 2)} ({round(valor2['theta_normal'], 2)})"
             f"<br>Probabilidade P(θ): {round(valor2['probabilidade'] * 100, 2)}%",
        showarrow=True,
        arrowhead=7,
        arrowwidth=2,
        ax=valor2['theta'] - 70,
        ay=-100,
        arrowcolor="#636363",
        bordercolor="#c7c7c7",
        bgcolor="#BCBD22",
        font=dict(color="white")
    )

    # Adiciona anotação para o examinando B (valor1)
    fig.add_annotation(
        x=valor1['theta'],
        y=valor1['probabilidade'],
        text=f"{examinando_B}<br>Habilidade θ: {round(valor1['theta'], 2)} ({round(valor1['theta_normal'], 2)})"
             f"<br>Probabilidade P(θ): {round(valor1['probabilidade'] * 100, 2)}%",
        showarrow=True,
        arrowhead=7,
        arrowwidth=2,
        ax=valor1['theta'] + 40,
        ay=100,
        arrowcolor="#636363",
        bordercolor="#c7c7c7",
        bgcolor="#FF7F0E",
        font=dict(color="white")
    )

    return fig


def normalize_habil(habil):
    if habil > 4:
        habil = 4.00
    elif habil < -4:
        habil = -4.00
    
    habil_normalizada = ((habil + 4)/8) * 800 + 200
    return habil_normalizada

area_conhecimento = "MT"
estado = "PA"
items = [12, 27, 39, 21, 17, 19, 9, 29, 11]
items_curva_unica = [39]
valor1 = {'theta': 1.21, 'probabilidade': 0.5, 'theta_normal': normalize_habil(1.21)}
valor2 = {'theta': -0.95, 'probabilidade': 0.5, 'theta_normal': normalize_habil(-0.95)}
item1 = "Item 11"
item2 = "Item 27"
df = pd.read_csv(f'probabilidades/prob_ERM_1PL_{area_conhecimento}_{estado}.csv')

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

# print(df.head())

scatter = gera_scatter_comp(df, items, valor1, valor2, item1, item2, title)
# scatter = gera_scatter_pers(df, items, title)
# scatter = gera_scatter_curva_unica(df, items_curva_unica, "Curva Característica do Item")

# scatter.show()

pio.write_image(scatter, f"graficos_python/grafico_ERM_{area_conhecimento}_{estado}.pdf", format="pdf")
# pio.write_image(scatter, f"graficos_python/grafico_CCI.pdf", format="pdf")

print("grafico gerado")
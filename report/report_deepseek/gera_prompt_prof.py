import pandas as pd
import numpy as np

def gera_prompt(area, estado, item, bar_file, pie_file, cci_file):
    area_conhecimento = area

    if area == "CN":
        area_conhecimento = "Ciências da Natureza e suas Tecnologias"
    elif area == "CH":
        area_conhecimento = "Ciências Humanas e suas Tecnologias"
    elif area == "MT":
        area_conhecimento = "Matemática e suas Tecnologias"
    elif area == "LC":
        area_conhecimento = "Linguagens, Códigos e suas Tecnologias"
    
    estado = estado
    item = item

    INPUT_FILE = "template_prompt_prof.txt"
    OUTPUT_FILE = "prompt_prof.txt"

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

    # Pegando dados da questao a partir do csv gerado a partir do modelo de 3 parametros
    dificuldades_df = pd.read_csv(f'../normalized_data/dificuldades/dif_{area_conhecimento}_{estado}.csv')
    dificuldades_df = dificuldades_df[dificuldades_df['questao'] == item]
    dificuldades_df_nao_normalizado = pd.read_csv(f'../../codigos_R/LTM_3PL/dificuldades/dif_modelo_3PL_ltm_{area_conhecimento}_{estado}.csv')
    dificuldades_df_nao_normalizado = dificuldades_df_nao_normalizado[dificuldades_df_nao_normalizado['questao'] == item]


    dificuldade = dificuldades_df['dificuldade_item_normalizado'].values[0]
    classificacao_dificuldade = dificuldades_df['classificacao_dificuldade'].values[0]
    acerto_acaso = dificuldades_df_nao_normalizado['acerto_acaso_item'].values[0]
    discriminacao = dificuldades_df_nao_normalizado['discriminacao_item'].values[0]


    # Calculando probabilidade de acerto 'media' da questao
    prob_correct_ans = (1+acerto_acaso)/2
    prob_correct_ans = round(prob_correct_ans, 4)


    # Convertendo a probabilidade de acerto media da questao na habilidade correspondente do aluno
    probabilidades_df = pd.read_csv(f"../../codigos_R/LTM_3PL/probabilidades/df_prob_3PL_LTM_{area_conhecimento}_{estado}.csv")
    probabilidades_df = probabilidades_df[["theta", f"Item  {item}"]]
    habilidade_mais_proxima_index = np.abs(probabilidades_df[f"Item  {item}"] - prob_correct_ans).argsort().values[0]
    habilidade_mais_proxima = probabilidades_df['theta'].iloc[habilidade_mais_proxima_index]


    # Separando as habilidades dos alunos que acertaram e erraram a questao
    habilidades_df = pd.read_csv(f"../../codigos_R/LTM_3PL/habilidades/habil_3PL_ltm_{area_conhecimento}_{estado}.csv")
    habilidades_df = habilidades_df[[f'Q{item}', 'habilidade']]
    qtde_respostas_total = habilidades_df.count().values[0]


    alunos_acertaram = habilidades_df[habilidades_df[f'Q{item}'] == 1]
    # alunos_acertaram_percent = 100*(alunos_acertaram/qtde_respostas_total)
    alunos_erraram = habilidades_df[habilidades_df[f'Q{item}'] == 0]
    # alunos_erraram_percent = 100*(alunos_erraram/qtde_respostas_total)

    alunos_acertaram_abaixo_media = alunos_acertaram[alunos_acertaram["habilidade"] < habilidade_mais_proxima].count().values[0]
    alunos_acertaram_acima_media = alunos_acertaram[alunos_acertaram["habilidade"] >= habilidade_mais_proxima].count().values[0]
    alunos_erraram_abaixo_media = alunos_erraram[alunos_erraram["habilidade"] < habilidade_mais_proxima].count().values[0]
    alunos_erraram_acima_media = alunos_erraram[alunos_erraram["habilidade"] >= habilidade_mais_proxima].count().values[0]

    alunos_acertaram_abaixo_media_percent = 100*(alunos_acertaram_abaixo_media/(alunos_acertaram_abaixo_media+alunos_erraram_abaixo_media))
    alunos_acertaram_acima_media_percent = 100*(alunos_acertaram_acima_media/(alunos_erraram_acima_media+alunos_acertaram_acima_media))
    alunos_erraram_abaixo_media_percent = 100*(alunos_erraram_abaixo_media/(alunos_erraram_abaixo_media+alunos_acertaram_abaixo_media))
    alunos_erraram_acima_media_percent = 100*(alunos_erraram_acima_media/(alunos_erraram_acima_media+alunos_acertaram_acima_media))

    alunos_acima_media_percent = 100*(alunos_erraram_acima_media+alunos_acertaram_acima_media)/qtde_respostas_total
    alunos_abaixo_media_percent = 100*(alunos_erraram_abaixo_media+alunos_acertaram_abaixo_media)/qtde_respostas_total


    # Pegando estatísticas de respostas em cada opção
    respostas_alunos = pd.read_csv(f"../../pre-processamento/respostas_alunos/respostas_alunos_estado_{estado}_{area_conhecimento}_amarela.csv", index_col=0)

    marcacoes = respostas_alunos[f"Q{item}"].value_counts()
    marcacoes_porcentagem = respostas_alunos[f"Q{item}"].value_counts(normalize=True)*100
    respostas_nulas = respostas_alunos[f"Q{item}"].value_counts().sum() - (marcacoes["A"]+marcacoes["B"]+marcacoes["C"]+marcacoes["D"]+marcacoes["E"])
    respostas_nulas_porcentagem = 100 - (marcacoes_porcentagem["A"]+marcacoes_porcentagem["B"]+marcacoes_porcentagem["C"]+marcacoes_porcentagem["D"]+marcacoes_porcentagem["E"])

    # Pegando gabarito da questão
    questao = get_question(area_conhecimento, item)
    gabarito = questao["TX_GABARITO"].values[0]


    dados = {
        "item": item,
        "area": area_conhecimento,
        "dificuldade": round(dificuldade, 2),
        "classificacao": classificacao_dificuldade,
        "prob_acaso": round((acerto_acaso*100), 2),
        "discriminacao": round(discriminacao, 2),
        "total_respostas": qtde_respostas_total,
        "acima": round(alunos_acima_media_percent, 2),
        "acertos_acima": round(alunos_acertaram_acima_media_percent, 2),
        "erros_acima": round(alunos_erraram_acima_media_percent, 2),
        "abaixo": round(alunos_abaixo_media_percent, 2),
        "acertos_abaixo": round(alunos_acertaram_abaixo_media_percent, 2),
        "erros_abaixo": round(alunos_erraram_abaixo_media_percent, 2),
        "gabarito": gabarito,
        "a": round(marcacoes_porcentagem['A'], 2),
        "b": round(marcacoes_porcentagem['B'], 2),
        "c": round(marcacoes_porcentagem['C'], 2),
        "d": round(marcacoes_porcentagem['D'], 2),
        "e": round(marcacoes_porcentagem['E'], 2),
        "nulas": round(respostas_nulas_porcentagem, 2),
        "bar_file": bar_file,
        "pie_file": pie_file,
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

# def main():
#     dados = gera_prompt("CH", "PR", 19, "", "", "")
#     for key, value in dados.items():
#         print(f"{key}: {value}")

# main()

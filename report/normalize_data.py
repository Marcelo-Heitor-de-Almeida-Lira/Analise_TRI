import pandas as pd
import numpy as np

def normalize_dif(estado, area_conhecimento):
    df = pd.read_csv(f"../codigos_R/LTM_3PL/dificuldades/dif_modelo_3PL_ltm_{area_conhecimento}_{estado}.csv")
    df = df[["dificuldade_item", "questao"]]
    
    df["dificuldade_item_normalizado"] = ((df["dificuldade_item"] + 4) / 8) * 800 + 200

    df["classificacao_dificuldade"] = np.select(
        [df["dificuldade_item"] <= -1.28, 
         (df["dificuldade_item"] <= -0.52) & (df["dificuldade_item"] > -1.28),
         (df["dificuldade_item"] <= 0.51) & (df["dificuldade_item"] > -0.52),
         (df["dificuldade_item"] <= 1.27) & (df["dificuldade_item"] > 0.51),
         df["dificuldade_item"] > 1.27],
         ["Muito facil", "Facil", "Media", "Dificil", "Muito dificil"],
         default="Indefinido"
    )

    df.to_csv(f"normalized_data/dificuldades/dif_{area_conhecimento}_{estado}.csv", index=False)


def normalize_habil(estado, area_conhecimento):
    df = pd.read_csv(f"../codigos_R/LTM_3PL/habilidades/habil_3PL_ltm_{area_conhecimento}_{estado}.csv")
    df = df[["habilidade", "alunos_id_string"]]

    df["habilidade_normalizada"] = ((df["habilidade"] + 4) / 8) * 800 + 200

    df.to_csv(f"normalized_data/habilidades/habil_{area_conhecimento}_{estado}.csv", index=False)

estados = ["PA", "PR"]
areas_conhecimento = ["CH", "CN", "MT", "LC"]

for estado in estados:
    for area_conhecimento in areas_conhecimento:
        normalize_dif(estado, area_conhecimento)


# estado = "PR"
# area_conhecimento = "CH"
    
# normalizado = ((1.27 + 4) / 8) * 800 + 200

# print(normalizado)


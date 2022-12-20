# Desenvolvimento 14
# autor: Alex Barros
# Data: 20/12/2022

import pandas as pd

df = pd.read_csv("notas_alunos.csv")

media = (df["nota_1"] + df["nota_2"])/2
df["media"] = media

maior_faltas = df["faltas"].max()
media_geral = df["media"].mean()
maior_media = df["media"].max()

df.loc[(df["media"] >= 7) & (df["faltas"] <= 5), "situacao"] = "APROVADO"
df.loc[(df["media"] < 7) | (df["faltas"] > 5), "situacao"] = "REPROVADO"

df.to_csv("alunos_situacao.csv")

print()
print(df)
print()
print("Maior número de faltas: "+str(maior_faltas))
print("Média geral das notas dos alunos: "+str(media_geral))
print("Maior média: "+str(maior_media))
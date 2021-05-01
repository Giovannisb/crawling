import pandas as pd 

df = pd.read_json("../quotes.json", orient='columns')
df.titulo = df.astype(str)
df.titulo = df.titulo.str.strip("[]")

df.to_csv("noticias.csv")
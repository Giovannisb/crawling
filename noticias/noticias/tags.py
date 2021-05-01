import pandas as pd


df = pd.read_json("quotes.json")
df.dropna(inplace=True)

df.author = df.author.astype(str)
df.quote = df.quote.astype(str)
df.author = df.author.str.strip("[]'")
df.quote = df.quote.str.strip("[]'")

df_tags = pd.DataFrame()
for i in df.tags.iteritems():
    tam = len(list(i[1]))
    for j in range(tam):
        k = i[1][j]
        data = {
            "tag": [k]
        }

        dados = pd.DataFrame.from_dict(data=data)
        df_tags = pd.concat([df_tags, dados], ignore_index=True)
        
alfa = df_tags.tag.value_counts()[:10]
df_resumo = pd.DataFrame(alfa)
df_resumo.to_csv("resumo.csv")
import pandas as pd

df1 = pd.read_csv("./data/emb_nyp.csv")
df2 = pd.read_csv("./data/emb_fox.csv")
df3 = pd.read_csv("./data/mond-hr.csv")

df_final = pd.concat([df1, df2, df3], ignore_index=True)

df_final.to_csv('./data/combined.csv', index=False)
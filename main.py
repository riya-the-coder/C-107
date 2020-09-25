import pandas as pd
import csv
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())
fig=go.Figure(go.Bar(

    y=df.groupby("level")["attempt"].mean(),
    x=["level1","level2","level3","level4"],
    orientation="v"
))
fig.show()
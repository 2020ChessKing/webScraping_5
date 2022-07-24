import plotly.express as px
import pandas as pd

df = pd.read_csv("./stars_data.csv")
Radius = df['Radius']
Mass = df['Mass']

scatter = px.scatter(df, x='Radius', y='Mass', title="Radius x Mass of Stars", )
scatter.show()

scatter2 = px.scatter(df, x='Mass', y='Gravity', title="Gravity x Mass of Stars", )
scatter2.show()
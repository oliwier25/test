import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
from dash import html

app = dash.Dash()


df = pd.read_csv('/Users/oliwierzajac/Desktop/test_hdi.csv', sep=';')

df.set_index('country', inplace=True)

#filtrowanie column, które chcemy wykorzystać
list_of_years_col = [col for col in df.columns if col.startswith('19') or col.startswith('20')]

#robimy data frame z listy kolumn, które przefiltrowaliśmy
df = df[list_of_years_col]

data = [go.Scatter(x=df.columns,
                      y=df.loc[country],
                      mode='markers+lines',
                      name=country) for country in df.index]

layout = go.Layout(title='Wskaźnik HDI', font=dict(family='ArialNarrow'))


fig = go.Figure(data=data, layout=layout)

fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(200, 200, 200)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='ArialNarrow',
            size=15,
            color='rgb(82, 82, 82)')),
    yaxis=dict(
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='rgb(200, 200, 200)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='ArialNarrow',
            size=15,
            color='rgb(82, 82, 82)'
    )))


app.layout = html.Div([dcc.Graph(id='plot',
                      figure={'data':data,
                              'layout':layout})])

if __name__ == '__main__':
    app.run_server()

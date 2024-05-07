import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
n=40
# 샘플 데이터프레임 생성
df = pd.DataFrame({
    'A': range(n),
    'B': [i * 2 for i in range(n)],
    'C': [i * 3 for i in range(n)]
})

def table():
    return  dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                style_table={ 'overflowY': 'auto'}
            )
# Dash 앱 생성
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 레이아웃 생성
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([        ]),
        dbc.Col([        ]),
        dbc.Col(table())
    ],style={'height':'500px'}),
    dbc.Row([
        dbc.Col([table()]),
        dbc.Col([]),
        dbc.Col()
    ],style={'height':'300px'}),
])

if __name__ == '__main__':
    app.run_server(debug=True)

# 콕 찝어 설명하지 않으면 입문자 머리를 복잡하게 하는 것들
# 즉,, 몰라도 되는것들...
# input, range, map, filter, unpacking,
# comprehension, 한줄 if, Class,
# iterator , generator, decorator

import dash
from dash import dcc, html, dash_table, Input,Output,State
import dash_ag_grid as dag  # pip install dash-ag-grid
import dash_bootstrap_components as dbc
import pandas as pd

# 샘플 데이터프레임 생성

# Dash 앱 생성
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


df = pd.read_clipboard()
df = df.query("정부.isnull()")
df = df.pivot(
        index='부서',
        columns='직무',
        values='이름'
    ).reset_index()


# 레이아웃 생성
app.layout = html.Div([
    html.H6('짜장', style={'textAlign': 'center'}),
    html.H1('마스터', style={'textAlign': 'center'}),
    dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        fill_width=False
    )
], className='border rounded-2 p-3 m-3 d-inline-block')



if __name__ == '__main__':
    app.run_server(debug=True)

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
n=40
# 샘플 데이터프레임 생성
def makedf(x,y):
    df = pd.DataFrame({
    str(i) : range(y) for i in range(x)
    })
    return df

df_link = pd.DataFrame(
    {
        '과제명': ['a','b','c'],
        'Link': ['https://naver.com', None,'https://google.com']
    }
)

def table(x,y):
    df = makedf(x,y)
    return dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        css=[{
            'selector': '.dash-table-tooltip',
            'rule': 'width: fit-content; min-width: unset; background-color:blue;'
        }],
        # css=[{
        #     'selector': '.dash-tooltip',
        #     'rule': 'width: fit-content; min-width: unset; background-color:blue;'
        # }],
        tooltip_data=[
            {
                column: {'value': str(value)*10, 'type': 'markdown'}
                for column, value in row.items()
            } for row in df.to_dict('records')
        ],
        style_table={
            # 'overflow': 'auto',
            # 'width': '100%',
            # 'flex': 1,
        },
        style_data_conditional=[
            {
                'if': {'column_editable': False},
                'whiteSpace': 'normal',
                'height': 'auto',
            }
        ],
        fill_width=False)


def table_ag(x,y):
    df = makedf(x,y)
    return dag.AgGrid(
        id="my-table",
        rowData=df.to_dict("records"),                                                          # **need it
        columnDefs=[{"field": i,'cellStyle': {'textAlign': 'right'}} for i in df.columns],                                          # **need it
        defaultColDef={"resizable": True, "sortable": True, "filter": True},
        columnSize="sizeToFit",
        # dashGridOptions={"pagination": True, "paginationPageSize":10},
        # className="ag-theme-alpine",  # https://dashaggrid.pythonanywhere.com/layout/themes
        style={
            # 'height':'100%',
            # 'flex':1,
            # 'overflow':'auto'
        }
        )


# Dash 앱 생성
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

#흠

# 레이아웃 생성
app.layout = html.Div([
    html.Div(id='disqus_thread'),
    html.Button(id='heropy',className='heropy', style={'width': '100px', 'height': '100px', 'backgroundColor': 'orange'}),
    html.Div(id='heropyicon',className='icon',style = {'animationPlayState':'running'}),
    dbc.Container([
        dbc.Row([
            dbc.Col(['ss']),
            dbc.Col([html.H1('안녕'),'안녕',table_ag(40,40)],width=4,style={'height':'400px'}),
            dbc.Col([html.H1('안녕'),'잘가',table(40,5)],width=4,style={'height':'400px'})
        ],
        style={
        }),
        dbc.Row([
            dbc.Col([html.Img(src='/assets/apple.png')],style={}),
            dbc.Col([html.A('구글메일창',href='https://mail.google.com/mail/u/0/#inbox?compose=CllgCJZcRTdSsLnhQKknDcKzbRVxpsfmcfFllKFSjqpLJcxZVMnzwLHxTNJGQxjWvSPMGJFqBcg')],style={}),
            dbc.Col([html.A('아웃룩?',href='mailto:nicobockko@gmail.com'),
                     html.Div('',className='card')],style={'height':'300px'})
        ],

        ),

    ]),
    table(20,4),
    html.Div(id='dummy_output'),
])

@app.callback(
    Output('heropyicon','style'),
    Input('heropy','n_clicks'),
    State('heropyicon','style'),
    prevent_initial_call=True
)
def anyclick(n_clicks,style):
    print(style) #만약 애니메이션 최초부터 시작하게하고싶으면...?
    if style['animationPlayState'] =='running':
        return {'animationPlayState': 'paused'}
    return {'animationPlayState':'running'}


if __name__ == '__main__':
    app.run_server(debug=True)

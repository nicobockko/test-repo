import dash_echarts
import dash
from dash import html, Output,Input,callback,dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
from dash_extensions import DeferScript
scat = go.Scatter(
    x=[1,2,3,4],
    y=[1,2,3,4],
    mode="markers",
    marker={"size": 8},
)
fig = go.Figure(data=[scat])

def makeseriese(df):
    그래프시리즈 = []
    for k,v in df.groupby('지점'):
        데이터  = {
            'name': k,
            'type': 'line',
            'stack': 'Total', #이렇게해야 누적이된당
            # 'symbol': 'none',
            'symbolSize':10,
            'data': v[['날',0]].values.tolist(),
            'areaStyle': {
                'opacity': 0.3,
            },
            'emphasis': {
                'focus': 'series'
            },
        }
        그래프시리즈.append(데이터)
    return 그래프시리즈


# 데이터 생성
data = {
    '지점': ['A', 'A', 'A', 'B', 'B'],
    '날짜': ['2023-11-25', '2023-12-30', '2024-01-02', '2024-01-05', '2024-01-10'],
    '방문자수': [3, 1, 1, 1, 4]
}
df = pd.DataFrame(data)

# 날짜를 datetime 형식으로 변환하고 인덱스로 설정
df['날짜'] = pd.to_datetime(df['날짜'])#.dt.normalize()
all_dates = pd.date_range(start = df['날짜'].min(), end = df['날짜'].max(), freq='D')
df['날'] = df['날짜'].dt.strftime('%Y-%m-%d')
df['날'] = df['날'].astype('category').cat.set_categories(all_dates)# 이렇게해줘야  cumsum()해서 모든값이 생긴다

t = df.groupby(['지점', '날'],observed=False).size().cumsum().reset_index()
option = {
        'title': {
            'text': 'Line Stacked'
        },
        'tooltip': {
            'trigger': 'axis',
        },
        'brush': {
            'toolbox': [
                'rect',
                'polygon',
                'lineX',
                'lineY',
                'keep',
                'clear'
            ],
            'xAxisIndex': 0
        },


        'legend': {},
        'xAxis': {
            'type': 'time',
            'boundaryGap': False,
            'axisPointer': {
                'label': {  # 이것도 대단한꺠달음이었다, 시간이 표시되지않게하려고 ,,
                         'formatter':'ttt'
                },
            },
        },
        'yAxis': {
            'type': 'value',
            'axisLabel': {
                'formatter': '{value}' # y축 값을 변경하는거당
            },
        },
        'series': makeseriese(t)
    }
mychart =  dash_echarts.DashECharts(
            option=option,
            id='myecharts',
        )


def create_card(title, content):
    card = dbc.Card(
        dbc.CardBody(
            [
                html.H4(title, className="card-title"),
                html.Br(),
                html.Br(),
                html.H2(content, className="card-subtitle"),
                html.Br(),
                html.Br(),
                ]
        ),
        color="info", inverse=True
    )
    return(card)
card4 = create_card("Number of Comment on Articles", "None Comments")
card3 = create_card("Number of Articles", "None Articles")
card2 = create_card("Number of Likes On Articles", "None Likes")
card1 = create_card("Number of Helpfuls On Articles", "None    Helpfuls")

cards = dbc.Row([
            dbc.Col(card1,width=6,lg=3,sm=6),
            dbc.Col(card1,width=6,lg=3,sm=6),
            dbc.Col(card1,width=6,lg=3,sm=6),
            dbc.Col(card1,width=6,lg=3,sm=6)
])

external_scripts=['https://cdnjs.cloudflare.com/ajax/libs/echarts/5.0.2/echarts.min.js']


def main():
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP]
                    ,external_scripts=external_scripts
                    )

    app.layout = dbc.Container([
        html.Div(id='aaaa'),
        dbc.Row([
            dbc.Col(html.Div(mychart,id='aaa'),width=6),
            dbc.Col(cards,width=6),
        ],style={'minHeight':'500px'}),
        dbc.Row([
            dbc.Col('1'),

        ]),
        dbc.Row([
            dbc.Col('2',width=3),
            dbc.Col(dcc.Graph(figure=fig,id='graph')),
        ]),
    DeferScript(src='/assets/custom-script.js')

    ])

    app.run_server(debug=True)



if __name__ == '__main__':
    main()
import dash_echarts
import dash
from dash import html, Output,Input,callback

import pandas as pd
def makeseriese(df):
    #가로축이 time축임을 활용하려면 시리즈 내 데이터가 [[시간,값]] 이렇게 찎혀야한다,아.......!!!!!!!!!!!갯수가
    # 일치하지않아도 되게끔하려고 이러는건가보다 미친꺠달음이다
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


def main():
    app = dash.Dash(__name__)

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
    app.layout = html.Div([
        html.Div(id='output'),
        html.Div(id='output2'),
        html.Div(id='output3'),
        html.Div(id='output4'),
        dash_echarts.DashECharts(
            option=option,
            id='echarts',
            funs={
                "ttt":
                '''
                function (params) {
                var date = new Date(params.value); // Date 객체 생성
                var formattedDate = date.toISOString().slice(0, 10); 
                return formattedDate;
                }
                '''
            },
            fun_values=['ttt'],

            style={
                "width": '100vw',
                "height": '100vh',
            }
        ),
    ])


    app.run_server(debug=True)
@callback(
    Output('output', 'children'),
    [Input('echarts', 'click_data')])
def update(data):
    print("click_data",data)
    if data:
        return f"clicked: {data['name']}"
    return 'not clicked!'

@callback(
    Output('output2', 'children'),
    [Input('echarts', 'selected_data')])
def update2(data):
    print("selected_data",data)
    return 'not clicked!'
@callback(
    Output('output3', 'children'),
    [Input('echarts', 'brush_data')])
def update3(data):
    print("brush_data",data)
    return 'not clicked!'
@callback(
    Output('output4', 'children'),
    [Input('echarts', 'n_clicks')])
def update4(data):
    print("event",data)
    return 'not clicked!'


if __name__ == '__main__':
    main()
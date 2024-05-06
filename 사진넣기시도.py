import dash_echarts
import dash
from dash import html
from flask import url_for,Flask
import pandas as pd

# 데이터 생성

import os

print(os.getcwd())
def main():
    server = Flask(__name__)
    app = dash.Dash(__name__,server=server)
    with server.test_request_context():
        a = url_for('static', filename='assets/img.png')
        print(a,type(a))
    option = {
        'legend': {
            'data': ['City Alpha', 'City Beta', 'City Gamma']
        },
        'xAxis': {
            'type': 'value',
        },
        'yAxis': {
            'type': 'category',
            'data': ['Sunny', 'Cloudy', 'Showers'],
            'axisLabel': {
                'formatter': 'imglabel', # 문법이좀 생소하긴해...
                'rich': {  #
                    'Sunny': {
                        'height': 40,
                        'align': 'center',
                        'backgroundColor':  {
                            # 'image': r'C:\Users\cjs91\PycharmProjects\pythonProject\git_pjt\img.png'
                            #  'image': a #로컬파일을 심으려면어떻게해야하지..
                            'image':'https://echarts.apache.org/examples/data/asset/img/weather/sunny_128.png'
                        }
                    },
                }
            },

        },

        'series': [
            {
              'name': 'City Alpha',
              'type': 'bar',
              'data': [165, 170, 30],

              'markPoint': {
                'label': {
                  'formatter': '{b|{b}헤헤}',  #된다 쩐다
                  'rich': {
                    'b': {
                      'align': 'center',
                      'color': '#0000ff',
                    },
                  }
                },
                'data': [
                  { 'type': 'max', 'name': 'max days: ' },
                  { 'type': 'min', 'name': 'min days: ' }
                ]
              }
            },
        ]
    }
    app.layout = html.Div([
        dash_echarts.DashECharts(
            option=option,
            id='echarts',
            funs={
                "imglabel":
                '''
                function (value) {
                console.log(value);
                console.log('{' + value + '| }{value|' + value + '}');
                 return '{' + value + '| }{value|' + value + '}'
                }
                '''
            },
            fun_values=['imglabel'],
            style={
                "width": '100vw',
                "height": '100vh',
            }
        ),
    ])
    app.run_server(host='0.0.0.0',debug=True)


if __name__ == '__main__':
    main()
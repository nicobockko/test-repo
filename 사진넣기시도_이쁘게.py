import dash_echarts
import dash
from dash import html
from flask import url_for,Flask
import pandas as pd

# 데이터 생성

import os
#https://echarts.apache.org/examples/en/editor.html?c=bar-rich-text
print(os.getcwd())
def main():
    server = Flask(__name__)
    app = dash.Dash(__name__,server=server)
    with server.test_request_context():
        a = url_for('static', filename='assets/img.png')
        print(a,type(a))
    option = {
        'title': {
            'text': 'Weather Statistics'
        },
        'tooltip': {
            'trigger': 'axis',
            'axisPointer': {
                'type': 'shadow'
            },
            'legend': {
                'data': ['City Alpha', 'City Beta', 'City Gamma']
            },
        },
        'grid': {
            'left': 100
        },
        'xAxis': {
            'type': 'value',
        },
        'yAxis': {
            'type': 'category',
            'data': ['Sunny', 'Cloudy', 'Showers'],
            'axisLabel': {
                'formatter': 'imglabel', # 문법이좀 생소하긴해...
                'margin': 20,
                'rich': {  #
                    'value': {
                        'lineHeight': 30,
                        'align': 'center'
                    },
                    'Sunny': {
                        'height': 40,
                        'align': 'center',
                        'backgroundColor':  {
                            # 'image': r'C:\Users\cjs91\PycharmProjects\pythonProject\git_pjt\img.png'
                            #  'image': a #로컬파일을 심으려면어떻게해야하지..
                            'image':'https://echarts.apache.org/examples/data/asset/img/weather/sunny_128.png'
                        }
                    },
                    'Cloudy': {
                        'height': 40,
                        'align': 'center',
                        'backgroundColor': {
                            'image':'https://echarts.apache.org/examples/data/asset/img/weather/cloudy_128.png'
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
              'label': {
                    'show': 'true'
              },
              'markPoint': {
                'symbolSize': 1,
                'symbolOffset': [0, '50%'],
                'label': {
                    'formatter': '{a|{a}\n}{b|{b} }{c|{c}}',#된다 쩐다
                    'backgroundColor': 'rgb(242,242,242)',
                    'borderColor': '#aaa',
                    'borderWidth': 1,
                    'borderRadius': 4,
                    'padding': [4, 10],
                    'lineHeight': 26,
                    'shadowBlur': 5,
                    'shadowColor': '#000',
                    'shadowOffsetX': 0,
                    'shadowOffsetY': 1,
                    'position': 'right',
                    'distance': 20,


                    'rich': {

                        'a': {
                            'align': 'center',
                            'color': '#fff',
                            'fontSize': 18,
                            'textShadowBlur': 2,
                            'textShadowColor': '#000',
                            'textShadowOffsetX': 0,
                            'textShadowOffsetY': 1,
                            'textBorderColor': '#333',
                            'textBorderWidth': 2
                        },
                        'b': {
                            'align': 'center',
                            'color': '#0000ff',
                        },

                        'c': {
                            'color': '#ff8811',
                            'textBorderColor': '#000',
                            'textBorderWidth': 1,
                            'fontSize': 22
                        }
                  }
                },
                'data': [
                  { 'type': 'max', 'name': 'max days: ' },
                  { 'type': 'min', 'name': 'min days: ' }
                ]
              }
            },
            {
                'name': 'City Beta',
                'type': 'bar',
                'label': {
                        'show':'true'
                },
                'data': [150, 105, 110]
            },
            {
                'name': 'City Gamma',
                'type': 'bar',
                'label': {
                        'show':'true'
                },
                'data': [220, 82, 63]
            }

        ]
    }
    app.layout = html.Div([
        dash_echarts.DashECharts(
            option=option,
            id='echarts',
            funs={
                "imglabel":
                r'''
                function (value) {
                console.log(value);
                console.log('{' + value + '| }{value|' + value + '}');
                 return '{' + value + '| }\n{value|' + value + '}'
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
    app.run_server(debug=True)


if __name__ == '__main__':
    main()
"""
This example demonstrates sharing data between pages of a multi-page app.
Note that dcc.Store is in the app.py file so that it's accessible to all pages.
"""


from dash import html, dcc
import dash
from dash_extensions import DeferScript
# app = dash.Dash(__name__,
#                 assets_external_path='https://unpkg.com/swiper/swiper-bundle.min.css')
external_scripts=['https://unpkg.com/swiper@6.8.4/swiper-bundle.min.js']
external_stylesheets = [
    {
        'href': 'https://unpkg.com/swiper@6.8.4/swiper-bundle.min.css',
        'rel': 'stylesheet',
    }
]
app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)
app.layout = html.Div(
    [
        html.Div([
            html.Div([
                html.Div('slider1',className='swiper-slide'),
                html.Div('slider2', className='swiper-slide'),
                html.Div('slider3', className='swiper-slide'),
            ],className='swiper-wrapper')
        ],className='swiper-container',style={'height':'30px','backgroundColor':'blue'}),
        html.Div('헤헤헤헤',style={'height':'50px','backgroundColor':'red'}),
        DeferScript(src='/assets/custom-script.js'),

    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)

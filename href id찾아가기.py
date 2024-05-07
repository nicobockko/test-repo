import dash
from dash import dcc, html, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Home'),
    html.Div([
        html.H2('Section 1', id='section1'),
        html.P('Content of section 1...')
    ]),
    html.Div([
        html.H2('Section 2', id='section2'),
        html.P('Content of section 2...')
    ]),
    dcc.Location(id='url', refresh=False),
    html.Div(id='content'),
    html.Div([
        html.A('Go to Section 1', href='#section1'),
        html.Br(),
        html.A('Go to Section 2', href='#section2')
    ]*50)
])



if __name__ == '__main__':
    app.run_server(debug=True)

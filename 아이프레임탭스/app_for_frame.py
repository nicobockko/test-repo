import dash
from dash import dcc, html, Output, Input
import dash_bootstrap_components as dbc

from flask import session,Flask
import datetime


server = Flask(__name__)
server.secret_key  = 'supersecretkey'
server.permanent_session_lifetime = datetime.timedelta(seconds=500)
app = dash.Dash(__name__,server=server)


@server.before_request
def before_request():
    print(session)


def layout():
    if session.get('아하'):
        끼 = '세션있음'
    return 끼
app.layout = layout()

if __name__=='__main__':
    port = 8000
    app.run_server(port=port, debug=True)

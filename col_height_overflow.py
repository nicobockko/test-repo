import dash
from dash import dcc, html, dash_table
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

def table(x,y):
    df = makedf(x,y)
    return  dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={
            'overflow': 'auto',
            'width': '100%',
            'flex': 1,
            # 'height':'100%'
        },
        style_data_conditional=[
            {
                'if': {'column_editable': False},
                'whiteSpace': 'normal',
                'height': 'auto',
            }
        ],
        # fill_width=False
            )
def table_ag(x,y):
    df = makedf(x,y)
    return dag.AgGrid(
        id="my-table",
        rowData=df.to_dict("records"),                                                          # **need it
        columnDefs=[{"field": i} for i in df.columns],                                          # **need it
        defaultColDef={"resizable": True, "sortable": True, "filter": True},
        # columnSize="sizeToFit",
        # dashGridOptions={"pagination": True, "paginationPageSize":10},
        # className="ag-theme-alpine",  # https://dashaggrid.pythonanywhere.com/layout/themes
        style={
            # 'height':'100%',
            'flex':1,
            'overflow':'auto'
        }
        )


# Dash 앱 생성
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 레이아웃 생성
app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([]),
            dbc.Col(['안녕',table_ag(40,40)],width=4),
            dbc.Col(['안녕',table(40,40)],width=4)
        ],
        style={
             'height':'500px',
        }),
        dbc.Row([
            dbc.Col([]),
            dbc.Col([]),
            dbc.Col()
        ],
        style={
            'height':'300px'
        }),

    ]),
    table(10,10)
])

if __name__ == '__main__':
    app.run_server(debug=True)

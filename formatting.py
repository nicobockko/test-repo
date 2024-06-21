import dash
from dash import dash_table, dcc, html,Input, Output
import pandas as pd

app = dash.Dash(__name__)

# Initial data
data = [
    {'a': 0.123, 'b': 'Text1'},
    {'a': 0.456, 'b': 'Text2'},
    {'a': 0.789, 'b': 'Text3'}
]

# Define the DataTable layout
app.layout = html.Div([
    html.H3('??'),
    dash_table.DataTable(
        id='table',
        columns=[
            {'id': 'a', 'name': 'Custom Numeric'},
            {'id': 'b', 'name': 'Custom String'}
        ],
        data=data
    )
])

# Callback to format the data
@app.callback(
    Output('table', 'data'),
    [Input('table', 'data')]
)
def format_data(rows):
    print(rows)
    # Iterate over rows to format the numeric column 'a'
    for row in rows:
        if isinstance(row['a'], (int, float)):
            row['a'] = f"{row['a'] * 100:.2f}%"
    print(rows)

    return rows

if __name__ == '__main__':
    app.run_server(debug=True)
import dash
from dash import dash_table, html

import pandas as pd

def f(row):
    if row['Link']:
        return f"[{row['과제명']}]({row['Link']})"
    return row['과제명']

df_link = pd.DataFrame(
    {
        '이름':['누구1','누구2','누구3'],
        '과제명': ['a','b','c'],
        'Link': ['https://naver.com', None,'https://google.com']
    }
)
df_link["과제명"] = df_link.apply(f, axis=1)

print(df_link)
app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(

        columns=[{"name": i, "id": i, 'presentation':'markdown' } for i in df_link.columns],
        data=df_link.to_dict('records'),
    )
])
#
app.run_server(debug=True)

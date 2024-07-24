import dash
import dash_bootstrap_components as dbc
from dash import html,dcc,Input,Output
from dash_bootstrap_templates import ThemeSwitchAIO
import plotly.graph_objects as go
import plotly_express as px
import pandas as pd
import calendar
import locale


# import dados
df=pd.read_csv('arquivos/dados_completos.csv')


# criando app
app=dash.Dash(__name__)


# montando layout
linha_cabecalho=html.Div([
    html.Div([
        dcc.Dropdown(
            id='dropdown_clientes',
            options=df['Cliente'].unique(),
            placeholder='Clientes',
            style={
                'font-Family':'Fira Code'
            }
        )
    ],style={'width':'25%'})

])




app.layout=html.Div([
    linha_cabecalho
])

# callbacks


# subindo no servidor
if __name__=='__main__':app.run_server(debug=True)



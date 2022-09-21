import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
df.columns = map(lambda x: x.replace("_", " ").title(), df.columns)


charts_1 = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(
                id="graph-7",
                className="rounded-lg",
            )
        ),
        dbc.Col(
            dcc.Graph(
                id="graph-8",
                className="rounded-lg",
            )
        ),
    ]
)

charts_2 = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(
                id="graph-9",
                className="rounded-lg",
            )
        ),
        dbc.Col(
            dcc.Graph(
                id="graph-10",
                className="rounded-lg",
            )
        ),
    ]
)

categorical_tab = html.Div(
    [
        html.H3("Categorical Data", className="tab-title"),
        html.Br(),
        charts_1,
        html.Br(),
        charts_2,
    ]
)
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go


summary_cards = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5(id="card-1-title", className="card-title"),
                        html.P("Total Accounts"),
                        html.Hr(),
                        html.H5(id="card-1-subtitle", className="card-title"),
                        html.P("Qtr DWP"),
                    ]
                ),
                className="rounded-lg",
            )
        ),
        dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5(id="card-2-title", className="card-title"),
                    html.P("Total Accounts"),
                    html.Hr(),
                    html.H5(id="card-2-subtitle", className="card-title"),
                    html.P("Qtr DWP"),
                ]
            ),
            className="rounded-lg",
        )),
        dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5(id="card-3-title", className="card-title"),
                    html.P("Total Accounts"),
                    html.Hr(),
                    html.H5(id="card-3-subtitle", className="card-title"),
                    html.P("Qtr DWP"),
                ]
            ),
            className="rounded-lg",
        )),
        dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5(id="card-4-title", className="card-title"),
                    html.P("Total Accounts"),
                    html.Hr(),
                    html.H5(id="card-4-subtitle", className="card-title"),
                    html.P("Qtr DWP"),
                ]
            ),
            className="rounded-lg",
        )),
    ]
)

charts_final = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(
                id="graph-1",
                figure={
                    "data": [],
                    "layout": go.Layout(title="Chart 1 Title", barmode="stack")
                },
                className="rounded-lg",
            )
        ),
        dbc.Col(
            dcc.Graph(
                id="graph-2",
                figure={
                    "data": [],
                    "layout": go.Layout(title="Chart 2 Title", barmode="stack")
                },
                className="rounded-lg",
            )
        ),
    ]
)

home_tab = html.Div(
    [
        html.H3("Home Tab", className="tab-title"),
        html.Br(),
        summary_cards,
        html.Br(),
        charts_final,
    ]
)
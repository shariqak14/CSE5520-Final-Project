import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go


tab_layout = html.Div(
    [
        dcc.Tabs(
            [
                dcc.Tab(label="Home", value="home-tab"),
                dcc.Tab(label="Tab 1", value="tab-1"),
                dcc.Tab(label="Tab 2", value="tab-2"),
                dcc.Tab(label="Tab 3", value="tab-3"),
            ],
            id="tabs",
            value="home-tab",
        ),
        html.Br(),
        dcc.Loading(
            id="loading-1",
            type="default",
            children=html.Div(id="tabs-content")
        )
    ]
)

page_content_layout = html.Div(id="page-content")
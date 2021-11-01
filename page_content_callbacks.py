import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

from page_content_layout import tab_layout
from home_tab import home_tab

from app import app

@app.callback(Output("tabs-content", "children"), [Input("tabs", "value")])
def render_tab_layout(tab):
    if tab == "home-tab":
        return home_tab


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_contents(pathname):
    if pathname in ["/", "/home"]:
        return tab_layout
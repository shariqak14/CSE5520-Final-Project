import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from app import app

# ==============================================================
# Session Variables
# ==============================================================

demo_var = dcc.Store(id="demo-var", data=[1, 2, 3])

# ==============================================================
# Logo
# ==============================================================

logo = html.Div(
    html.Img(src=app.get_asset_url("logo.svg"), id="logo"),
    className="d-flex justify-content-center",
)

# ==============================================================
# Input 1
# ==============================================================

input_1 = html.Div(
    [
        dbc.Label("Input", html_for="example"),
        dbc.Input(type="email", id="example", placeholder="Enter email"),
        dbc.FormText(
            "Are you on email? You simply have to be these days", color="secondary",
        ),
    ],
    className="mb-3",
)

# ==============================================================
# Input 2
# ==============================================================

input_2 = html.Div(
    [
        dbc.Label("Dropdown"),
        dbc.InputGroup(
            [
                dbc.Select(
                    options=list(
                        {"label": option, "value": option} for option in ["A", "B", "C"]
                    ),
                    value="A",
                    id="input-2",
                ),
            ]
        ),
        dbc.FormText(
            "Are you on email? You simply have to be these days", color="secondary",
        ),
    ],
    className="mb-3",
)

# ==============================================================
# Input 3
# ==============================================================

input_3 = html.Div(
    [
        dbc.Label("Slider", html_for="example-email"),
        dcc.Slider(
            min=0,
            max=100,
            marks={i: str(i) + "%" for i in range(0, 101, 20)},
            value=80,
            tooltip={"always_visible": False, "placement": "bottom"},
            id="input-3",
        ),
        dbc.FormText(
            "Are you on email? You simply have to be these days", color="secondary",
        ),
    ],
    className="mb-3",
)

# ==============================================================
# Input 4
# ==============================================================

radioitems = dbc.Row(
    [
        dbc.Label("Radios", html_for="example-radios-row", width=2),
        dbc.Col(
            dbc.RadioItems(
                id="example-radios-row",
                options=[
                    {"label": "First radio", "value": 1},
                    {"label": "Second radio", "value": 2},
                    {
                        "label": "Third disabled radio",
                        "value": 3,
                        "disabled": True,
                    },
                ],
            ),
            width=10,
        ),
    ],
    className="mb-3",
)

checklist = dbc.Row(
    [
        dbc.Label("Options", html_for="example-radios-row", width=2),
        dbc.Col(
            dbc.Checklist(
                options=[
                    {"label": "Option 1", "value": 1},
                    {"label": "Option 2", "value": 2},
                    {"label": "Disabled Option", "value": 3, "disabled": True},
                ],
                value=[1],
                id="checklist-input",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)

switches = dbc.Row(
    [
        dbc.Label("Switch", html_for="example-radios-row", width=2),
        dbc.Col(
            dbc.Checklist(
                options=[
                    {"label": "Option 1", "value": 1},
                    {"label": "Option 2", "value": 2},
                    {"label": "Disabled Option", "value": 3, "disabled": True},
                ],
                value=[1],
                id="switches-input",
                switch=True,
            ),
            width=10,
        ),
    ],
    className="mb-3",
)

inputs = html.Div(
    [
        dbc.Form([radioitems, checklist, switches]),
        html.P(id="radioitems-checklist-output"),
    ]
)

# ==============================================================
# Submit Button
# ==============================================================

submit_btn = html.Div(
    dbc.Button("Submit", n_clicks=0, color="success", id="submit-btn"),
    className="d-grid gap-2 viewport-bottom",
)

# ==============================================================
# Reset Button
# ==============================================================

reset_btn = html.Div(
    dbc.Button("Reset to Defaults", color="outline-danger", id="reset-btn"),
    className="d-grid gap-2 viewport-bottom",
)

# ==============================================================
# Sidebar Filters
# ==============================================================

dashboard_filter_form = dbc.Form(
    [input_1, input_2, input_3, inputs, html.Br(), submit_btn, html.Br(), reset_btn]
)

# ==============================================================
# Sidebar Layout
# ==============================================================

sidebar_layout = html.Div(
    [logo, html.H3("Heart Failure Monitoring", className="d-flex justify-content-center"), dashboard_filter_form,],
    id="sidebar",
)

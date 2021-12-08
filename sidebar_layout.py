import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import pandas as pd
from app import app

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
df.columns = map(lambda x: x.replace("_", " ").title(), df.columns)

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
        dbc.Label("Numerical"),
        dbc.InputGroup(
            [
                dbc.Select(
                    options=list(
                        {"label": option, "value": option} for option in df.columns
                    ),
                    value="A",
                    id="input-1",
                ),
            ]
        ),
        dbc.FormText(
            "Pick an attribute that you want to explore further", color="secondary",
        ),
    ],
    className="mb-3",
)

# ==============================================================
# Input 2
# ==============================================================

input_2 = html.Div(
    [
        dbc.Label("Categorical"),
        dbc.InputGroup(
            [
                dbc.Select(
                    options=list(
                        {"label": option, "value": option} for option in df.columns
                    ),
                    value="A",
                    id="input-2",
                ),
            ]
        ),
        dbc.FormText(
            "Navigate to the categorical tab to further explore this variable",
            color="secondary",
        ),
    ],
    className="mb-3",
)

# ==============================================================
# Input 3
# ==============================================================

input_3 = html.Div(
    [
        dbc.Label("Time", html_for="example-email"),
        dcc.Slider(
            min=4,
            max=285,
            marks={i: str(i) for i in range(4, 286, 49)},
            value=285,
            tooltip={"always_visible": False, "placement": "bottom"},
            id="input-3",
        ),
        dbc.FormText("Some sub-text about the input", color="secondary",),
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
                    {"label": "Third disabled radio", "value": 3, "disabled": True,},
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
# Sidebar Filters
# ==============================================================

dashboard_filter_form = dbc.Form([input_1, input_2, input_3, inputs])

# ==============================================================
# Sidebar Layout
# ==============================================================

sidebar_layout = html.Div(
    [
        logo,
        html.H3("Heart Failure Monitoring", className="d-flex justify-content-center"),
        dashboard_filter_form,
    ],
    id="sidebar",
)

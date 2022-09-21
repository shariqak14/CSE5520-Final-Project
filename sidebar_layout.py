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

numerical_var = dcc.Store(id="numerical-var", data="Age")

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
                        {"label": option, "value": option}
                        for option in [
                            "Age",
                            "Creatinine Phosphokinase",
                            "Ejection Fraction",
                            "Platelets",
                            "Serum Creatinine",
                            "Serum Sodium",
                            "Time",
                        ]
                    ),
                    value="Age",
                    id="input-1",
                ),
            ]
        ),
        dbc.FormText(
            "Pick a numerical attribute that you want to explore further and navigate to the numerical tab.",
            color="secondary",
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
                        {"label": option, "value": option}
                        for option in [
                            "Anaemia",
                            "Diabetes",
                            "High Blood Pressure",
                            "Sex",
                            "Smoking",
                        ]
                    ),
                    value="Anaemia",
                    id="input-2",
                ),
            ]
        ),
        dbc.FormText(
            "Pick a categorical attribute that you want to explore further and navigate to the categorical tab.",
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
        dbc.Label("Max Age"),
        dcc.Slider(
            min=40,
            max=95,
            marks={i: str(i) for i in range(40, 96, 5)},
            value=95,
            tooltip={"always_visible": False, "placement": "bottom"},
            id="input-3",
        ),
        html.Br(),
        html.Br(),
        dbc.FormText("The video presentation is available here:", color="secondary",),
        html.Br(),
        html.A("https://www.youtube.com/", href="https://www.youtube.com/"),
    ],
    className="mb-3",
)

# ==============================================================
# Sidebar Filters
# ==============================================================

dashboard_filter_form = dbc.Form([input_1, input_2, input_3])

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

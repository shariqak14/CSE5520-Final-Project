import dash_bootstrap_components as dbc
from dash import html
import pandas as pd

import pandas as pd
from dtreeviz.trees import dtreeviz  # remember to load the package
from app import app

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
df.columns = map(lambda x: x.replace("_", " ").title(), df.columns)

X = df.drop("Death Event", axis=1)
y = df["Death Event"].copy()

charts_1 = dbc.Row(
    [
        dbc.Col(
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("dt_1.png"),
                        width="48.5%",
                        className="m-3",
                    ),
                ],
                className="rounded-lg bg-light d-flex justify-content-center",
            )
        ),
        dbc.Col(
            html.Div(
                [html.Img(src=app.get_asset_url("dt_1_con.png"), className="m-3"),],
                className="rounded-lg bg-light d-flex justify-content-center",
            )
        ),
    ]
)

charts_2 = dbc.Row(
    [
        dbc.Col(
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("dt_2.png"),
                        width="48.5%",
                        className="m-3",
                    ),
                ],
                className="rounded-lg bg-light d-flex justify-content-center",
            )
        ),
        dbc.Col(
            html.Div(
                [html.Img(src=app.get_asset_url("dt_2_con.png"), className="m-3"),],
                className="rounded-lg bg-light d-flex justify-content-center",
            )
        ),
    ]
)

charts_3 = dbc.Row(
    [
        dbc.Col(
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("dt_3.png"),
                        width="48.5%",
                        className="m-3",
                    ),
                ],
                className="rounded-lg bg-light d-flex justify-content-center",
            )
        ),
        dbc.Col(
            html.Div(
                [html.Img(src=app.get_asset_url("dt_3_con.png"), className="m-3"),],
                className="rounded-lg bg-light d-flex justify-content-center",
            )
        ),
    ]
)

modeling_tab = html.Div(
    [
        html.H3("Decision Tree - Overfitting", className="tab-title"),
        html.Br(),
        charts_1,
        html.Br(),
        html.H3("Decision Tree - Pruned Using Grid Search", className="tab-title"),
        html.Br(),
        charts_2,
        html.Br(),
        html.H3(
            "Decision Tree - Pruned Using Cost Complexity Pruning",
            className="tab-title",
        ),
        html.Br(),
        charts_3,
    ]
)

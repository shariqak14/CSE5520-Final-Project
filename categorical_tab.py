import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
df.columns = map(lambda x: x.replace("_", " ").title(), df.columns)

stats = df.describe()["High Blood Pressure"]

summary_cards = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5(
                            stats["count"], id="card-1-title", className="card-title"
                        ),
                        html.P("Count"),
                    ]
                ),
                className="rounded-lg",
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5(
                            len(df["High Blood Pressure"].unique()),
                            id="card-1-subtitle",
                            className="card-title",
                        ),
                        html.P("No. of unique values"),
                    ]
                ),
                className="rounded-lg",
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5(
                            round(stats["std"], 3),
                            id="card-2-title",
                            className="card-title",
                        ),
                        html.P("Standard Deviation"),
                    ]
                ),
                className="rounded-lg",
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5(
                            stats["min"], id="card-4-title", className="card-title"
                        ),
                        html.P("Minimum Value"),
                    ]
                ),
                className="rounded-lg",
            )
        ),
    ]
)

sun = (
    df.groupby(["Sex", "Diabetes", "Smoking", "Death Event"])["Age"]
    .count()
    .reset_index()
)

sun.columns = ["sex", "diabetes", "smoking", "DEATH_EVENT", "count"]

sun.loc[sun["sex"] == 0, "sex"] = "female"
sun.loc[sun["sex"] == 1, "sex"] = "male"
sun.loc[sun["smoking"] == 0, "smoking"] = "doesn't smoke"
sun.loc[sun["smoking"] == 1, "smoking"] = "smoke"
sun.loc[sun["diabetes"] == 0, "diabetes"] = "no diabetes"
sun.loc[sun["diabetes"] == 1, "diabetes"] = "diabetes"
sun.loc[sun["DEATH_EVENT"] == "No", "DEATH_EVENT"] = "alive"
sun.loc[sun["DEATH_EVENT"] == "Yes", "DEATH_EVENT"] = "dead"

charts_1 = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(
                id="graph-7",
                figure=px.bar(
                    df,
                    x="High Blood Pressure",
                    y="Age",
                    color="Death Event",
                    barmode="group",
                    title="High Blood Pressure Pie Chart",
                ),
                className="rounded-lg",
            )
        ),
        dbc.Col(
            dcc.Graph(
                id="graph-8",
                figure=px.sunburst(
                    sun,
                    path=["sex", "diabetes", "smoking", "DEATH_EVENT"],
                    values="count",
                    title="High Blood Pressure Pie Chart",
                ),
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
                figure=px.violin(
                    df,
                    x="High Blood Pressure",
                    y="Age",
                    color="Death Event",
                    title="Age & Death Event Box Plot",
                ),
                className="rounded-lg",
            )
        ),
        dbc.Col(
            dcc.Graph(
                id="graph-10",
                figure=px.box(
                    df,
                    x="High Blood Pressure",
                    y="Age",
                    color="Death Event",
                    title="Age & Death Event Box Plot",
                ),
                className="rounded-lg",
            )
        ),
    ]
)

categorical_tab = html.Div(
    [
        html.H3("Categorical Data", className="tab-title"),
        html.Br(),
        summary_cards,
        html.Br(),
        charts_1,
        html.Br(),
        charts_2,
    ]
)

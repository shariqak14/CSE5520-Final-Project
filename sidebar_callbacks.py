from dash.dependencies import Input, Output
import plotly.express as px
import plotly.figure_factory as ff
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

import pandas as pd

from app import app

@app.callback(
    [
        Output("graph-1", "figure"),
        Output("graph-2", "figure"),
        Output("graph-3", "figure"),
        Output("graph-4", "figure"),
        Output("num-cards", "children"),
    ],
    [Input("input-1", "value"), Input("input-3", "value")],
)
def display_num(num_var, age):
    df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
    df.columns = map(lambda x: x.replace("_", " ").title(), df.columns)

    df = df[df["Age"] <= age]

    hist = px.histogram(
        df,
        num_var,
        color="Death Event",
        nbins=50,
        title=f"{num_var} Distribution",
    )

    box_plot = px.box(
        df,
        x="Death Event",
        y=num_var,
        points="all",
        title=f"{num_var} & Death Event Box Plot",
    )

    dist_plot = ff.create_distplot([list(df[num_var])], [num_var], colors=["orangered"])
    dist_plot.layout.update(title=f"Histogram, KDE and Rug Plot for {num_var}")

    violin_plot = px.violin(
        df,
        x="Death Event",
        y=num_var,
        points="all",
        box=True,
        title=f"{num_var} & Death Event Violin Plot",
    )

    stats = df.describe()[num_var]

    summary_cards = dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5(
                                children=stats["count"], className="card-title"
                            ),
                            html.P("Count"),
                            html.Hr(),
                            html.H5(
                                stats["25%"], className="card-title"
                            ),
                            html.P("25%"),
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
                                round(stats["mean"], 3),
                                className="card-title",
                            ),
                            html.P("Mean"),
                            html.Hr(),
                            html.H5(
                                stats["50%"], className="card-title"
                            ),
                            html.P("50%"),
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
                                className="card-title",
                            ),
                            html.P("Standard Deviation"),
                            html.Hr(),
                            html.H5(
                                stats["75%"], className="card-title"
                            ),
                            html.P("75%"),
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
                                stats["min"], className="card-title"
                            ),
                            html.P("Minimum Value"),
                            html.Hr(),
                            html.H5(
                                stats["max"], className="card-title"
                            ),
                            html.P("Maximum Value"),
                        ]
                    ),
                    className="rounded-lg",
                )
            ),
        ]
    )

    return (
        hist,
        box_plot,
        dist_plot,
        violin_plot,
        summary_cards,
    )


@app.callback(
    [
        Output("graph-7", "figure"),
        Output("graph-8", "figure"),
        Output("graph-9", "figure"),
        Output("graph-10", "figure"),
    ],
    [Input("input-1", "value"), Input("input-2", "value"), Input("input-3", "value")],
)
def display_cat(num_var, cat_var, age):
    df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
    df.columns = map(lambda x: x.replace("_", " ").title(), df.columns)

    df = df[df["Age"] <= age]

    bar = px.bar(
        df,
        x=cat_var,
        y=num_var,
        color="Death Event",
        barmode="group",
        title=f"{num_var} & {cat_var} Bar Chart",
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

    sunburst = px.sunburst(
        sun,
        path=["sex", "diabetes", "smoking", "DEATH_EVENT"],
        values="count",
        title="Categorical Attributes Sunburst Chart",
    )

    violin = px.violin(
        df,
        x=cat_var,
        y=num_var,
        color="Death Event",
        title=f"{num_var} & {cat_var} Violin Plot",
    )

    box = px.box(
        df,
        x=cat_var,
        y=num_var,
        color="Death Event",
        title=f"{num_var} & {cat_var} Box Plot",
    )

    return (
        bar,
        sunburst,
        violin,
        box,
    )

import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from sklearn.decomposition import PCA

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
df.columns = map(lambda x: x.replace("_", " ").title(), df.columns)

stats = df.describe()["Age"]

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
                        html.Hr(),
                        html.H5(
                            stats["25%"], id="card-2-subtitle", className="card-title"
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
                            id="card-1-subtitle",
                            className="card-title",
                        ),
                        html.P("Mean"),
                        html.Hr(),
                        html.H5(
                            stats["50%"], id="card-3-title", className="card-title"
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
                            id="card-2-title",
                            className="card-title",
                        ),
                        html.P("Standard Deviation"),
                        html.Hr(),
                        html.H5(
                            stats["75%"], id="card-3-subtitle", className="card-title"
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
                            stats["min"], id="card-4-title", className="card-title"
                        ),
                        html.P("Minimum Value"),
                        html.Hr(),
                        html.H5(
                            stats["max"], id="card-4-subtitle", className="card-title"
                        ),
                        html.P("Maximum Value"),
                    ]
                ),
                className="rounded-lg",
            )
        ),
    ]
)


charts_1 = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(
                id="graph-1",
                figure=px.histogram(
                    df,
                    "Age",
                    color="Death Event",
                    nbins=50,
                    title="Patient Age Distribution",
                ),
                className="rounded-lg",
            )
        ),
        dbc.Col(
            dcc.Graph(
                id="graph-2",
                figure=px.box(
                    df,
                    x="Death Event",
                    y="Age",
                    points="all",
                    title="Age & Death Event Box Plot",
                ),
                className="rounded-lg",
            )
        ),
    ]
)

X = df.copy()
y = X["Death Event"]
X = X.drop(["Death Event"], axis=1)
pca = PCA(n_components=3, random_state=5520)

X = pd.DataFrame(pca.fit_transform(X))
X["Death Event"] = y

charts_2 = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(
                id="graph-3",
                figure=ff.create_distplot([list(df["Age"])], ["Age"]),
                className="rounded-lg",
            )
        ),
        dbc.Col(
            dcc.Graph(
                id="graph-4",
                figure=px.violin(
                    df,
                    x="Death Event",
                    y="Age",
                    points="all",
                    box=True,
                    title="Age & Death Event Violin Plot",
                ),
                className="rounded-lg",
            )
        ),
    ]
)

numerical_tab = html.Div(
    [
        html.H3("Numerical Data", className="tab-title"),
        html.Br(),
        summary_cards,
        html.Br(),
        charts_1,
        html.Br(),
        charts_2,
    ]
)

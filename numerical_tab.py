import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import pandas as pd
from sklearn.decomposition import PCA

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
df.columns = map(lambda x: x.replace("_", " ").title(), df.columns)

stats = df.describe()["Age"]

summary_cards = dbc.Row(id="num-cards")

charts_1 = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(
                id="graph-1",
                className="rounded-lg",
            )
        ),
        dbc.Col(
            dcc.Graph(
                id="graph-2",
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
                className="rounded-lg",
            )
        ),
        dbc.Col(
            dcc.Graph(
                id="graph-4",
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

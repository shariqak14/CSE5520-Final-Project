import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

import warnings

warnings.filterwarnings(action="ignore", message="^internal gelsd")
warnings.filterwarnings("ignore")
warnings.filterwarnings(action="ignore", category=DeprecationWarning)
warnings.filterwarnings(action="ignore", category=FutureWarning)

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
df.columns = map(lambda x: x.replace("_", " ").title(), df.columns)

X = df.copy()
y = X["Death Event"]
X = X.drop(["Death Event"], axis=1)

pca = PCA(n_components=2, random_state=5520)

X_2 = pd.DataFrame(pca.fit_transform(X))
X_2["Death Event"] = y

tsne = TSNE(n_components=2, random_state=5520)
X_2_tsne = tsne.fit_transform(X)

charts_1 = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(
                id="2d-scatter-pca",
                figure=px.scatter(
                    X_2, x=0, y=1, color="Death Event", title="2D scatter for PCA"
                ),
                className="rounded-lg",
            )
        ),
        dbc.Col(
            dcc.Graph(
                id="2d-scatter-tsne",
                figure=px.scatter(
                    X_2_tsne,
                    x=0,
                    y=1,
                    color=df["Death Event"],
                    labels={"color": "Death Event"},
                    title="2D scatter for t-SNE",
                ),
                className="rounded-lg",
            )
        ),
    ]
)

pca = PCA(n_components=3, random_state=5520)
X_3 = pd.DataFrame(pca.fit_transform(X))
X_3["Death Event"] = y

tsne = TSNE(n_components=3, random_state=5520)
X_3_tsne = tsne.fit_transform(X)

charts_2 = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(
                id="3d-scatter-pca",
                figure=px.scatter_3d(
                    X_3, x=0, y=1, z=2, color="Death Event", title="3D Scatter for PCA"
                ),
                className="rounded-lg",
            )
        ),
        dbc.Col(
            dcc.Graph(
                id="3d-scatter-tsne",
                figure=px.scatter_3d(
                    X_3_tsne,
                    x=0,
                    y=1,
                    z=2,
                    color=df["Death Event"],
                    labels={"color": "Death Event"},
                    title="3D scatter for t-SNE",
                ),
                className="rounded-lg",
            )
        ),
    ]
)

corr = df.corr()
trace = go.Heatmap(
    z=corr.values, x=corr.index.values, y=corr.columns.values, colorscale="Cividis"
)
heatmap = dcc.Graph(
    id="heatmap",
    figure=go.Figure(
        data=trace, layout={"title": "Features Correlation Matrix", "height": 800}
    ),
    className="rounded-lg h-100",
)


overview_tab = html.Div(
    [
        html.H3("Overview", className="tab-title"),
        html.Br(),
        charts_1,
        html.Br(),
        charts_2,
        html.Br(),
        heatmap,
    ]
)

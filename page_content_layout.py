from dash import dcc
from dash import html


tab_layout = html.Div(
    [
        dcc.Tabs(
            [
                dcc.Tab(label="Overview", value="overview"),
                dcc.Tab(label="Numerical", value="numerical"),
                dcc.Tab(label="Categorical", value="categorical"),
                dcc.Tab(label="Modeling", value="modeling"),
            ],
            id="tabs",
            value="overview",
        ),
        html.Br(),
        dcc.Loading(
            id="loading-1", type="default", children=html.Div(id="tabs-content")
        ),
    ]
)

page_content_layout = html.Div(id="page-content")

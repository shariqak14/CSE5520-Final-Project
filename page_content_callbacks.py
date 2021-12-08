from dash.dependencies import Input, Output

from page_content_layout import tab_layout
from overview_tab import overview_tab
from numerical_tab import numerical_tab
from categorical_tab import categorical_tab
from modeling_tab import modeling_tab


from app import app


@app.callback(Output("tabs-content", "children"), [Input("tabs", "value")])
def render_tab_layout(tab):
    if tab == "overview":
        return overview_tab
    elif tab == "numerical":
        return numerical_tab
    elif tab == "categorical":
        return categorical_tab
    elif tab == "modeling":
        return modeling_tab


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_contents(pathname):
    if pathname in ["/", "/home"]:
        return tab_layout

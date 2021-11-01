from dash import dcc
from dash import html

from app import app

from sidebar_layout import sidebar_layout, demo_var

from page_content_layout import page_content_layout

import sidebar_callbacks
import page_content_callbacks


app.layout = html.Div(
    [
        dcc.Location(id="url"),
        sidebar_layout,
        page_content_layout,
        # import session variables (if any)
        demo_var,
    ]
)

if __name__ == "__main__":
    app.run_server(host="localhost", port=8080, debug=True)

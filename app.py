from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    # Use the Bootstrap LUX theme as a base stylesheet
    external_stylesheets=[dbc.themes.LUX],
    # Some callbacks are generated based on other callbacks
    # By default, this causes exception which need to be subpressed
    suppress_callback_exceptions=True,
    # Meta Tags ensure that content is scaled on different devices
    meta_tags=[
        {"http-equiv": "X-UA-Compatible", "content": "IE=edge"},
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)

# Label for the browser tab
app.title = "Heart Failure Dashboard"

# Save the server for reference
server = app.server

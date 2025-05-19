import dash
from dash import html
import json
import os

# Load dashboard config
config_path = os.path.join(os.path.dirname(__file__), "dashboard_config.json")
with open(config_path, "r") as f:
    config = json.load(f)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("AI Agent Monitoring Dashboard"),
    html.H2("Dashboard Config:"),
    html.Pre(json.dumps(config, indent=2)),
    html.P("Add your metrics and graphs here.")
])

if __name__ == "__main__":
    app.run_server(debug=True)
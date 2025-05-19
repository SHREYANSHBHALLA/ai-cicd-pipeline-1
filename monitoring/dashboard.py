import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import json
import os
import random

# Load dashboard config
config_path = os.path.join(os.path.dirname(__file__), "dashboard_config.json")
with open(config_path, "r") as f:
    config = json.load(f)

metrics = config["dashboard"]["metrics"]
alert_thresholds = config["dashboard"].get("alertThresholds", {})
update_interval = config["dashboard"].get("updateInterval", 5000)

app = dash.Dash(__name__)

def get_metric_value(metric):
    # Read real metric values from metrics.json
    metrics_path = os.path.join(os.path.dirname(__file__), "metrics.json")
    try:
        with open(metrics_path, "r") as f:
            real_metrics = json.load(f)
        value = real_metrics.get(metric["name"], "--")
        return value
    except Exception:
        return "--"

def get_card_color(metric, value):
    thresholds = alert_thresholds.get(metric["name"].replace(" ", "").lower(), {})
    if not thresholds or not isinstance(value, (int, float)):
        return "#fff"
    if "critical" in thresholds and value >= thresholds["critical"]:
        return "#ffcccc"  # Red
    if "warning" in thresholds and value >= thresholds["warning"]:
        return "#fff3cd"  # Yellow
    return "#fff"  # Default

app.layout = html.Div([
    html.H1(config["dashboard"]["title"]),
    dcc.Interval(id="interval", interval=update_interval, n_intervals=0),
    html.Div(id="metrics-cards"),
    html.P("Add your metrics and graphs here."),
    dcc.Graph(id="response-time-graph")
])

@app.callback(
    Output("metrics-cards", "children"),
    Output("response-time-graph", "figure"),
    Input("interval", "n_intervals")
)
def update_metrics(n):
    cards = []
    response_time_history = []
    for metric in metrics:
        value = get_metric_value(metric)
        color = get_card_color(metric, value)
        cards.append(
            html.Div([
                html.H3(metric["name"]),
                html.P(metric["description"]),
                html.P(f"Type: {metric['type']}"),
                html.P(f"Unit: {metric['unit']}"),
                html.P(f"Value: {value}")
            ], style={
                "border": "1px solid #ccc",
                "padding": "16px",
                "margin": "8px",
                "borderRadius": "8px",
                "width": "250px",
                "display": "inline-block",
                "verticalAlign": "top",
                "backgroundColor": color
            })
        )
        # Collect data for response time graph
        if metric["name"].lower() == "response time":
            response_time_history.append(value)
    # Simple graph for Response Time (simulated)
    figure = {
        "data": [
            {"x": list(range(len(response_time_history))), "y": response_time_history, "type": "line", "name": "Response Time"}
        ],
        "layout": {"title": "Response Time Over Time"}
    }
    return cards, figure

if __name__ == "__main__":
    app.run(debug=True)
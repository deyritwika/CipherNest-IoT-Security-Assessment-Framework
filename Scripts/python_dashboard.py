import json
import pandas as pd
import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from datetime import datetime

# Load data
with open("device_data.json") as f:
    data = json.load(f)

devices = data["devices"]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
app.title = "CipherNest - IoT Security Dashboard"

# Utilities
def get_device_type(name):
    name = name.lower()
    if "bulb" in name or "light" in name:
        return "Lighting"
    elif "speaker" in name:
        return "Speaker"
    elif "echo" in name or "alexa" in name:
        return "Assistant"
    elif "home" in name:
        return "Smart Device"
    return "Other"

def get_risk_color(score):
    try:
        val = float(score)
        if val > 15:
            return "#dc3545"  # red
        elif val > 10:
            return "#6c757d"  # gray
        else:
            return "#28a745"  # green
    except:
        return "ffc107" # yellow for unknown

# KPI Cards
def generate_kpi_cards(devices):
    total_devices = len(devices)
    high_risk = sum(1 for d in devices if str(d["risk_score"]).isdigit() and float(d["risk_score"]) > 15)
    total_ports = sum(len(d["open_ports"]) for d in devices)
    active_firewalls = sum(1 for d in devices if d["firewall"].lower() == "active")

    cards = dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Total Devices"),
                html.H3(total_devices)
            ])
        ], color="dark", inverse=True), width=3),
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Devices at Risk"),
                html.H3(high_risk)
            ])
        ], color="danger", inverse=True), width=3),
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Open Ports"),
                html.H3(total_ports)
            ])
        ], color="info", inverse=True), width=3),
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Firewalls Active"),
                html.H3(active_firewalls)
            ])
        ], color="success", inverse=True), width=3)
    ], className="mb-4")
    return cards

# Device Card
def create_device_card(device):
    ports_df = pd.DataFrame(device["open_ports"])
    risk = device["risk_score"]
    risk_color = get_risk_color(risk)
    risk_text = f"{risk}%" if str(risk).isdigit() else "Unknown"

    # Gauge
    gauge_value = float(risk) if str(risk).isdigit() else 0
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=gauge_value,
        title={"text": "Risk Level"},
        gauge={
            "axis": {"range": [0, 30]},
            "bar": {"color": risk_color},
            "steps": [
                {"range": [0, 10], "color": "#28a745"},
                {"range": [10, 20], "color": "#ffc107"},
                {"range": [20, 30], "color": "#dc3545"},
            ]
        }
    ))
    gauge.update_layout(paper_bgcolor="#1b1b1b", font_color="white", height=250)

    # Pie chart if ports exist
    if not ports_df.empty and "status" in ports_df.columns:
        pie_chart = px.pie(
            ports_df, names="status", title="Port Status",
            color="status",
            color_discrete_map={"open": "green", "filtered": "blue", "closed": "red"}
        )
        pie_chart.update_layout(paper_bgcolor="#1b1b1b", font_color="white")
    else:
        pie_chart = go.Figure()
        pie_chart.update_layout(
            title="Port Status",
            annotations=[dict(text="No Port Data", x=0.5, y=0.5, font_size=18, showarrow=False)],
            paper_bgcolor="#1b1b1b"
        )

    return dbc.Card([
        dbc.CardHeader([
            html.H4(f"{device['device_name']} ", style={"color": risk_color}),
            dbc.Badge(get_device_type(device["device_name"]), color="info", className="ms-2")
        ]),
        dbc.CardBody([
            html.P(f"IP: {device['ip']}"),
            html.P(f"MAC Vendor: {device['mac_vendor']}"),
            html.P(f"OS: {device['os']}"),
            html.P(f"Firewall: {device['firewall']}"),
            html.P(f"Encryption: {device['encryption']['protocol']} (LAN: {device['encryption']['lan']}, Cloud: {device['encryption']['cloud']})"),
            html.P(f"mDNS: {', '.join(device['mdns_services']) if device['mdns_services'] else 'None'}"),
            html.P(f"TLS: {device['tls_analysis']['handshake']} | SNI: {device['tls_analysis']['sni']}"),
            html.P(f"Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"),
            html.Hr(style={"borderColor": risk_color}),
            dcc.Graph(figure=gauge),
            dcc.Graph(figure=pie_chart),
            dbc.Table.from_dataframe(ports_df, striped=True, bordered=True, hover=True) if not ports_df.empty else html.P("No open ports detected.")
        ])
    ], style={
    "backgroundColor": "#2c2c2c",
    "color": "#00d4ff",
    "border": "1px solid #00d4ff",
    "borderRadius": "5px",
    "padding": "5px",
    "fontWeight": "bold"

    })

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1(f"{data['project_name']} Dashboard", className="text-center my-4", style={"color": "#00d4ff"}))
    ]),
    dbc.Row([
        dbc.Col(html.H5(f"Network: {data['network']}", className="text-center text-muted mb-2"))
    ]),
    generate_kpi_cards(devices),
    dbc.Row([
        dbc.Col([
            html.Label("Select Device:", style={"color": "white"}),
            dcc.Dropdown(
    id="select-device",
    options=[{"label": d["device_name"], "value": d["device_name"]} for d in devices],
    value=devices[0]["device_name"],
    style={
        "backgroundColor": "#2c2c2c",
        "color": "#00d4ff",
        "border": "1px solid #00d4ff",
        "borderRadius": "5px",
        "padding": "5px",
        "fontWeight": "bold"
    }
)
,
            html.Div(id="device-details")
        ], width=12)
    ])
], fluid=True)

@app.callback(
    Output("device-details", "children"),
    Input("select-device", "value")
)
def update_device_card(value):
    device = next(d for d in devices if d["device_name"] == value)
    return create_device_card(device)

if __name__ == "__main__":
    app.run(debug=True)

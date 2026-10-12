import dash
import pandas as pd
import numpy as np
import plotly as pl

app = dash.Dash(modeling)
server = app.server
title = "tittel"


# Create layout
app.layout = html.Div(style={'fontFamily': 'Arial'}, children=[
    html.H2(title),
    
    # Plotly graph
    dcc.Graph(id='graph'),
    
    # Slider config for free vaule
    html.Label("Free value (\u03B6):"),
    dcc.Slider(
        id='slider',
        min=0.1, max=1.5, step=0.1, value=0.5,
        marks={i/10: str(i/10) for i in range(1, 16)},
        tooltip={"placement": "bottom", "always_visible": True}
    )
])

# Slider 
@app.callback(
  Output('graph', 'figure'),
  [Input('slider', 'value')]
)


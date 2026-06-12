"""Chart generation functions."""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def create_radar_chart(data_dict, title="Feature Profile"):
    """Create radar chart for feature comparison."""
    fig = go.Figure(data=go.Scatterpolar(
        r=list(data_dict.values()),
        theta=list(data_dict.keys()),
        fill='toself'
    ))
    
    fig.update_layout(
        title=title,
        height=500,
        template="plotly_dark"
    )
    
    return fig


def create_histogram(df, column, title="Distribution"):
    """Create histogram."""
    fig = px.histogram(df, x=column, title=title, nbins=30)
    fig.update_layout(template="plotly_dark", height=400)
    return fig


def create_scatter_plot(df, x_col, y_col, title="Scatter Plot", color_col=None):
    """Create scatter plot."""
    fig = px.scatter(df, x=x_col, y=y_col, color=color_col, title=title)
    fig.update_layout(template="plotly_dark", height=500)
    return fig


def create_violin_plot(df, column, group_by=None, title="Distribution"):
    """Create violin plot."""
    fig = px.violin(df, y=column, x=group_by, title=title, points="all")
    fig.update_layout(template="plotly_dark", height=500)
    return fig


def create_bar_chart(data_dict, title="Bar Chart"):
    """Create bar chart."""
    fig = go.Figure(data=go.Bar(
        x=list(data_dict.keys()),
        y=list(data_dict.values())
    ))
    
    fig.update_layout(
        title=title,
        height=400,
        template="plotly_dark"
    )
    
    return fig

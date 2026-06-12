"""Time Machine - explore music trends over time."""

import streamlit as st
import pandas as pd
from components.charts import create_histogram, create_violin_plot


def render_time_machine(df, current_mood):
    """Render the time machine view."""
    st.title("Time Machine")
    st.markdown("Explore trends and patterns in music")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Popularity Distribution")
        fig = create_histogram(df, "popularity", "Popularity Over Dataset")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Energy Distribution")
        fig = create_histogram(df, "energy", "Energy Levels")
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Feature analysis
    st.subheader("Feature Analysis")
    
    feature_select = st.selectbox(
        "Select feature to analyze",
        ["danceability", "energy", "valence", "tempo", "loudness", "acousticness"]
    )
    
    st.markdown(f"**{feature_select.title()} Statistics**")
    
    feature_data = df[feature_select]
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Mean", f"{feature_data.mean():.3f}")
    with col2:
        st.metric("Median", f"{feature_data.median():.3f}")
    with col3:
        st.metric("Std Dev", f"{feature_data.std():.3f}")
    with col4:
        st.metric("Range", f"{feature_data.max() - feature_data.min():.3f}")
    
    # Violin plot
    fig = create_violin_plot(
        df, feature_select,
        title=f"{feature_select.title()} Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

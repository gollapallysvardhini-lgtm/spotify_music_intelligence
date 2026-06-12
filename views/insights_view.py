"""Insights view - business intelligence and analytics."""

import streamlit as st
import pandas as pd
from utils.insights import get_viral_songs, generate_popularity_insight
from components.cards import track_card
from components.charts import create_bar_chart


def render_insights_view(df, current_mood):
    """Render the insights view."""
    st.title("Insights")
    st.markdown("Discover key patterns and viral tracks")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Tracks", len(df))
    with col2:
        st.metric("Unique Artists", df["artist_name"].nunique())
    with col3:
        st.metric("Avg Popularity", f"{df['popularity'].mean():.1f}")
    with col4:
        st.metric("Popular Range", f"{df['popularity'].min():.0f}-{df['popularity'].max():.0f}")
    
    st.divider()
    
    # Popularity insight
    st.subheader("Popularity Insight")
    insight = generate_popularity_insight(df)
    st.info(insight)
    
    st.divider()
    
    # Viral tracks
    st.subheader("Viral Tracks (95th Percentile)")
    
    viral = get_viral_songs(df, percentile=95)
    
    if len(viral) > 0:
        # Show top 5 viral tracks
        for idx, (_, track) in enumerate(viral.head(5).iterrows()):
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                st.markdown(f"**{track['track_name']}**")
                st.caption(track['artist_name'])
            with col2:
                st.metric("Popularity", f"{track['popularity']:.0f}")
            with col3:
                st.metric("Energy", f"{track['energy']:.2f}")
    else:
        st.warning("No viral tracks found")
    
    st.divider()
    
    # Feature correlation analysis
    st.subheader("Feature Relationships")
    
    col1, col2 = st.columns(2)
    with col1:
        feature1 = st.selectbox("Feature 1", 
            ["danceability", "energy", "valence", "tempo", "loudness", "acousticness"],
            key="insights_f1"
        )
    with col2:
        feature2 = st.selectbox("Feature 2",
            ["danceability", "energy", "valence", "tempo", "loudness", "acousticness"],
            key="insights_f2",
            index=1
        )
    
    correlation = df[feature1].corr(df[feature2])
    st.metric(f"{feature1} ↔ {feature2}", f"{correlation:.3f}")

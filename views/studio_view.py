"""Studio view - main music exploration interface."""

import streamlit as st
import pandas as pd
from components.styles import apply_glassmorphism_css
from components.charts import create_radar_chart, create_scatter_plot


def render_studio_view(df, current_mood):
    """Render the studio view."""
    apply_glassmorphism_css()
    
    st.title("Music Studio")
    st.markdown("Explore and analyze your favorite tracks")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Track Explorer")
        
        if len(df) > 0:
            selected_track = st.selectbox(
                "Select a track",
                df["track_name"].values,
                key="studio_track"
            )
            
            track_data = df[df["track_name"] == selected_track].iloc[0]
            
            st.markdown(f"### {track_data['track_name']}")
            st.markdown(f"**Artist:** {track_data['artist_name']}")
            st.markdown(f"**Popularity:** {track_data['popularity']:.0f}/100")
            
            # Display feature profile
            features = {
                "Danceability": track_data["danceability"],
                "Energy": track_data["energy"],
                "Valence": track_data["valence"],
                "Acousticness": track_data["acousticness"],
            }
            
            radar_fig = create_radar_chart(features, title="Track Profile")
            st.plotly_chart(radar_fig, use_container_width=True)
        else:
            st.warning("No tracks available")
    
    with col2:
        st.subheader("Statistics")
        st.metric("Total Tracks", len(df))
        st.metric("Avg Popularity", f"{df['popularity'].mean():.1f}")
        st.metric("Unique Artists", df["artist_name"].nunique())
    
    st.divider()
    
    # Feature comparison
    st.subheader("Feature Relationships")
    col1, col2 = st.columns(2)
    
    with col1:
        feature_x = st.selectbox("X Axis", df.columns[2:], key="studio_x")
    with col2:
        feature_y = st.selectbox("Y Axis", df.columns[2:], key="studio_y", index=1)
    
    scatter_fig = create_scatter_plot(
        df, feature_x, feature_y,
        title=f"{feature_x} vs {feature_y}",
        color_col="popularity"
    )
    st.plotly_chart(scatter_fig, use_container_width=True)

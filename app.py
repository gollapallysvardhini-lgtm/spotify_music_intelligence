"""
Spotify Music Intelligence - SoundMind
An interactive platform for music exploration and prediction
"""

import streamlit as st
import pandas as pd
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.generate_dataset import create_data_file
from utils.data_loader import load_spotify_data
from components.styles import apply_glassmorphism_css, set_mood_theme
from components.navigation import mood_selector
from views.studio_view import render_studio_view
from views.prediction_lab import render_prediction_lab
from views.time_machine import render_time_machine
from views.insights_view import render_insights_view


# Page configuration
st.set_page_config(
    page_title="SoundMind - Spotify Music Intelligence",
    page_icon="♫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "mood" not in st.session_state:
    st.session_state.mood = "Chill"
if "current_view" not in st.session_state:
    st.session_state.current_view = "Studio"


def main():
    """Main application entry point."""
    
    # Apply styling
    apply_glassmorphism_css()
    
    # Top header
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.title("SoundMind")
        st.caption("Spotify Music Intelligence Platform")
    
    with col3:
        # Mood selector in top right
        new_mood = mood_selector(st.session_state.mood)
        if new_mood != st.session_state.mood:
            st.session_state.mood = new_mood
            set_mood_theme(new_mood)
            st.rerun()
    
    st.divider()
    
    # Navigation tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "Studio",
        "Prediction Lab",
        "Time Machine",
        "Insights"
    ])
    
    # Load data
    try:
        # Create data if it doesn't exist
        df = create_data_file()
        # Load the data
        df = load_spotify_data()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        df = pd.DataFrame()
    
    # Render views based on selected tab
    with tab1:
        render_studio_view(df, st.session_state.mood)
    
    with tab2:
        render_prediction_lab(df, st.session_state.mood)
    
    with tab3:
        render_time_machine(df, st.session_state.mood)
    
    with tab4:
        render_insights_view(df, st.session_state.mood)
    
    # Footer
    st.divider()
    st.markdown("""
    <div style="text-align: center; color: #888; margin-top: 30px;">
        <small>SoundMind v1.0 | Music Intelligence Platform | Built with Streamlit & ML</small>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

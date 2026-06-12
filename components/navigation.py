"""Navigation component."""

import streamlit as st


def top_navigation(options):
    """Display top navigation menu."""
    cols = st.columns(len(options))
    selected = None
    
    for i, option in enumerate(options):
        if cols[i].button(option, use_container_width=True):
            selected = option
    
    return selected


def mood_selector(current_mood="Chill"):
    """Display mood selector."""
    from utils.constants import MOOD_THEMES
    
    moods = list(MOOD_THEMES.keys())
    selected_mood = st.selectbox("Select Mood Theme", moods, index=moods.index(current_mood))
    
    return selected_mood


def sidebar_navigation():
    """Display sidebar navigation."""
    with st.sidebar:
        st.title("Navigation")
        page = st.radio("Select Page", [
            "Studio",
            "Prediction Lab",
            "Time Machine",
            "Insights"
        ])
        return page

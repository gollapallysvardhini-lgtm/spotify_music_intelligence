"""Styling utilities for glassmorphism UI."""

import streamlit as st


def apply_glassmorphism_css():
    """Apply glassmorphism theme to Streamlit app."""
    st.markdown("""
    <style>
        .glassmorphic-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
        }
        
        .metric-card {
            background: linear-gradient(135deg, rgba(74, 144, 226, 0.2), rgba(123, 104, 238, 0.2));
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 15px;
            padding: 25px;
            text-align: center;
        }
        
        .chart-container {
            background: rgba(26, 26, 46, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 10px;
            padding: 15px;
        }
        
        .mood-button {
            padding: 10px 20px;
            border-radius: 20px;
            border: 2px solid currentColor;
            background: transparent;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .mood-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
    </style>
    """, unsafe_allow_html=True)


def set_mood_theme(mood):
    """Set color theme based on mood."""
    from utils.constants import MOOD_THEMES
    
    if mood not in MOOD_THEMES:
        mood = "Chill"
    
    theme = MOOD_THEMES[mood]
    st.markdown(f"""
    <style>
        :root {{
            --primary: {theme['primary']};
            --secondary: {theme['secondary']};
            --accent: {theme['accent']};
        }}
    </style>
    """, unsafe_allow_html=True)

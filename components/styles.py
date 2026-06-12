"""Styling utilities for glassmorphism UI."""

import streamlit as st


def apply_glassmorphism_css():
    """Apply modern glassmorphism theme to Streamlit app."""
    st.markdown("""
    <style>
        /* Modern glassmorphism with enhanced visual appeal */
        .glassmorphic-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 16px;
            padding: 24px;
            margin: 12px 0;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .glassmorphic-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.25);
        }
        
        .metric-card {
            background: linear-gradient(145deg, rgba(74, 144, 226, 0.15), rgba(123, 104, 238, 0.1));
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.25);
            border-radius: 20px;
            padding: 28px;
            text-align: center;
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        
        .metric-card:hover {
            transform: scale(1.02);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
        }
        
        .chart-container {
            background: linear-gradient(180deg, rgba(26, 26, 46, 0.6), rgba(18, 18, 32, 0.8));
            backdrop-filter: blur(12px);
            border-radius: 16px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.2);
        }
        
        .mood-button {
            padding: 12px 24px;
            border-radius: 25px;
            border: 2px solid currentColor;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
            backdrop-filter: blur(10px);
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            font-weight: 500;
            letter-spacing: 0.5px;
        }
        
        .mood-button:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1));
        }
        
        .mood-button:active {
            transform: translateY(-1px) scale(1.02);
        }
        
        /* Enhanced typography */
        h1 {
            font-weight: 700;
            letter-spacing: -0.5px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        h2, h3 {
            font-weight: 600;
            letter-spacing: -0.3px;
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.1);
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, rgba(74, 144, 226, 0.6), rgba(123, 104, 238, 0.6));
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(180deg, rgba(74, 144, 226, 0.8), rgba(123, 104, 238, 0.8));
        }
        
        /* Enhanced button styles */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: none;
            border-radius: 12px;
            padding: 12px 32px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        }
        
        /* Enhanced input styles */
        .stSelectbox > div > div > select,
        .stSlider > div > div > input {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 8px;
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

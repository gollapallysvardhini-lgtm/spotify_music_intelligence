"""Animation and visual effects."""

import streamlit as st
import time


def fade_in_effect():
    """Apply fade-in animation."""
    st.markdown("""
    <style>
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .fade-in {
            animation: fadeIn 1s ease-in-out;
        }
    </style>
    """, unsafe_allow_html=True)


def slide_in_animation():
    """Apply slide-in animation."""
    st.markdown("""
    <style>
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .slide-in {
            animation: slideIn 0.5s ease-out;
        }
    </style>
    """, unsafe_allow_html=True)


def loading_spinner():
    """Display loading spinner."""
    with st.spinner("Loading..."):
        time.sleep(1)

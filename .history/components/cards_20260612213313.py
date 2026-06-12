"""Card components for displaying information."""

import streamlit as st


def metric_card(title, value, description=""):
    """Display a metric card with glassmorphism style."""
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.metric(title, value)
        with col2:
            if description:
                st.caption(description)


def info_card(title, content, icon="ℹ️"):
    """Display an info card."""
    st.info(f"{icon} **{title}**\n\n{content}")


def track_card(track_name, artist_name, metrics=None):
    """Display a track information card."""
    st.markdown(f"""
    <div class="glassmorphic-card">
        <h3>{track_name}</h3>
        <p><strong>{artist_name}</strong></p>
        {f"<p>{metrics}</p>" if metrics else ""}
    </div>
    """, unsafe_allow_html=True)


def recommendation_card(track_name, artist_name, similarity, popularity):
    """Display a recommendation card."""
    st.markdown(f"""
    <div class="glassmorphic-card">
        <h4>{track_name}</h4>
        <p>{artist_name}</p>
        <p>Similarity: {similarity:.1%} | Popularity: {popularity:.0f}</p>
    </div>
    """, unsafe_allow_html=True)

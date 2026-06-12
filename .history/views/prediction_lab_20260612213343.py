"""Prediction Lab - what-if analysis and predictions."""

import streamlit as st
from models.popularity_model import PopularityModel
from utils.constants import FEATURES
from components.charts import create_bar_chart


def render_prediction_lab(df, current_mood):
    """Render the prediction lab view."""
    st.title("🔮 Prediction Lab")
    st.markdown("Predict track popularity with ML")
    
    # Initialize model
    model = PopularityModel()
    model_loaded = model.load()
    
    if not model_loaded:
        st.info("Training model on first launch...")
        metrics = model.train(df)
        st.success(f"Model trained! Test Score: {metrics['test_score']:.3f}")
    
    st.divider()
    
    # Feature sliders for what-if analysis
    st.subheader("What-If Analysis")
    st.markdown("Adjust features to see predicted popularity")
    
    col1, col2, col3 = st.columns(3)
    
    features_input = {}
    with col1:
        features_input["danceability"] = st.slider(
            "Danceability", 0.0, 1.0, 0.7
        )
        features_input["energy"] = st.slider(
            "Energy", 0.0, 1.0, 0.5
        )
    
    with col2:
        features_input["valence"] = st.slider(
            "Valence", 0.0, 1.0, 0.6
        )
        features_input["tempo"] = st.slider(
            "Tempo (BPM)", 50, 220, 120
        )
    
    with col3:
        features_input["loudness"] = st.slider(
            "Loudness (dB)", -60.0, 0.0, -5.0
        )
        features_input["acousticness"] = st.slider(
            "Acousticness", 0.0, 1.0, 0.2
        )
    
    # Predict
    if st.button("Predict Popularity", type="primary"):
        predicted = model.predict(features_input)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Predicted Popularity", f"{predicted:.1f}/100")
        with col2:
            avg_pop = df["popularity"].mean()
            st.metric("Dataset Average", f"{avg_pop:.1f}/100")
        
        # Feature importance
        importance = model.get_feature_importance()
        if importance:
            fig = create_bar_chart(importance, "Feature Importance")
            st.plotly_chart(fig, use_container_width=True)

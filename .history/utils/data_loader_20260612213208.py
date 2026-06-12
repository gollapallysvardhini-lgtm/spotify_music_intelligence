"""Data loading utilities."""

import os
import pandas as pd
from .constants import DATA_DIR, DATA_FILE


def load_spotify_data():
    """Load Spotify tracks dataset."""
    data_path = os.path.join(DATA_DIR, DATA_FILE)
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found at {data_path}")
    
    df = pd.read_csv(data_path)
    return df


def validate_data(df):
    """Validate dataframe has required columns."""
    required_columns = [
        "track_name", "artist_name", "danceability", "energy",
        "valence", "tempo", "loudness", "acousticness", "popularity"
    ]
    
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    
    return df

"""Generate sample dataset for the application."""

import os
import pandas as pd
import numpy as np
from .constants import DATA_DIR, DATA_FILE


def generate_sample_data(n_samples=500):
    """Generate sample Spotify-like data."""
    np.random.seed(42)
    
    artists = ["The Weeknd", "Drake", "Billie Eilish", "Ariana Grande", "Post Malone",
               "Dua Lipa", "Taylor Swift", "Ed Sheeran", "Harry Styles", "Olivia Rodrigo"]
    
    data = {
        "track_name": [f"Track {i}" for i in range(n_samples)],
        "artist_name": np.random.choice(artists, n_samples),
        "danceability": np.random.uniform(0.3, 1.0, n_samples),
        "energy": np.random.uniform(0.0, 1.0, n_samples),
        "valence": np.random.uniform(0.0, 1.0, n_samples),
        "tempo": np.random.uniform(80, 200, n_samples),
        "loudness": np.random.uniform(-10, 0, n_samples),
        "acousticness": np.random.uniform(0.0, 1.0, n_samples),
        "popularity": np.random.uniform(0, 100, n_samples),
    }
    
    df = pd.DataFrame(data)
    return df


def create_data_file():
    """Create data file if it doesn't exist."""
    os.makedirs(DATA_DIR, exist_ok=True)
    data_path = os.path.join(DATA_DIR, DATA_FILE)
    
    if not os.path.exists(data_path):
        print(f"Generating sample data at {data_path}...")
        df = generate_sample_data()
        df.to_csv(data_path, index=False)
        print(f"✓ Dataset created with {len(df)} tracks")
        return df
    
    return pd.read_csv(data_path)


if __name__ == "__main__":
    create_data_file()

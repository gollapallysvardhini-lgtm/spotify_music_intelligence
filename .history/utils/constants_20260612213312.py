"""Constants and configuration for the application."""

# Feature names and ranges
FEATURES = {
    "danceability": {"min": 0.0, "max": 1.0},
    "energy": {"min": 0.0, "max": 1.0},
    "valence": {"min": 0.0, "max": 1.0},
    "tempo": {"min": 50, "max": 220},
    "loudness": {"min": -60, "max": 0},
    "acousticness": {"min": 0.0, "max": 1.0},
}

# Mood themes configuration
MOOD_THEMES = {
    "Chill": {
        "primary": "#4A90E2",
        "secondary": "#7B68EE",
        "accent": "#FF6B9D",
    },
    "Happy": {
        "primary": "#FFD93D",
        "secondary": "#FF6B6B",
        "accent": "#FFA348",
    },
    "Energetic": {
        "primary": "#FF1744",
        "secondary": "#FF5722",
        "accent": "#FFCA28",
    },
    "Dark": {
        "primary": "#1A1A2E",
        "secondary": "#16213E",
        "accent": "#E94560",
    },
    "Romantic": {
        "primary": "#FF69B4",
        "secondary": "#FF1493",
        "accent": "#FFB6C1",
    },
}

# Viral detection threshold (95th percentile)
VIRAL_THRESHOLD_PERCENTILE = 95

# Model parameters
MODEL_PARAMS = {
    "n_estimators": 200,
    "max_depth": 5,
    "random_state": 42,
}

# Data paths
DATA_DIR = "data"
DATA_FILE = "spotify_tracks.csv"
MODEL_FILE = "models/popularity_model.pkl"
SCALER_FILE = "models/scaler.pkl"

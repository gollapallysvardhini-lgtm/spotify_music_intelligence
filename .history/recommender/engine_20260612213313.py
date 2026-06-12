"""Recommendation engine using cosine similarity."""

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


class RecommendationEngine:
    """Cosine similarity based recommendation engine."""
    
    def __init__(self, df):
        self.df = df.copy()
        self.feature_names = ["danceability", "energy", "valence", "tempo", 
                             "loudness", "acousticness", "popularity"]
        self.feature_matrix = None
        self.scaler = None
        self._prepare_features()
    
    def _prepare_features(self):
        """Prepare and normalize feature matrix."""
        # Select features and normalize to [0, 1]
        features = self.df[self.feature_names].copy()
        
        # Normalize each feature to [0, 1]
        for col in self.feature_names:
            min_val = features[col].min()
            max_val = features[col].max()
            features[col] = (features[col] - min_val) / (max_val - min_val) if max_val > min_val else 0
        
        self.feature_matrix = features.values
    
    def recommend_similar(self, track_idx, n_recommendations=10):
        """Get similar tracks to a given track."""
        if track_idx >= len(self.df):
            raise ValueError("Track index out of range")
        
        # Compute similarity
        similarities = cosine_similarity([self.feature_matrix[track_idx]], self.feature_matrix)[0]
        
        # Get top N similar (excluding the track itself)
        similar_idx = np.argsort(similarities)[::-1][1:n_recommendations+1]
        
        recommendations = []
        for idx in similar_idx:
            rec = {
                "track_name": self.df.iloc[idx]["track_name"],
                "artist_name": self.df.iloc[idx]["artist_name"],
                "similarity": float(similarities[idx]),
                "popularity": float(self.df.iloc[idx]["popularity"]),
            }
            recommendations.append(rec)
        
        return recommendations
    
    def recommend_by_artist(self, artist_name, n_recommendations=10):
        """Get top recommendations by artist."""
        artist_tracks = self.df[self.df["artist_name"] == artist_name].index.tolist()
        
        if not artist_tracks:
            return []
        
        # Use first track by artist as seed
        return self.recommend_similar(artist_tracks[0], n_recommendations)
    
    def get_track_profile(self, track_idx):
        """Get feature profile of a track."""
        if track_idx >= len(self.df):
            raise ValueError("Track index out of range")
        
        track = self.df.iloc[track_idx]
        profile = {}
        for feature in self.feature_names:
            profile[feature] = float(track[feature])
        
        return profile

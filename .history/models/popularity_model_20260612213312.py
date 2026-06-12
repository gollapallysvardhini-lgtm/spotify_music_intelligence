"""Popularity prediction model using GradientBoosting."""

import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from utils.constants import FEATURES, MODEL_PARAMS, MODEL_FILE, SCALER_FILE


class PopularityModel:
    """Gradient Boosting model for predicting track popularity."""
    
    def __init__(self):
        self.model = None
        self.scaler = None
        self.feature_names = list(FEATURES.keys())
        self.is_trained = False
    
    def train(self, df):
        """Train the popularity prediction model."""
        # Prepare data
        X = df[self.feature_names].values
        y = df["popularity"].values
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Scale features
        self.scaler = StandardScaler()
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train model
        self.model = GradientBoostingRegressor(**MODEL_PARAMS)
        self.model.fit(X_train_scaled, y_train)
        
        # Evaluate
        train_score = self.model.score(X_train_scaled, y_train)
        test_score = self.model.score(X_test_scaled, y_test)
        
        self.is_trained = True
        
        return {
            "train_score": train_score,
            "test_score": test_score,
            "n_features": len(self.feature_names),
        }
    
    def predict(self, features_dict):
        """Predict popularity for given features."""
        if not self.is_trained or self.model is None:
            raise ValueError("Model not trained yet")
        
        # Convert dict to array in correct order
        X = np.array([features_dict[f] for f in self.feature_names]).reshape(1, -1)
        X_scaled = self.scaler.transform(X)
        
        prediction = self.model.predict(X_scaled)[0]
        return max(0, min(100, prediction))  # Clamp to 0-100
    
    def get_feature_importance(self):
        """Get feature importance scores."""
        if self.model is None:
            return {}
        
        importances = self.model.feature_importances_
        return dict(zip(self.feature_names, importances))
    
    def save(self, model_path=MODEL_FILE, scaler_path=SCALER_FILE):
        """Save model and scaler to disk."""
        os.makedirs(os.path.dirname(model_path) or ".", exist_ok=True)
        joblib.dump(self.model, model_path)
        joblib.dump(self.scaler, scaler_path)
    
    def load(self, model_path=MODEL_FILE, scaler_path=SCALER_FILE):
        """Load model and scaler from disk."""
        if os.path.exists(model_path) and os.path.exists(scaler_path):
            self.model = joblib.load(model_path)
            self.scaler = joblib.load(scaler_path)
            self.is_trained = True
            return True
        return False

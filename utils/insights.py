"""Generate business insights from data."""

import pandas as pd
import numpy as np


def generate_trend_insight(df, feature, time_col="year"):
    """Generate insight about feature trends over time."""
    if time_col not in df.columns:
        return f"Average {feature}: {df[feature].mean():.2f}"
    
    trend = df.groupby(time_col)[feature].mean()
    change = trend.iloc[-1] - trend.iloc[0]
    direction = "increased" if change > 0 else "decreased"
    
    return f"{feature.title()} has {direction} by {abs(change):.2f} over the period."


def generate_popularity_insight(df):
    """Generate insight about popularity distribution."""
    mean_pop = df["popularity"].mean()
    median_pop = df["popularity"].median()
    
    if mean_pop > median_pop:
        return f"Distribution skewed toward high popularity (mean: {mean_pop:.1f}, median: {median_pop:.1f})"
    else:
        return f"Distribution skewed toward lower popularity (mean: {mean_pop:.1f}, median: {median_pop:.1f})"


def generate_feature_correlation(df, feature1, feature2):
    """Generate insight about feature correlation."""
    corr = df[feature1].corr(df[feature2])
    strength = "strong" if abs(corr) > 0.7 else "moderate" if abs(corr) > 0.4 else "weak"
    direction = "positive" if corr > 0 else "negative"
    
    return f"{strength.title()} {direction} correlation ({corr:.2f}) between {feature1} and {feature2}."


def get_viral_songs(df, percentile=95):
    """Get songs above popularity percentile."""
    threshold = df["popularity"].quantile(percentile / 100)
    return df[df["popularity"] >= threshold].sort_values("popularity", ascending=False)

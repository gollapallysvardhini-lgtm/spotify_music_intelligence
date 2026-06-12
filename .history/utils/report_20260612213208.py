"""Generate reports and summaries."""

import pandas as pd


def create_summary_report(df):
    """Create a summary report of the dataset."""
    report = {
        "Total Tracks": len(df),
        "Unique Artists": df["artist_name"].nunique() if "artist_name" in df.columns else 0,
        "Average Popularity": df["popularity"].mean() if "popularity" in df.columns else 0,
        "Popular Range": f"{df['popularity'].min():.0f} - {df['popularity'].max():.0f}" if "popularity" in df.columns else "N/A",
    }
    return report


def format_track_info(track_row):
    """Format a track row into readable info."""
    return {
        "Track": track_row.get("track_name", "Unknown"),
        "Artist": track_row.get("artist_name", "Unknown"),
        "Popularity": f"{track_row.get('popularity', 0):.0f}",
        "Energy": f"{track_row.get('energy', 0):.2f}",
        "Danceability": f"{track_row.get('danceability', 0):.2f}",
    }

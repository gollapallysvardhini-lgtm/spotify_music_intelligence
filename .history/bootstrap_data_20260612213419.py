"""Bootstrap data for the application."""

import os
import sys
from utils.generate_dataset import create_data_file

if __name__ == "__main__":
    print("🎵 SoundMind - Data Bootstrap")
    print("-" * 50)
    
    try:
        df = create_data_file()
        print(f"\n✓ Dataset ready!")
        print(f"  - Tracks: {len(df)}")
        print(f"  - Features: {df.columns.tolist()}")
        print(f"  - Location: data/spotify_tracks.csv")
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)

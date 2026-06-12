"""Generate CSV dataset from raw data."""

import pandas as pd
import os
from utils.generate_dataset import generate_sample_data
from utils.constants import DATA_DIR, DATA_FILE


def main():
    """Generate and save CSV file."""
    os.makedirs(DATA_DIR, exist_ok=True)
    
    print("📊 Generating CSV dataset...")
    
    # Generate sample data
    df = generate_sample_data(n_samples=500)
    
    # Save to CSV
    output_path = os.path.join(DATA_DIR, DATA_FILE)
    df.to_csv(output_path, index=False)
    
    print(f"✓ CSV file created: {output_path}")
    print(f"  - Records: {len(df)}")
    print(f"  - Columns: {len(df.columns)}")
    
    return df


if __name__ == "__main__":
    main()

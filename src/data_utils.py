"""Data utilities for financial inclusion analysis."""
import pandas as pd
import os

def load_data(filepath='data/raw/ethiopia_fi_unified_data.csv'):
    """Load the unified financial inclusion dataset."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    try:
        df = pd.read_csv(filepath)
        print(f"Loaded {len(df)} records")
        return df
    except Exception as e:
        raise ValueError(f"Error reading {filepath}: {e}")

def get_records_by_type(df, record_type):
    """Filter records by type."""
    return df[df['record_type'] == record_type]

def summarize_schema(df):
    """Print schema summary."""
    print(f"Records: {len(df)}")
    print(f"Types: {df['record_type'].value_counts().to_dict()}")
    print(f"Pillars: {df['pillar'].value_counts().to_dict()}")
    print(f"Date range: {df['observation_date'].min()} to {df['observation_date'].max()}")
    return df

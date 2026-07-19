import pandas as pd

df = pd.read_csv('data/raw/ethiopia_fi_unified_data.csv')
ref = pd.read_csv('data/raw/reference_codes.csv')

print("Data shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nRecord types:")
print(df['record_type'].value_counts())
print("\nPillars:")
print(df['pillar'].value_counts())
print("\nIndicators:")
print(df['indicator_code'].value_counts())
print("\nEvents:")
events = df[df['record_type'] == 'event']
print(events[['indicator_code', 'observation_date', 'category']].to_string())
print("\nDone")

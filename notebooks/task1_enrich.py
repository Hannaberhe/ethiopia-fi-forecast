import pandas as pd

df = pd.read_csv('data/raw/ethiopia_fi_unified_data.csv')
print(f"Before: {len(df)} rows")

# New observations
new_rows = [
    {
        'record_id': 'REC_ENR_001', 'record_type': 'observation', 'pillar': 'ACCESS',
        'indicator': 'Account Ownership Rate', 'indicator_code': 'ACC_OWNERSHIP',
        'value_numeric': 49, 'observation_date': '2024-12-31',
        'source_name': 'Global Findex 2024', 'source_type': 'survey',
        'confidence': 'high', 'collected_by': 'Hana Berhe', 'collection_date': '2026-07-19',
        'notes': '2024 Findex survey result for Ethiopia'
    },
    {
        'record_id': 'REC_ENR_002', 'record_type': 'observation', 'pillar': 'ACCESS',
        'indicator': 'Mobile Money Account', 'indicator_code': 'ACC_MM_ACCOUNT',
        'value_numeric': 9.45, 'observation_date': '2024-12-31',
        'source_name': 'Global Findex 2024', 'source_type': 'survey',
        'confidence': 'high', 'collected_by': 'Hana Berhe', 'collection_date': '2026-07-19',
        'notes': 'Mobile money account ownership from Findex 2024'
    },
    {
        'record_id': 'REC_ENR_003', 'record_type': 'observation', 'pillar': 'USAGE',
        'indicator': 'Digital Payment Rate', 'indicator_code': 'USG_DIGITAL_PAYMENT',
        'value_numeric': 35, 'observation_date': '2024-12-31',
        'source_name': 'Global Findex 2024', 'source_type': 'survey',
        'confidence': 'medium', 'collected_by': 'Hana Berhe', 'collection_date': '2026-07-19',
        'notes': 'Estimated from Findex microdata'
    },
]

new_df = pd.DataFrame(new_rows)
df = pd.concat([df, new_df], ignore_index=True)
print(f"After enrichment: {len(df)} rows")
print(f"New records added: {len(new_rows)}")

# Save enriched dataset
df.to_csv('data/processed/ethiopia_fi_enriched.csv', index=False)
print("Saved enriched dataset to data/processed/")

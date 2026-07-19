import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('data/raw/ethiopia_fi_unified_data.csv')

# 1. Dataset Overview
print("=== 1. DATASET OVERVIEW ===")
print(f"Total records: {len(df)}")
print(f"Record types:\n{df['record_type'].value_counts()}")
print(f"\nPillars:\n{df['pillar'].value_counts()}")
print(f"\nConfidence levels:\n{df['confidence'].value_counts()}")
print(f"\nDate range: {df['observation_date'].min()} to {df['observation_date'].max()}")

# 2. Temporal Coverage
print("\n=== 2. TEMPORAL COVERAGE ===")
obs = df[df['record_type'] == 'observation']
for ind in obs['indicator_code'].unique():
    ind_data = obs[obs['indicator_code'] == ind]
    print(f"{ind}: {len(ind_data)} points, years: {ind_data['observation_date'].unique()}")

# 3. Access Analysis
print("\n=== 3. ACCESS ANALYSIS ===")
access = obs[obs['pillar'] == 'ACCESS']
print(access[['indicator_code', 'value_numeric', 'observation_date']])

# Chart 1: Account Ownership
years = [2011, 2014, 2017, 2021, 2024]
values = [14, 22, 35, 46, 49]
growth = [0, 8, 13, 11, 3]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].plot(years, values, 'o-', color='blue', linewidth=2, markersize=10)
axes[0].set_title('Account Ownership Rate (%)')
axes[0].set_ylabel('% of adults')
for y, v in zip(years, values):
    axes[0].text(y, v+2, f'{v}%', ha='center', fontweight='bold')

axes[1].bar([f'{years[i]}-{years[i+1]}' for i in range(len(years)-1)], growth[1:], color='steelblue')
axes[1].set_title('Growth Between Surveys (pp)')
axes[1].axhline(3, color='red', linestyle='--', label='2021-24: +3pp')
axes[1].legend()
plt.tight_layout()
plt.savefig('reports/access_analysis.png', dpi=150)
print("Chart 1 saved")

# 4. Events Timeline
events_dict = {
    '2021-05': 'Telebirr Launch',
    '2022-08': 'Safaricom Entry', 
    '2023-08': 'M-Pesa Entry',
    '2024-01': 'Fayda Digital ID',
    '2024-07': 'FX Reform',
    '2024-10': 'P2P/ATM Crossover'
}

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(years, values, 'o-', color='blue', linewidth=3, markersize=12, label='Account Ownership', zorder=5)
for date_str, name in events_dict.items():
    yr = float(date_str.split('-')[0]) + (float(date_str.split('-')[1])-1)/12
    ax.axvline(yr, color='red', linestyle='--', alpha=0.5, linewidth=1)
    ax.text(yr, 53, name, rotation=90, fontsize=8, color='darkred', fontweight='bold')
ax.set_title('Account Ownership with Key Events')
ax.set_ylabel('% of adults')
ax.legend()
plt.tight_layout()
plt.savefig('reports/events_timeline.png', dpi=150)
print("Chart 2 saved")

# 5. Usage Analysis
print("\n=== 4. USAGE ANALYSIS ===")
usage = obs[obs['pillar'] == 'USAGE']
print(usage[['indicator_code', 'value_numeric', 'observation_date']])

# Chart 3: Indicators comparison
fig, ax = plt.subplots(figsize=(10, 6))
indicators = ['ACC_OWNERSHIP', 'ACC_MM_ACCOUNT', 'USG_P2P_COUNT']
colors = ['blue', 'green', 'orange']
for ind, col in zip(indicators, colors):
    ind_data = obs[obs['indicator_code'] == ind]
    if len(ind_data) > 0:
        ax.plot(ind_data['observation_date'], ind_data['value_numeric'], 'o-', label=ind, color=col)
ax.set_title('Key Financial Inclusion Indicators')
ax.legend()
plt.tight_layout()
plt.savefig('reports/indicators_comparison.png', dpi=150)
print("Chart 3 saved")

# 6. Key Insights
print("\n=== 5. KEY INSIGHTS ===")
print("1. Account ownership grew 35pp (14% to 49%) over 13 years but slowed to only +3pp in 2021-24")
print("2. The 2021-24 slowdown happened despite Telebirr adding 54M+ users - registered accounts ≠ active usage")
print("3. Mobile money account ownership reached only 9.45% by 2024, far below total account ownership")
print("4. Six major events occurred in 2021-2024 creating a concentrated period of change")
print("5. Data sparsity (only 5 Findex points) limits forecasting precision - wide uncertainty is appropriate")
print("6. Impact links provide modeled relationships but need validation against observed changes")
print("7. Gender gap data exists but is incomplete - limits equity analysis")

# 7. Data Limitations
print("\n=== 6. DATA LIMITATIONS ===")
print("- Only 5 Findex survey points over 13 years")
print("- No sub-national or regional disaggregation")
print("- Impact links are modeled, not directly observed")
print("- Operator user numbers may not match survey-based Findex")
print("- Missing data on rural/urban splits and income levels")

print("\nDone! All charts saved.")

import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('data/raw/ethiopia_fi_unified_data.csv')

# Access trajectory
years = [2011, 2014, 2017, 2021, 2024]
values = [14, 22, 35, 46, 49]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(years, values, 'o-', color='blue', linewidth=2, markersize=10)
ax.set_title('Ethiopia Account Ownership (% of adults)')
ax.set_ylabel('Account Ownership (%)')
for y, v in zip(years, values):
    ax.text(y, v+2, f'{v}%', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('reports/account_ownership.png', dpi=150)
print("Chart 1 saved")

# Events timeline
fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(years, values, 'o-', color='blue', linewidth=2, markersize=10, label='Account Ownership')
events = {2021: 'Telebirr Launch', 2022: 'Safaricom Entry', 2023: 'M-Pesa Entry'}
for yr, name in events.items():
    ax.axvline(yr, color='red', linestyle='--', alpha=0.7)
    ax.text(yr, 52, name, rotation=90, fontsize=9, color='red')
ax.set_title('Account Ownership with Key Events')
ax.legend()
plt.tight_layout()
plt.savefig('reports/events_timeline.png', dpi=150)
print("Chart 2 saved")

print("\n=== KEY INSIGHTS ===")
print("1. Account ownership grew from 14% (2011) to 49% (2024)")
print("2. Growth slowed after 2021: only +3pp despite Telebirr")
print("3. Registered accounts do not equal active usage")
print("4. Key events cluster in 2021-2023")
print("5. Only 5 Findex data points over 13 years limits forecasting")

print("\nDone")

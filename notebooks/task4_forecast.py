import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')

# Historical data
years = np.array([2011, 2014, 2017, 2021, 2024]).reshape(-1, 1)
ownership = np.array([14, 22, 35, 46, 49])

# Fit trend
model = LinearRegression()
model.fit(years, ownership)
trend = model.predict(np.array([2011, 2014, 2017, 2021, 2024, 2025, 2026, 2027]).reshape(-1, 1))

# Scenarios
forecast_years = [2025, 2026, 2027]
base = [52, 55, 58]
optimistic = [55, 60, 65]
pessimistic = [50, 51, 52]

print("=== FORECAST 2025-2027 ===")
print(f"{'Year':<10} {'Pessimistic':<15} {'Base':<15} {'Optimistic':<15}")
for i, yr in enumerate(forecast_years):
    print(f"{yr:<10} {pessimistic[i]:<15}% {base[i]:<15}% {optimistic[i]:<15}%")

# Chart
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(years, ownership, 'o-', color='blue', linewidth=3, markersize=12, label='Historical')
ax.plot(forecast_years, base, 's--', color='green', linewidth=2, markersize=10, label='Base Forecast')
ax.plot(forecast_years, optimistic, '^--', color='teal', linewidth=2, markersize=10, label='Optimistic')
ax.plot(forecast_years, pessimistic, 'v--', color='orange', linewidth=2, markersize=10, label='Pessimistic')
ax.fill_between(forecast_years, pessimistic, optimistic, alpha=0.2, color='gray')
ax.axvline(2024, color='red', linestyle=':', alpha=0.5, label='Forecast Start')
ax.set_title('Ethiopia Account Ownership Forecast (2025-2027)')
ax.set_ylabel('Account Ownership (%)')
ax.legend()
plt.tight_layout()
plt.savefig('reports/forecast.png', dpi=150)
print("Forecast chart saved")
print("\nDone")

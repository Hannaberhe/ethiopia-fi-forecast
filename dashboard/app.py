import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Ethiopia Financial Inclusion", layout="wide")
st.title("🇪🇹 Ethiopia Financial Inclusion Forecasting")
st.markdown("Selam Analytics - Dashboard for Stakeholders")

# Key metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Account Ownership (2024)", "49%", "+3pp")
col2.metric("Mobile Money Accounts", "9.45%", "+4.75pp")
col3.metric("Digital Payments", "35%", "Estimated")
col4.metric("2027 Forecast (Base)", "58%", "+9pp")

# Trends tab
tab1, tab2, tab3 = st.tabs(["Trends", "Forecast", "Events"])

with tab1:
    st.subheader("Account Ownership Trajectory")
    years = [2011, 2014, 2017, 2021, 2024]
    values = [14, 22, 35, 46, 49]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(years, values, 'o-', color='blue', linewidth=3, markersize=12)
    ax.set_ylabel('Account Ownership (%)')
    st.pyplot(fig)

with tab2:
    st.subheader("Forecast 2025-2027")
    forecast_years = [2025, 2026, 2027]
    base = [52, 55, 58]
    optimistic = [55, 60, 65]
    pessimistic = [50, 51, 52]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(years, values, 'o-', color='blue', linewidth=3, label='Historical')
    ax.plot(forecast_years, base, 's--', color='green', linewidth=2, label='Base')
    ax.plot(forecast_years, optimistic, '^--', color='teal', linewidth=2, label='Optimistic')
    ax.plot(forecast_years, pessimistic, 'v--', color='orange', linewidth=2, label='Pessimistic')
    ax.fill_between(forecast_years, pessimistic, optimistic, alpha=0.2, color='gray')
    ax.legend()
    ax.set_ylabel('Account Ownership (%)')
    st.pyplot(fig)

with tab3:
    st.subheader("Key Events Timeline")
    events = {
        'Telebirr Launch': '2021-05',
        'Safaricom Entry': '2022-08',
        'M-Pesa Entry': '2023-08',
        'Fayda Digital ID': '2024-01',
        'FX Reform': '2024-07',
        'P2P/ATM Crossover': '2024-10'
    }
    for event, date in events.items():
        st.write(f"**{date}** - {event}")

st.markdown("---")
st.caption("Data sources: Global Findex, NBE, operator reports | Forecast with uncertainty")

import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load mock dataset
df = pd.read_csv("pm25_dataset.csv")

st.title("🌍 Air Pollution Monitoring App")
st.markdown("Monitor PM2.5 pollution levels across multiple cities.")

# City selector
cities = df['city'].unique()
selected_city = st.selectbox("Select a City", cities)

# Filter for selected city
city_data = df[df['city'] == selected_city]

# Line Plot
st.subheader("📈 PM2.5 Over Time")
fig1 = px.line(city_data, x='date', y='pm25', title=f"PM2.5 in {selected_city}")
st.plotly_chart(fig1)

# Heatmap
st.subheader("🌡️ Heatmap of PM2.5 per City")
pivot_df = df.pivot_table(index='date', columns='city', values='pm25')
fig2, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(pivot_df.fillna(0).T, cmap="Reds", ax=ax)
st.pyplot(fig2)

# AQI Category
st.subheader("🏷️ AQI Category Distribution")
df['AQI Category'] = pd.cut(df['pm25'], bins=[0, 50, 100, 150, 200, 300, 500],
                            labels=['Good', 'Moderate', 'Unhealthy for Sensitive', 'Unhealthy', 'Very Unhealthy', 'Hazardous'])
aqi_counts = df['AQI Category'].value_counts().sort_index()
fig3 = px.bar(x=aqi_counts.index.astype(str), y=aqi_counts.values, labels={'x': 'AQI Category', 'y': 'Count'}, title="AQI Category Distribution")
st.plotly_chart(fig3)

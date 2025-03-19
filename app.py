import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data (you can replace this with your actual dataset path)
data = pd.DataFrame([
    {"Gas Name": "SF6", "Dielectric Strength (kV/cm)": 56.0, "GWP": 24300, "Cost ($/kg)": 40},
    {"Gas Name": "Fluoroketones", "Dielectric Strength (kV/cm)": 95.2, "GWP": 1, "Cost ($/kg)": 50},
    {"Gas Name": "G3", "Dielectric Strength (kV/cm)": 123.2, "GWP": 2100, "Cost ($/kg)": 30},
    {"Gas Name": "Heptafluorobutyronitrile", "Dielectric Strength (kV/cm)": 123.2, "GWP": 2750, "Cost ($/kg)": 30},
    {"Gas Name": "CO2", "Dielectric Strength (kV/cm)": 16.8, "GWP": 1, "Cost ($/kg)": 5},
    {"Gas Name": "Nitrogen", "Dielectric Strength (kV/cm)": 20.16, "GWP": 273, "Cost ($/kg)": 3},
])

# Streamlit layout
st.title("Gas Properties Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
selected_gases = st.sidebar.multiselect("Select Gases:", data["Gas Name"].unique(), default=data["Gas Name"].unique())
pressure_factor = st.sidebar.slider("Adjust Pressure Factor:", 0.8, 1.2, 1.0, 0.1)

# Filter data based on selections
filtered_data = data[data["Gas Name"].isin(selected_gases)]
filtered_data["Simulated Strength"] = filtered_data["Dielectric Strength (kV/cm)"] * pressure_factor

# Show filtered data
st.subheader("Filtered Gas Data")
st.dataframe(filtered_data)

# Plot: Simulated Dielectric Strength
st.subheader("Simulated Dielectric Strength")
fig1, ax1 = plt.subplots()
sns.barplot(data=filtered_data, x="Gas Name", y="Simulated Strength", ax=ax1)
ax1.set_title("Simulated Dielectric Strength under Pressure Factor")
ax1.set_xlabel("Gas Name")
ax1.set_ylabel("Simulated Strength (kV/cm)")
st.pyplot(fig1)

# Plot: Global Warming Potential
st.subheader("Global Warming Potential (GWP)")
fig2, ax2 = plt.subplots()
sns.barplot(data=filtered_data, x="Gas Name", y="GWP", ax=ax2, palette="viridis")
ax2.set_title("Global Warming Potential of Selected Gases")
ax2.set_xlabel("Gas Name")
ax2.set_ylabel("GWP")
st.pyplot(fig2)
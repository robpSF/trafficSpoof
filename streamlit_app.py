import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Input example data
data = {
    "Date": ["2024-01", "2024-02", "2024-03", "2024-04", "2024-05"],
    "Traffic": [10000, 15000, 20000, 25000, 30000],
    "Bounce Rate (%)": [50, 48, 47, 45, 44],
    "Avg Visit Duration (s)": [180, 190, 200, 210, 220],
}

demographics = {
    "Gender": ["Male", "Female"],
    "Percentage": [60, 40],
}

age_groups = {
    "Age Group": ["18-24", "25-34", "35-44", "45-54", "55+"],
    "Percentage": [25, 35, 20, 15, 5],
}

# Convert input data to pandas DataFrames
traffic_data = pd.DataFrame(data)
demographics_data = pd.DataFrame(demographics)
age_groups_data = pd.DataFrame(age_groups)

# Streamlit app title
st.title("Website Analytics Dashboard")

# Create a 2x2 grid layout for charts
col1, col2 = st.columns(2)

# Chart 1: Traffic over time
with col1:
    st.subheader("Website Traffic Over Time")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    ax1.plot(traffic_data["Date"], traffic_data["Traffic"], marker="o", label="Traffic")
    ax1.set_title("Website Traffic Over Time")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Traffic")
    ax1.grid(True)
    ax1.legend()
    st.pyplot(fig1)

# Chart 2: Bounce rate over time
with col2:
    st.subheader("Bounce Rate Over Time")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.bar(traffic_data["Date"], traffic_data["Bounce Rate (%)"], color="orange")
    ax2.set_title("Bounce Rate Over Time")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Bounce Rate (%)")
    st.pyplot(fig2)

# Chart 3: Average visit duration over time
with col1:
    st.subheader("Average Visit Duration Over Time")
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    ax3.plot(traffic_data["Date"], traffic_data["Avg Visit Duration (s)"], marker="s", color="green", label="Avg Visit Duration")
    ax3.set_title("Average Visit Duration Over Time")
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Duration (s)")
    ax3.grid(True)
    ax3.legend()
    st.pyplot(fig3)

# Chart 4: Gender distribution
with col2:
    st.subheader("Gender Distribution")
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    ax4.pie(demographics_data["Percentage"], labels=demographics_data["Gender"], autopct="%1.1f%%", startangle=140)
    ax4.set_title("Gender Distribution")
    st.pyplot(fig4)

# Age group distribution (below the grid)
st.subheader("Age Group Distribution")
fig5, ax5 = plt.subplots(figsize=(6, 4))
sns.barplot(x="Age Group", y="Percentage", data=age_groups_data, ax=ax5, palette="muted")
ax5.set_title("Age Group Distribution")
ax5.set_xlabel("Age Group")
ax5.set_ylabel("Percentage")
st.pyplot(fig5)

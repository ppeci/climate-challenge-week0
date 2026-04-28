

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import load_data


df = load_data()

st.title(" African Climate Dashboard")

countries = st.multiselect(
    "Select Countries",
    df["Country"].unique(),
    default=df["Country"].unique()
)

year_range = st.slider(
    "Select Year Range",
    int(df["YEAR"].min()),
    int(df["YEAR"].max()),
    (2015, 2026)
)

variable = st.selectbox(
    "Select Variable",
    ["T2M", "PRECTOTCORR", "RH2M"]
)


filtered = df[
    (df["Country"].isin(countries)) &
    (df["YEAR"] >= year_range[0]) &
    (df["YEAR"] <= year_range[1])
]



st.subheader(" Temperature Trend")

trend = filtered.groupby(["Country","YEAR"])[variable].mean().reset_index()

fig, ax = plt.subplots()

for c in countries:
    data = trend[trend["Country"] == c]
    ax.plot(data["YEAR"], data[variable], label=c)

ax.legend()
st.pyplot(fig)

st.subheader(" Distribution")

fig2, ax2 = plt.subplots()
sns.boxplot(x="Country", y=variable, data=filtered, ax=ax2)

st.pyplot(fig2)
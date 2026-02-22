import streamlit as st
import pandas as pd

st.set_page_config(page_title="Signal Scout", layout="wide")

st.title("📡 Signal Scout Dashboard")

df = pd.read_csv("output.csv")

st.sidebar.header("Filters")

category_filter = st.sidebar.multiselect(
    "Filter by Category",
    options=df["category_tag"].unique(),
    default=df["category_tag"].unique()
)

source_filter = st.sidebar.multiselect(
    "Filter by Source",
    options=df["source_name"].unique(),
    default=df["source_name"].unique()
)

filtered_df = df[
    (df["category_tag"].isin(category_filter)) &
    (df["source_name"].isin(source_filter))
]

search = st.text_input("Search by keyword")

if search:
    filtered_df = filtered_df[
        filtered_df["entity_name"].str.contains(search, case=False)
    ]

filtered_df = filtered_df.sort_values(by="confidence", ascending=False)

st.write(f"Showing {len(filtered_df)} signals")

st.dataframe(filtered_df, use_container_width=True)
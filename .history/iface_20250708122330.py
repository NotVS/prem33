import streamlit as st
import numpy as np 

from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

import pandas as pd


# Download latest version
path = "C:\\Users\\Lenovo\\Downloads\\archive (3)\\premier-player-23-24.csv"
dataframe = pd.read_csv(path)


st.title("Database UI")
st.header("Premier League Dataset")
st.header("Filter out data based on categories")

# display dataframe
st.dataframe(dataframe)

# Filtering out data based on selected categories
st.sidebar("Filter Options")

# placing a new markdown in the sidebar
if st.sidebar.markdown("")

st.subheader("Filter by Team")
st.selectbox("Choose Club", dataframe['Team'].unique())


st.subheader("Filter by Position")
st.selectbox("Choose Position", dataframe['Pos'].unique())

st.subheader("Filter by Player Name")
st.text_input("Enter Player Name", placeholder = "e.g Mohammed Salah")

st.subheader("Filter by Nation")
st.text_input("Enter Nation", placeholder = "e.g  eng ENG")


# downloading dataset as a CSV file
st.download_button(label = "Download CSV",
                   data = dataframe.to_csv().encode('utf-8'),
                   file_name = "premier-player-23-24.csv",
                   mime = "text/csv")

## Tinkering with Streamlit
st.markdown("## Markdown Example")
# st.badge("Arsenal")
st.caption("Yeah bro... pack it up")
st.divider("## Divider Example")
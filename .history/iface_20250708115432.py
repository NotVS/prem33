import streamlit as st
import numpy as np 
import pandas as pd

# Download latest version
path = "


st.title("Database UI")
st.header("Premier League Dataset")
st.header("Filter out data based on categories")

# display dataframe
st.dataframe(dataframe)

# Filtering out data based on selected categories

st.subheader("Filter by Team")


# downloading dataset as a CSV file
st.download_button(label = "Download CSV",
                   data = dataframe.to_csv().encode('utf-8'),
                   file_name = "epldata_final.csv",
                   mime = "text/csv")

## Tinkering with Streamlit
st.markdown("## Markdown Example")
st.badge("Arsenal")
st.caption("Yeah bro... pack it up")
st.divider("## Divider Example")
import streamlit as st
import numpy as np 
import pandas as pd

import kagglehub

# Download latest version
path = "C:/Users/Lenovo/Downloads/archive(2)/epldata_final.csv"
dataframe = pd.read_csv(path + "/players.csv")


st.title("Database UI")
st.header("Premier League Dataset")
st.header("Filter out data based on categories")

# display dataframe
st.dataframe(dataframe)


## Tinkering with Streamlit
st.markdown("## Markdown Example")
st.badge("Arsenal")
st.caption("Yeah bro... pack it up")
st.divider("## Divider Example")
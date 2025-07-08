import streamlit as st
import numpy as np 
import pandas as pd

import kagglehub

# Download latest version
path = kagglehub.dataset_download("mauryashubham/english-premier-league-players-dataset")
dataframe = pd.read_csv(path + "/players.csv")

print("Path to dataset files:", path)

st.title("Database UI")
st.header("Premier League Dataset")
st.header("Filter out data based on categories")



## Tinkering with Streamlit
st.markdown("## Markdown Example")
st.badge("Arsenal")
st.caption("Yeah bro... pack it up")
st.divider("## Divider Example")
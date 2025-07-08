import streamlit as st
import pandas as pd

path = "C:\\Users\\Lenovo\\Downloads\\archive (3)\\premier-player-23-24.csv"
dataframe = pd.read_csv(path)

st.title("Data Analysis")
st.header("Data Analysis - Create Charts")

# Dataframe for analysis
filtered_dataframe = dataframe.copy()



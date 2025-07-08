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
st.sidebar.markdown("## Filter Options")

st.sidebar.subheader("Filter by Club")
selected_club = st.sidebar.selectbox("Choose Club", dataframe['Team'].unique())


st.sidebar.subheader("Filter by Position")
selected_position = st.sidebar.selectbox("Choose Position", dataframe['Pos'].unique())

st.sidebar.subheader("Filter by Player Name")
selected_player = (st.sidebar.text_input("Enter Player Name", placeholder = "e.g Mohammed Salah")).lower()

st.sidebar.subheader("Filter by Nation")
selected_nation = st.sidebar.text_input("Enter Nation", placeholder = "e.g  eng ENG")

def filter_dataframe(df, selected_club, selected_position, selected_player, selected_nation):
    filtered_df = df.copy()
    
    if selected_club:
        filtered_df = filtered_df[filtered_df['Team'] == selected_club]
        
    if selected_position:
        filtered_df = filtered_df[filtered_df['Pos'] == selected_position]
        
    if selected_player:
        filtered_df = filtered_df[filtered_df['Player']

# downloading dataset as a CSV file
st.download_button(label = "Download CSV",
                   data = dataframe.to_csv().encode('utf-8'),
                   file_name = "premier-player-23-24.csv",
                   mime = "text/csv")


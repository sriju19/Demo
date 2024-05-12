import streamlit as st
import pandas as pd
import numpy as np
st.title("hello")
data= pd.read_csv("/Users/gvsrijanreddy/Desktop/data sets/weather_data.csv")
st.dataframe(data)
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
import streamlit as st 
import pandas as pd

st.title("Data Integration")

file = st.file_uploader("Upload your file",["CSV"])

if file:
    data = pd.read_csv(file)
    st.header("Your data")
    st.write(data)
    year = st.slider("Experience_Year",0,10,1)
    filter_data = data[data["Experience_Years"] == year]    
    st.dataframe(filter_data)
    
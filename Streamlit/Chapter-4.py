import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Integration")

file = st.file_uploader("Upload your file",["CSV"])


if file:
    data = pd.read_csv(file)
    st.header("Your data")
    st.write(data)
    year = st.slider("Experience_Year",0,10,1)
    filter_data = data[data["Experience_Years"] == year]    
    st.dataframe(filter_data)
    
    st.header("Salary Distribution (Matplotlib)")
    fig, ax = plt.subplots()
    ax.hist(filter_data["Salary"], bins=20, color='skyblue', edgecolor='black')
    ax.set_xlabel("Salary")
    ax.set_ylabel("Count")
    ax.set_title(f"Salary Distribution for {year} Years Experience")
    st.pyplot(fig)

import streamlit as st 
import requests

st.title("Live Currency Converter")
amount = st.number_input("Enter valur",min_value=1)
convert = st.selectbox("Currency",["USD","EUR","GPP","JPY"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][convert]
        value = amount*rate
        st.success(f"Amount {amount} INR Converted to {value:.2f} {convert}")
    else:
        st.error("Faild to fetch conversion rate")
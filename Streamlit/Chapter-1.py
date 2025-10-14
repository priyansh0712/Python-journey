import streamlit as st

st.title("Title : Hello")
st.subheader("Subheader : Streamlit")
st.text("Text : Welcome to first Streamlit Web Application")
st.write("Normal Writing : Hello, I'm learning streamlit from sractch")

sport = st.selectbox("Your fav Sport : ",["Cricket","Football","Hockey","Kabbadi"])
st.write(f"You Selected {sport}.")
st.success(f"Selected {sport} Successfully.")
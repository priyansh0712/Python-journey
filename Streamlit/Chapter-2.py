import streamlit as st 

st.title("Chai Maker App")

name = st.text_input("Enter your name : ")
if name:
    st.write(f"Welcome {name} !")

dob = st.date_input("select DOB : ")

cups = st.number_input("Number of cups : ",min_value=1,max_value=10,step=1)

Type = st.radio("Select your base : ",["Milk","Water"])

flavour = st.selectbox("Select Flavour : ",["Adrak", "Kesar", "Tulsi"]) 

sugar_masala = st.slider("Sugar lavel(Spoon) : ",0,5,2)

masala = st.checkbox("Add Masala")

if st.button("Make Chai"):
    st.success("Your chai is being brewed")
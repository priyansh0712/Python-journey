import streamlit as st 
from PIL import Image

st.title("Chai Test Poll")

# Columns & Images

col1 , col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/5946614/pexels-photo-5946614.jpeg",width=250)
    vote1=st.button("Vote for masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/29054033/pexels-photo-29054033.jpeg",width=250)
    vote2=st.button("vote for Adrak chai")
    
if vote1:
    st.success("Thakns for voting masala chai")
elif vote2:
    st.success("THanks for Adrak chai")
    
# Optional for image height,width

st.header("Resize the image with PTL library")
img = Image.open(r"C:\Users\Priyansh\Downloads\glass-cola-with-ice.jpg")
img = img.resize((300,300))
st.image(img)

# Side Bar

st.sidebar.text_input("Enter your name")
st.sidebar.selectbox("Chai",["Masala","Adrak","Kesar"])

#Expander

with st.expander("Show Instruction"):
    st.write("""
        1. Boil Water with tea leaves
        2. Add Milk
        3. Serve It          
    """)

#Mark_Down

st.markdown("# Welcome")
st.markdown("> Hello")
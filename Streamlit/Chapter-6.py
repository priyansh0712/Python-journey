import streamlit as st

# Initialize page state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Function to update page
def navigate_to(page):
    st.session_state.page = page
    st.rerun()        # Forces instant rerender

# HOME PAGE
if st.session_state.page == 'home':
    st.title("Home Page")
    if st.button("Go to About"):
        navigate_to("about")
    if st.button("Go to Contact"):
        navigate_to("contact")

# ABOUT PAGE
elif st.session_state.page == 'about':
    st.title("About Page")
    if st.button("Back to Home"):
        navigate_to("home")

# CONTACT PAGE
elif st.session_state.page == 'contact':
    st.title("Contact Page")
    if st.button("Back to Home"):
        navigate_to("home")

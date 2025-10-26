import streamlit as st
from pages import page1, page2,page3
from utils import load_custom_css

# Load custom CSS
load_custom_css()

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'page1'

# Initialize random position for No button
if 'no_button_pos' not in st.session_state:
    st.session_state.no_button_pos = 0

# Page routing
if st.session_state.page == 'page1':
    page1.show()
elif st.session_state.page == 'page2':
    page2.show()
elif st.session_state.page == 'page3':
    page3.show()
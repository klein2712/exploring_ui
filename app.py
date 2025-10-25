import streamlit as st
import random

# Custom CSS for warm and charming design
st.markdown("""
    <style>
    /* Main background with gradient */
    .stApp {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    }
    
    /* Custom font */
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
    }
    
    /* Style buttons */
    .stButton>button {
        background-color: #ff9a9e;
        color: white;
        border-radius: 25px;
        border: none;
        padding: 15px 30px;
        font-size: 18px;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(255, 154, 158, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #fad0c4;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 154, 158, 0.6);
    }
    
    /* Title styling */
    h1 {
        color: #ff6b6b;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        font-weight: 700;
    }
    
    /* Card-like container */
    .main-container {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 30px;
        padding: 40px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        margin: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'page1'

# Initialize random position for No button
if 'no_button_pos' not in st.session_state:
    st.session_state.no_button_pos = 0

def go_to_page2():
    st.session_state.page = 'page2'

def move_no_button():
    # Generate new random position (0-9 for different layouts)
    st.session_state.no_button_pos = random.randint(0, 9)

# PAGE 1
if st.session_state.page == 'page1':
    
    st.markdown("<h1 style='text-align: center; font-size: 72px;'>✨ Willst du mit mir auf ein Date gehen? ✨</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px; color: #666;'>Make your choice!</p>", unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    # Create columns for button placement
    cols = st.columns(10)
    
    # Place Yes button in a fixed position
    with cols[4]:
        if st.button("Jaa💖", key="yes_btn", use_container_width=True):
            go_to_page2()
    
    no_pos = st.session_state.no_button_pos
    with cols[no_pos]:
        if st.button("Nein..", key="no_btn", use_container_width=True, on_click=move_no_button):
            pass
    
    st.markdown("</div>", unsafe_allow_html=True)

# PAGE 2
elif st.session_state.page == 'page2':
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>🎉 Page 2 🎉</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 24px; color: #ff9a9e;'>Yay! You clicked Yes!</p>", unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("← Back to Page 1", use_container_width=True):
            st.session_state.page = 'page1'
    
    st.markdown("</div>", unsafe_allow_html=True)
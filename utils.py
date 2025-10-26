import streamlit as st

def load_custom_css():
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

import streamlit as st
import random
import base64

st.set_page_config(
    page_title="Date App",
    layout="wide",  # "centered" or "wide"
    initial_sidebar_state="collapsed"
)

def go_to_page2():
    st.session_state.page = 'page2'

# List of strings to display when "Nein.." or "Vielleicht" is clicked
response_strings = [
    "Oh.. der Button funktioniert nicht richtig 😿",
    "Hat nicht geklappt, versuch's nochmal!",
    "Glaube hab vergessen den Button zu programmieren... 🙀",
    "Hab nicht hingeschaut, probier's nochmal! 🐱",
    "Ups, da ist was schiefgelaufen... 😿",
    "Klick nochmal, vielleicht klappt's dann ja! 🐾",
    "Der Button ist ein bisschen schüchtern... Versuch's nochmal! 🐈",
    "Achtung, der Button löst Katzenallergie aus!",
    "Der Button ist gerade auf Kaffeepause ☕",
    "Der Button hat gerade eine Identitätskrise...",
    "Der Button ist im Urlaub und kann nicht antworten.",
    "Der Button ist gerade auf einer Mission und kann nicht gestört werden.",
    "Der Button ist wohl kaputt.. Probiers mal mit dem 'Jaa💖' Button hihi",
]

def show():
    # Title centered and doesn't wrap
    st.markdown("<p style='text-align: center; font-size: 38px; color: #666;'>✨ Willst du mit mir auf ein Date gehen? ✨</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px; color: #666;'>Du hast die freie Wahl</p>", unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    # Buttons in one row with better spacing
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1], gap="small")
    
    # Place Yes button
    with col2:
        if st.button("Jaa💖", key="yes_btn", use_container_width=True):
            go_to_page2()
    
    # Place No button
    with col3:
        if st.button("Nein..", key="no_btn", use_container_width=True):
            # Pick a random response string to display
            st.session_state.response = random.choice(response_strings)
    
    # Place Vielleicht button
    with col4:
        if st.button("Vielleicht", key="maybe_btn", use_container_width=True):
            st.session_state.response = random.choice(response_strings)
    
    st.write("")
    st.write("")
    
    # Display response string if set
    if "response" in st.session_state:
        st.markdown(
            f"<p style='text-align: center; font-size: 22px; color: #888;'>{st.session_state.response}</p>",
            unsafe_allow_html=True
        )
    
    # GIF display with base64 encoding
    gif_path = "./cat_gifs/bubble_tea_cat.gif"  # Replace with your actual gif path
    
    try:
        with open(gif_path, "rb") as f:
            contents = f.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        
        st.markdown(
            f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url}" alt="animated gif" width="400"></div>',
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning(f"GIF not found at: {gif_path}")

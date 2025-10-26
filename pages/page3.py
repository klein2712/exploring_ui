import streamlit as st
import random
import base64
import os
import time

def show():
    st.markdown("<h1 style='text-align: center;'>🌸 Du willst Blumen? Dann drück den Button 🌸 (ist auch der letzte, versprochen) </h1>", unsafe_allow_html=True)

    if st.button("🌸 Blumen für dich 🌸", key="final_flowers_btn", use_container_width=True):
        st.session_state.flowers_started = True

    if st.session_state.get("flowers_started", False):
        # Progress bar with warm charming color
        progress_bar = st.progress(0)
        status_text = st.empty()
        gif_placeholder = st.empty()
        
        # Step 1: Show message and wait 3 seconds
        status_text.markdown("<p style='text-align: center; font-size: 22px; color: #ff9a9e;'>Okay du willst Blumen.. dann lass mich kurz welche wachsen lassen :)</p>", unsafe_allow_html=True)
        progress_bar.progress(16, text="🌱 Vorbereitung...")
        time.sleep(3)
        
        # Step 2: Kaufe Blumensamen
        status_text.markdown("<p style='text-align: center; font-size: 22px; color: #ff9a9e;'>Kaufe Blumensamen...</p>", unsafe_allow_html=True)
        progress_bar.progress(33, text="🛒 Samen kaufen...")
        time.sleep(3)
        
        # Step 3: Planze Samen
        status_text.markdown("<p style='text-align: center; font-size: 22px; color: #ff9a9e;'>Pflanze Samen...</p>", unsafe_allow_html=True)
        progress_bar.progress(50, text="🌱 Samen pflanzen...")
        time.sleep(3)
        
        # Step 4: Bewässer die Blumen
        status_text.markdown("<p style='text-align: center; font-size: 22px; color: #ff9a9e;'>Bewässer nun die Blumen..</p>", unsafe_allow_html=True)
        progress_bar.progress(66, text="💧 Blumen gießen...")
        # Show gardening gif
        gardening_gif_path = "./cat_gifs/gardening_flowers.gif"
        try:
            with open(gardening_gif_path, "rb") as f:
                contents = f.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            gif_placeholder.markdown(
                f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url}" alt="gardening cat gif" width="400"></div>',
                unsafe_allow_html=True
            )
        except FileNotFoundError:
            gif_placeholder.warning(f"GIF not found at: {gardening_gif_path}")
        
        time.sleep(5)
        
        # Step 5: Pflücke Blumen
        status_text.markdown("<p style='text-align: center; font-size: 22px; color: #ff9a9e;'>Pflücke Blumen...</p>", unsafe_allow_html=True)
        progress_bar.progress(83, text="💐 Blumen pflücken...")
        gif_placeholder.empty()
        time.sleep(3)
        
        # Step 6: Hier sind deine Blumen
        status_text.markdown("<p style='text-align: center; font-size: 22px; color: #ff9a9e;'>Hier sind deine Blumen 💐</p>", unsafe_allow_html=True)
        progress_bar.progress(100, text="✨ Fertig!")
        
        # Show flower cat gif
        flower_gif_path = "./cat_gifs/flower_cat.gif"
        try:
            with open(flower_gif_path, "rb") as f:
                contents = f.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            gif_placeholder.markdown(
                f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url}" alt="flower cat gif" width="400"></div>',
                unsafe_allow_html=True
            )
        except FileNotFoundError:
            gif_placeholder.warning(f"GIF not found at: {flower_gif_path}")

    st.markdown("<p style='text-align: center; font-size: 24px; color: #ff9a9e;'>Danke, dass du mich auf ein Date eingeladen hast! 💖</p>", unsafe_allow_html=True)


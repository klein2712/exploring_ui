import streamlit as st
import os
import random
import base64
def go_to_page3():
    st.session_state.page = 'page3'
def show():
    st.markdown("<h1 style='text-align: center;'>🎉 yay 🎉</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 24px; color: #ff9a9e;'>Du hast auf (freiwillig) Ja gedrückt💖</p>", unsafe_allow_html=True)
    
    # Show a random gif from /cat_gifs/happy_gifs/
    happy_gifs_dir = "./cat_gifs/happy_gifs/"

    gif_files = [f for f in os.listdir(happy_gifs_dir) if f.lower().endswith('.gif')]
    if gif_files:
        selected_gif = random.choice(gif_files)
        gif_path = os.path.join(happy_gifs_dir, selected_gif)
        with open(gif_path, "rb") as f:
                contents = f.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        st.markdown(
            f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url}" alt="happy cat gif" width="400"></div>',
            unsafe_allow_html=True
        )
    st.write("")
    st.markdown("<p style='text-align: center; font-size: 20px; color: #666;'>Was möchtest du als erstes Date tun?</p>", unsafe_allow_html=True)
    col2, col3, col4 = st.columns([1, 1, 1], gap="small")
    # Filmabend Button
    with col2:
        if st.button("Filmabend mit Kuscheldecke", use_container_width=True):
            st.session_state.trip_clicked = False
            st.session_state.museum_clicked = False
            st.session_state.filmabend_clicked = True
    
    # Tagestrip Button
    with col3:
        if st.button("Tagestrip in eine andere Stadt", use_container_width=True):
            st.session_state.trip_clicked = True
            st.session_state.museum_clicked = False
            st.session_state.filmabend_clicked = False

    # Museum Button
    with col4:
        if st.button("Museum besuchen", use_container_width=True):
            st.session_state.trip_clicked = False
            st.session_state.museum_clicked = True
            st.session_state.filmabend_clicked = False

    # Show filmabend content if clicked
    if st.session_state.get("filmabend_clicked", False):
        answer = "Gute Wahl, bei der Kälte genau das richtige.. am besten noch mit Tee und Snacks 🍵"
        st.markdown(f"<div style='text-align: center; font-size: 22px; color: #888;'>{answer}</div>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(f"<div style='text-align: center; font-size: 22px; color: #888;'>Schöne Idee! Mach am besten davon ein Screenshot und schicks mir, ich hab leider kein Plan wie ich die das was du eingegeben hast sonst sehen kann haha</div>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(f"<div style='text-align: center; font-size: 22px; color: #888;'>Bonus: Wenn du Blumen möchtest, dann klick hier!</div>", unsafe_allow_html=True)
        if st.button("🌸 Blumen für dich 🌸", key="filmabend_flowers_btn", use_container_width=True):
            go_to_page3()

    # Show text input only for Tagestrip
    if st.session_state.get("trip_clicked", False):
        answer = "Klingt nach nem Abenteuer! Wo solls hingehen?"
        st.markdown(f"<div style='text-align: center; font-size: 22px; color: #888;'>{answer}</div>", unsafe_allow_html=True)
        user_input = col3.text_input("Deine Wunschstadt oder Idee:", key="trip_idea_persist")
        if user_input:
            st.markdown(f"<div style='text-align: center; font-size: 20px; color: #ff9a9e;'>Aha <b>{user_input}</b> also, nicht schlecht </div>", unsafe_allow_html=True)
            st.markdown("---")
            st.markdown(f"<div style='text-align: center; font-size: 22px; color: #888;'>Schöne Idee! Mach am besten davon ein Screenshot und schicks mir, ich hab leider kein Plan wie ich die das was du eingegeben hast sonst sehen kann haha</div>", unsafe_allow_html=True)
            st.markdown("---")
            st.markdown(f"<div style='text-align: center; font-size: 22px; color: #888;'>Bonus: Wenn du Blumen möchtest, dann klick hier!</div>", unsafe_allow_html=True)
            if st.button("🌸 Blumen für dich 🌸", key="trip_flowers_btn", use_container_width=True):
                go_to_page3()

    # Show museum content if clicked
    if st.session_state.get("museum_clicked", False):
        answer = "Klingt gut, dann kannst du mir was über Kunst beibringen haha"
        st.markdown(f"<div style='text-align: center; font-size: 22px; color: #888;'>{answer}</div>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(f"<div style='text-align: center; font-size: 22px; color: #888;'>Schöne Idee! Mach am besten davon ein Screenshot und schicks mir, ich hab leider kein Plan wie ich die das was du eingegeben hast sonst sehen kann haha</div>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(f"<div style='text-align: center; font-size: 22px; color: #888;'>Bonus: Wenn du Blumen möchtest, dann klick hier!</div>", unsafe_allow_html=True)
        if st.button("🌸 Blumen für dich 🌸", key="museum_flowers_btn", use_container_width=True):
            go_to_page3()

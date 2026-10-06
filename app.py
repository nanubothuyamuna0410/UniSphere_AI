import streamlit as st
import os

st.set_page_config(page_title="UniSphere AI", page_icon="🎓", layout="wide")

css_path = os.path.join("assets", "style.css")
if os.path.exists(css_path):
    with open(css_path, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if not st.session_state.get("logged_in"):
    st.title("🎓 UniSphere AI")
    st.subheader("Your Intelligent University Information Assistant")
    st.write("Please login to access the UniSphere AI platform.")
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🤖 AI Assistant\n\nAsk questions about your university.")
    with col2:
        st.info("📚 RAG Knowledge Base\n\nGet answers from university documents.")
    with col3:
        st.info("🎤 Voice Assistant\n\nInteract with the AI using your voice.")
    if st.button("🔐 Go to Login", use_container_width=True):
        st.switch_page("pages/login.py")
    st.divider()
    st.caption("UniSphere AI • RAG + ChromaDB + Llama 3.2")
    st.stop()

role = st.session_state.get("role")
if role == "student":
    st.switch_page("pages/student.py")
elif role == "admin":
    st.switch_page("pages/admin.py")
else:
    st.session_state.clear()
    st.switch_page("pages/login.py")

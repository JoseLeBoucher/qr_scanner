import streamlit as st

st.title("Test d'OpenCV")

try:
    import cv2
    st.write(f"OpenCV version: {cv2.__version__}")
except ImportError as e:
    st.error(f"Erreur lors de l'importation de cv2: {e}")

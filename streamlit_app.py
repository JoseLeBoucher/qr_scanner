import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Scanner de Codes-Barres avec Streamlit")
st.write("Utilisez votre caméra pour détecter automatiquement des codes-barres.")

# Widget pour capturer une image depuis la caméra
uploaded_image = st.camera_input("Activez votre caméra et prenez une photo")

# Initialiser BarcodeDetector
barcode_detector = cv2.barcode_BarcodeDetector()

def detect_barcodes(image):
    """
    Détecte et décode les codes-barres dans une image.

    Args:
        image (PIL.Image): Image capturée via le widget caméra.

    Returns:
        list: Liste des données des codes-barres détectés.
    """
    # Convertir l'image PIL en tableau NumPy (OpenCV)
    image_np = np.array(image)
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Détecter et décoder les codes-barres
    ok, decoded_info, _, _ = barcode_detector.detectAndDecode(image_cv)
    if ok:
        return decoded_info
    return []

if uploaded_image:
    # Charger l'image capturée
    image = Image.open(uploaded_image)
    st.image(image, caption="Image Capturée", use_column_width=True)

    # Détecter les codes-barres
    detected_barcodes = detect_barcodes(image)

    # Afficher les résultats
    if detected_barcodes:
        st.success(f"Codes détectés : {', '.join(detected_barcodes)}")
    else:
        st.warning("Aucun code-barres détecté. Essayez de réajuster l'image.")

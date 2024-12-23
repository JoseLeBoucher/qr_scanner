import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Scanner de Codes-Barres avec Streamlit et OpenCV")
st.write("Activez votre caméra pour détecter des codes-barres automatiquement.")

# Charger l'entrée de la caméra en continu
frame_placeholder = st.empty()  # Placeholder pour afficher les frames
barcode_result = st.empty()  # Placeholder pour afficher le résultat

# Démarrer la caméra
video_capture = cv2.VideoCapture(0)  # Utiliser la caméra par défaut (id=0)

# Initialiser BarcodeDetector
barcode_detector = cv2.barcode_BarcodeDetector()

# Fonction de détection de codes-barres
def detect_barcodes(frame):
    """
    Détecte et décode les codes-barres dans une frame.

    Args:
        frame (numpy.ndarray): Image capturée de la caméra.

    Returns:
        list: Liste des données des codes-barres détectés.
    """
    ok, decoded_info, _, _ = barcode_detector.detectAndDecode(frame)
    if ok:
        return decoded_info
    return []

# Boucle pour capturer les frames de la caméra
while True:
    ret, frame = video_capture.read()
    if not ret:
        st.error("Erreur : impossible d'accéder à la caméra.")
        break

    # Convertir la frame en RGB pour l'affichage dans Streamlit
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Détecter les codes-barres dans la frame
    detected_barcodes = detect_barcodes(frame)

    # Afficher les résultats
    if detected_barcodes:
        barcode_result.success(f"Codes détectés : {', '.join(detected_barcodes)}")
    else:
        barcode_result.warning("Aucun code-barres détecté.")

    # Afficher la vidéo dans Streamlit
    frame_placeholder.image(rgb_frame, channels="RGB")

# Libérer les ressources
video_capture.release()

import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.title("Scanner de Codes-Barres avec Streamlit et OpenCV")
st.write("Utilisez la caméra de votre téléphone pour scanner un code-barres. Le code sera détecté automatiquement.")

# Utiliser le widget camera_input pour capturer une image
uploaded_image = st.camera_input("Prenez une photo du code-barres")

def decode_barcode(image):
    """
    Détecte et décode les codes-barres dans une image en utilisant OpenCV BarcodeDetector.

    Args:
        image (PIL.Image): Image capturée.

    Returns:
        list: Liste des données décodées des codes-barres.
    """
    # Convertir l'image PIL en format OpenCV (BGR)
    cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Initialiser le détecteur de codes-barres
    barcode_detector = cv2.barcode_BarcodeDetector()

    # Détecter et décoder les codes-barres
    ok, decoded_info, decoded_type, corners = barcode_detector.detectAndDecode(cv_image)

    if ok:
        return decoded_info
    else:
        return []

if uploaded_image is not None:
    try:
        # Ouvrir l'image avec PIL
        image = Image.open(uploaded_image)
        st.image(image, caption='Image Capturée', use_column_width=True)

        # Détecter et décoder les codes-barres
        barcodes = decode_barcode(image)

        if barcodes:
            st.success(f"**{len(barcodes)} code(s) barre détecté(s) :**")
            for idx, barcode_data in enumerate(barcodes, start=1):
                st.write(f"**Code-barres {idx} :** {barcode_data}")
        else:
            st.error("Aucun code-barres détecté. Veuillez réessayer.")
    except Exception as e:
        st.error(f"Une erreur est survenue lors du traitement de l'image : {e}")

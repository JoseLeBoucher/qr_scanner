import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.title("Scanner de Code-Barres avec Streamlit et OpenCV")
st.write("Utilisez la caméra de votre téléphone pour scanner un code-barres.")

# Utiliser le widget camera_input pour capturer une image
uploaded_image = st.camera_input("Prenez une photo du code-barres")


def decode_qr(image):
    """
    Détecte et décode un code QR dans une image.

    Args:
        image (PIL.Image): Image capturée.

    Returns:
        str: Données décodées du QR code, ou chaîne vide si aucun QR code détecté.
    """
    # Convertir l'image PIL en format OpenCV
    cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    qr_decoder = cv2.QRCodeDetector()
    data, bbox, _ = qr_decoder.detectAndDecode(cv_image)
    return data


if uploaded_image is not None:
    try:
        # Ouvrir l'image avec PIL
        image = Image.open(uploaded_image)
        st.image(image, caption='Image Capturée', use_column_width=True)

        # Détecter et décoder le code QR
        code = decode_qr(image)

        if code:
            st.success(f"**Code QR détecté :** {code}")
        else:
            st.error("Aucun code QR détecté. Veuillez réessayer.")
    except Exception as e:
        st.error(f"Une erreur est survenue lors du traitement de l'image : {e}")

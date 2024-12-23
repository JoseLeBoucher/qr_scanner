import streamlit as st
from PIL import Image
import numpy as np
from pyzbar.pyzbar import decode

st.title("Scanner de Code-Barres avec Streamlit et Pyzbar")
st.write("Utilisez la caméra de votre téléphone pour scanner un code-barres. Le code sera détecté automatiquement.")

# Utiliser le widget camera_input pour capturer une image
uploaded_image = st.camera_input("Prenez une photo du code-barres")


def decode_barcode(image):
    """
    Détecte et décode les codes-barres dans une image.

    Args:
        image (PIL.Image): Image capturée.

    Returns:
        list: Liste des données décodées des codes-barres.
    """
    # Convertir l'image PIL en format RGB
    img = image.convert('RGB')
    # Convertir l'image en tableau NumPy
    np_image = np.array(img)
    # Décoder les codes-barres présents dans l'image
    barcodes = decode(np_image)
    return barcodes


if uploaded_image is not None:
    try:
        # Ouvrir l'image avec PIL
        image = Image.open(uploaded_image)
        st.image(image, caption='Image Capturée', use_column_width=True)

        # Détecter et décoder les codes-barres
        barcodes = decode_barcode(image)

        if barcodes:
            st.success(f"**{len(barcodes)} code(s) barres détecté(s) :**")
            for idx, barcode in enumerate(barcodes, start=1):
                barcode_data = barcode.data.decode('utf-8')
                barcode_type = barcode.type
                st.write(f"**Code-barres {idx} :** {barcode_data} ({barcode_type})")
        else:
            st.error("Aucun code-barres détecté. Veuillez réessayer.")
    except Exception as e:
        st.error(f"Une erreur est survenue lors du traitement de l'image : {e}")

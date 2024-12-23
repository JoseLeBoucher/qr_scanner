import streamlit as st
from PIL import Image
from pyzbar.pyzbar import decode

st.title("Scanner de Code-Barres avec Streamlit")
st.write("Utilisez la caméra de votre téléphone pour scanner un code-barres.")

# Utiliser le widget camera_input pour capturer une image
uploaded_image = st.camera_input("Prenez une photo du code-barres")

if uploaded_image is not None:
    # Ouvrir l'image avec PIL
    image = Image.open(uploaded_image)
    st.image(image, caption='Image capturée', use_column_width=True)

    # Décoder les codes-barres présents dans l'image
    codes = decode(image)

    if codes:
        for idx, code in enumerate(codes, start=1):
            st.success(f"**Code-barres {idx} :** {code.data.decode('utf-8')}")
    else:
        st.error("Aucun code-barres détecté. Veuillez réessayer.")

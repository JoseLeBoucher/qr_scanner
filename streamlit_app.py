import streamlit as st
from PIL import Image
import numpy as np
import cv2
from pyzbar.pyzbar import decode

st.set_page_config(page_title="Scanner de QR Code", layout="centered")

st.title("📷 Scanner de QR Code avec Streamlit")

st.write("Cliquez sur le bouton ci-dessous pour capturer une image et scanner un QR code.")

# Bouton pour capturer une image depuis la caméra
captured_image = st.camera_input("Prenez une photo")

if captured_image:
    # Afficher l'image capturée
    st.image(captured_image, caption='Image Capturée', use_column_width=True)

    # Convertir l'image en format utilisable par OpenCV
    image = Image.open(captured_image)
    image_np = np.array(image.convert('RGB'))
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Scanner le QR code
    decoded_objects = decode(image_cv)

    if decoded_objects:
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            st.success(f"🔍 QR Code Scanné: {qr_data}")
            # Optionnel: Afficher un encadré autour du QR code détecté
            points = obj.polygon
            if len(points) > 4:  # Si le QR code est dessiné avec plus de 4 points
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                hull = list(map(tuple, np.squeeze(hull)))
            else:
                hull = points
            n = len(hull)
            for j in range(0, n):
                cv2.line(image_cv, hull[j], hull[(j + 1) % n], (0, 255, 0), 3)

        # Afficher l'image avec le QR code encadré
        st.image(cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB), caption='QR Code détecté', use_column_width=True)
    else:
        st.error("❌ Aucun QR Code détecté. Veuillez réessayer.")

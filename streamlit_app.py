import streamlit as st
from PIL import Image, ImageDraw
import numpy as np
from pyzbar.pyzbar import decode

st.set_page_config(page_title="Scanner de QR Code", layout="centered")

st.title("📷 Scanner de QR Code avec Streamlit")

st.write("Cliquez sur le bouton ci-dessous pour capturer une image et scanner un QR code.")

# Bouton pour capturer une image depuis la caméra
captured_image = st.camera_input("Prenez une photo")

if captured_image:
    # Afficher l'image capturée
    st.image(captured_image, caption='Image Capturée', use_column_width=True)

    # Ouvrir l'image avec PIL
    image = Image.open(captured_image).convert('RGB')
    draw = ImageDraw.Draw(image)

    # Scanner le QR code
    decoded_objects = decode(image)

    if decoded_objects:
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            st.success(f"🔍 QR Code Scanné: {qr_data}")

            # Dessiner un encadré autour du QR code détecté
            points = obj.polygon

            # Si le QR code est dessiné avec plus de 4 points, approximer un rectangle
            if len(points) > 4:
                hull = []
                for point in points:
                    hull.append((point.x, point.y))
                points = hull

            # Dessiner les lignes du polygone
            draw.line(points + [points[0]], fill='green', width=3)

        # Afficher l'image avec les encadrés
        st.image(image, caption='QR Code détecté', use_column_width=True)
    else:
        st.error("❌ Aucun QR Code détecté. Veuillez réessayer.")

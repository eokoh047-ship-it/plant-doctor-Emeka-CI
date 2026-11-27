import streamlit as st
import urllib.parse
import os

WHATSAPP_NUMBER = "225508032267"

st.set_page_config(page_title="EMEKA Plant Doctor CI", page_icon="🌿")
st.title("🌱 PlantDoctor CI - Emeka")
st.write("Diagnose your crop / Diagnostiquez votre culture")
st.write("📞 WhatsApp: 05 08 03 22 67")

crops = {
    "Manioc": "🥔", "Maize": "🌽", "Tomate": "🍅", "Piment": "🌶️", "Riz": "🍚",
    "Igname": "🍠", "Banane": "🍌", "Cacao": "🍫", "Cafe": "☕", "Arachide": "🥜",
}

# --- 1. CROP ---
crop = st.selectbox("1. Select Crop / Choisir Culture", list(crops.keys()))
st.write(f"### {crops[crop]} {crop}")

# --- 2. TAKE CROP PHOTO - NEW! ---
st.write("### 2. Take Photo of Your Crop / Prenez Photo de Votre Culture 📸")
st.write("Take photo of the sick leaf / Prenez photo de la feuille malade")

# For phone: camera go open. For computer: upload go show
crop_photo = st.camera_input("📷 Take Photo / Prendre Photo", label_visibility="collapsed")

# If camera no work, use upload as backup
if crop_photo is None:
    uploaded = st.file_uploader("Or Upload Photo / Ou Télécharger Photo", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    if uploaded is not None:
        crop_photo = uploaded

if crop_photo is not None:
    st.image(crop_photo, caption=f"Your {crop} photo / Votre photo {crop}", width=300)
    st.success("✅ Photo received / Photo reçue !")
else:
    st.info("👆 Take photo first to continue / Prenez photo d'abord")

# --- 3. SYMPTOMS ---
symptoms = st.multiselect("3. What do you see? / Que voyez-vous?",
    ["Dusty / Powder", "Insect / Holes", "Yellow Leaves", "Wilting"])

# --- PRODUCTS - WITH SPACE NAMES ---
products = {
    "Dusty / Powder": {
        "diagnosis": "Fungal Attack / Attaque Fongique",
        "product": "LDC",
        "price": "24,900 FCFA",
        "use": "1 spoon in 5L water / 1 cuillère dans 5L d'eau",
        "image": "LDC .jpeg"
    },
    "Insect / Holes": {
        "diagnosis": "Insect Attack / Attaque d'Insectes",
        "product": "SUPER 10",
        "price": "24,900 FCFA",
        "use": "1 spoon in 5L water / 1 cuillère dans 5L d'eau",
        "image": "SUPER 10 .jpeg"
    },
    "Yellow Leaves": {
        "diagnosis": "Lack of Nutrients / Manque de Nutriments",
        "product": "SUPER GRO",
        "price": "70,000 FCFA",
        "use": "1 spoon in 5L water / 1 cuillère dans 5L d'eau",
        "image": "SUPERGRO .jpeg"
    },
    "Wilting": {
        "diagnosis": "Root / Water Problem / Problème Racine / Eau",
        "product": "CARE",
        "price": "25,000 FCFA",
        "use": "1 spoon in 5L water / 1 cuillère dans 5L d'eau",
        "image": "CARE .jpeg"
    }
}

# --- 4. DIAGNOSE ---
if st.button("DIAGNOSE / DIAGNOSTIQUER", type="primary"):
    if crop_photo is None:
        st.warning("⚠️ Take crop photo first! / Prenez photo de la culture d'abord!")
    elif not symptoms:
        st.warning("Select symptom first / Choisissez symptôme d'abord")
    else:
        for s in symptoms:
            info = products[s]
            st.divider()
            st.success(f"DIAGNOSIS for {crop}: {info['diagnosis']}")
            col_p1, col_p2 = st.columns([1, 1])
            with col_p1:
                st.image(info['image'], caption=info['product'], use_container_width=True)
            with col_p2:
                st.write(f"### {info['product']}")
                st.write(f"**PRICE / PRIX: {info['price']}**")
                st.write(f"**USE: {info['use']}**")
                st.write(f"**FOR / POUR: {crop}**")
            msg = f"Bonjour Emeka, je veux commander {info['product']} pour {crop} - {info['diagnosis']} - Prix {info['price']}"
            link = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(msg)}"
            st.link_button(f"Commander {info['product']} sur WhatsApp 📲", link, use_container_width=True)

st.divider()
st.write("PlantDoctor CI - By Emeka | Directeur Neolife")

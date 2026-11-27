import streamlit as st
import urllib.parse
import os

WHATSAPP_NUMBER = "225508032267"

st.set_page_config(page_title="PlantDoctor CI - Emeka", page_icon="🌱")
st.title("🌱 PlantDoctor CI - Emeka")
st.write("Diagnose your crop / Diagnostiquez votre culture")
st.write("📞 WhatsApp: 05 08 03 22 67")

# --- 10 CROPS ---
crops = {
    "Manioc": "🥔", "Maize": "🌽", "Tomate": "🍅", "Piment": "🌶️", "Riz": "🍚",
    "Igname": "🍠", "Banane": "🍌", "Cacao": "🍫", "Cafe": "☕", "Arachide": "🥜",
}

# --- 1. CROP NAME + CROP PHOTO ---
crop = st.selectbox("1. Select Crop / Choisir Culture", list(crops.keys()))
st.write(f"### {crops[crop]} {crop}")

# Check crop photo if e dey
crop_photo = f"{crop.lower()}.jpg"
if os.path.exists(crop_photo):
    st.image(crop_photo, width=250)
else:
    st.write(f"{crops[crop]} Photo coming soon")

symptoms = st.multiselect("2. What do you see? / Que voyez-vous?",
    ["Dusty / Powder", "Insect / Holes", "Yellow Leaves", "Wilting"])

# --- PRODUCTS WITH PHOTOS ---
products = {
    "Dusty / Powder": {
        "diagnosis": "Fungal Attack / Attaque Fongique",
        "product": "LDC",
        "price": "24,900 FCFA",
        "use": "1 spoon in 5L water / 1 cuillère dans 5L d'eau",
        "image": "ldc.jpg"
    },
    "Insect / Holes": {
        "diagnosis": "Insect Attack / Attaque d'Insectes",
        "product": "SUPER 10",
        "price": "24,900 FCFA",
        "use": "1 spoon in 5L water / 1 cuillère dans 5L d'eau",
        "image": "super10.jpg"
    },
    "Yellow Leaves": {
        "diagnosis": "Lack of Nutrients / Manque de Nutriments",
        "product": "SUPER GRO",
        "price": "70,000 FCFA",
        "use": "1 spoon in 5L water / 1 cuillère dans 5L d'eau",
        "image": "supergro.jpg"
    },
    "Wilting": {
        "diagnosis": "Root / Water Problem / Problème Racine / Eau",
        "product": "CARE",
        "price": "25,000 FCFA",
        "use": "1 spoon in 5L water / 1 cuillère dans 5L d'eau",
        "image": "care.jpg"
    }
}

# --- 3. DIAGNOSE + PRODUCT PHOTO + PRICE + WHATSAPP ---
if st.button("DIAGNOSE / DIAGNOSTIQUER", type="primary"):
    if not symptoms:
        st.warning("Select symptom first / Choisissez symptôme d'abord")
    else:
        for s in symptoms:
            info = products[s]
            st.divider()
            st.success(f"DIAGNOSIS for {crop}: {info['diagnosis']}")

            col_p1, col_p2 = st.columns([1, 1])
            with col_p1:
                # FIX: If photo no dey, no crash
                if os.path.exists(info['image']):
                    st.image(info['image'], caption=info['product'], use_container_width=True)
                else:
                    st.write(f"📷 {info['product']} photo - check GitHub upload")
                    st.write(f"File missing: {info['image']}")
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

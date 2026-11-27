import streamlit as st
import urllib.parse
import os

WHATSAPP_NUMBER = "225508032267"

st.set_page_config(page_title="PlantDoctor CI - Emeka", page_icon="🌱")
st.title("🌱 PlantDoctor CI - Emeka")
st.write("Diagnose your crop / Diagnostiquez votre culture")
st.write("📞 WhatsApp: 05 08 03 22 67")

# --- HELPER: Find photo no matter the name ---
def find_photo(names):
    for n in names:
        if os.path.exists(n):
            return n
    return None

# Show what files Streamlit sees - for debug
# st.write("Files in app:", os.listdir("."))

crops = {
    "Manioc": "🥔", "Maize": "🌽", "Tomate": "🍅", "Piment": "🌶️", "Riz": "🍚",
    "Igname": "🍠", "Banane": "🍌", "Cacao": "🍫", "Cafe": "☕", "Arachide": "🥜",
}

crop = st.selectbox("1. Select Crop / Choisir Culture", list(crops.keys()))
st.write(f"### {crops[crop]} {crop}")

symptoms = st.multiselect("2. What do you see? / Que voyez-vous?",
    ["Dusty / Powder", "Insect / Holes", "Yellow Leaves", "Wilting"])

products = {
    "Dusty / Powder": {
        "diagnosis": "Fungal Attack / Attaque Fongique",
        "product": "LDC",
        "price": "24,900 FCFA",
        "use": "1 spoon in 5L water / 1 cuillère dans 5L d'eau",
        "images": ["LDC.jpeg", "LDC.jpg", "ldc.jpg", "ldc.jpeg", "LDC.JPG"]
    },
    "Insect / Holes": {
        "diagnosis": "Insect Attack / Attaque d'Insectes",
        "product": "SUPER 10",
        "price": "24,900 FCFA",
        "use": "1 spoon in 5L water / 1 cuillère dans 5L d'eau",
        "images": ["SUPER 10.jpeg", "SUPER 10.jpg", "super10.jpg", "SUPER10.jpeg", "SUPER10.jpg", "Super 10.jpeg"]
    },
    "Yellow Leaves": {
        "diagnosis": "Lack of Nutrients / Manque de Nutriments",
        "product": "SUPER GRO",
        "price": "70,000 FCFA",
        "use": "1 spoon in 5L water / 1 cuillère dans 5L d'eau",
        "images": ["SUPERGRO.jpeg", "SUPERGRO.jpg", "supergro.jpg", "SUPER GRO.jpeg", "SUPER GRO.jpg", "SUPERGRO2.jpeg", "SUPERGRO2.jpg"]
    },
    "Wilting": {
        "diagnosis": "Root / Water Problem / Problème Racine / Eau",
        "product": "CARE",
        "price": "25,000 FCFA",
        "use": "1 spoon in 5L water / 1 cuillère dans 5L d'eau",
        "images": ["CARE.jpeg", "CARE.jpg", "care.jpg", "care.jpeg"]
    }
}

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
                photo = find_photo(info['images'])
                if photo:
                    st.image(photo, caption=info['product'], use_container_width=True)
                else:
                    st.error(f"Photo not found for {info['product']}")
                    st.write("Files Streamlit sees:", os.listdir("."))
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

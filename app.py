import streamlit as st
import urllib.parse

WHATSAPP_NUMBER = "225508032267"

st.set_page_config(page_title="PlantDoctor CI - Emeka", page_icon="🌱")
st.title("🌱 PlantDoctor CI - Emeka")
st.write("Diagnose your crop / Diagnostiquez votre culture")
st.write("📞 WhatsApp: 05 08 03 22 67")

crop = st.selectbox("1. Select Crop / Choisir Culture",
    ["Manioc", "Maize", "Tomate", "Piment", "Riz", "Igname", "Banane", "Cacao", "Cafe", "Arachide"])

symptoms = st.multiselect("2. What do you see? / Que voyez-vous?",
    ["Dusty / Powder", "Insect / Holes", "Yellow Leaves", "Wilting"])

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
        "use": "1 spoon in 5L water / 1 cuillère dans 5L d'eau - Pour croissance",
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

if st.button("DIAGNOSE / DIAGNOSTIQUER", type="primary"):
    if not symptoms:
        st.warning("Please select a symptom / Svp choisissez un symptôme")
    else:
        st.write(f"**Crop / Culture:** {crop}")
        for s in symptoms:
            info = products[s]
            st.divider()
            st.success(f"DIAGNOSIS: {info['diagnosis']}")
            st.image(info['image'], width=300)
            st.write(f"**BUY / ACHETER:** {info['product']}")
            st.write(f"**PRICE / PRIX:** {info['price']}")
            st.write(f"**USE / UTILISATION:** {info['use']}")
            msg = f"Bonjour Emeka, je veux commander {info['product']} pour {crop} - {info['diagnosis']} - Prix {info['price']}"
            link = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(msg)}"
            st.link_button(f"Commander {info['product']} sur WhatsApp 📲", link)

st.divider()
st.write("PlantDoctor CI - By Emeka | Directeur Neolife")

import streamlit as st
# --- NEOLIFE PRODUCTS ---
PRODUCTS = {
    "SUPERGRO": {
        "image": "SUPERGRO VIP.jpeg",
        "name": "SUPERGRO - Engrais Liquide",
        "desc": "Fait pousser la plante vite, rend les feuilles vertes et fortes.",
        "usage": "1ml pour 1 litre d'eau. Arroser chaque 2 semaines.",
        "price": "Prix: Contact Emeka"
    },
    "SUPER 10": {
        "image": "SUPER 10 VIP.jpeg",
        "name": "SUPER 10 - Anti-Insectes",
        "desc": "Tue les insectes, pucerons, chenilles qui mangent les feuilles.",
        "usage": "1ml pour 1 litre d'eau. Pulvériser sur feuilles matin ou soir.",
        "price": "Prix: Contact Emeka"
    },
    "LDC": {
        "image": "LDC VIP.jpeg",
        "name": "LDC - Anti-Maladies",
        "desc": "Nettoie et protège contre les maladies de la plante.",
        "usage": "1ml pour 1 litre d'eau. Pulvériser chaque 2 semaines.",
        "price": "Prix: Contact Emeka"
    },
    "CARE": {
        "image": "CARE VIP.jpeg",
        "name": "CARE - Soin & Protection",
        "desc": "Protège la plante, aide à guérir les feuilles malades.",
        "usage": "1ml pour 1 litre d'eau. Pulvériser sur feuilles malades.",
        "price": "Prix: Contact Emeka"
    },
    "3 COMBATTANTS": {
        "image": "3 COMBATTANT VIP.jpeg",
        "name": "LES 3 COMBATTANTS - Pack Complet",
        "desc": "Super 10 + LDC + Care ensemble. Le meilleur pour tuer insectes + maladies + protéger la plante.",
        "usage": "1ml de chaque pour 1 litre d'eau. Pulvériser chaque 2 semaines.",
        "price": "Prix Pack: Contact Emeka"
    }
}
def show_product(key):
    p = PRODUCTS[key]
    import os
    if os.path.exists(p["image"]):
        st.image(p["image"], use_column_width=True)
    else:
    st.write(f"Photo {p['image']} no found - but product dey below")  
    st.write(f"Photo {p['image']} no found - but product dey below")
    st.markdown(f"### {p['name']}")
    st.write(p["desc"])
    st.info(f"*Comment utiliser:* {p['usage']}")
    st.success(p["price"])
st.set_page_config(page_title="PlantDoctor CI")
st.title("🌿 PlantDoctor CI")
st.write("Scan your leaf, we tell you what to buy")

crop = st.selectbox("Choose your crop:", ["Cocoa", "Manioc", "Banana", "Riz", "Patata", "Graine", "Cashew", "Eveiah", "Yam", "Groundnuts"])

photo = st.file_uploader("Take photo of leaf", type=["jpg", "png", "jpeg"])
PRODUCTS = {
    "SUPERGRO": {
        "image": "SUPERGRO.jpeg",
        "name": "SUPERGRO - Engrais Liquide",
        "desc": "Fait pousser la plante vite, rend les feuilles vertes et fortes.",
        "usage": "1ml pour 1 litre d'eau. Arroser chaque 2 semaines.",
        "price": "Prix: Contact Emeka"
    },
    "SUPER 10": {
        "image": "SUPER 10.jpeg",
        "name": "SUPER 10 - Anti-Insectes",
        "desc": "Tue les insectes, pucerons, chenilles qui mangent les feuilles.",
        "usage": "1ml pour 1 litre d'eau. Pulveriser sur feuilles matin ou soir.",
        "price": "Prix: Contact Emeka"
    },
    "LDC": {
        "image": "LDC.jpeg",
        "name": "LDC - Anti-Maladies",
        "desc": "Nettoie et protege contre les maladies de la plante.",
        "usage": "1ml pour 1 litre d'eau. Pulveriser chaque 2 semaines.",
        "price": "Prix: Contact Emeka"
    },
    "CARE": {
        "image": "CARE.jpeg",
        "name": "CARE - Soin & Protection",
        "desc": "Protege la plante, aide a guerir les feuilles malades.",
        "usage": "1ml pour 1 litre d'eau. Pulveriser sur feuilles malades.",
        "price": "Prix: Contact Emeka"
    },
    "3 COMBATTANTS": {
        "image": "COMBATANT.jpeg",
        "name": "LES COMBATTANT - Pack Complet",
        "desc": "Super 10 + LDC + Care ensemble. Le meilleur pour tuer insectes + maladies + proteger la plante.",
        "usage": "1ml de chaque pour 1 litre d'eau. Pulveriser chaque 2 semaines.",
        "price": "Prix Pack: Contact Emeka"
    }
}

def show_product(key):
    p = PRODUCTS[key]
    st.image(p["image"], use_column_width=True)
    st.markdown(f"### {p['name']}")
    st.write(p["desc"])
    st.info(f"**Comment utiliser:** {p['usage']}")
    st.success(p["price"])

    if st.button("DIAGNOSE"):
        st.write(f"*Crop:* {crop}")
        if "Dusty" in symptom:
            st.error("DIAGNOSIS: Fungal Attack")
            st.success("BUY: LDC - Kill fungals, leaves dryness, deadly micro fungals and prevent plants from early death or attack")
            st.write("Dosage: 1ml in 1L water")
        elif "Insect" in symptom:
            st.error("DIAGNOSIS: Pest / Insect Attack")
            st.success("BUY: SUPER 10 - Kill pest, kill germs, remove black pods, prevent yellowish colors, prevent dangerous plants organisms")
            st.write("Dosage: 1ml in 1L water")
        elif "Poor growth" in symptom:
            st.error("DIAGNOSIS: Poor Growth")
            st.success("BUY: CARE - Prevent poor growth, bad insects, pest, fungals and bactérie from plants")
            st.write("Dosage: 1ml in 1L water")
        elif "Black Pod" in symptom:
            st.error("DIAGNOSIS: Black Pod / Fungal + Pest")
            st.success("BUY: SUPER 10 + LDC")
            st.write("Dosage: 1ml in 1L water")
        else:
            st.error("DIAGNOSIS: Multiple Attack")
            st.success("BUY: PACK COMPLETE - LDC + SUPER 10 + CARE + SuperGro")
            st.write("Price: 130,000F - Dosage: 1ml in 1L water")
            st.write("For Cocoa, Manioc, Banana, Riz, Patata, Graine, Cashew, Eveiah, Yam, Groundnuts")
# --- SHOW PRODUCT AFTER DIAGNOSIS ---
st.markdown("---")
st.markdown("## 💊 Traitement Recommandé - NEOLIFE")

# if is insectes -> Super 10
# if is microb et fungal  -> LDC + Care
# if is all  -> 3 Combattants
# Toi tu peux changer ici

st.markdown("### Pour ce problème, utilise:")
show_product("3 COMBATTANTS")

st.markdown("### Ou achète séparément:")
col1, col2, col3 = st.columns(3)
with col1:
    show_product("SUPER 10")
with col2:
    show_product("LDC")
with col3:
    show_product("CARE")

st.markdown("### Pour faire pousser plus vite:")
show_product("SUPERGRO")

st.markdown("📞 *Pour commander, contact Emeka - WhatsApp*")
st.link_button("📲 Order on WhatsApp", "https://wa.me/2250508032267?text=Hello, I want to order for PlantDoctor")

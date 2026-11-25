import streamlit as st

st.set_page_config(page_title="PlantDoctor CI")
st.title("🌿 PlantDoctor CI")
st.write("Scan your leaf, we tell you what to buy")

crop = st.selectbox("Choose your crop:", ["Cocoa", "Manioc", "Banana", "Riz", "Patata", "Graine", "Cashew", "Eveiah", "Yam", "Groundnuts"])

photo = st.file_uploader("Take photo of leaf", type=["jpg", "png", "jpeg"])

if photo:
    st.image(photo, caption="Your leaf", width=300)
    
    st.subheader("What do you see on the leaf?")
    symptom = st.selectbox("Pick symptom:", 
        ["Dusty part / Dry / Fungus", 
         "Insect hole / Pest don chop am", 
         "Poor growth / Plant no dey grow well",
         "Black Pod / Yellowish color",
         "All of them together"])

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

        st.link_button("📲 Order on WhatsApp", "https://wa.me/2250508032267?text=Hello, I want to order for PlantDoctor")
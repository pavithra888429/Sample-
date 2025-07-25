import streamlit as st
import google.generativeai as genai

# ---- Setup Gemini API ----
st.set_page_config(page_title="Daily Fashion Tips", layout="centered")
st.title("👗 Daily Fashion Tips Generator")

# Input API Key
api_key = st.text_input("🔑 Enter your Gemini API Key", type="password")

# If API key is entered
if api_key:
    genai.configure(api_key=api_key)

    # ---- User Input ----
    st.subheader("🧍 Select Your Preferences")

    gender = st.selectbox("👤 Select Gender", ["Male", "Female", "Other"])
    occasion = st.selectbox("🎉 Select Occasion", ["Casual", "Office", "Party", "Workout", "Date"])
    season = st.selectbox("🌦️ Select Season", ["Summer", "Winter", "Rainy", "Spring", "Autumn"])

    if st.button("✨ Generate Fashion Tip"):
        with st.spinner("Generating your daily fashion tip..."):
            prompt = f"""
            You are a professional fashion stylist. Suggest a fashion outfit for:
            - Gender: {gender}
            - Occasion: {occasion}
            - Season: {season}

            Include styling tips and accessories. Make it beginner-friendly and trendy.
            """

            try:
                model = genai.GenerativeModel(model_name="gemini-1.5-pro")  # Use latest Gemini model
                response = model.generate_content(prompt)
                fashion_tip = response.text

                st.success("Here's your fashion tip 👇")
                st.markdown(f"📝 **Fashion Advice**:\n\n{fashion_tip}")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
else:
    st.warning("Please enter your Gemini API key to continue.")

# Optional Footer
st.markdown("---")
st.caption("Created with 💖 using Streamlit & Gemini AI")

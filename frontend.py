import streamlit as st
import requests

# API Endpoint
API_URL = "http://127.0.0.1:8000/predict"

# App Title
st.set_page_config(page_title="Insurance Premium Predictor", layout="centered")
st.title("🛡️ Insurance Premium Category Predictor")
st.markdown("Fill in your details below to get a premium category prediction.")

# Sidebar for user inputs
with st.form("user_input_form"):
    st.subheader("👤 Personal Details")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=1, max_value=119, value=30, step=1)
        weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
        smoker = st.selectbox("Do you smoke?", options=["No", "Yes"])
    with col2:
        height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
        income_lpa = st.number_input("Annual Income (in LPA)", min_value=0.1, value=10.0)
        city = st.text_input("City", value="Mumbai")

    st.subheader("💼 Employment Details")
    occupation = st.selectbox(
        "Occupation",
        ['Retired', 'Freelancer', 'Student', 'Government Job', 'Business Owner', 'Unemployed', 'Private Job']
    )

    # Submit button
    submitted = st.form_submit_button("🔍 Predict Premium Category")

# On form submission
if submitted:
    # Convert input to expected format
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker == "Yes",
        "city": city,
        "occupation": occupation.lower().replace(" ", "_")
    }

    # Make API call
    with st.spinner("Predicting... Please wait"):
        try:
            response = requests.post(API_URL, json=input_data)
            if response.status_code == 200:
                result = response.json()
                st.success(f"✅ Predicted Insurance Premium Category: **{result['predicted_category']}**")
            else:
                st.error(f"❌ API Error {response.status_code}: {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("🚫 Could not connect to the FastAPI server. Is it running on port 8000?")




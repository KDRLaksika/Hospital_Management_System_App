import streamlit as st
from db import get_connection

def render():
    st.header("🧾 Register New Patient")

    with st.form("register_form"):
        name = st.text_input("Full Name")
        gender = st.selectbox("Gender", ["Male", "Female"]) # display Male and Female for give good user experience
        # this send M and F to the database
        if gender == "Male":
            gender = "M"
        else:
            gender = "F"

        dob = st.date_input("Date of Birth")
        dob_str = dob.strftime('%Y-%m-%d')  

        phone = st.text_input("Phone")
        address = st.text_area("Address")
        submitted = st.form_submit_button("Register")

        if submitted:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "EXEC sp_AddPatient ?, ?, ?, ?, ?",
                    name, gender, dob.strftime('%Y-%m-%d'), phone, address
                )
                conn.commit()
                st.success("✅ Patient Registered Successfully!")
            except Exception as e:
                st.error(f"❌ Error: {e}")

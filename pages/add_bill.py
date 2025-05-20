
import streamlit as st
from db import get_connection
import datetime

def render():
    st.header("🧾 Add Billing Information")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT PatientID, Name FROM Patient")
        patients = cursor.fetchall()
        patient_options = {f"{name} (ID: {pid})": pid for pid, name in patients}
    except Exception as e:
        st.error(f"❌ Failed to load patients: {e}")
        return

    with st.form("bill_form"):
        selected_patient = st.selectbox("Select Patient", list(patient_options.keys()))
        patient_id = patient_options[selected_patient]

        amount = st.number_input("Amount", min_value=0.0, step=100.0, format="%.2f")
        date_issued = st.date_input("Date Issued", value=datetime.date.today())

        submitted = st.form_submit_button("Add Bill")

        if submitted:
            try:
                cursor.execute(
                    "INSERT INTO Bill (PatientID, Amount, DateIssued) VALUES (?, ?, ?)",
                    patient_id, amount, date_issued.strftime('%Y-%m-%d')
                )
                conn.commit()
                st.success("✅ Bill added successfully!")
            except Exception as e:
                st.error(f"❌ Error adding bill: {e}")
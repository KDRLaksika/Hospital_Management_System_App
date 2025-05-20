import streamlit as st
from pages import register_patient, billing_report, add_bill, view_bills

st.set_page_config(page_title="Hospital Management System", layout="wide")
st.title("🏥 Hospital Management System")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Register Patient","Add Bill","view Bills", "Billing Report"))

if page == "Register Patient":
    register_patient.render()
elif page == "Billing Report":
    billing_report.render()
elif page == "Add Bill":
    add_bill.render()
elif page == "view Bills":
    view_bills.render()




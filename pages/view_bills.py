
import streamlit as st
import pandas as pd
from db import get_connection

def render():
    st.header("📋 View & Search Patient Bills")

    # Input for filtering
    patient_id = st.text_input("Search by Patient ID")
    date_filter = st.date_input("Filter by Date Issued (optional)", value=None)

    try:
        conn = get_connection()
        query = "SELECT BillID, PatientID, Amount, DateIssued FROM Bill"
        filters = []

        if patient_id:
            filters.append(f"PatientID = {patient_id}")
        if date_filter:
            filters.append(f"DateIssued = '{date_filter.strftime('%Y-%m-%d')}'")

        if filters:
            query += " WHERE " + " AND ".join(filters)
        query += " ORDER BY DateIssued DESC"

        df = pd.read_sql(query, conn)

        if not df.empty:
            st.dataframe(df)
        else:
            st.info("No matching records found.")

    except Exception as e:
        st.error(f"❌ Error fetching bill records: {e}")
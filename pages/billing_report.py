import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from db import get_connection

def render():
    st.header("📊 Monthly Billing Report")

    try:
        conn = get_connection()

        # 📌 Step 1: Year dropdown
        years_df = pd.read_sql("SELECT DISTINCT YEAR(DateIssued) as Year FROM Bill ORDER BY Year DESC", conn)
        years = years_df["Year"].tolist()

        if not years:
            st.warning("No billing records available.")
            return

        selected_year = st.selectbox("Select Year", years)

        # 📌 Step 2: Query based on selected year
        query = f"""
        SELECT MONTH(DateIssued) AS Month, SUM(Amount) AS Total
        FROM Bill
        WHERE YEAR(DateIssued) = {selected_year}
        GROUP BY MONTH(DateIssued)
        ORDER BY Month
        """
        df = pd.read_sql(query, conn)

        if df.empty:
            st.warning(f"No billing records found for the year {selected_year}.")
            return

        df.set_index("Month", inplace=True)

        # 📊 Streamlit Chart (smaller & responsive)
        st.subheader("📈 Interactive Revenue Chart (Streamlit)")
        st.bar_chart(df)

        # 📊 Matplotlib Chart
        st.subheader("📊 Detailed Revenue Chart (Matplotlib)")
        fig, ax = plt.subplots(figsize=(6, 4))  # smaller size
        ax.bar(df.index, df["Total"], color="skyblue")
        ax.set_xlabel("Month (1–12)")
        ax.set_ylabel("Total Revenue (Rs.)")
        ax.set_title(f"Monthly Revenue in {selected_year}")
        ax.set_xticks(range(1, 13))
        ax.set_xticklabels([str(i) for i in range(1, 13)])
        st.pyplot(fig)

        # 📑 Table
        st.subheader("🧾 Monthly Revenue Data")
        st.dataframe(df.reset_index())

    except Exception as e:
        st.error(f"❌ Error loading billing data: {e}")


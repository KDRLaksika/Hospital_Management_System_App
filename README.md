# Hospital Management System (Streamlit + SQL Server)

## 📦 Description
A simple hospital app built with Python Streamlit and Microsoft SQL Server to manage patient registration and view billing analytics.

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/KDRLaksika/hospital_app.git
cd hospital_app
```

### 2. Set Up SQL Server
- Create a database named `HospitalDB`
- Add required tables (Patient, Bill, etc.)
- Add stored procedure `sp_AddPatient`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

### 5. App Pages
- Register Patient
- Billing Report with chart

## 💡 Note
- Make sure your SQL Server is running and `HospitalDB` is accessible.
- Update `db.py` if your server configuration is different.

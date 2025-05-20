# Hospital Management System (Streamlit + SQL Server)

## 📦 Description
A simple hospital app built with Python Streamlit and Microsoft SQL Server to manage patient registration and view billing analytics.

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/KDRLaksika/Hospital_Management_System_App.git
cd Hospital_Management_System_App
```

### 2. Set Up SQL Server
- Create a database named `HospitalDB`
- Add required tables (Patient, Bill, etc.)
- Add stored procedure `sp_AddPatient`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create and activate a virtual environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS
source venv/bin/activate
# On Linux
```

### 4. Run the App
```bash
streamlit run app.py
# or try with
python -m streamlit run app.py
```

### 5. App Pages
- Register Patient
- Billing Report with chart

## 💡 Note
- Make sure your SQL Server is running and `HospitalDB` is accessible.
- Update `db.py` if your server configuration is different.

## Not working? Check if Python is installed or not, and the environment variables

If Streamlit is installed but not recognized:
- Add this to your system PATH:
Windows:
- Find where Python is installed (look for a path like C:\Users\YourName\AppData\Local\Programs\Python\Python39\Scripts)
- Search for "Environment Variables" in Start menu
- Click "Edit the system environment variables"
- Click "Environment Variables"
- Under "System variables", find "Path" and click "Edit"
- Click "New" and add the path to your Python Scripts folder
- Click OK on all dialogs

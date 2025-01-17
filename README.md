# PHRMS
# Personal Health Record Management System

## Overview

This project is a **Personal Health Record Management System** built using **Flask** (Python). The system allows users to maintain their medical history (appointments, prescriptions, lab reports). The application has a secure login system for both **patients** and **doctors**, allowing them to manage their data securely.

### Features

- **Patient**:
  - Login and registration for users (patients).
  - Ability to view and manage personal medical records.
  - Add new medical records such as appointments, prescriptions, and lab reports.

- **Doctor**:
  - Login and registration for doctors.
  - View all medical records of patients.
  - View appointments, prescriptions, and lab reports of any patient.

- **Secure Login**: 
  - Passwords are securely hashed using **bcrypt**.
  
- **Data Storage**: 
  - All data is stored in an **SQLite** database (`health_records.db`).

### Requirements

- Python 3.x
- Flask
- bcrypt
- SQLite (used automatically with Flask)

You can install the required Python libraries using `requirements.txt` by running:

```bash
pip install -r requirements.txt






Setup Instructions
Clone the repository:


git clone https://github.com/your-username/Health-Records-Management-System.git
Navigate to the project directory:


cd Health-Records-Management-System
Install dependencies:


pip install -r requirements.txt
Run the application:


python app.py
Access the application: Open your browser and go to http://127.0.0.1:5000.

Features in Detail
1. Login Page
Patients and doctors can log in using their respective roles.
After successful login, users are redirected to their role-specific dashboards.
2. Patient Dashboard
Patients can view their medical records.
They can also add new records including appointments, prescriptions, and lab reports.
3. Doctor Dashboard
Doctors can view all patients' medical records, including appointments, prescriptions, and lab reports.
4. Registration Page
Users (patients or doctors) can create a new account with a username, password, and role selection.
Project Structure
app.py: The main Python file for the Flask application.
templates/: Directory containing all HTML templates for the login page, dashboards, and registration.
health_records.db: The SQLite database that stores user information and medical records (this will be created automatically upon running the app).
requirements.txt: A text file containing all the necessary Python libraries for the project.
.gitignore: Git ignore file to exclude unnecessary files like *.pyc and health_records.db.
Running the App
Once the app is running, you can access it in your browser by going to:


http://127.0.0.1:5000
You will see the login page where you can log in as a patient or doctor, or register a new account.

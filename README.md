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

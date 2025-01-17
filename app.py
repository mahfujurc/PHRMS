from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # You should change this in production

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('health_records.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create tables if they don't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS medical_records (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        appointment_date TEXT,
                        prescription TEXT,
                        lab_report TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(id))''')

    conn.commit()
    conn.close()

# Home page (login page)
@app.route('/')
def home():
    return render_template('login.html')

# Login page logic
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    role = request.form['role']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')) and user['role'] == role:
        session['user_id'] = user['id']
        session['username'] = user['username']
        session['role'] = role
        if role == 'patient':
            return redirect(url_for('patient_dashboard'))
        elif role == 'doctor':
            return redirect(url_for('doctor_dashboard'))
    else:
        flash("Invalid credentials. Please try again.", 'danger')
        return redirect(url_for('home'))

# Patient Dashboard
@app.route('/patient_dashboard')
def patient_dashboard():
    if 'user_id' not in session or session['role'] != 'patient':
        return redirect(url_for('home'))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medical_records WHERE user_id = ?", (session['user_id'],))
    records = cursor.fetchall()
    conn.close()

    return render_template('patient_dashboard.html', records=records)

# Doctor Dashboard
@app.route('/doctor_dashboard')
def doctor_dashboard():
    if 'user_id' not in session or session['role'] != 'doctor':
        return redirect(url_for('home'))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medical_records")
    records = cursor.fetchall()
    conn.close()

    return render_template('doctor_dashboard.html', records=records)

# Add medical record (for patients)
@app.route('/add_record', methods=['POST'])
def add_record():
    if 'user_id' not in session or session['role'] != 'patient':
        return redirect(url_for('home'))

    appointment_date = request.form['appointment_date']
    prescription = request.form['prescription']
    lab_report = request.form['lab_report']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO medical_records (user_id, appointment_date, prescription, lab_report) 
                      VALUES (?, ?, ?, ?)''', (session['user_id'], appointment_date, prescription, lab_report))
    conn.commit()
    conn.close()

    flash("Record added successfully!", 'success')
    return redirect(url_for('patient_dashboard'))

# Register page logic (for both patients and doctors)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                       (username, hashed_pw, role))
        conn.commit()
        conn.close()

        flash("Account created successfully! You can now login.", 'success')
        return redirect(url_for('home'))

    return render_template('register.html')

# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", 'success')
    return redirect(url_for('home'))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

import sqlite3
import json

# 1. DATABASE SETUP (SQLite)
def setup_database():
    """Bazanı sıfırdan düzgün sütunlarla yaradır"""
    conn = sqlite3.connect('edureg.db')
    cursor = conn.cursor()
    # Sütunlar: id, name, course, gpa
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            course TEXT,
            gpa REAL
        )
    ''')
    conn.commit()
    conn.close()
    print("System: Database initialized successfully.")

# 2. CRUD OPERATIONS
def add_student(name, course, gpa):
    conn = sqlite3.connect('edureg.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, course, gpa) VALUES (?, ?, ?)', (name, course, gpa))
    conn.commit()
    conn.close()
    print(f"System: Student '{name}' added.")

def show_students():
    conn = sqlite3.connect('edureg.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    print("\n--- Current Student List ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Course: {row[2]} | GPA: {row[3]}")
    conn.close()

# 3. JSON CONFIGURATION (Practical Exercise)
def load_config():
    """JSON faylını oxuyur (De-serialization)"""
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            print(f"\n[CONFIG] App: {config.get('app_name', 'Edureg System')}")
            print(f"[CONFIG] Theme: {config['theme']}, Language: {config['language']}")
            return config
    except FileNotFoundError:
        # Fayl yoxdursa standart ayarlar yaradır
        initial_config = {"app_name": "Edureg System", "theme": "dark", "language": "en", "version": 1.0}
        with open('config.json', 'w') as f:
            json.dump(initial_config, f, indent=4)
        return initial_config

# 4. EXECUTION
if __name__ == "__main__":
    setup_database()  # Bazanı və düzgün sütunları yaradır
    load_config()     # Ayarları oxuyur
    
    # Test məlumatları əlavə edirik (POST Simulyasiyası)
    add_student("Fatma Qarayeva", "Information Technology", 3.9)
    add_student("Tural Quluyev", "Computer Science", 3.7)
    
    # Nəticəni göstəririk (GET/Read Simulyasiyası)
    show_students()
    import os

# ... digər kodlar ...

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

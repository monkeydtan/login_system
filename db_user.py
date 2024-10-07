import sqlite3
import bcrypt # library สำหรับการแฮชรหัสผ่าน

# เชื่อมต่อกับฐานข้อมูล sqlite
def connect_db():
    conn = sqlite3.connect("users.db")
    print("เชื่อมต่อฐานข้อมูลสำเร็จ !")
    return conn

def login():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        # สร้างตารางสำหรับเก็บข้อมูลผู้ใช้
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )                
        ''')
        
        # บันทึกการเปลี่ยนแปลง
        conn.commit()
        print("สร้างตารางเก็บข้อมูลสำเร็จ")
        
    except sqlite3.Error as e:
        print(f"เกิดข้อผิดพลาดในการเชื่ือมต่อ: {e}")
   
    # ปิดการเชื่อมต่อเมื่อทำงานเสร็จ
    finally:
        if conn:
            conn.close()
            print("ปิดการเชื่อมต่อฐานข้อมูลแล้ว")




# เรียกใช้ฟังก์ชัน login
login()
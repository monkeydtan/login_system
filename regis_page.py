import tkinter as tk
from tkinter import messagebox
import sqlite3
import bcrypt

def open_regis_page():
    
    def click_regis():
        #print("ลงทะเบียนสำเร็จ")
        username = entry_user_name.get()
        password = entry_user_pw.get()
        password_again = entry_user_pw_2nd.get()
        
        if not username or not password or not password_again:
            messagebox.showerror("Error","กรุณากรอกให้ครบถ้วน")
            return
        
        # รหัสผ่านต้องเหมือนกันทั้งสองรอบ
        if password != password_again:
            messagebox.showerror("Error","รหัสผ่านไม่ตรงกัน กรุณาลองใหม่อีกครั้ง")
            return
        
        hash_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO users (username,password)
        VALUES (?,?)
        ''',(username,hash_password))
        conn.commit() # บันทึกการเปลี่ยนแปลง
        conn.close() # ปิดการเชื่อมต่อฐานข้อมูล
        
        messagebox.showinfo("Success","ลงทะเบียนสำเร็จ")
        regis_window.destroy()
    
    regis_window = tk.Tk()
    regis_window.title("ลงทะเบียน")
    regis_window.geometry("300x300")
    
    regis_title = tk.Label(regis_window,text="ลงทะเบียนผู้ใช้ใหม่")
    regis_title.pack(pady=10)
    
    # กรอบสำหรับการกรอกข้อมูลลงทะเบียนผู้ใช้ใหม่
    regis_frame = tk.Frame(regis_window)
    regis_frame.pack(expand=False)

    # กรอก username
    user_name = tk.Label(regis_frame,text="Username")
    user_name.grid(row=0,column=0,padx=(0,10),sticky="w")
    
    entry_user_name = tk.Entry(regis_frame)
    entry_user_name.grid(row=0,column=1)
    
    # กรอก password
    user_pw = tk.Label(regis_frame,text="Password ")
    user_pw.grid(row=1,column=0,padx=(0,10),pady=(10,0),sticky="w")
    
    entry_user_pw = tk.Entry(regis_frame,show='*')
    entry_user_pw.grid(row=1,column=1,pady=(10,0))
    
    # กรอก password อีกครั้ง
    user_pw_2nd = tk.Label(regis_frame,text="Password again ")
    user_pw_2nd.grid(row=2,column=0,padx=(0,10),pady=(10,0),sticky="w")
    
    entry_user_pw_2nd = tk.Entry(regis_frame,show='*')
    entry_user_pw_2nd.grid(row=2,column=1,pady=(10,0))
    
    # ปุ่มลงทะเบียน
    regis_btn = tk.Button(regis_frame,text="ลงทะเบียน",command=click_regis,width=10)
    regis_btn.grid(row=3,column=0,columnspan=2,pady=(20,0))
    
    
    


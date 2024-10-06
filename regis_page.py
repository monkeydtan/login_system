import tkinter as tk

def open_regis_page():
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
    
    entry_user_pw = tk.Entry(regis_frame)
    entry_user_pw.grid(row=1,column=1,pady=(10,0))
    
    # กรอก password อีกครั้ง
    user_pw_2nd = tk.Label(regis_frame,text="Password again ")
    user_pw_2nd.grid(row=2,column=0,padx=(0,10),pady=(10,0),sticky="w")
    
    entry_user_pw_2nd = tk.Entry(regis_frame)
    entry_user_pw_2nd.grid(row=2,column=1,pady=(10,0))
    
    # ปุ่มลงทะเบียน
    regis_btn = tk.Button(regis_frame,text="ลงทะเบียน",command=click_regis,width=10)
    regis_btn.grid(row=3,column=0,columnspan=2,pady=(20,0))
    
    
def click_regis():
    print("ลงทะเบียนสำเร็จ")



import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from regis_page import open_regis_page

app = tk.Tk()
app.title("กรอกชื่อ")
app.geometry("300x300")


# รูปตา
eyes_view = Image.open("pic/view.png") #ดึงรูปเข้ามา เก็บไว้ที่ตัวแปร eyes_view
eyes_view_img = ImageTk.PhotoImage(eyes_view)
eyes_hide = Image.open("pic/hide.png") 
eyes_hide_img = ImageTk.PhotoImage(eyes_hide)

# กรอบใหญ่
frame_window = tk.Frame(app)
frame_window.pack(expand=True)

# head
head_title = tk.Label(frame_window,text="Welcome to game")
head_title.grid(row=0,columnspan=2)

# ไอดี
fname = tk.Label(frame_window,text="Username : ")
fname.grid(row=1,column=0)

entry_fname = tk.Entry(frame_window,bd=2)
entry_fname.grid(row=1,column=1)

# รหัสผ่าน
lname = tk.Label(frame_window,text="Password : ")
lname.grid(row=2,column=0)

entry_lname = tk.Entry(frame_window,bd=2,show="*")
entry_lname.grid(row=2,column=1,pady=5)

def on_click(event):
    print("Click this!")

def cursor_on(event):
    #event.widget.config(font=('Arial', 10, 'underline'))
    forget_pw.config(font=('Arial', 10, 'underline'))
    
    
def cursor_leave(event):
    #event.widget.config(font=('Arial', 10))
    forget_pw.config(font=('Arial', 10))
    
    
# สร้างปุ่มข้อความ
forget_pw = tk.Button(frame_window,text="ลืมรหัสผ่าน",bd=0,cursor="hand2",fg='blue', font=('Arial', 10))
forget_pw.grid(row=3,column=1,columnspan=2,sticky="e",padx=(0,20))

# จับ event ตอนวางเม้าส์
forget_pw.bind("<Enter>",cursor_on)
forget_pw.bind("<Leave>",cursor_leave)
forget_pw.bind("<Button-1>",on_click)

# ฟังก์ชัน toggle
# เรากำลังประกาศตัวแปรนี้นอกฟังก์ชัน => ตัวแปรนี้อยู่ใน global scope หมายถึง ตัวแปรนี้มีอยู่ในระดับทั่วทั้งโปรแกรม
show_password = False # สร้างตัวแปรขึ้นว่า ตอนนี้มันกำลังโชว์รหัสผ่านไหม ซึ่งก็คือ ไม่ (โชว์ * อยู่)

def view_and_hide():
    global show_password
    if show_password:
        entry_lname.config(show="*")  #เป็น default เท่ากับว่า * คือ false / ตัวเลข คือ True
        icon_eye.config(image=eyes_view_img) # default คือ eye view
        show_password = False
    else:
        entry_lname.config(show="")
        icon_eye.config(image=eyes_hide_img)
        show_password = True
    
    
icon_eye = tk.Button(frame_window,image=eyes_view_img,width=13,height=13,command=view_and_hide)
icon_eye.grid(row=2,column=2)

# ฟังก์ชันการกดปุ่ม login
def user_id():
    str_name = entry_fname.get() # .get คือการรับข้อความจากช่องข้อความ มาเก็บไว้ในตัวแปร ซึ่งชื่อ str_name
    str_pw = entry_lname.get()
    if not str_name or not str_pw:
        messagebox.showerror("พบข้อผิดพลาด","Username หรือ Password ไม่ถูกต้อง")
    else:
        messagebox.showinfo("เข้าสู่ระบบสำเร็จ","Login Successful ! \nWelcome "+str_name)


# สร้างหน้าต่างใหม่
def new_window_regis():
    open_regis_page()


# กรอบย่อยสำหรับปุ่ม
sub_btn_frame = tk.Frame(frame_window)
sub_btn_frame.grid(row=4,column=1)

# ปุ่ม Login
submit_btn = tk.Button(sub_btn_frame,text="Login",command=user_id)
submit_btn.grid(row=0,column=0,sticky="w",padx=(0,10)) # sticky e คือ ชิดขอบขวา / w คือ ชิดขอบซ้าย
# ปุ่ม Register
regis_btn = tk.Button(sub_btn_frame,text="Register",command=new_window_regis) #command คือมันจะไปหน้าใหม่ (เพิ่ม delay)
regis_btn.grid(row=0,column=1)



app.mainloop()
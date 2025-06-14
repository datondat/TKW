<<<<<<< HEAD
import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess
from werkzeug.security import generate_password_hash, check_password_hash

DB_PATH = "weather.db"
APP_PATH = "app_desktop.py"

def switch_to_register():
    login_frame.pack_forget()
    register_frame.pack()

def switch_to_login():
    register_frame.pack_forget()
    login_frame.pack()

def handle_register():
    username = reg_username.get()
    password = reg_password.get()

    if not username or not password:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đủ thông tin.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, generate_password_hash(password)))
        conn.commit()
        messagebox.showinfo("Thành công", "Đăng ký thành công! Mời đăng nhập.")
        switch_to_login()
    except sqlite3.IntegrityError:
        messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại.")
    finally:
        conn.close()

def handle_login():
    username = login_username.get()
    password = login_password.get()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result and check_password_hash(result[0], password):
        messagebox.showinfo("Thành công", "Đăng nhập thành công!")
        root.destroy()
        subprocess.Popen(["python", APP_PATH])
    else:
        messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu.")

# ==== Giao diện chính ====
# Khởi động với màn hình đăng nhập
login_frame.pack()

root.mainloop()
=======
import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess
from werkzeug.security import generate_password_hash, check_password_hash
from PIL import Image, ImageTk
import sys

DB_PATH = "weather.db"
APP_PATH = "app_desktop.py"

def switch_to_register():
    login_frame.place_forget()
    register_frame.place(relx=0.5, rely=0.5, anchor="center")

def switch_to_login():
    register_frame.place_forget()
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

def handle_register():
    username = reg_username.get()
    password = reg_password.get()
    if not username or not password:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đủ thông tin.")
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, generate_password_hash(password)))
        conn.commit()
        messagebox.showinfo("Thành công", "Đăng ký thành công! Mời đăng nhập.")
        switch_to_login()
    except sqlite3.IntegrityError:
        messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại.")
    finally:
        conn.close()

def handle_login():
    username = login_username.get()
    password = login_password.get()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result and check_password_hash(result[0], password):
        messagebox.showinfo("Thành công", "Đăng nhập thành công!")
        root.destroy()
        subprocess.Popen(["python", APP_PATH])
    else:
        messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu.")

# ==== Giao diện chính ====
root = tk.Tk()
root.title("Đăng nhập")
root.geometry("360x640")
root.resizable(False, False)

# Tạo ảnh nền gradient pastel
width, height = 360, 640
gradient = Image.new('RGB', (width, height), color=0)
# Màu gradient (nhạt pastel từ tím sang xanh)
color1 = (224, 195, 252)  # tím nhạt
color2 = (142, 197, 252)  # xanh da trời nhạt
for y in range(height):
    ratio = y / (height - 1)
    r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
    g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
    b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
    for x in range(width):
        gradient.putpixel((x, y), (r, g, b))
bg_image = ImageTk.PhotoImage(gradient)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Cấu hình font cho giao diện iOS-style
if sys.platform == 'darwin':  # macOS
    title_font = ("-apple-system", 20, "bold")
    header_font = ("-apple-system", 14, "bold")
    button_font = ("-apple-system", 12)
    small_font = ("-apple-system", 10)
elif sys.platform == 'win32':  # Windows
    title_font = ("Segoe UI", 20, "bold")
    header_font = ("Segoe UI", 14, "bold")
    button_font = ("Segoe UI", 12)
    small_font = ("Segoe UI", 10)
else:  # Other (Linux, etc.)
    title_font = ("Helvetica", 20, "bold")
    header_font = ("Helvetica", 14, "bold")
    button_font = ("Helvetica", 12)
    small_font = ("Helvetica", 10)

# Màu sắc
primary_color = "#5ac8fa"   # xanh pastel
text_color = "#333333"

# ==== Frame đăng nhập ====
login_frame = tk.Frame(root, bg="#ffffff", bd=0)
tk.Label(login_frame, text="🌤️ Weather App", font=title_font,
         bg="#ffffff", fg=primary_color).pack(pady=20)
tk.Label(login_frame, text="ĐĂNG NHẬP", font=header_font,
         bg="#ffffff", fg=text_color).pack(pady=(0, 10))

tk.Label(login_frame, text="Tên đăng nhập", bg="#ffffff", fg=text_color).pack()
login_username = tk.Entry(login_frame, width=30, relief=tk.FLAT, bd=1, highlightthickness=1, highlightcolor="#ccc")
login_username.pack(pady=5, ipady=5)

tk.Label(login_frame, text="Mật khẩu", bg="#ffffff", fg=text_color).pack()
login_password = tk.Entry(login_frame, show="*", width=30, relief=tk.FLAT, bd=1, highlightthickness=1, highlightcolor="#ccc")
login_password.pack(pady=5, ipady=5)

tk.Button(login_frame, text="Đăng nhập", command=handle_login,
          bg=primary_color, fg="white", font=button_font,
          width=20, relief=tk.FLAT, bd=0).pack(pady=15, ipady=5)

tk.Label(login_frame, text="Chưa có tài khoản?", bg="#ffffff", fg=text_color).pack()
tk.Button(login_frame, text="Đăng ký", command=switch_to_register,
          font=small_font, bg="#ffffff", fg=primary_color, bd=0).pack(pady=(0, 10))

# ==== Frame đăng ký ====
register_frame = tk.Frame(root, bg="#ffffff", bd=0)
tk.Label(register_frame, text="🌤️ Weather App", font=title_font,
         bg="#ffffff", fg=primary_color).pack(pady=20)
tk.Label(register_frame, text="ĐĂNG KÝ", font=header_font,
         bg="#ffffff", fg=text_color).pack(pady=(0, 10))

tk.Label(register_frame, text="Tên đăng nhập", bg="#ffffff", fg=text_color).pack()
reg_username = tk.Entry(register_frame, width=30, relief=tk.FLAT, bd=1, highlightthickness=1, highlightcolor="#ccc")
reg_username.pack(pady=5, ipady=5)

tk.Label(register_frame, text="Mật khẩu", bg="#ffffff", fg=text_color).pack()
reg_password = tk.Entry(register_frame, show="*", width=30, relief=tk.FLAT, bd=1, highlightthickness=1, highlightcolor="#ccc")
reg_password.pack(pady=5, ipady=5)

tk.Button(register_frame, text="Đăng ký", command=handle_register,
          bg=primary_color, fg="white", font=button_font,
          width=20, relief=tk.FLAT, bd=0).pack(pady=15, ipady=5)

tk.Label(register_frame, text="Đã có tài khoản?", bg="#ffffff", fg=text_color).pack()
tk.Button(register_frame, text="Quay lại đăng nhập", command=switch_to_login,
          font=small_font, bg="#ffffff", fg=primary_color, bd=0).pack(pady=(0, 10))

# Khởi động với màn hình đăng nhập
login_frame.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
>>>>>>> 63d605de596475f16a46be4ec03a4ca2fe6d33af

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

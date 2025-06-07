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
root = tk.Tk()
root.title("Đăng nhập")
root.geometry("360x640")
root.resizable(False, False)
root.configure(bg="#87CEEB")  # nền xanh trời

# ==== Frame đăng nhập ====
login_frame = tk.Frame(root, bg="#ffffff", bd=0)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(login_frame, text="🌤️ Weather App", font=("Segoe UI", 20, "bold"), bg="#ffffff", fg="#007aff").pack(pady=20)
tk.Label(login_frame, text="ĐĂNG NHẬP", font=("Segoe UI", 14, "bold"), bg="#ffffff").pack(pady=(0, 10))

tk.Label(login_frame, text="Tên đăng nhập", bg="#ffffff").pack()
login_username = tk.Entry(login_frame, width=30)
login_username.pack(pady=5)

tk.Label(login_frame, text="Mật khẩu", bg="#ffffff").pack()
login_password = tk.Entry(login_frame, show="*", width=30)
login_password.pack(pady=5)

tk.Button(login_frame, text="Đăng nhập", command=handle_login,
          bg="#007aff", fg="white", font=("Segoe UI", 12), width=20).pack(pady=15)

tk.Label(login_frame, text="Chưa có tài khoản?", bg="#ffffff").pack()
tk.Button(login_frame, text="Đăng ký", command=switch_to_register,
          font=("Segoe UI", 10), bg="#ffffff", fg="#007aff", bd=0).pack()

# ==== Frame đăng ký ====
register_frame = tk.Frame(root, bg="#ffffff", bd=0)

tk.Label(register_frame, text="🌤️ Weather App", font=("Segoe UI", 20, "bold"), bg="#ffffff", fg="#007aff").pack(pady=20)
tk.Label(register_frame, text="ĐĂNG KÝ", font=("Segoe UI", 14, "bold"), bg="#ffffff").pack(pady=(0, 10))

tk.Label(register_frame, text="Tên đăng nhập", bg="#ffffff").pack()
reg_username = tk.Entry(register_frame, width=30)
reg_username.pack(pady=5)

tk.Label(register_frame, text="Mật khẩu", bg="#ffffff").pack()
reg_password = tk.Entry(register_frame, show="*", width=30)
reg_password.pack(pady=5)

tk.Button(register_frame, text="Đăng ký", command=handle_register,
          bg="#007aff", fg="white", font=("Segoe UI", 12), width=20).pack(pady=15)

tk.Label(register_frame, text="Đã có tài khoản?", bg="#ffffff").pack()
tk.Button(register_frame, text="Quay lại đăng nhập", command=switch_to_login,
          font=("Segoe UI", 10), bg="#ffffff", fg="#007aff", bd=0).pack()

# Khởi động với màn hình đăng nhập
login_frame.pack()

root.mainloop()

import tkinter as tk
from tkinter import messagebox
import mouse
import keyboard
import time

running = False
delay = 0

def start_clicker():
    global running, delay
    
    try:
        clicks_per_second = float(entry.get())
        if clicks_per_second <= 0:
            messagebox.showerror("Ошибка", "Скорость кликов должна быть больше нуля.")
            return
        
        delay = int(1000 / clicks_per_second)

        messagebox.showinfo("Auto Clicker", "Auto Clicker запущен! Нажмите 'ESC', чтобы остановить.")
        running = True

        schedule_click()

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректное число кликов в секунду.")

def schedule_click():
    if running:
        mouse.click('left')

        root.after(delay, schedule_click)

def exit_app():
    global running
    if running:
        running = False
    
    messagebox.showinfo("Auto Clicker", "Auto Clicker остановлен.")
    root.destroy()

def show_info():
    messagebox.showinfo("Информация", "Это автокликер, он будет кликать мышью с заданной скоростью!")

root = tk.Tk()
root.title("Auto Clicker")
root.geometry("300x220")
root.resizable(0, 0)
root.configure(bg="#e0f7fa")

root.bind('i', show_info)

title_label = tk.Label(
    root,
    text="Auto Clicker",
    font=("Trebuchet MS", 16, "bold"),
    bg="#e0f7fa",
    fg="#00796b"
)
title_label.pack(pady=10)

label = tk.Label(
    root,
    text="Клики в секунду:",
    font=("Trebuchet MS", 12),
    bg="#e0f7fa",
    fg="#00796b"
)
label.pack(pady=5)

entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=10,
    justify="center"
)
entry.pack(pady=5)
entry.insert(0, "10")

button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.pack(side=tk.BOTTOM, pady=(20, 30))

start_button = tk.Button(
    button_frame,
    text="Старт",
    command=start_clicker,
    bg="#4caf50",
    activebackground="#66bb6a",
    fg="white",
    font=("Trebuchet MS", 12),
    width=8
)
start_button.grid(row=0, column=0, padx=10)

exit_button = tk.Button(
    button_frame,
    text="Выход",
    command=exit_app,
    bg="#f44336",
    activebackground="#ef5350",
    fg="white",
    font=("Trebuchet MS", 12),
    width=8
)
exit_button.grid(row=0, column=1, padx=10)

keyboard.add_hotkey('esc', exit_app)
root.protocol("WM_DELETE_WINDOW", exit_app)
root.mainloop()
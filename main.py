import customtkinter as ctk
from tkinter import messagebox
import time

# Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Study Planner + Focus Timer")
app.geometry("800x600")
app.configure(fg_color="#DFF5E1")  # Pastel mint background

# Global timer variables
timer_running = False
start_time = 25 * 60
time_left = start_time
task_name = ""

# ------------------ Timer Functions ------------------

def update_timer():
    global time_left, timer_running
    if timer_running and time_left > 0:
        minutes = time_left // 60
        seconds = time_left % 60
        timer_label.configure(text=f"{minutes:02}:{seconds:02}")
        time_left -= 1
        app.after(1000, update_timer)
    elif time_left == 0 and timer_running:
        timer_label.configure(text="00:00")
        timer_running = False
        messagebox.showinfo("Time's up!", f"Focus session for '{task_entry.get()}' is done.")
        if task_entry.get() != "":
            record_focus(task_entry.get())

def start_focus():
    global timer_running, task_name
    if not timer_running:
        timer_running = True
        task_name = task_entry.get()
        update_timer()

def pause_focus():
    global timer_running
    timer_running = False

def reset_focus():
    global timer_running, time_left
    timer_running = False
    time_left = start_time
    timer_label.configure(text="25:00")

# ------------------ Task Management ------------------

def add_task():
    task = task_entry.get()
    if task != "":
        today_tasks.insert("end", f"• {task}")
        task_entry.delete(0, "end")

def record_focus(task):
    focus_records.insert("end", f"{task} - 25m")

# ------------------ UI Layout ------------------

# Entry box
task_entry = ctk.CTkEntry(app, placeholder_text="Enter your task here", width=250)
task_entry.place(relx=0.5, rely=0.1, anchor="center")

# Timer Label
timer_label = ctk.CTkLabel(app, text="25:00", font=("Arial", 40, "bold"), text_color="#000")
timer_label.place(relx=0.5, rely=0.25, anchor="center")

# Buttons
start_button = ctk.CTkButton(app, text="▶ Start Focus", command=start_focus, fg_color="#CFE2F3", text_color="#000")
pause_button = ctk.CTkButton(app, text="⏸ Pause", command=pause_focus, fg_color="#F8C8DC", text_color="#000")
reset_button = ctk.CTkButton(app, text="🔁 Reset", command=reset_focus, fg_color="#FFFACD", text_color="#000")

start_button.place(relx=0.5, rely=0.4, anchor="center", y=0)
pause_button.place(relx=0.5, rely=0.4, anchor="center", y=40)
reset_button.place(relx=0.5, rely=0.4, anchor="center", y=80)

# Quote
quote_label = ctk.CTkLabel(app, text="Progress over perfection.", font=("Georgia", 14, "italic"), text_color="#444")
quote_label.place(relx=0.5, rely=0.9, anchor="center")

# Right-side task panel
right_frame = ctk.CTkFrame(app, width=250, height=500, corner_radius=10, fg_color="#f4f4f4")
right_frame.place(relx=0.85, rely=0.5, anchor="center")

# Today Label
today_label = ctk.CTkLabel(right_frame, text="🗓 Today", font=("Arial", 16, "bold"), text_color="#000")
today_label.pack(pady=(10, 5))

today_tasks = ctk.CTkTextbox(right_frame, height=100, width=220, font=("Arial", 13), text_color="#F1E6E6")
today_tasks.pack()

# Focus Records Label
record_label = ctk.CTkLabel(right_frame, text="🗂 Focus Records", font=("Arial", 15, "bold"), text_color="#000")
record_label.pack(pady=(10, 5))

focus_records = ctk.CTkTextbox(right_frame, height=100, width=220, font=("Arial", 13), text_color="#000")
focus_records.pack()

# Add Task Button
add_task_button = ctk.CTkButton(right_frame, text="+ Add Task", command=add_task, fg_color="#89CFF0", text_color="#000")
add_task_button.pack(pady=10)

# Run app
app.mainloop()

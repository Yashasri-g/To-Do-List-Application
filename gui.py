import tkinter as tk
from tkinter import messagebox, ttk
import json

# File to save the task list
FILE_NAME = 'tasks.json'

# Load the task list from the file
def load_tasks():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save the task list to a file
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    task_name = task_entry.get()
    if task_name:
        tasks.append({"name": task_name, "completed": False})
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Input Error", "Task name cannot be empty!")

# Mark a task as complete
def mark_task_complete():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks[selected_task_index]['completed'] = True
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task.")

# Delete a selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task.")

# Update the task list display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔️" if task['completed'] else "❌"
        task_listbox.insert(tk.END, f"{task['name']} [{status}]")

# Create gradient background (dynamic based on window size)
def create_gradient(canvas, color1, color2, width, height):
    for i in range(height):
        ratio = i / height
        r = int(ratio * (int(color2[1:3], 16) - int(color1[1:3], 16)) + int(color1[1:3], 16))
        g = int(ratio * (int(color2[3:5], 16) - int(color1[3:5], 16)) + int(color1[3:5], 16))
        b = int(ratio * (int(color2[5:7], 16) - int(color1[5:7], 16)) + int(color1[5:7], 16))
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, width, i, fill=color)

# Function to resize canvas and maintain gradient during window resize
def resize_bg(event):
    canvas.config(width=event.width, height=event.height)
    canvas.delete("all")
    create_gradient(canvas, "#3a7bd5", "#00d2ff", event.width, event.height)

# Initialize the app
tasks = load_tasks()

# Create the main window
window = tk.Tk()
window.title("Advanced Task Manager")
window.geometry("700x800")
window.minsize(500, 600)

# Create canvas for gradient background
canvas = tk.Canvas(window, highlightthickness=0)
canvas.pack(fill="both", expand=True)
create_gradient(canvas, "#3a7bd5", "#00d2ff", 700, 800)

# Handle window resize to adjust gradient
window.bind("<Configure>", resize_bg)

# Main Frame for Task Manager (to place content over the gradient background)
main_frame = tk.Frame(window, bg="#ffffff", relief=tk.RAISED, bd=2)
main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Add a title label with scaling font and advanced font style
title_label = tk.Label(main_frame, text="Task Manager", font=("Poppins", 28, "bold"), fg="#ffffff", bg="#3a7bd5")
title_label.pack(fill=tk.X, pady=20)

# Task Entry Box with custom font
task_entry = tk.Entry(main_frame, width=30, font=("Poppins", 14), bd=2, relief=tk.GROOVE)
task_entry.pack(pady=10)

# Add Task Button with hover effect and stylish look
def on_enter(e):
    add_button.config(bg="#006994", fg="white", relief=tk.RAISED)

def on_leave(e):
    add_button.config(bg="#3a7bd5", fg="white", relief=tk.FLAT)

add_button = tk.Button(main_frame, text="Add Task", command=add_task, font=("Poppins", 14, "bold"), 
                       bg="#3a7bd5", fg="white", activebackground="#0077b6", activeforeground="white", 
                       bd=2, relief=tk.FLAT, highlightthickness=2)
add_button.pack(pady=10)

# Bind hover effect to button
add_button.bind("<Enter>", on_enter)
add_button.bind("<Leave>", on_leave)

# Listbox for tasks with Scrollbar and custom style
task_listbox_frame = tk.Frame(main_frame)
task_listbox_frame.pack(pady=10)

task_listbox = tk.Listbox(task_listbox_frame, width=50, height=10, font=("Poppins", 12), 
                          selectbackground="#00d2ff", selectforeground="black", bd=2, relief=tk.GROOVE)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(task_listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Buttons (Mark Complete, Delete) placed directly on main_frame
# Mark as Complete Button with advanced styling
def on_enter_complete(e):
    complete_button.config(bg="#006994", fg="white", relief=tk.RAISED)

def on_leave_complete(e):
    complete_button.config(bg="#3a7bd5", fg="white", relief=tk.FLAT)

complete_button = tk.Button(main_frame, text="Mark as Complete", command=mark_task_complete, 
                            font=("Poppins", 14, "bold"), bg="#3a7bd5", fg="white", 
                            bd=2, relief=tk.FLAT, highlightthickness=2)
complete_button.pack(pady=10)

complete_button.bind("<Enter>", on_enter_complete)
complete_button.bind("<Leave>", on_leave_complete)

# Delete Task Button with advanced styling
def on_enter_delete(e):
    delete_button.config(bg="#e63946", fg="white", relief=tk.RAISED)

def on_leave_delete(e):
    delete_button.config(bg="#ff4757", fg="white", relief=tk.FLAT)

delete_button = tk.Button(main_frame, text="Delete Task", command=delete_task, 
                          font=("Poppins", 14, "bold"), bg="#ff4757", fg="white", 
                          bd=2, relief=tk.FLAT, highlightthickness=2)
delete_button.pack(pady=10)

delete_button.bind("<Enter>", on_enter_delete)
delete_button.bind("<Leave>", on_leave_delete)

# Update the task list display on startup
update_task_list()

# Run the main loop
window.mainloop()

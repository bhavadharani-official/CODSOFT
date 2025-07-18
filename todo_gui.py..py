import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []
def save_tracks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["completed"] else " ❌ "
        listbox.insert(tk.END, f"{status} {task['title']}")

def add_task():
    global tasks
    title= entry.get()
    if title.strip() == "":
        messagebox.showwarning("Warning", "Task title cannot be empty.")
        return
    tasks.append({"title": title,"completed":False})
    print("Added:",title)
    entry.delete(0, tk.END)
    update_listbox()
    save_tasks()

def complete_task():
    global tasks
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = True
        update_listbox()
        save_tasks()
    else:
        messagebox.showinfo("Info", "Select a task to mark as completed.")

def delete_task():
    global tasks
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        update_listbox()
        save_tasks()
    else:
        messagebox.showinfo("Info","Select a task to delete.")

root = tk.Tk()
root.title("📝 To-Do List App")
root.geometry("400x400")
root.resizable(False, False)

entry = tk.Entry(root, width=30,font=("Arial", 12))
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=10)

complete_button = tk.Button(root,text="Mark as Completed" , width=20,command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(root,text="Delete Task", width=20,command=delete_task)
delete_button.pack(pady=5)

tasks = load_tasks()
update_listbox()

root.mainloop()

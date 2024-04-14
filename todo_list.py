import tkinter as tk
from tkinter import simpledialog, messagebox


class TodoListApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(master)
        self.task_entry.pack()

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(master)
        self.task_listbox.pack()

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.refresh_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.refresh_tasks()
            self.task_entry.delete(0, tk.END)

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = simpledialog.askstring("Update Task", "Enter the updated task:")
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.refresh_tasks()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            confirmation = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
            if confirmation:
                self.tasks.pop(selected_task_index[0])
                self.refresh_tasks()

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.geometry("400x300")
    root.mainloop()

if __name__ == "__main__":
    main()
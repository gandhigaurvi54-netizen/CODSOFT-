import tkinter as tk
from tkinter import messagebox

class TodoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python To-Do List")
        self.root.geometry("600x650")
        self.root.config(bg="#893d3d")
        
        # Heading
        self.title_label = tk.Label(root, text="My Tasks", font=("cursive", 16, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)
        
        # Input Frame
        self.input_frame = tk.Frame(root, bg="#f0f0f0")
        self.input_frame.pack(pady=5)
        
        self.task_entry = tk.Entry(self.input_frame, font=("Arial", 12), width=25)
        self.task_entry.pack(side=tk.LEFT, padx=5)
        
        self.add_button = tk.Button(self.input_frame, text="Add", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)
        
        # Listbox Frame
        self.list_frame = tk.Frame(root)
        self.list_frame.pack(pady=15)
        
        self.task_listbox = tk.Listbox(self.list_frame, font=("Arial", 12), width=32, height=12, selectbackground="#a6a6a6")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)
        
        # Action Buttons
        self.action_frame = tk.Frame(root, bg="#f0f0f0")
        self.action_frame.pack(pady=5)
        
        self.complete_button = tk.Button(self.action_frame, text="Toggle Complete", font=("Arial", 10), bg="#2196F3", fg="white", command=self.toggle_task)
        self.complete_button.pack(side=tk.LEFT, padx=10)
        
        self.delete_button = tk.Button(self.action_frame, text="Delete Task", font=("Arial", 10), bg="#f44336", fg="white", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, f"[ ] {task}")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def toggle_task(self):
        try:
            selected_idx = self.task_listbox.curselection()[0]
            task_text = self.task_listbox.get(selected_idx)
            
            if task_text.startswith("[ ]"):
                updated_text = task_text.replace("[ ]", "[✔]", 1)
            else:
                updated_text = task_text.replace("[✔]", "[ ]", 1)
                
            self.task_listbox.delete(selected_idx)
            self.task_listbox.insert(selected_idx, updated_text)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task first!")

    def delete_task(self):
        try:
            selected_idx = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_idx)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoGUI(root)
    root.mainloop()
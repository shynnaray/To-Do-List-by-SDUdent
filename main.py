import tkinter
import tkinter.messagebox
import pickle



class MAIN_UI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("To-Do List by SDUdent")
        self.frame_tasks = tkinter.Frame(self.root)
        self.frame_tasks.pack()

        self.tasks = tkinter.Listbox(self.frame_tasks, height=10, width=50)
        self.tasks.pack(side=tkinter.LEFT)

        self.scrollbar_tasks = tkinter.Scrollbar(self.frame_tasks)
        self.scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.tasks.config(yscrollcommand=self.scrollbar_tasks.set)
        self.scrollbar_tasks.config(command=self.tasks.yview)
    
        self.entry_task = tkinter.Entry(self.root, width=50)
        self.entry_task.pack()

        self.button_add_task = tkinter.Button(self.root, text="Add task", width=48, command=self.add_task)
        self.button_add_task.pack()

        self.button_delete_task = tkinter.Button(self.root, text="Delete task", width=48, command=self.delete_task)
        self.button_delete_task.pack()

        self.button_load_tasks = tkinter.Button(self.root, text="Load tasks", width=48, command=self.load_tasks)
        self.button_load_tasks.pack()

        self.button_save_tasks = tkinter.Button(self.root, text="Save tasks", width=48, command=self.save_tasks)
        self.button_save_tasks.pack()

        self.root.mainloop()

    def add_task(self):
        task = self.entry_task.get()
        if task != "":
            self.tasks.insert(tkinter.END, task)
            self.entry_task.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

    def delete_task(self):
        try:
            task_index = self.tasks.curselection()[0]
            self.tasks.delete(task_index)
        except:
            tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

    def load_tasks(self):
        try:
            tasks = pickle.load(open("tasks.dat", "rb"))
            self.tasks.delete(0, tkinter.END)
            for task in tasks:
                self.tasks.insert(tkinter.END, task)
        except:
            tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

    def save_tasks(self):
        tasks = self.tasks.get(0, self.tasks.size())
        pickle.dump(tasks, open("tasks.dat", "wb"))


def main():
    ui = MAIN_UI()


if __name__ == '__main__':
    main()
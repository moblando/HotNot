import tkinter as tk


class appScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1080x980")

        self.root.title("App Screen")
        self.label = tk.Label(self.root, text="Welcome to the App Screen!") 
        self.label.pack(pady=20)
        

        self.root.mainloop()

if __name__ == "__main__":
    appScreen()

import tkinter as tk


class WebsiteBlocker:
    def __init__(self, root):
        self.root = root
        self.root.title("Website Blocker")
        self.root.geometry("400x400")
        self.root.configure(bg = "#1f1f1f")



if __name__ == "__main__":
    root = tk.Tk()
    app = WebsiteBlocker(root)
    root.mainloop()
    
import tkinter as tk
import customtkinter as ctk

class StudyInterface:

    def __init__(self, root):
        self.root = root
        self.root.title("FcosusFly")
        self.root.geometry("400x400")
        self.root.configure(bg = "#1f1f1f")

        self.app_title = tk.Label(root, text = "FocusFly", font = ("Courier Prime 16", 22), fg = "#ececec", bg = "#1f1f1f")
        self.app_title.pack(pady = 25)

        self.title_desc = tk.Label(root, text = "Focus is here. Procfrasination is gone.", font = ("Courier Prime 16", 10), fg = "#a5a5a5", bg = "#1f1f1f")
        self.title_desc.pack(pady = 30)


        self.study_button = ctk.CTkButton(root, text = "Study Timer", corner_radius = 20, command = self.open_study_timer, width = 20, height = 30, fg_color = "#4a7eff", text_color = "#ececec", hover_color = "#3a6eff", font = ("Courier Prime 16", 14))
        self.study_button.pack(pady = 10)


    def open_study_timer(self):
        self.root.destroy()
        import study_timer
        study_timer_root = tk.Tk()
        study_timer_app = study_timer.StudyTimer(study_timer_root)
        study_timer_root.mainloop()





if __name__ == "__main__":
    root = tk.Tk()
    app = StudyInterface(root)
    root.mainloop()
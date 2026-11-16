# imports
from cProfile import label
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import pygame
from study_timer import StudyTimer
from study_app import StudyApp


class BreakTimer(StudyApp):

    def __init__(self, root):
        super().__init__(root)
        self.root.title("Break Timer")

        # instructions
        self.instructions = tk.Label(root, text = "Break time!", font = ("Courier Prime 16", 13), fg = "#ececec", bg = "#1f1f1f")
        self.instructions.pack(pady = 25)

        # countdown text
        self.countdown_text = tk.Label(root, text = "10:00", font =("Courier Prime 16", 50), fg = "#4a7eff", bg = "#1f1f1f")
        self.countdown_text.pack()

        # slider
        self.slider.pack(pady = 50)
        self.slider.set(10)

    def update_timer(self):
        # update the countdown text
        super().update_timer()

        if self.countdown_text.cget("text") == "00:00" and self.is_timer_running:
            messagebox.showinfo("Time's up! Break time is over :D")
            pygame.mixer.init()
            pygame.mixer.music.load("bell.mp3")
            
            pygame.mixer.music.set_volume(0.6)
            pygame.mixer.music.play()
            self.is_timer_running = False
            pygame.mixer.music.stop()


if __name__ == "__main__":
    root = tk.Tk()
    break_timer = BreakTimer(root)
    root.mainloop()
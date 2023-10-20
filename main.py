import tkinter as tk


class Timer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Timer")
        self.overrideredirect(True)
        self.wm_attributes("-topmost", True)


        self.bind("<KeyPress-s>", self.toggle_timer)
        self.bind("<KeyPress-e>", self.terminate)
        
        self.configure(bg="black")
        self.geometry(f"200x50+{5120-200}+{2160-50}")
        self.label = tk.Label(self, text="00:00:00", font=("Courier", 30), bg="black", fg="white")
        self.label.pack(pady=10)

        self.elapsed = 0
        self.running = False
        self.count_up()

    def count_up(self):
        if self.running:
            self.elapsed += 1
            minutes, seconds = divmod(self.elapsed, 60)
            hours, minutes = divmod(minutes, 60)
            self.label.configure(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        self.after(1000, self.count_up)

    def toggle_timer(self, event):
        self.running = not self.running

    def terminate(self, event):
        exit()

if __name__ == "__main__":
    timer = Timer()
    timer.mainloop()

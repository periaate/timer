import tkinter as tk
import tkinter.simpledialog

class Timer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Timer")
        self.overrideredirect(True)
        self.wm_attributes("-topmost", True)

        self.bind("<KeyPress-s>", self.toggle_timer)
        self.bind("<KeyPress-e>", self.terminate)
        self.bind("<KeyPress-k>", self.edit_time)
        
        self.configure(bg="black")
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"200x50+{screen_width-200}+{screen_height-50}")

        self.label = tk.Label(self, text="00:00:00", font=("Courier", 30), bg="black", fg="white")
        self.label.pack(pady=10)

        self.elapsed = 0
        self.running = False
        self.count_up()

    def count_up(self):
        if self.running:
            self.elapsed += 1
            self.update_label()
        self.after(1000, self.count_up)

    def update_label(self):
        minutes, seconds = divmod(self.elapsed, 60)
        hours, minutes = divmod(minutes, 60)
        self.label.configure(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    def toggle_timer(self, event):
        self.running = not self.running

    def terminate(self, event):
        exit()

    def edit_time(self, event):
        user_input = tk.simpledialog.askstring("Input Time", "Enter elapsed time (e.g., 1200 for 00:12:00)")
        if user_input and user_input.isdigit():
            self.elapsed = int(user_input[-2:])  # seconds
            self.elapsed += int(user_input[-4:-2] or "0") * 60  # minutes
            self.elapsed += int(user_input[:-4] or "0") * 60 * 60  # hours
            self.update_label()

if __name__ == "__main__":
    timer = Timer()
    timer.mainloop()

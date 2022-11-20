import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title('英和・和英辞書')
        master.geometry('900x500')
        master.resizable(width=False, height=False)

        self.widgets()

    def widgets(self):
        self.result_word = tk.StringVar(self.master)

        # フレーム1
        self.frame1 = ttk.Frame(self.master)
        self.frame1.pack(side=tk.TOP, padx=30, pady=20, fill=tk.BOTH)
        
        self.search_icon = tk.PhotoImage(file='../assets/search_icon.png').subsample(2, 2)
        search_label = ttk.Label(self.frame1, image=self.search_icon)
        search_label.pack(side=tk.LEFT)

        self.font =('', 18)
        self.search_text = ttk.Entry(self.frame1, font=self.font, width=30, textvariable=self.result_word)
        self.search_text.pack(side=tk.LEFT)

        self.clear_icon = tk.PhotoImage(file='../assets/close_icon.png').subsample(2, 2)
        self.clear_button = ttk.Button(self.frame1, image=self.clear_icon)
        self.clear_button['command'] = lambda: self.search_text.delete(0, tk.END)
        self.clear_button.pack(side=tk.LEFT)
        
        # フレーム2
        self.frame2 = tk.Frame(self.master, width=900, height=400, bg="red")
        self.frame2.pack(side=tk.TOP, padx=30, fill=tk.BOTH)

        self.result = ttk.Label(self.frame2, textvariable=self.result_word)
        self.result.pack(side=tk.TOP)

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

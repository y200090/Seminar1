import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title('英和・和英辞書')
        master.geometry('900x500')
        master.resizable(width=False, height=False)

        self.widgets()

    def widgets(self):
        # フレーム1
        self.frame1 = tk.Frame(self.master, width=900, height=30)
        self.frame1.pack(side=tk.TOP, padx=51, pady=40, fill=tk.BOTH)

        self.font1 =('', 18)
        self.search_text = tk.Entry(self.frame1, font=self.font1, width=30, relief=tk.SOLID, bd=1)
        self.search_text.pack(side=tk.LEFT, ipady=3)

        # 削除ボタン
        self.clear_icon = tk.PhotoImage(file='../assets/close_icon.png').subsample(2, 2)
        self.clear_button = tk.Button(self.frame1, image=self.clear_icon, relief=tk.FLAT, width=30, height=30)
        self.clear_button['command'] = lambda: [
            self.search_text.delete(0, tk.END),
            self.textbox.delete(1.0, tk.END)
        ]
        self.clear_button.pack(side=tk.LEFT)

        # 検索ボタン
        self.search_icon = tk.PhotoImage(file='../assets/search_icon.png').subsample(2, 2)
        self.search_button = tk.Button(self.frame1, image=self.search_icon, relief=tk.FLAT, width=30, height=30)
        self.search_button['command'] = lambda: self.textbox.insert('1.0', self.search_text.get())
        self.search_button.pack(side=tk.LEFT)

        # フレーム2
        self.frame2 = tk.Frame(self.master, width=900)
        self.frame2.pack(side=tk.TOP, padx=30)

        self.font2 = ('', 16)
        self.textbox = tk.Text(self.frame2, font=self.font2, width=72, height=17, relief=tk.SOLID, bd=1)
        self.textbox.pack(side=tk.TOP)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

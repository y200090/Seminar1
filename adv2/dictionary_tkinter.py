# ===============最終発展課題2 12/1===============

import tkinter
from tkinter import ttk

# def print_terminal():
#     print(textbox.get())

# def delete_text():
#     textbox.delete(0, tkinter.END)

# # メインウィンドウ作成
# window = tkinter.Tk()
# window.title('start window!')
# window.geometry('900x500')
# window.resizable(width=False, height=False)

# label = tkinter.Label(text='検索')
# label.place(x=50, y=50)

# textbox = tkinter.Entry(width=40)
# textbox.place(x=90, y=50)

# button_output = tkinter.Button(
#     text='ターミナルに出力',
#     command=print_terminal
# ).place(x=350, y=50)

# button_delete = tkinter.Button(
#     text='削除',
#     command=delete_text
# ).place(x=450, y=50)


class Application(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title('英和・和英辞書')
        master.geometry('900x500')
        master.resizable(width=False, height=False)

        style = ttk.Style()
        style.theme_use('vista')
        self.widgets()

    def widgets(self):
        frame_top = ttk.Frame(
            self.master, 
            width=900, 
            height=30, 
            takefocus=True
        ).pack()

        self.search_icon = tkinter.PhotoImage(file='../assets/search_icon.png').subsample(2, 2)
        self.search_label = ttk.Label(
            self.master, 
            image=self.search_icon
            ).place(
                x=50, y=50
                )

        self.font =('', 16)
        self.search_text = ttk.Entry(self.master, font=self.font, ).place(x=82, y=50, width=300, height=28)

        self.clear_icon = tkinter.PhotoImage(file='../assets/close_icon.png').subsample(2, 2)
        self.clear_button = ttk.Button(self.master, image=self.clear_icon).place(x=382, y=50)

if __name__ == '__main__':
    root = tkinter.Tk()
    app = Application(master=root)
    app.mainloop()
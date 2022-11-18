# ===============最終発展課題2 12/1===============

import tkinter

def print_terminal():
    print(textbox.get())

def delete_text():
    textbox.delete(0, tkinter.END)

# メインウィンドウ作成
window = tkinter.Tk()
window.title('start window!')
window.geometry('900x500')
window.resizable(width=False, height=False)

label = tkinter.Label(text='検索')
label.place(x=50, y=50)

textbox = tkinter.Entry(width=40)
textbox.place(x=90, y=50)

button_output = tkinter.Button(
    text='ターミナルに出力',
    command=print_terminal
).place(x=350, y=50)

button_delete = tkinter.Button(
    text='削除',
    command=delete_text
).place(x=450, y=50)

# プログラム終了後もウィンドウを保持
window.mainloop()

import tkinter as tk
from tkinter import ttk
import re

with open('../assets/je_sys.tsv', 'r', encoding='utf-8') as f:
    je_sys_data = f.read()

with open('../assets/ej_sys.tsv', 'r', encoding='utf-8') as f:
    ej_sys_data = f.read()

class Application(tk.Frame):
    def select_dict(self, event):
        if self.pulldown_menu.get() == '英和':
            self.content = ej_sys_data
        elif self.pulldown_menu.get() == '和英':
            self.content = tk.StringVar(value=je_sys_data)

    def search_dict(self, event):
        if self.pulldown_menu.get() == '英和':
            pattern1 = re.compile('([.+*?$^\-/(){|}\[\]\\\])')
            words = pattern1.sub(r'\\\1', self.search_text.get())
            pattern2 = re.compile(f'{words}\t.\t(.*)', re.MULTILINE)
            results = pattern2.finditer(self.content)

        elif self.pulldown_menu.get() == '和英':
            pattern = re.compile(f'{self.search_text.get()}\t.\t(.*)', re.MULTILINE)
            results = pattern.finditer(self.content)

        conclude = ''
        result = None
        for result in results:
            conclude += result.group(1) + ' / '
        if result is None:
            conclude = 'Not Found!'
        self.textbox.insert(1.0, conclude)
    
    def __init__(self, master):
        super().__init__(master)
        master.title('英和・和英辞書')
        master.geometry('900x520')
        master.resizable(width=False, height=False)

        self.widgets()

    def widgets(self):
        self.content = ej_sys_data
        self.font1 =('', 18)
        self.font2 = ('', 16)
        pulldown_menu_style = ttk.Style()
        pulldown_menu_style.theme_use('vista')
        pulldown_menu_style.configure('option.TCombobox')

        # フレーム1
        self.frame1 = tk.Frame(self.master, width=900, height=30)
        self.frame1.pack(side=tk.TOP, padx=51, pady=40, fill=tk.BOTH)

        # オプション選択
        self.pulldown_menu = ttk.Combobox(self.frame1, state='readonly', values=('英和', '和英'), width=4, height=32, font=self.font1, style='option.TCombobox')
        self.pulldown_menu.pack(side=tk.LEFT, ipady=2)
        self.pulldown_menu.bind('<<ComboboxSelected>>', self.select_dict)
        self.pulldown_menu.set('英和')

        # 検索バー
        self.search_text = tk.Entry(self.frame1, font=self.font1, width=30, relief=tk.SOLID, bd=1)
        self.search_text.pack(side=tk.LEFT, ipady=3)
        self.search_text.bind('<Return>', self.search_dict)

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

        self.textbox = tk.Text(self.frame2, font=self.font2, width=72, height=17, relief=tk.SOLID, bd=1)
        self.textbox.pack(side=tk.TOP)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

import tkinter as tk


def select_all():
    for check in [over_18, commercial, follow]:
        check.select()


def deselect_all():
    for check in [over_18, commercial, follow]:
        check.deselect()


def switch_all():
    for check in [over_18, commercial, follow]:
        check.toggle()


def show():
    print('over_18', over_18_value.get())
    print('commercial', commercial_value.get())


win = tk.Tk()
win.geometry(f'300x400+100+200')
win.title('Моё первое графическое приложение')

over_18_value = tk.StringVar()  # строковая переменная, которая будет связана с чекбаттоном over_18
over_18_value.set('No')
commercial_value = tk.IntVar()  # числовая переменная, которая будет связана с чекбаттоном commercial

over_18 = tk.Checkbutton(win, text='Вам исполнилось 18 лет?',
                         variable=over_18_value,
                         onvalue='Yes',
                         offvalue='No')
commercial = tk.Checkbutton(win, text='Хотите получать рекламу?',
                            variable=commercial_value,
                            onvalue=1,
                            offvalue=0)
follow = tk.Checkbutton(win, text='Хотите подписаться на канал?', indicatoron=0)
over_18.pack()
commercial.pack()
follow.pack()

tk.Button(win, text='select all', command=select_all).pack()
tk.Button(win, text='deselect all', command=deselect_all).pack()
tk.Button(win, text='switch all', command=switch_all).pack()
tk.Button(win, text='Show', command=show).pack()

win.mainloop()

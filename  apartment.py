import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.resizable(False, False)
win.title('Квартиры')
win.config(padx=5, pady=5)
win.config(bg='#AFB3B6')

lab_data = tk.Label(win, text='Февраль 2023', font=('Arial', 16), bg='#AFB3B6', relief=tk.RAISED, bd=1)\
                    .grid(row=1, column=2, sticky='we', padx=3, pady=3, ipadx=3, ipady=3)
lab_flat1_adres = tk.Label(win, text='ул .Байсеитовой', font=('Arial', 16), bg='#AFB3B6', relief=tk.RAISED, bd=1)\
                    .grid(row=1, column=0, sticky='we', padx=3, pady=3, ipadx=3, ipady=3)

lab_flat1_com = tk.Label(win, text='Электроэнергия', font=('Arial', 13), relief=tk.RAISED, padx=20, pady=3, bd=0, anchor='e')\
                    .grid(row=2, column=0, sticky='we', padx=3, pady=1)
lab_flat1_mus = tk.Label(win, text='Мусор', font=('Arial', 13), relief=tk.RAISED, padx=20, pady=3, bd=0, anchor='e')\
                    .grid(row=3, column=0, sticky='we', padx=3, pady=3)
lab_flat1_voda = tk.Label(win, text='Вода', font=('Arial', 13), relief=tk.RAISED, padx=20, pady=3, bd=0, anchor='e')\
                    .grid(row=4, column=0, sticky='we', padx=3, pady=3)
lab_flat1_ksk = tk.Label(win, text='КСК', font=('Arial', 13), relief=tk.RAISED, padx=20, pady=3, bd=0, anchor='e')\
                    .grid(row=5, column=0, sticky='we', padx=3, pady=3)
lab_flat1_lift = tk.Label(win, text='Лифт', font=('Arial', 13), relief=tk.RAISED, padx=20, pady=3, bd=0, anchor='e')\
                    .grid(row=6, column=0, sticky='we', padx=3, pady=3)

lab_flat1_com_sel = tk.Label(win, text='оплачено', font=('Arial Narrow', 14), bg='#AFB3B6', fg='#275F2F', relief=tk.RAISED, bd=0)\
                    .grid(row=2, column=1, sticky='we')
lab_flat1_mus_sel = tk.Label(win, text='не оплачено', font=('Arial Narrow', 14), bg='#AFB3B6', fg='#D5323D', relief=tk.RAISED, bd=0)\
                    .grid(row=3, column=1, sticky='we')
lab_flat1_voda_sel = tk.Label(win, text='не оплачено', font=('Arial Narrow', 14), bg='#AFB3B6', fg='#D5323D', relief=tk.RAISED, bd=0)\
                    .grid(row=4, column=1, sticky='we')
lab_flat1_ksk_sel = tk.Label(win, text='не оплачено', font=('Arial Narrow', 14), bg='#AFB3B6', fg='#D5323D', relief=tk.RAISED, bd=0)\
                    .grid(row=5, column=1, sticky='we')
lab_flat1_lift_sel = tk.Label(win, text='не оплачено', font=('Arial Narrow', 14), bg='#AFB3B6', fg='#D5323D', relief=tk.RAISED, bd=0)\
                    .grid(row=6, column=1, sticky='we')


check_flat_com = tk.Checkbutton(win, text='последняя оплата 14.02.2023', indicatoron=0, font=('Arial', 12), pady=0)\
                    .grid(row=2, column=2, sticky='we', padx=3, pady=1)
check_flat_mus = tk.Checkbutton(win, text='последняя оплата 14.02.2023', indicatoron=0, font=('Arial', 12), pady=0)\
                    .grid(row=3, column=2, sticky='we', padx=3, pady=1)
check_flat_voda = tk.Checkbutton(win, text='последняя оплата 14.02.2023', indicatoron=0, font=('Arial', 12), pady=0)\
                    .grid(row=4, column=2, sticky='we', padx=3, pady=1)
check_flat_ksk = tk.Checkbutton(win, text='последняя оплата 14.02.2023', indicatoron=0, font=('Arial', 12), pady=0)\
                    .grid(row=5, column=2, sticky='we', padx=3, pady=1)
check_flat_lift = tk.Checkbutton(win, text='последняя оплата 14.02.2023', indicatoron=0, font=('Arial', 12), pady=0)\
                    .grid(row=6, column=2, sticky='we', padx=3, pady=1)


win.grid_columnconfigure(0, minsize=400)
win.grid_columnconfigure(1, minsize=100)
win.grid_columnconfigure(2, minsize=200)


win.update_idletasks()          # обновляем информацию по размерам окна
s = win.geometry()
s = s.split('+')
s = s[0].split('x')
width_root = int(s[0])
height_root = int(s[1])
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
w = w // 2
h = h // 2
w = w - width_root // 2
h = h - height_root // 2
x = (win.winfo_screenwidth() // 2)
y = (win.winfo_screenheight() // 2)
win.geometry('+{}+{}'.format(w, h))          # устанавливаем окно по середине экрана

win.mainloop()

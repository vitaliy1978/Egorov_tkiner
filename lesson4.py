import tkinter as tk

win = tk.Tk()
win.geometry(f'400x500+100+200')
win.title('Урок 4')

btn1 = tk.Button(win, text='Hello 1')
btn2 = tk.Button(win, text='Hello 2')
btn3 = tk.Button(win, text='Hello 3')
btn4 = tk.Button(win, text='Hello world')
btn5 = tk.Button(win, text='Hello 5')
btn6 = tk.Button(win, text='Hello 6')
btn7 = tk.Button(win, text='Hello 7')
btn8 = tk.Button(win, text='Hello 8')

for i in range(4,9):
    for j in range(2):
        tk.Button(win, text=f'Hello {i-4} {j}').grid(row=i, column=j, stick='we')

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1, sticky='we')
btn3.grid(row=1, column=0, sticky='we')
btn4.grid(row=1, column=1)
btn5.grid(row=2, column=0)
btn6.grid(row=2, column=1, sticky='we')
btn7.grid(row=3, column=0, columnspan=2, stick='we')  # columnspan=2 - размещает на две колонки, stick='we' - расстягивает по горизонтали
btn7.grid(row=0, column=2, rowspan=4, sticky='ns')  # columnspan=4 - размещает на 4 колонки, stick='ns' - расстягивает по вертикали


win.grid_columnconfigure(0, minsize=150)
win.grid_columnconfigure(1, minsize=50)

win.mainloop()

import tkinter as tk


def show_output():
    x = []
    output = ''
    y = int(numbers_input.get())

    for i in range(25):
        if i == 0:
            x.append((y * y + 5) / 10)
        else:
            x.append((x[i - 1] * x[i - 1] + 5) / 10)

    for i in range(25):
        output += str(i) + '=' + str('%.4f' % x[i]) + '\n'
    output_label.configure(text=output)

window = tk.Tk()
window.title('pythonProject')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='ระเบียบวิธีซ้ำเดิมเชิงเดียว')
title_label.pack(pady=20)

numbers_input = tk.Entry(master=window)
numbers_input.pack()

go_button = tk.Button(
    master=window, text='OK',
    command=show_output
)
go_button.pack()

output_label = tk.Label(master=window)
output_label.pack(pady=20)

window.mainloop()
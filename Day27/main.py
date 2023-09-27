import tkinter as t

FONT = ('Consolas', 16, 'normal')

window = t.Tk()
window.title('Miles to Km Converter')
window.config(pady=50, padx=50)

phrase = t.Label(text='is equal to', font=FONT, cursor='none')
phrase.grid(column=0, row=1)

result = t.Text(font=FONT, cursor="arrow", width=9, height=1)
result.tag_configure("center", justify='center')
result.insert(1.0, "0", "center")
result.config(state='disabled', bg=window.cget('bg'), relief="flat")
result.grid(column=1, row=1)

result_units = t.Label(text='Km', font=FONT, cursor='none')
result_units.grid(column=2, row=1)


def convert():
    result.config(state='normal')
    result.insert(1.0, f'{int(my_input.get()) * 1.60934:.2f}', "center")
    result.config(state='disabled')


my_button = t.Button(text='Calculate', font=FONT, cursor='hand2', relief='raised', border=5, width=9, command=convert)
my_button.grid(column=1, row=2)

my_input = t.Entry(font=FONT, justify='center', width=9)
my_input.insert(0, "0")
my_input.grid(column=1, row=0)

input_units = t.Label(text='Miles', font=FONT, cursor='none')
input_units.grid(column=2, row=0)

window.mainloop()

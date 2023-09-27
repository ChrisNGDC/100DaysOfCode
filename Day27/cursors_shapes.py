import tkinter as t

FONT = ('Consolas', 30, 'normal')

window = t.Tk()
window.title('Test')
window.minsize(500, 500)

cursors_shapes = ["arrow",
                  "circle",
                  "clock",
                  "cross",
                  "dotbox",
                  "exchange",
                  "fleur",
                  "heart",
                  "heart",
                  "man",
                  "mouse",
                  "pirate",
                  "plus",
                  "shuttle",
                  "sizing",
                  "spider",
                  "spraycan",
                  "star",
                  "target",
                  "tcross",
                  "trek",
                  "watch"]

print(len(cursors_shapes))
i = 0
j = 0
for shape in cursors_shapes:
    new_label = t.Label(text=shape, font=FONT, cursor=shape)
    new_label.grid(column=i, row=j)
    i += 1
    if i == 5:
        j += 1
        i = 0

window.mainloop()

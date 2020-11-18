from tkinter import *
window = Tk()


def create_board():
    count_rows = 8
    pawn_rows = 2
    width = 75
    start_x = 0
    start_y = 0
    width_p = 73
    start_y_p = 0
    start_x_p = 0
    cell_color = "white"
    pawn_color = "yellow"
    for i in range(count_rows):
        for j in range(count_rows):
            canvas.create_rectangle(start_x, start_y, start_x + width, start_y + width, fill=cell_color)
            start_x = start_x + width
            if cell_color == "white":
                cell_color = "brown"
            else:
                cell_color = "white"
        start_x = 0
        start_y = start_y + width
        if cell_color == "white":
            cell_color = "brown"
        else:
            cell_color = "white"
    for k in range(pawn_rows):
        for e in range(count_rows):
            pawn = canvas.create_rectangle(start_x_p + 30, start_y_p + 95, start_x_p + 65, start_y_p + 130, fill = pawn_color)
            start_x_p = start_x_p + width_p
        start_y_p = start_y_p + 375
        start_x_p = 0
        pawn_color = "black"




canvas = Canvas(window, width=600, height=600)
canvas.pack()

create_board()

window.mainloop()
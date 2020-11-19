from tkinter import *
window = Tk()


def create_board():
    count_rows = 8
    figure_count_rows = 2
    figure_rows = 2
    figure_count_rows_two = 1
    width = 75
    start_x = 0
    start_y = 0
    width_p = 73
    start_y_p = 0
    start_x_p = 0
    start_x_q = 0
    start_y_q = 0
    width_q = 75
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
    for k in range(figure_rows):
        for e in range(count_rows):
            pawn = canvas.create_rectangle(start_x_p + 30, start_y_p + 95, start_x_p + 65, start_y_p + 130, fill = pawn_color)
            start_x_p = start_x_p + width_p
        start_y_p = start_y_p + 375
        start_x_p = 0
        pawn_color = "black"
    for t in range(figure_count_rows):
        for y in range(figure_count_rows_two):
            qeen = canvas.create_rectangle(start_x_q + 325, start_y_q + 25, start_x_q + 360, start_y_q + 60, fill = pawn_color)
            start_x_q = start_x_q + width_q
        start_y_q = start_y_q + 525
        start_x_q = 0
        pawn_color = "black"





canvas = Canvas(window, width=600, height=600)
canvas.pack()

create_board()

window.mainloop()
from tkinter import *
window = Tk()
window.title("flex")


canvas = Canvas(window, width=600, height=600)
canvas.pack()






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
start_x_k = 0
start_y_k = 0
start_x_t = 0
start_y_t = 0
start_x_h = 0
start_y_h = 0
start_x_o = 0
start_y_o = 0
start_x_t1 = 0
start_y_t1= 0
start_x_h1 = 0
start_y_h1 = 0
start_x_o1 = 0
start_y_o1 = 0
width_t1 = 75
width_t = 75
width_k = 75
width_q = 75
width_o = 75
width_h = 75
width_o1 = 75
width_h1 = 75
tura_model = "♜"
queen_model = "♛"
pawn_model = "♟"
king_model = "♚"
horse_model="♞"
officer_model="♝"
cell_color = "white"
pawn_color = "black"
for i in range(count_rows):
    for j in range(count_rows):
        row = canvas.create_rectangle(start_x, start_y, start_x + width, start_y + width, fill=cell_color)
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
        #pawn = canvas.create_rectangle(start_x_p + 30, start_y_p + 95, start_x_p + 65, start_y_p + 130, fill = pawn_color)
        pawn = canvas.create_text(start_x_p + 35, start_y_p + 115, text = pawn_model, font = "Arial 50", fill = pawn_color)
        start_x_p = start_x_p + width_p
    start_y_p = start_y_p + 375
    start_x_p = 0
    pawn_color = "orange"
for t in range(figure_count_rows):
    for y in range(figure_count_rows_two):
        #queen = canvas.create_rectangle(start_x_q + 255, start_y_q + 25, start_x_q + 280, start_y_q + 60, fill = pawn_color)
        queen = canvas.create_text(start_x_q + 260, start_y_q + 40, text=queen_model, font="Arial 50", fill= pawn_color)
        start_x_q = start_x_q + width_q
    start_y_q = start_y_q + 525
    start_x_q = 0
    pawn_color = "orange"

for x in range(figure_count_rows):
    for l in range(figure_count_rows_two):
        #king = canvas.create_rectangle(start_x_k + 320, start_y_k + 25, start_x_k + 355, start_y_k + 60, fill = pawn_color)
        king = canvas.create_text(start_x_k + 335, start_y_k + 40, text=king_model, font="Arial 50", fill= pawn_color)
        start_x_k = start_x_k + width_k
    start_y_k = start_y_k + 525
    start_x_k = 0
    pawn_color = "orange"
for p in range(figure_count_rows):
    for z in range(figure_count_rows_two):
        #king = canvas.create_rectangle(start_x_k + 320, start_y_k + 25, start_x_k + 355, start_y_k + 60, fill = pawn_color)
        tura = canvas.create_text(start_x_t + 40, start_y_t + 40, text= tura_model, font="Arial 50", fill= pawn_color)
        start_x_t = start_x_t + width_t
    start_y_t = start_y_t + 525
    start_x_t = 0
    pawn_color = "orange"
for t in range(figure_count_rows):
    for y in range(figure_count_rows_two):
        #queen = canvas.create_rectangle(start_x_h + 255, start_y_h + 25, start_x_h + 280, start_y_h + 60, fill = pawn_color)
        horse = canvas.create_text(start_x_h + 110, start_y_h + 40, text=horse_model, font="Arial 50", fill= pawn_color)
        start_x_h = start_x_h + width_h
    start_y_h = start_y_h + 525
    start_x_h = 0
    pawn_color = "orange"
for t in range(figure_count_rows):
    for y in range(figure_count_rows_two):
        #queen = canvas.create_rectangle(start_x_o + 255, start_y_o + 25, start_x_o + 280, start_y_o + 60, fill = pawn_color)
        officer = canvas.create_text(start_x_o + 180, start_y_o + 40, text=officer_model, font="Arial 50", fill= pawn_color)
        start_x_o = start_x_o + width_o
    start_y_o = start_y_o + 525
    start_x_o = 0
    pawn_color = "orange"
for p in range(figure_count_rows):
    for z in range(figure_count_rows_two):
        #king = canvas.create_rectangle(start_x_t1 + 320, start_y_t1 + 25, start_x_t1 + 355, start_y_t1 + 60, fill = pawn_color)
        tura = canvas.create_text(start_x_t1 + 570, start_y_t1 + 40, text= tura_model, font="Arial 50", fill= pawn_color)
        start_x_t1 = start_x_t1 + width_t1
    start_y_t1 = start_y_t1 + 525
    start_x_t1 = 0
    pawn_color = "orange"
for t in range(figure_count_rows):
    for y in range(figure_count_rows_two):
        #queen = canvas.create_rectangle(start_x_h1 + 255, start_y_h1 + 25, start_x_h1 + 280, start_y_h1 + 60, fill = pawn_color)
        horse = canvas.create_text(start_x_h1 +490, start_y_h1 + 40, text=horse_model, font="Arial 50", fill= pawn_color)
        start_x_h1 = start_x_h1 + width_h1
    start_y_h1 = start_y_h1 + 525
    start_x_h1 = 0
    pawn_color = "orange"
for t in range(figure_count_rows):
    for y in range(figure_count_rows_two):
        #queen = canvas.create_rectangle(start_x_o1 + 255, start_y_o1 + 25, start_x_o1 + 280, start_y_o1 + 60, fill = pawn_color)
        officer = canvas.create_text(start_x_o1 + 420, start_y_o1 + 40, text=officer_model, font="Arial 50", fill= pawn_color)
        start_x_o1 = start_x_o1 + width_o1
    start_y_o1 = start_y_o1 + 525
    start_x_o1 = 0
    pawn_color = "orange"

#window.bind('<Button-1>',figure_choose)
window.mainloop()
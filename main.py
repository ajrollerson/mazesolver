from graphics import Window, Point, Line, Cell

def main():

    win = Window(800, 600)

    cell1 = Cell(win)
    cell2 = Cell(win)
    cell3 = Cell(win)
    cell4 = Cell(win)

    cell2.has_bottom_wall = False
    cell1.has_left_wall = False
    cell2.has_right_wall = False
    cell3.has_top_wall = False

    cell1.draw(100, 100, 200, 200)
    cell2.draw(200, 200, 300, 300)
    cell3.draw(300, 300, 400, 400)
    cell4.draw(400, 400, 500, 500)

    cell1.draw_move(cell3, False)
    cell2.draw_move(cell3, False)
    cell3.draw_move(cell4, False)
    cell3.draw_move(cell4, True)


    win.wait_for_close()

if __name__ == "__main__":
    main()
    

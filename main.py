from graphics import Window, Point, Line, Cell, Maze

def main():

    win = Window(1200, 800)

    maze = Maze(100, 100, 20, 30, 25, 25, win)
    


    win.wait_for_close()

if __name__ == "__main__":
    main()
    

from graphics import Window
from maze import Maze
import time

def main():

    win = Window(1200, 800)

    maze = Maze(100, 100, 10, 20, 50, 50, win)

    maze.solve_dfs()
    maze.reset_timer()
    maze.solve_dh_dfs()
    

    win.wait_for_close()

if __name__ == "__main__":
    main()
    

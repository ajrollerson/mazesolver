from graphics import Cell
import time
import random

class Maze():
    def __init__(
      self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.timer_on = False
        if seed is not None:
            random.seed(seed)
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()
    

    def __create_cells(self):
        for col in range(self.num_cols):
            column = []
            for row in range(self.num_rows):
                column.append(Cell(self.win))
            self.__cells.append(column)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i, j)
        

    def __draw_cell(self, i, j):
        x1 = self.x1 + (i * self.cell_size_x)
        y1 = self.y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.win != None:
            self.win.redraw()
            if self.timer_on == True:
                self.win.elapsed_time = time.perf_counter() - self.win.start_time
            time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False 
        self.__draw_cell(self.num_cols - 1, self.num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        candidates = [
            (i - 1, j),
            (i + 1, j),
            (i, j - 1),
            (i, j + 1),
        ]

        while True:
            visitable = []
            for next_i, next_j in candidates:
                if 0 <= next_i < self.num_cols and 0 <= next_j < self.num_rows:
                    if not self.__cells[next_i][next_j].visited:
                        visitable.append((next_i, next_j))

            if not visitable:
                self.__draw_cell(i, j)
                return
            else:
                chosen_cell = random.choice(visitable)
                next_i, next_j = chosen_cell
                if next_i == i + 1:
                    self.__cells[i][j].has_right_wall = False
                    self.__cells[next_i][next_j].has_left_wall = False
                if next_i == i - 1:
                    self.__cells[i][j].has_left_wall = False
                    self.__cells[next_i][next_j].has_right_wall = False
                if next_j == j + 1:
                    self.__cells[i][j].has_bottom_wall = False
                    self.__cells[next_i][next_j].has_top_wall = False
                if next_j == j - 1:
                    self.__cells[i][j].has_top_wall = False
                    self.__cells[next_i][next_j].has_bottom_wall = False
                self.__break_walls_r(next_i, next_j)

    def __reset_cells_visited(self):
        for col in self.__cells:
            for j in col:
                j.visited = False
        
    def solve(self):
        self.timer_on = True
        self.win.start_time = time.perf_counter()
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self.__cells[i][j].visited = True
        self.__animate()
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        if i > 0 and not self.__cells[i - 1][j].visited and not self.__cells[i][j].has_left_wall:
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i - 1][j], undo=True)
        
        if i < self.num_cols - 1 and not self.__cells[i + 1][j].visited and not self.__cells[i][j].has_right_wall:
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i + 1][j], undo=True)

        if j > 0 and not self.__cells[i][j - 1].visited and not self.__cells[i][j].has_top_wall:
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j - 1], undo=True)

        if j < self.num_rows - 1 and not self.__cells[i][j + 1].visited and not self.__cells[i][j].has_bottom_wall:
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j + 1], undo=True)

        
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=self.width, height=self.height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_colour):
        line.draw(self.__canvas, fill_colour)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_colour):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_colour, width=2
        )

class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
        if self.__win != None:
            if self.has_left_wall:
                left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
                self.__win.draw_line(left_wall, "black")
            else:
                left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
                self.__win.draw_line(left_wall, "white")

            if self.has_right_wall:
                right_wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
                self.__win.draw_line(right_wall, "black")
            else:
                right_wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
                self.__win.draw_line(right_wall, "white")

            if self.has_top_wall:
                top_wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
                self.__win.draw_line(top_wall, "black")
            else:
                top_wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
                self.__win.draw_line(top_wall, "white")

            if self.has_bottom_wall:
                bottom_wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
                self.__win.draw_line(bottom_wall, "black")
            else:
                bottom_wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
                self.__win.draw_line(bottom_wall, "white")
        
    def draw_move(self, to_cell, undo=False):
        if self.__win != None:
            self_x = (self.__x1 + self.__x2) // 2
            self_y = (self.__y1 + self.__y2) // 2
            to_cell_x = (to_cell.__x1 + to_cell.__x2) // 2
            to_cell_y = (to_cell.__y1 + to_cell.__y2) // 2
            to_line = Line(Point(self_x, self_y), Point(to_cell_x, to_cell_y))
            if not undo:
                self.__win.draw_line(to_line, "red")
            else:
                self.__win.draw_line(to_line, "gray")

"""Neon Snake – starten mit: python snake_3d.py"""
import random
import tkinter as tk

COLS, ROWS, CELL = 20, 20, 30
BG, BOARD, GRID = "#07111f", "#10243a", "#1a3650"
GREEN, FRUIT, TEXT = "#48e6a5", "#ff5d72", "#edf7ff"


class Snake:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NEON SNAKE")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)
        self.canvas = tk.Canvas(self.root, width=850, height=650, bg=BG,
                                highlightthickness=0)
        self.canvas.pack()
        self.root.bind("<Key>", self.key)
        self.best = 0
        self.reset()
        self.loop()
        self.root.mainloop()

    def reset(self):
        self.snake = [(10, 10), (9, 10), (8, 10), (7, 10)]
        self.direction = self.next_direction = (1, 0)
        self.score, self.paused, self.over = 0, False, False
        self.new_fruit()

    def new_fruit(self):
        choices = [(x, y) for x in range(COLS) for y in range(ROWS)
                   if (x, y) not in self.snake]
        self.fruit = random.choice(choices)

    def key(self, event):
        moves = {"Left": (-1, 0), "a": (-1, 0), "Right": (1, 0),
                 "d": (1, 0), "Up": (0, -1), "w": (0, -1),
                 "Down": (0, 1), "s": (0, 1)}
        if event.keysym in moves and not self.over:
            move = moves[event.keysym]
            if move != (-self.direction[0], -self.direction[1]):
                self.next_direction = move
        elif event.keysym.lower() == "p" and not self.over:
            self.paused = not self.paused
        elif event.keysym.lower() == "r":
            self.reset()
        elif event.keysym == "Escape":
            self.root.destroy()

    def loop(self):
        if not self.paused and not self.over:
            self.direction = self.next_direction
            x, y = self.snake[0]
            # Die Wände sind Portale: Die Schlange erscheint gegenüber wieder.
            head = ((x + self.direction[0]) % COLS,
                    (y + self.direction[1]) % ROWS)
            ate = head == self.fruit
            if head in (self.snake if ate else self.snake[:-1]):
                self.over = True
                self.best = max(self.best, self.score)
            else:
                self.snake.insert(0, head)
                if ate:
                    self.score += 10
                    self.best = max(self.best, self.score)
                    self.new_fruit()
                else:
                    self.snake.pop()
        self.draw()
        self.root.after(max(60, 120 - self.score // 4), self.loop)

    def cell(self, position):
        x, y = 25 + position[0] * CELL, 25 + position[1] * CELL
        return x, y, x + CELL, y + CELL

    def rr(self, x1, y1, x2, y2, radius, **kwargs):
        points = [x1+radius,y1, x2-radius,y1, x2,y1, x2,y1+radius,
                  x2,y2-radius, x2,y2, x2-radius,y2, x1+radius,y2,
                  x1,y2, x1,y2-radius, x1,y1+radius, x1,y1]
        self.canvas.create_polygon(points, smooth=True, splinesteps=18, **kwargs)

    def draw(self):
        c = self.canvas
        c.delete("all")
        self.rr(31, 34, 631, 634, 18, fill="#02060b", outline="")
        self.rr(25, 25, 625, 625, 18, fill=BOARD, outline="#355b7b", width=2)
        for i in range(1, COLS):
            c.create_line(25+i*CELL, 35, 25+i*CELL, 615, fill=GRID)
        for i in range(1, ROWS):
            c.create_line(35, 25+i*CELL, 615, 25+i*CELL, fill=GRID)

        x1, y1, x2, y2 = self.cell(self.fruit)
        c.create_oval(x1+8, y1+11, x2-4, y2-2, fill="#741a2c", outline="")
        c.create_oval(x1+7, y1+5, x2-7, y2-7, fill=FRUIT, outline="#ffabb5")
        c.create_oval(x1+12, y1+9, x1+17, y1+14, fill="#fff7f8", outline="")

        for index, part in reversed(list(enumerate(self.snake))):
            x1, y1, x2, y2 = self.cell(part)
            self.rr(x1+6, y1+8, x2-3, y2-2, 7, fill="#07543e", outline="")
            color = "#72f7c0" if index == 0 else GREEN
            self.rr(x1+4, y1+4, x2-5, y2-5, 7, fill=color, outline="#a6ffda")
            c.create_line(x1+10, y1+8, x2-11, y1+8, fill="#d0ffe8")

        x1, y1, x2, y2 = self.cell(self.snake[0])
        if self.direction[0]:
            ex = x2-10 if self.direction[0] > 0 else x1+10
            eyes = [(ex, y1+10), (ex, y2-10)]
        else:
            ey = y2-10 if self.direction[1] > 0 else y1+10
            eyes = [(x1+10, ey), (x2-10, ey)]
        for ex, ey in eyes:
            c.create_oval(ex-3, ey-3, ex+3, ey+3, fill="#062317", outline="")

        c.create_text(665, 38, anchor="nw", text="NEON\nSNAKE", fill=TEXT,
                      font=("Helvetica", 25, "bold"))
        c.create_text(665, 105, anchor="nw", text="WÄNDE SIND PORTALE", fill=GREEN,
                      font=("Helvetica", 9, "bold"))
        self.rr(665, 145, 825, 225, 14, fill="#0d1b2e", outline="#25435e")
        c.create_text(680, 160, anchor="nw", text="PUNKTE", fill="#90a8bd",
                      font=("Helvetica", 9, "bold"))
        c.create_text(680, 180, anchor="nw", text=f"{self.score:04d}", fill=TEXT,
                      font=("Helvetica", 22, "bold"))
        c.create_text(760, 160, anchor="nw", text="BESTE", fill="#90a8bd",
                      font=("Helvetica", 9, "bold"))
        c.create_text(760, 181, anchor="nw", text=f"{self.best:04d}", fill=GREEN,
                      font=("Helvetica", 14, "bold"))
        c.create_text(665, 270, anchor="nw", fill="#a9bed0", font=("Helvetica", 11),
                      text="STEUERUNG\n\nPfeiltasten / WASD\nP  Pause\nR  Neustart\nEsc  Beenden")

        if self.over or self.paused:
            self.rr(125, 240, 525, 390, 18, fill="#081522", outline="#4d7893", width=2)
            title = "GAME OVER" if self.over else "PAUSE"
            subtitle = "R für eine neue Runde" if self.over else "P zum Fortsetzen"
            c.create_text(325, 290, text=title, fill=TEXT, font=("Helvetica", 26, "bold"))
            c.create_text(325, 335, text=subtitle, fill=GREEN, font=("Helvetica", 12, "bold"))


Snake()

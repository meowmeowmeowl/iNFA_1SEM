from random import randint
from tkinter import *
from datetime import datetime

WIDTH = 500
HEIGHT = 100


class Ball:
    def __init__(self):
        self.R = randint(10, 15) #храним размер, при каждом создании объекта будет выбираться случайно
        self.x = randint(self.R, WIDTH - self.R) # храним положение по x и y
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (10, 10) # это по сути шаг движения шаров. если увеличить -- будут двигаться быстрее
        d = {}
        d[1] = "orange"
        d[2] = "green"
        d[3] = "blue"
        d[4] = "red"
        d[5] = "purple"
        d[6] = "grey"
        d[7] = "black"
        d[8] = "white"
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill=d[randint(1,8)]) # при создании шарика отрисовываем его

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0: # отражение от стенок
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0: # отр
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def click_handler(event):
    balls.append(Ball())

#здесь мы уже привычно обращаемся к balls как к глобальной переменной. На самом деле дело в том, что нам лень писать классы.
def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)

if __name__ == "__main__":
	root = Tk()
	root.geometry(f'{WIDTH}x{HEIGHT}')
	canvas = Canvas(root)
	canvas.pack()
	#сделаем так, чтобы нажатие левой кнопки на поле выводило координаты точки, в которую мы нажали
	canvas.bind('<Button-1>', click_handler)
	balls = [Ball() for i in range(1)]
	# делаем шаг перемещения и отрисовки шаров. поскольку mainloop циклит наше приложение, это будет происходить, пока мы не закроем окно
	tick()
	root.mainloop()

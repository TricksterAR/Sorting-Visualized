import pygame as pg
import random


WINDOW_SIZE = 720       # (720x720)
elements = 60          # must be a factor of WINDOW_SIZE

# initialising window
win = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pg.display.set_caption("Bubble Sort Visual")

stroke = WINDOW_SIZE//elements
sort = False

# Numbers from 1 to no. of elements
arr = [i*stroke for i in range(1, elements+1)]
random.shuffle(arr)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    for i in range(elements):
        pg.draw.line(win, (173, 239, 209), (stroke*i, WINDOW_SIZE), (stroke*i, arr[i]), stroke)

    pg.display.update()
    win.fill((0, 32, 63))

    def bubblesort(arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-1-i):
                if arr[j]<arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

                # exit condition
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        exit()

                # drawing the elements
                for k in range(elements):
                    pg.draw.line(win, (173, 239, 209), (stroke * k, WINDOW_SIZE), (stroke * k, arr[k]), stroke)
                pg.draw.line(win, (173, 0, 0), (stroke * j, WINDOW_SIZE), (stroke * j, arr[j]), stroke)
                pg.draw.line(win, (173, 0, 0), (stroke * (j+1), WINDOW_SIZE), (stroke * (j+1), arr[j+1]), stroke)
                pg.display.update()
                win.fill((0, 32, 63))
        return arr

    if not sort:
        arr = bubblesort(arr)
        sort = True 

pg.quit()

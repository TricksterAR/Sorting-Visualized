import pygame as pg
import random

height = width = 800		# dimensions of the window
elements = 400			# must be factor of width
counter = 0
arr = []
run = True
var = var2 = True
stroke = width//elements

# Numbers from 1 to no. of elements
for i in range(1, elements+1):
    arr.append(i*stroke)

# initialising the game window
pg.init()
win = pg.display.set_mode((width, height))
pg.display.set_caption("Quick Sort Visual")

# main loop
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
	
    # shuffling for the first time
    if var:
        random.shuffle(arr)
        var = False

    for i in range(elements):
        pg.draw.line(win, (255, 140, 0), (stroke*i, height), (stroke*i, arr[i]), stroke)

    pg.display.update()
    win.fill((0, 0, 0))
    pg.time.delay(1000)

    def quicksort(arr, low, high):
        if low < high:
            k = low - 1
            piv = arr[high]

            for i in range(low, high):
                if piv < arr[i]:
                    k += 1
                    arr[i], arr[k] = arr[k], arr[i]
                    # drawing the elements
                    for x in range(elements):
                        pg.draw.line(win, (255, 140, 0), (stroke * x, height), (stroke * x, arr[x]), stroke)
                    pg.draw.line(win, (0, 0, 255), (high * stroke, height), (high * stroke, piv), stroke+1)
                    pg.draw.line(win, (0, 255, 0), (i * stroke, height), (i * stroke, arr[i]), stroke + 1)
                    pg.draw.line(win, (0, 255, 0), (k * stroke, height), (k * stroke, arr[k]), stroke + 1)
                    pg.display.update()
                    win.fill((0, 0, 0))
                    pg.time.delay(5)
            k += 1
            arr[k], arr[high] = arr[high], arr[k]
            quicksort(arr, low, k - 1)
            quicksort(arr, k + 1, high)

    if var2:
        quicksort(arr, 0, elements-1)
        var2 = False

pg.quit()

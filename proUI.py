from pygame import *

init()
Window_size = 1000, 800
window = display.set_mode(Window_size)
clock = time.Clock()

rect = Rect(0, 0, 100, 100)

while True:
    for e in event.get():
        if e.type ==QUIT:
            quit()
    draw.rect(window, (255, 0, 0), rect)

    display.update()
    clock.tick(60)
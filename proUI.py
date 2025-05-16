from pygame import *

init()
Window_size = 1000, 800
window = display.set_mode(Window_size)
clock = time.Clock()

while True:
    for e in event.get():
        if e.type ==QUIT:
            quit()

    display.update()
    clock.tick(60)

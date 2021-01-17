import pyautogui as pt

while True:
    posXY = pt.position()
    print(posXY, pt.pixel(posXY[0], posXY[1]))
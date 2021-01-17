import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(5)


def copy_message_routine():
    global x, y

    get_position('wpp_project\img\smile_paperclip.png')
    pt.moveTo(x, y, duration=.05)
    pt.moveTo(x + 40, y - 40, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()


def paste_message_routine(message):
    global x, y

    pt.moveTo(x + 30, y + 20, duration=.5)
    pt.click()

    pt.typewrite(message)


def get_position(path):
    global x, y

    position1 = pt.locateOnScreen(path, confidence=.6)

    if position1:
        x = position1[0]
        y = position1[1]

        return True

    else:
        return False


def get_message():
    global x, y

    get_position('wpp_project\img\smile_paperclip.png')

    copy_message_routine()

    wpp_message = pyperclip.paste()
    pt.click()
    print('message received: ' + wpp_message)

    return wpp_message


def post_response(message):
    global x, y

    get_position('wpp_project\img\\text_box.png')

    paste_message_routine(message)


while True:
    if get_position('wpp_project\img\smile_paperclip.png'):
        post_response(get_message())
        sleep(3)

    else:
        print('no coords')
        sleep(5)
        continue

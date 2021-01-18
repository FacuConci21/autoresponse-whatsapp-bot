import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(5)


def copy_message_routine():
    global x, y

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

    pt.typewrite('\n')


def open_chat_routine():
    global x, y

    pt.moveTo(x, y)
    pt.moveRel(-100, 0)
    pt.click()


def press_send_button_routine():
    global x, y

    get_position('wpp_project\img\send_button.png')

    pt.moveTo(x + 20, y + 20, duration=.5)

    pt.click()


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


def process_response(message):

    if '?' in str(message).lower():
        return 'beep! boop! soy un bot y vengo a responderte'

    else:
        return 'beep! boop! soy un bot y segun mis calculos hay un 99.9999% de probabilidades de que esta noche te rompan el ojt porque sos un tolazo SAPEEEEE'


def message_checker():
    global x, y

    while True:
        if get_position('wpp_project\img\green_point1.png'):

            open_chat_routine()

            processed_message = process_response(get_message())
            post_response(processed_message)

        print('Sleepen for 5 seconds')
        sleep(5)


x = 0
y = 0
message_checker()
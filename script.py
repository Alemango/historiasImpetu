import webbrowser
import keyboard
import time
import mouse
import datetime

while True:
    hora = str(datetime.datetime.now().time())[:5]
    print(hora)
    time.sleep(10)

    if hora == '06:29':
        webbrowser.open('https://www.instagram.com/')
        time.sleep(15)
        keyboard.press_and_release('f12')
        time.sleep(10)
        keyboard.press_and_release('f5')
        time.sleep(10)
        mouse.move(639, 203,absolute=True)
        mouse.click()
        time.sleep(5)
        mouse.move(645, 259,absolute=True)
        mouse.click()
        time.sleep(5)
        keyboard.write('dia-14.png', delay=0.1)
        keyboard.press_and_release('enter')
        time.sleep(10)
        mouse.move(473, 660, absolute=True)
        mouse.click()
    
        break
    
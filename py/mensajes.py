import pyautogui as pg
import time


mensajes= int(input('cuantos: '))
mensaje=input('mensaje: ')
time.sleep(3)


for i in range(mensajes):
    pg.write(f' {mensaje}')
    pg.press('enter')



import pyautogui
import time

time.sleep(5)

pyautogui.typewrite("c!roubarbanco")
pyautogui.press("enter")

time.sleep(0.4)

for i in range(28):
    pyautogui.typewrite("coletar")
    pyautogui.press("enter")
    time.sleep(0.7)
for i in range(4):
    pyautogui.typewrite("fugir")
    pyautogui.press("enter")

"""
c!loja
c!sacar 5000
c!depositar td
c!blackjack 2000c!roubarbanco
c!crime
c!semanal
c!c
c!cavalo
c!trabalhar
"""
import pyautogui
import time

# 1 - Tamanho da Tela
print(pyautogui.size())

# 2 - Pegar a Posição Atual do Cursos
print(pyautogui.position())
time.sleep(1.5)

# 3 - App para ver a posição do mouse em tempo real
# python
# from pyautogui import mouseInfo
# mouseInfo()

# 4 - Mover o cursor do Mouse
# pyautogui.moveTo(2443, 18, 1)
# time.sleep(1.5)
# pyautogui.click()

# 5 - Realizando o Scroll
time.sleep(1)
pyautogui.moveTo(2443, 18, 0.5)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(2050, 514, 0.5)
pyautogui.scroll(-900)
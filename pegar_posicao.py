import pyautogui
import time

# Funções de pegar posição do mouse e da tela:
time.sleep(5)
print(pyautogui.position()) # Position of my mouse
# pyautogui.scroll(-1000)
# print(pyautogui.KEYBOARD_KEYS) # Esse comando me mostra o nome de todas as teclas 
#do meu teclado para eu usar no comando pyautogui.press() ou pyautogui.hotkey();
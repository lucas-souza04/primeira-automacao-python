import pyautogui
import time

# RPA, o pyaotogui é uma ferramenta de RPA (Robot Process Automation);

pyautogui.POUSE = 0.3

# FUNÇÕES DE PEGAR POSIÇÃO DO MOUSE E DA TELA:
print(pyautogui.position()) # Pega a posição do meu mouse
print(pyautogui.size()) # Me mostra o tamanho/resolução da minha tela

# As automações feitas pelo pyautogui servem para qualquer tipo de computador/tela, desde que,
#as restições de tamanho e posição sejam seguidas;

# FUNÇÕES DE MOUSE:
time.sleep(5)
# pyautogui.click(x=3850, y=1320) # A função click tem algumas personalizações, como:
# pyautogui.click(x=3850, y=1320, button="right/middle")
# pyautogui.click(x=3850, y=1320, clicks=2)
# pyautogui.moveTo(x=3218, y=149, duration=1) # O duration, é uma especificação, se não tiver
#ele no código, meu mouse se move automaticamente;
# pyautogui.click(x=3294, y=275)
# pyautogui.scroll(-1000) # Número negatico = scroll para baixo
# Número positivo = scroll para cima;

# FUNÇÕES DE TECLADO:
pyautogui.write("Quero trabalhar home office") # Esse comando escreve uma frase na tela, mas antes,
#eu tenho que garantir a posição do meu mouse, aonde eu quero que essa frase seja escrita;
# pyautogui.hotkey("ctrl", "c") # Aperta várias teclas de uma vez;
pyautogui.press("win") # Aperta uma tecla do meu teclado;








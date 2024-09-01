# Essa automação só ira funcionar em sua máquina se você alterar as restições de tamanho e posição de tela

import pyautogui
import time

pyautogui.POUSE = 0.3

# Apertando a tecla "win" e abrindo o navegador:
pyautogui.press("win")
pyautogui.moveTo(x=713, y=162, duration=1)
pyautogui.click(x=713, y=162)
pyautogui.write("Navegador Opera GX")
pyautogui.press("enter")

# Escrevendo na URL o site que eu quero abrir:
time.sleep(3)
pyautogui.click(x=433, y=70)
pyautogui.write("https://www.hashtagtreinamentos.com")
pyautogui.press("enter")

# Fechando uma propaganda automatica:
time.sleep(11)
pyautogui.moveTo(x=1318, y=282, duration=1)
pyautogui.click(x=1318, y=282)

# Abrindo a aba "Curso de Python":
time.sleep(1)
pyautogui.moveTo(x=1115, y=131, duration=0.5)
pyautogui.click(x=1115, y=131)
# Ou
# posicao_curso_python = pyautogui.locateCenterOnScreen("curso_pyhon")
# pyautogui.click(posicao_curso_python)

# Preenchendo os dados do formulário:
# Primeiro nome
time.sleep(1)
pyautogui.moveTo(x=452, y=760, duration=0.5)
pyautogui.click(x=452, y=760)
pyautogui.write("Lucas")

# Email
time.sleep(1)
pyautogui.moveTo(x=425, y=837, duration=0.5)
pyautogui.click(x=425, y=837)
pyautogui.write("santos.lucasbw@gmail.com")

# WhatsApp com DDD
time.sleep(1)
pyautogui.moveTo(x=321, y=914, duration=0.5)
pyautogui.click(x=321, y=914)
pyautogui.write("11972618032")

# Enviando os dados do formulário
time.sleep(1)
pyautogui.moveTo(x=551, y=986, duration=0.5)
# pyautogui.click(x=551, y=986) está comentado para que eu possa testar várias vezes

# Para passar de campo no formulário, eu também poderia utilizar o comando: pyautogui.press("tab")

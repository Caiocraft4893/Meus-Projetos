import pyautogui
import time 

'''pyautogui.click(x=605, y=740)
pyautogui.PAUSE = 4
pyautogui.hotkey('ctrl', 't')''' # hotkey = atalho de teclado!! tipo CTRL + C - para copiar!


pyautogui.press('win')
pyautogui.write('google')  
pyautogui.PAUSE = 2                
pyautogui.press('enter')    
pyautogui.PAUSE = 1
pyautogui.write('vs code')
pyautogui.press('enter')      
pyautogui.PAUSE = 3
pyautogui.click(x=293, y=342)
pyautogui.PAUSE = 7
pyautogui.press('f12')
pyautogui.PAUSE = 4
pyautogui.hotkey('ctrl', 'shift', 'c') # Clica no botão de "inspecinar objeto"
pyautogui.PAUSE = 6
pyautogui.click(x=1070, y=265) # Clica no texto "The open source...."
pyautogui.PAUSE = 5
pyautogui.doubleClick(x=928, y=312) # Clica no "The open source...", em "elements", para mudá-lo.
pyautogui.PAUSE = 1
pyautogui.press('backspace')
pyautogui.PAUSE = 1
pyautogui.write('Me contrata, Luis Totoso 😘')
pyautogui.PAUSE = 2
pyautogui.press('enter')
pyautogui.PAUSE = 2
pyautogui.click(x=1347, y=196)

# pyautogui.PAUSE = 2
print(pyautogui.position())


# Obs: para pausar a automação, posicione o mouse no canto superior esquerdo da tela!!
# Obs2: essas posições variam muito!!!

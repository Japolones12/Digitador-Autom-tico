import pyautogui

# Define a posição da área onde o texto será copiado
x, y = 100, 200
width, height = 200, 50

# Copia o texto da área especificada
pyautogui.moveTo(x, y)
pyautogui.dragTo(x + width, y + height, duration=0.5, button='left')
pyautogui.hotkey('ctrl', 'c')

# Cola o texto em outra área
pyautogui.moveTo(300, 300)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')

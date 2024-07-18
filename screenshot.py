import pyautogui

try:
    # Capturar uma screenshot da tela inteira
    screenshot = pyautogui.screenshot()

    # Salvar a screenshot em um arquivo para verificar
    screenshot.save("screenshot.png")
    print("Screenshot salva com sucesso.")
except pyautogui.PyAutoGUIException as e:
    print(f"Ocorreu um erro: {e}")
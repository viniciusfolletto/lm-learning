import pygetwindow as gw
import pyautogui
from PIL import Image

def screenshot_window(window_title):
    # Encontra a janela pelo título
    window = gw.getWindowsWithTitle(window_title)
    if not window:
        raise Exception(f"No window found with title '{window_title}'")
    
    window = window[0]
    
    # Obtém as coordenadas da janela
    x, y, width, height = window.left, window.top, window.width, window.height

    # Captura a screenshot da área da janela
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    
    # Salva a imagem
    screenshot.save(f"screenshots/{window_title}_screenshot.png")

# Exemplo de uso
window_title = "Learning World"
screenshot_window(window_title)

from pywinauto import Desktop
from PIL import Image
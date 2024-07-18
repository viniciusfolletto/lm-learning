import random
import time
import pyautogui
import cv2
import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define o tempo de processamento do movimento do mouse
pyautogui.PAUSE = 0.0001

# Defina as coordenadas e tamanho da janela do BlueStacks (ajuste conforme necessário)
bluestacks_region = (0, 0, 1920, 1080)  # Exemplo: captura a janela completa do BlueStacks

# Função para capturar a tela do BlueStacks
def capture_bluestacks(region):
    tempo = time.perf_counter()
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(f"screenshots/screenshot_{tempo}.png")
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screenshot

# Função para encontrar um elemento na tela do BlueStacks
def find_element(template_path, region):
    screenshot = capture_bluestacks(region)
    
    template = cv2.imread(template_path, 0)
    if template is None:
        print("Erro ao carregar a imagem do template. Verifique o caminho da imagem.")
        return None
    
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    
    # Defina um limiar para considerar uma correspondência válida
    threshold = 0.8
    if max_val >= threshold:
        return max_loc
    return None

def click_inventory_icon():
    template_path = "images/inventory.png"
    position = find_element(template_path, bluestacks_region)
    
    if position and position != (0, 0):
        print(f"Ícone do inventário encontrado na posição: {position}")
        # Ajuste a posição para clicar corretamente
        adjusted_position = (position[0] + bluestacks_region[0], position[1] + bluestacks_region[1])
        print(f"Posição ajustada para clique: {adjusted_position}")
        # Clicar na posição do elemento encontrado
        move_mouse_relative_humanized(adjusted_position)
        #pyautogui.click(adjusted_position)
    else:
        print("Ícone do inventário não encontrado ou posição inválida.")
        
def click_combat_icon():
    template_path = "images/combat.png"
    position = find_element(template_path, bluestacks_region)
    
    if position and position != (0, 0):
        print(f"Ícone de Combate encontrado na posição: {position}")
        # Ajuste a posição para clicar corretamente
        adjusted_position = (position[0] + bluestacks_region[0], position[1] + bluestacks_region[1])
        print(f"Posição ajustada para clique: {adjusted_position}")
        # Clicar na posição do elemento encontrado
        move_mouse_relative_humanized(adjusted_position)
        #pyautogui.click(adjusted_position)
    else:
        print("Ícone de Combate não encontrado ou posição inválida.")

#---------------------------------------------------------------------------------

def getRoute(x1, y1, x2, y2, n):
    """
    Returns an (x, y) tuple of the point that has progressed a proportion ``n`` along the line defined by the two
    ``x1``, ``y1`` and ``x2``, ``y2`` coordinates.

    This function was copied from pytweening module, so that it can be called even if PyTweening is not installed.
    """
    x = ((x2 - x1) * n) + x1
    y = ((y2 - y1) * n) + y1
    return (x, y)
    
#---------------------------------------------
    
def easeOutQuad(n):  # type: (Union[int, float]) -> Union[int, float]
    """Starts fast and decelerates to stop. (Quadratic function.)

    Args:
      n (int, float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    return -n * (n - 2)
    
#---------------------------------------------

def move_mouse_relative_humanized(pos_final):
    
    dx, dy = pos_final
    
    # Obter a posição atual do cursor
    startx, starty = pyautogui.position()
    current_x, current_y = pyautogui.position()
    
    FAILSAFE_POINTS = [(0, 0)]
    
    graph_t = []
    
    t_inicial = time.perf_counter()
    new_x = dx - current_x
    new_y = dy - current_y
    
    duration = random.uniform(0.15, 0.25)*(abs(new_x)+abs(new_y))+0.000001
    
    #if duration > 0.1:
        # Non-instant moving/dragging involves tweening:
    num_steps = max(bluestacks_region[2], bluestacks_region[3])
    sleep_amount = duration / num_steps
    if sleep_amount < 0.05:
        num_steps = int(duration / 0.05)
        sleep_amount = duration / num_steps

    steps = [getRoute(startx, starty, dx, dy, easeOutQuad(n / num_steps)) for n in range(num_steps)]
    # Making sure the last position is the actual destination.
    steps.append((dx, dy))
    
    '''# Calcular a velocidade
    velocidades = []
    tempos = []
    for i in range(0, len(steps)):
        dx, dy = steps[i]
        velocidade = np.sqrt(dx**2 + dy**2)
        velocidades.append(velocidade)
        tempos.append(i)
    
    # Criar o gráfico
    plt.plot(tempos, velocidades, marker='o')
    plt.title('Movimento do Mouse')
    plt.xlabel('Tick')
    plt.ylabel('Velocidade')
    plt.grid(True)
    plt.show()'''
    
    for tweenX, tweenY in steps:
        #if len(steps) > 1:
            # A single step does not require tweening.
            #time.sleep(0.000001)

        tweenX = int(round(tweenX))
        tweenY = int(round(tweenY))
        
        #print(tweenX, tweenY)

        # Do a fail-safe check to see if the user moved the mouse to a fail-safe position, but not if the mouse cursor
        # moved there as a result of this function. (Just because tweenX and tweenY aren't in a fail-safe position
        # doesn't mean the user couldn't have moved the mouse cursor to a fail-safe position.)
        if (tweenX, tweenY) not in FAILSAFE_POINTS:
            pyautogui.failSafeCheck()

        #pyautogui.moveTo(tweenX, tweenY)
        
        platform_module = pyautogui.platformModule
        platform_module._moveTo(tweenX, tweenY)
        
        time.sleep(0.0001)
    
    pyautogui.click(pos_final)
    
    time.sleep(0.240)
    
    click_combat_icon()
      
#---------------------------------------------------------------------------------

click_inventory_icon()
import pyautogui
import cv2
import numpy as np
import time
import keyboard  # Instale o pacote keyboard usando pip se ainda não tiver: pip install keyboard

# Defina as coordenadas e tamanho da janela do BlueStacks (ajuste conforme necessário)
bluestacks_region = (0, 0, 1920, 1080)  # Exemplo: captura a janela completa do BlueStacks

# Função para capturar a tela do BlueStacks
def capture_bluestacks(region):
    screenshot = pyautogui.screenshot(region=region)
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

# Função para clicar no ícone do escudo
def click_shield_icon():
    template_path = "images/template.png"
    position = find_element(template_path, bluestacks_region)
    
    if position and position != (0, 0):
        print(f"Ícone do escudo encontrado na posição: {position}")
        # Ajuste a posição para clicar corretamente
        adjusted_position = (position[0] + bluestacks_region[0], position[1] + bluestacks_region[1])
        print(f"Posição ajustada para clique: {adjusted_position}")
        # Clicar na posição do elemento encontrado
        pyautogui.click(adjusted_position)
    else:
        print("Ícone do escudo não encontrado ou posição inválida.")

print("Pressione 'Q' para encerrar.")

# Loop principal para automação contínua
running = True
while running:
    # Verificar se a tecla 'q' foi pressionada para encerrar o programa
    if keyboard.is_pressed('q'):
        print("Encerrado")
        running = False
    else:
        # Verificar o estado atual do escudo e renová-lo se necessário
        # Implemente sua lógica aqui para verificar o estado do escudo
        
        # Exemplo simplificado: clicar no ícone do escudo a cada 5 minutos
        click_shield_icon()
        
        # Aguardar 5 minutos antes de verificar novamente (ajuste conforme necessário)
        time.sleep(300)  # 300 segundos = 5 minutos
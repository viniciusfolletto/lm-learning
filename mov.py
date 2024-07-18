import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import pyautogui
import time

print("Programa iniciado!")

# Listas para armazenar as coordenadas do mouse
x_coords = []
y_coords = []
t_coords = []

# Inicia as variáveis
sleep_time = 0.0001
n = 0

pyautogui.PAUSE = sleep_time

last_x, last_y = pyautogui.position()
t_inicial = time.perf_counter()
last_t = t_inicial

# Tempo em segundos para rastrear o mouse
duration = 2
end_time = t_inicial + duration

while time.perf_counter() < end_time:
    x, y = pyautogui.position()
    y = 1080-y
    t = time.perf_counter()-t_inicial
  
    x_coords.append(x)
    y_coords.append(y)
    t_coords.append(t)
    
    #print(v)
    
    n = n+1
    last_t = t
    last_x, last_y = (x, y)
    
    time.sleep(sleep_time)  # Atraso para evitar muita amostragem

print("Dados coletados")
print(f"Ponto incial: {x_coords[0]}, {y_coords[0]}")
print(f"Ponto final: {x_coords[n-1]}, {y_coords[n-1]}")

# Calcular a velocidade
velocidades = []
tempos = []
dt=0
for i in range(1, len(x_coords)):
    tx = x_coords[i]
    ty = y_coords[i]
    dt = t_coords[i] - t_coords[i-1]
    vx = tx/dt
    vy = ty/dt
    
    velocidade = np.sqrt(tx**2 + ty**2)
    velocidades.append(velocidade)
    print(velocidade)
    
    tempos.append(t_coords[i])
        
# Criar o gráfico
plt.plot(tempos, velocidades, marker='o')
plt.title('Movimento do Mouse')
plt.xlabel('Tick')
plt.ylabel('Velocidade')
plt.grid(True)
plt.show()

print(x_coords[0], y_coords[0], tempos[0])

'''# Plotar dados de exemplo
plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='b')
plt.title('Movimento do Mouse')
plt.xlabel('Posição X')
plt.ylabel('Posição Y')
plt.grid(True)
plt.show()'''

# Análise de padrões (exemplo simples: interpolação linear)
interp_func_x = interp1d(t_coords, x_coords, kind='cubic', fill_value='extrapolate')
interp_func_y = interp1d(t_coords, y_coords, kind='cubic', fill_value='extrapolate')

# Gerar novo movimento do mouse entre dois pontos desejados (por exemplo, inicial e final)
new_time = np.linspace(min(t_coords), max(t_coords), len(t_coords))  # Novo tempo para interpolação

new_mouse_x = interp_func_x(new_time)
new_mouse_y = interp_func_y(new_time)

# Plotar novo movimento gerado
plt.figure(figsize=(8, 6))
plt.plot(new_mouse_x, new_mouse_y, marker='o', linestyle='-', color='r')
plt.title('Novo Movimento do Mouse Gerado')
plt.xlabel('Posição X')
plt.ylabel('Posição Y')
plt.grid(True)
plt.show()

'''print("Simulando")

# Simulação de movimento do mouse
for x, y in zip(x_coords, y_coords):
    pyautogui.moveTo(x, 1080-y)  # Ajuste para coordenadas da tela
    time.sleep(sleep_time)'''
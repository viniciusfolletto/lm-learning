import pyautogui
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import math
from scipy.interpolate import interp1d

print("Programa iniciado!")

# Listas para armazenar as coordenadas do mouse
x_coords = []
y_coords = []
t_coords = []
v_coords = []

# Inicia as variáveis
last_x, last_y = pyautogui.position()
last_t = time.time()
t_inicial = time.time()
n=0
sleep_time = 0.0001

# Tempo em segundos para rastrear o mouse
duration = 2
end_time = time.time() + duration

while time.time() < end_time:
    n = n+1
    x, y = pyautogui.position()
    y = 1080-y
    t = time.time()-t_inicial
    
    if last_x == x and last_y == y:
        last_t = t
        last_x, last_y = (x, y)
        #time.sleep(sleep_time)
        continue
    else:
        v = math.sqrt(abs(last_x-x)**2 + abs(last_y-y)**2)
  
    x_coords.append(x)
    y_coords.append(y)
    t_coords.append(t)
    v_coords.append(v)
    
    #print(v)
    
    last_t = t
    last_x, last_y = (x, y)
    
    time.sleep(sleep_time)  # Atraso para evitar muita amostragem

'''# Criar o gráfico
plt.plot(x_coords, y_coords, marker='o')
plt.title('Movimento do Mouse')
plt.xlabel('Posição X')
plt.ylabel('Posição Y')
plt.show()'''

print(f"Interações: {n}")
print(f"Média:{last_t/n}")

'''# Criar o gráfico de tempo
plt.plot(t_coords, v_coords, marker='o')
plt.title('Movimento do Mouse')
plt.xlabel('Posição X')
plt.ylabel('Posição Y')
plt.show()'''

# Criar o gáfico 3D

# Criar figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Criar gráfico de dispersão
ax.scatter(x_coords, y_coords, t_coords, c='r', marker='o')

ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo t')

plt.show()
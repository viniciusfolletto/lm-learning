import tkinter as tk
import pyautogui
import time

class MouseOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)  # Remove a barra de título e bordas
        self.root.attributes("-transparentcolor", "white")  # Define a cor transparente

        self.canvas = tk.Canvas(self.root, width=1920, height=1080, bg="white", highlightthickness=0)
        self.canvas.pack()
        
        # Desenha o retângulo vermelho
        self.rect = self.canvas.create_rectangle(0, 0, 20, 20, outline="red", width=2)
       
        self.update_position()

    def update_position(self):
        x, y = pyautogui.position()
        x1, y1 = x - 10, y - 10
        x2, y2 = x + 10, y + 10
        self.canvas.coords(self.rect, x1, y1, x2, y2)
        print(time.perf_counter())
        self.root.after(1, self.update_position)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    overlay = MouseOverlay()
    overlay.run()
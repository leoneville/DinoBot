from PIL import ImageGrab
import pyautogui
import time
import os

class Dino_Bot:
    def __init__(self):
        #Pixels de detecção da tela baseada em uma resolução de 1366 x 768
        self.value_x = 365.0 # pixels de detecção da tela (x2 = x + 21)
        self.value_y = 385 # pixels de detecção da tela (y2 = y + 70)
        self.screen = ImageGrab.grab()

    
    def Start(self):
        self.Print_Screen()
        self.Detect_Obstacles(self.screen)
        self.Dino_Jump()
        self.Message_Starting()
        while True:
            self.screen = self.Print_Screen()
            if self.Detect_Obstacles(self.screen):
                self.Dino_Jump()

    
    def Print_Screen(self): # Função que tira screenshots da tela usando o PIL lib
        self.screen = ImageGrab.grab()
        return self.screen

    
    def Detect_Obstacles(self, screen): # Função para detectar os obstáculos através dos pixels
        aux_color = screen.getpixel((int(self.value_x), self.value_y))
        for i in range(int(self.value_x), int(self.value_x + 21)):
            for j in range(self.value_y, self.value_y + 70):
                color = screen.getpixel((i,j))
                if color != aux_color:
                    return True # retorna verdadeiro para detectar os obstáculos
                else:
                    aux_color = color

    
    def Dino_Jump(self): # Função para o Dino pular
        pyautogui.press('up')
        self.value_x += 0.6 # aumenta a distancia de detecção de pixels para tentar adaptar ao aumento de velocidade do jogo

    
    def Message_Starting(self):
        print('  ____            _   _    U  ___ u       ____    U  ___ u_____   ')
        print(' |  _"\   ___    | \ |"|    \/"_ \/    U | __")u   \/"_ \|_ " _|  ')
        print('/| | | | |_"_|  <|  \| |>   | | | |     \|  _ \/   | | | | | |    ')
        print('U| |_| |\ | |   U| |\  |.-,_| |_| |      | |_) .-,_| |_| |/| |\   ')
        print(' |____/ U/| |\\u  |_| \_| \_)-\___/       |____/ \_)-\___/u |_|U   ')
        print('  |||.-,_|___|_,-||   \\\,-.   \\\        _|| \\\_      \\\  _// \\\_  ')
        print(' (__)_\_)-\' \'-(_/(_")  (_/   (__)      (__) (__)    (__)(__) (__) \n\n\n')
        print('#############################')
        print('Created By: Neville Guimarães')
        print('#############################\n\n')
        time.sleep(3)
        os.system('cls')
        print("O bot inicia em 3 segundos...")
        time.sleep(1)
        os.system('cls')
        print("O bot inicia em 2 segundos...")
        time.sleep(1)
        os.system('cls')
        print("O bot inicia em 1 segundos...")
        time.sleep(1)
        os.system('cls')
        print("**********Iniciando**********")


DinoBot = Dino_Bot()
DinoBot.Start()
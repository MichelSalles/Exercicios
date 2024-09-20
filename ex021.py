import pygame
import time

# Inicializa o módulo de mixer do pygame
pygame.mixer.init()

# Carrega o arquivo de áudio
pygame.mixer.music.load('ex021.mp3')

# Reproduz o áudio
pygame.mixer.music.play()

# Mantém o programa em execução até que o áudio termine
while pygame.mixer.music.get_busy():
    # Espera um pouco antes de verificar novamente
    time.sleep(1)

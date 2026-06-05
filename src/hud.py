# src/hud.py
import pygame
from setting import TEXTO_PRINCIPAL

class HUD:
    def __init__(self):
        pygame.font.init()
        self.fuente = pygame.font.SysFont("Arial", 28, bold=True)

    def dibujar(self, ventana, puntaje, vidas):

        texto_puntos = self.fuente.render(f"Bananas: {puntaje}", True, TEXTO_PRINCIPAL)
        texto_vidas = self.fuente.render(f"Vidas: {vidas}", True, TEXTO_PRINCIPAL)
        
        ventana.blit(texto_puntos, (20, 20)) 
        ventana.blit(texto_vidas, (ventana.get_width() - texto_vidas.get_width() - 20, 20))

    def dibujar_game_over(self, ventana):
        fuente_go = pygame.mixer.init()
        fuente_grande = pygame.font.SysFont("Arial", 50, bold=True)
        texto_go = fuente_grande.render("GAME OVER", True, (255, 0, 0)) 
        
        # Centrar en pantalla
        x = (ventana.get_width() // 2) - (texto_go.get_width() // 2)
        y = (ventana.get_height() // 2) - (texto_go.get_height() // 2)
        ventana.blit(texto_go, (x, y))
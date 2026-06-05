# src/banana.py
import pygame
import random
from setting import ANCHO, ALTO

class Banana:
    def __init__(self):
        self.imagen = pygame.image.load("assets/images/banana.png")
        self.imagen = pygame.transform.scale(self.imagen, (40, 40))
        self.rect = self.imagen.get_rect()
        self.respawn()
        self.velocidad = 6

    def respawn(self):
        self.rect.x = random.randint(0, ANCHO - self.rect.width)
        self.rect.y = -50

    def caer(self):
        self.rect.y += self.velocidad
        if self.rect.y > ALTO:
            self.respawn()
            return True 
        return False 


    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.rect)
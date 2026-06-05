# src/mono.py
import pygame
from setting import ANCHO, ALTO

class Mono(pygame.sprite.Sprite):
    """Clase encargada de gestionar el comportamiento y renderizado del personaje principal."""
    
    def __init__(self):
        super().__init__()
        
        # Gestión y carga del recurso gráfico (Textura)
        self.superficie_grafica = pygame.image.load("assets/images/mono.png").convert_alpha()
        # Puedes ajustar el tamaño si es necesario con transform
        self.image = pygame.transform.scale(self.superficie_grafica, (64, 64))
        
        # Configuración del contenedor de posición física (Hitbox)
        self.rect = self.image.get_rect()
        
        # Posicionamiento inicial en el eje horizontal y vertical (Abajo al centro)
        self.rect.centerx = ANCHO // 2
        self.rect.bottom = ALTO - 20
        
        # Parámetros dinámicos de desplazamiento
        self.ritmo_marcha = 8

    def controlar(self):
        """Detecta las pulsaciones del teclado y altera la posición horizontal dentro de los límites."""
        teclas_pulsadas = pygame.key.get_pressed()
        
        # Movimiento hacia el flanco izquierdo
        if teclas_pulsadas[pygame.K_LEFT] or teclas_pulsadas[pygame.K_a]:
            self.rect.x -= self.ritmo_marcha
            # Restricción para no salir por el borde izquierdo
            if self.rect.left < 0:
                self.rect.left = 0
                
        # Movimiento hacia el flanco derecho
        if teclas_pulsadas[pygame.K_RIGHT] or teclas_pulsadas[pygame.K_d]:
            self.rect.x += self.ritmo_marcha
            # Restricción para no salir por el borde derecho
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO

    def dibujar(self, superficie_destino):
        """Proyecta el gráfico actual del personaje sobre la pantalla activa."""
        superficie_destino.blit(self.image, self.rect)
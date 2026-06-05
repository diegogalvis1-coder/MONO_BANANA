# main.py
import sys
import pygame

# Importaciones directas de los módulos del juego
from src.mono import Mono
from src.banana import Banana
from src.hud import HUD 
from setting import ANCHO, ALTO, FPS, COLOR_FONDO

def iniciar_partida():
    """Inicializa los módulos de Pygame y los componentes principales del juego."""
    pygame.init()
    pygame.mixer.init()
    
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Atrapa la Banana")
    
    return pantalla

# Ejecución de la configuración inicial
display_juego = iniciar_partida()
cronometro = pygame.time.Clock()

# Instanciación de objetos de la escena
avatar = Mono()
fruta = Banana()
marcador = HUD()

# Variables de control de estado (Nombres cambiados)
score = 0
salud_restante = 3
partida_activa = True

# Gestión de recursos de audio
audio_click = pygame.mixer.Sound("assets/sounds/recoger.mp3")
audio_fallo = pygame.mixer.Sound("assets/sounds/perder.mp3")
audio_click.set_volume(0.4)
audio_fallo.set_volume(0.55)

# Bucle Principal de Ejecución (Game Loop)
while True:
    
    # 1. Registro y lectura de entradas/eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Control de reinicio cuando el juego termina
        if not partida_activa and evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                score = 0
                salud_restante = 3
                fruta.respawn()
                partida_activa = True

    # 2. Actualización de físicas y mecánicas
    if partida_activa:
        avatar.controlar()
        
        # Validación si el objeto llega al límite inferior
        limite_alcanzado = fruta.caer()
        if limite_alcanzado:
            salud_restante -= 1
            audio_fallo.play()
            
            if salud_restante <= 0:
                partida_activa = False

        # Comprobación de intersección de cajas de colisión (Hitboxes)
        if avatar.rect.colliderect(fruta.rect):
            score += 1
            audio_click.play()
            fruta.respawn()

    # 3. Dibujado y renderizado de elementos en pantalla
    display_juego.fill(COLOR_FONDO)
    
    # Dibujar actores del juego
    avatar.dibujar(display_juego)
    fruta.dibujar(display_juego)
    marcador.dibujar(display_juego, score, salud_restante)
    
    # Interfaz superpuesta en caso de derrota
    if not partida_activa:
        marcador.dibujar_game_over(display_juego)

    # Actualización del búfer de pantalla y control de frames
    pygame.display.flip()
    cronometro.tick(FPS)
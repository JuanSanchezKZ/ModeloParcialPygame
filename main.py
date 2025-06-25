import pygame
import random

# Inicializar Pygame

pygame.init()
pygame.mixer.init()

## ANCHO Y ALTO

ancho_y_alto = (800, 600)

## CONFIGURACION DE VENTANA Y SETEO DE TEXTO DESCRIPTIVO

pantalla = pygame.display.set_mode(ancho_y_alto)

pygame.display.set_caption("Adivina el Número")

## Definición de colores

color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)
color_rojo = (255, 15, 0)

## Fuente general

pygame.font.init()

## Cargamos sonido

sonido_error = pygame.mixer.Sound("error.wav")


def mostrar_texto(texto, x, y):

    fuente = pygame.font.SysFont('freesansbold.ttf', 48)

    text = fuente.render(texto, False, color_rojo)

    textRect = text.get_rect()

    textRect.x = x
    textRect.y = y

    pantalla.blit(text, textRect)
    
def dibujar_cruces(pantalla, errores):
    for i in range(errores):
        x = 50 + i * 50
        pygame.draw.line(pantalla, color_rojo, (x, 50), (x + 20, 70), 4)
        pygame.draw.line(pantalla, color_rojo, (x + 20, 50), (x, 70), 4)


def nuevo_juego():
    numero_random = random.randint(1, 9)
    errores = 0
    intentos = []

    return {
        "numero_random": numero_random,
        "errores": errores,
        "intentos": intentos
    }


def inicializar_juego():

    while True:
        # Gestión de eventos (cerrar ventana etc.)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        mostrar_texto('hola mundo', 100, 100)
        dibujar_cruces(pantalla, 4)

        pygame.display.update()  

# Dibujar en la ventana
        pantalla.fill(color_blanco)

inicializar_juego()


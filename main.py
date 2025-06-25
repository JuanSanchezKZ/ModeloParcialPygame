import pygame
import random


# Inicializar Pygame

pygame.init()
pygame.mixer.init()

## ANCHO Y ALTO

ancho_y_alto = (800, 600)

## CONFIGURACION DE VENTANA Y SETEO DE TEXTO DESCRIPTIVO

pantalla = pantalla = pygame.display.set_mode(ancho_y_alto)

pygame.display.set_caption("Adivina el Número")

## Definición de colores

color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)
color_rojo = (255, 15, 0)

## Fuente general

pygame.font.init()


def mostrar_texto():
    
    fuente = pygame.font.SysFont('freesansbold.ttf', 48)

    text = fuente.render('Hola', False, color_rojo)

    textRect = text.get_rect()

    pantalla.blit(text, textRect)
    

## Cargamos sonido

sonido_error = pygame.mixer.Sound("error.wav")

def inicializar_juego():

    while True:
        # Gestión de eventos (cerrar ventana etc.)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        mostrar_texto()

        pygame.display.update()  

# Dibujar en la ventana
       # pantalla.fill(color_blanco)

inicializar_juego()


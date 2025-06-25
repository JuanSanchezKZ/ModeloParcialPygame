import pygame
import pygame.time
import random
from funciones import mostrar_texto, dibujar_cruces, nuevo_juego, procesar_tecla

# Inicializar Pygame

pygame.init()
pygame.mixer.init()

## ANCHO Y ALTO

ancho_y_alto = (800, 600)
pantalla = pygame.display.set_mode(ancho_y_alto)

## CONFIGURACION DE VENTANA Y SETEO DE TEXTO DESCRIPTIVO


pygame.display.set_caption("Adivina el Número")

## Definición de colores

color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)
color_rojo = (255, 15, 0)

## Fuente general

pygame.font.init()

clock = pygame.time.Clock()

## Cargamos sonido

sonido_error = pygame.mixer.Sound("error.wav")

## Cargar nuevo juego

datos_juego = nuevo_juego()

def jugar():

    while True:
        # Gestión de eventos (cerrar ventana etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    procesar_tecla(1, datos_juego['numero_random'])
                elif event.key == pygame.K_2:
                    procesar_tecla(2, datos_juego['numero_random'])
                elif event.key == pygame.K_3:
                    procesar_tecla(3, datos_juego['numero_random'])
                elif event.key == pygame.K_4:
                    procesar_tecla(4, datos_juego['numero_random'])
                elif event.key == pygame.K_5:
                    procesar_tecla(5, datos_juego['numero_random'])
                elif event.key == pygame.K_6:
                    procesar_tecla(6, datos_juego['numero_random'])
                elif event.key == pygame.K_7:
                    procesar_tecla(7, datos_juego['numero_random'])
                elif event.key == pygame.K_8:
                    procesar_tecla(8, datos_juego['numero_random'])
                elif event.key == pygame.K_9:
                    procesar_tecla(9, datos_juego['numero_random'])

        clock.tick(30)

        dibujar_cruces(pantalla, datos_juego['errores'])

        pygame.display.flip()  

# Dibujar en la ventana
        pantalla.fill(color_blanco)

jugar()


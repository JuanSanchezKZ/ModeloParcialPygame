import pygame
import pygame.time
import random
from funciones import mostrar_texto, dibujar_cruces, nuevo_juego, procesar_tecla
import sys, time

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

    ## Flag para definir si gano el juego    

    gano = False

    while True:
       
        ## Limitación 30 fotogramas por segundos

        clock.tick(30)

         # Gestión de eventos (cerrar ventana etc.)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                ## Verificamos teclas y llamamos a la funcion para procesarla
                if event.key == pygame.K_1:
                    gano = procesar_tecla(1, datos_juego)
                elif event.key == pygame.K_2:
                    gano = procesar_tecla(2, datos_juego)
                elif event.key == pygame.K_3:
                    gano = procesar_tecla(3, datos_juego)
                elif event.key == pygame.K_4:
                    gano = procesar_tecla(4, datos_juego)
                elif event.key == pygame.K_5:
                    gano = procesar_tecla(5, datos_juego)
                elif event.key == pygame.K_6:
                    gano = procesar_tecla(6, datos_juego)
                elif event.key == pygame.K_7:
                    gano = procesar_tecla(7, datos_juego)
                elif event.key == pygame.K_8:
                    gano = procesar_tecla(8, datos_juego)
                elif event.key == pygame.K_9:
                    gano = procesar_tecla(9, datos_juego)

        ## llamamos la función de dibujar cruces con la cantidad de errores
        dibujar_cruces(pantalla, datos_juego['errores'])

        ## Si llega a 4 errores mostramos texto de que perdio y cerramos el juego
        if datos_juego["errores"] >= 4:
            mostrar_texto(f"Perdiste. El número era {datos_juego['numero_random']}", 250, 300)
            pygame.display.flip()
            time.sleep(3)
            pygame.quit()
            sys.exit()

        ## Si gano mostramos texto de que gano y cerramos tambien
        if gano:
            mostrar_texto(f"¡Ganaste! El número era {datos_juego['numero_random']}", 250, 300)
            pygame.display.flip()
            time.sleep(3)
            pygame.quit()
            sys.exit()

        ## actualizamos la pantalla
        pygame.display.flip()  

        # Dibujar de blanco la pantalla
        pantalla.fill(color_blanco)

# llamamos la funcion principal
jugar()


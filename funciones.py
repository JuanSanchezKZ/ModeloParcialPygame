import pygame
import random

ancho_y_alto = (800, 600)
pantalla = pygame.display.set_mode(ancho_y_alto)
color_rojo = (255, 15, 0)
errores = 0

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
    
    intentos = []

    return {
        "numero_random": numero_random,
        "errores": errores,
        "intentos": intentos
    }

def procesar_tecla(tecla, numero_secreto):

    juego = nuevo_juego()

    if tecla == numero_secreto:
        mostrar_texto("GANASTE", 400, 300)
    elif tecla != numero_secreto:
        juego["errores"] += 1
        print(juego["errores"])

        

        


        
import pygame
import random
import pygame.mixer

ancho_y_alto = (800, 600)
pantalla = pygame.display.set_mode(ancho_y_alto)
color_rojo = (255, 15, 0)
pygame.mixer.init()
error = pygame.mixer.Sound("error.wav")
pygame.mixer.Sound.set_volume(error, 0.4)

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

def procesar_tecla(tecla, estado_juego):
    if tecla == estado_juego['numero_random']:
        return True
    elif tecla != estado_juego['numero_random']:
        estado_juego["errores"] += 1
        pygame.mixer.Sound.play(error)
        estado_juego["intentos"].append(tecla)
        return False

 

        

        


        
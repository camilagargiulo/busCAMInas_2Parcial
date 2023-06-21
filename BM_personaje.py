import pygame

def getSuperficies(path, filas, columnas):
    lista = []
    superficie_imagen = pygame.image.load(path)
    fotograma_ancho = int(superficie_imagen.get_width()/columnas)
    fotograma_alto = int(superficie_imagen.get_height()/filas)
    #debo tomar las imagenes como superficies para poder recorrerlas
    #a mano debo establecer lo limites de las imagenes del sprite y armar una lista
    #filas, columnas, imagenes
    for fila in range(filas):
        for columna in range(columnas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            #un pedacito de la imagen del sprite
            superficie_fotograma = superficie_imagen.subsurface(x,y, fotograma_ancho, fotograma_alto)
            lista.append(superficie_fotograma)
    return lista

#Creo la clase personaje para manejar la expresion del emoji a traves de un sprite
class Personaje:
    def __init__(self) -> None:
        self.caras = getSuperficies("/Users/camilagargiulomundo/iCloud Drive (archivo)/Documents/Facultad/UTN/Visual Studio Code/2do Parcial/Limpio/personaje.png", 1,5)
        self.animacion = self.caras #lista
        self.expresion = 0
        self.imagen = self.animacion[self.expresion]
        self.rect = self.imagen.get_rect()
        self.rect.centery = 90
        self.rect.centerx = 500

    def dibujar(self, pantalla):
        self.imagen = self.animacion[self.expresion]
        pantalla.blit(self.imagen, self.rect) 

#Emoji
emoji = Personaje()
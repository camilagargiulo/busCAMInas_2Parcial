import pygame
import colores
from BM_constantes import *



pygame.init()

imagen_bandera = pygame.image.load("/Users/camilagargiulomundo/iCloud Drive (archivo)/Documents/Facultad/UTN/Visual Studio Code/2do Parcial/Limpio/bandera.png")
imagen_bandera = pygame.transform.scale(imagen_bandera, (TAMAÑO_CELDA, TAMAÑO_CELDA))

imagen_bomba = pygame.image.load("/Users/camilagargiulomundo/iCloud Drive (archivo)/Documents/Facultad/UTN/Visual Studio Code/2do Parcial/Limpio/bombamala.png")
imagen_bomba = pygame.transform.scale(imagen_bomba, (TAMAÑO_CELDA, TAMAÑO_CELDA))


class Celda():
    def __init__(self, columna, fila) -> None:
        self.columna = columna
        self.fila = fila
        self.coord = (columna, fila)
        self.bomba = False
        self.visible = False
        self.bandera = False
        self.bombas_vecinas = 0
        self.lista_coord_vecinos = self.devolver_coord_vecinos()
        self.rect = pygame.Rect((POS_LEFT_TABLERO + self.columna * TAMAÑO_CELDA), (POS_TOP_TABLERO + self.fila * TAMAÑO_CELDA), TAMAÑO_CELDA, TAMAÑO_CELDA)

    def dibujar(self, pantalla):
        x = self.columna * TAMAÑO_CELDA + POS_LEFT_TABLERO
        y = self.fila * TAMAÑO_CELDA + POS_TOP_TABLERO

        
        pygame.draw.rect(pantalla, colores.GRAY, (x, y, TAMAÑO_CELDA - 1, TAMAÑO_CELDA -  1))

        if self.visible:
            if self.bomba:
                pygame.draw.rect(pantalla, colores.RED1, (x, y, TAMAÑO_CELDA, TAMAÑO_CELDA))
                #pygame.draw.circle(pantalla, colores.BLACK, (x + TAMAÑO_CELDA // 2, y + TAMAÑO_CELDA // 2), TAMAÑO_CELDA // 4)
                pantalla.blit(imagen_bomba, (x, y))

            else:
                pygame.draw.rect(pantalla, colores.ARENA, (x, y, TAMAÑO_CELDA, TAMAÑO_CELDA))
                if self.bombas_vecinas > 0:
                    fuente = pygame.font.SysFont(VERDANA, 20)
                    texto = fuente.render(str(self.bombas_vecinas), True, colores.BLUE)
                    pantalla.blit(texto, (self.rect[0]+ TAMAÑO_CELDA/3, self.rect[1] + 2))
                    self.bandera = False
        elif self.bandera:
                pantalla.blit(imagen_bandera, (x, y))

        pygame.draw.rect(pantalla, colores.GRAY18, (x, y, TAMAÑO_CELDA, TAMAÑO_CELDA), 2)
        
            
    def devolver_coord_vecinos(self):
        lista_coord_vecinos = []
        for i in [-1,0, 1]:
            for j in [-1,0,1]:
                coord_vecino = list(self.coord)
                coord_vecino[0] += i  #x
                coord_vecino[1] += j #y
                if coord_vecino[0] < CANTIDAD_X and coord_vecino[0] > -1 and coord_vecino[1] < CANTIDAD_Y and coord_vecino[1] > -1:
                    lista_coord_vecinos.append(coord_vecino)
        return lista_coord_vecinos #lista de listas
        
   
    
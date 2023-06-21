import pygame
import random
import colores
import BM_funciones
from BM_constantes import *
from BM_personaje import emoji
from BM_funciones import crear_lista_celdas

sonido_destapar = pygame.mixer.Sound("/Users/camilagargiulomundo/iCloud Drive (archivo)/Documents/Facultad/UTN/Visual Studio Code/2do Parcial/Limpio/destapar.mp3")
sonido_destapar.set_volume(1)

sonido_ganador = pygame.mixer.Sound("/Users/camilagargiulomundo/iCloud Drive (archivo)/Documents/Facultad/UTN/Visual Studio Code/2do Parcial/Limpio/ganador.mp3")
sonido_ganador.set_volume(0.5)

sonido_explosion = pygame.mixer.Sound("/Users/camilagargiulomundo/iCloud Drive (archivo)/Documents/Facultad/UTN/Visual Studio Code/2do Parcial/Limpio/explosion_recortada.wav")
sonido_explosion.set_volume(0.5)

sonido_explosion_final = pygame.mixer.Sound("/Users/camilagargiulomundo/iCloud Drive (archivo)/Documents/Facultad/UTN/Visual Studio Code/2do Parcial/Limpio/mi_explosion_03_hpx.wav")
sonido_explosion_final.set_volume(0.7)
        
class Tablero:
    def __init__(self) -> None:
        self.lista_celdas = crear_lista_celdas()
        self.bombas_restantes = CANTIDAD_BOMBAS 
        self.flag_play = False
        self.flag_ganador = False
        self.desbloqueado = True
        self.cantidad_visibles = 0
        self.flag_bandera = False
        self.flag_ditribucion = False
    
    def asignar_bombitas(self, cantidad_bombas, lista_posicion):
        posicion_inicial = 0
        for e_celda in self.lista_celdas:
            if e_celda.rect.collidepoint(lista_posicion):
                posicion_inicial = self.lista_celdas.index(e_celda)
        lista_posiciones_bombas = random.sample(range(len(self.lista_celdas)), cantidad_bombas)
        while posicion_inicial in lista_posiciones_bombas:
            lista_posiciones_bombas = random.sample(range(len(self.lista_celdas)), cantidad_bombas)
        for i in lista_posiciones_bombas:
            e_celda = self.lista_celdas[i]
            #print(e_celda)
            e_celda.bomba = True

            
    def definir_elementos_celdas(self, lista_posicion):
        self.asignar_bombitas(CANTIDAD_BOMBAS, lista_posicion)
        for e_celda in self.lista_celdas:
            lista_coord_vecinos = e_celda.lista_coord_vecinos
            for e_coord in lista_coord_vecinos:
                if self[(e_coord)].bomba == True: 
                    e_celda.bombas_vecinas += 1 

    
    def analizar_movimiento(self, lista_posicion):
        for e_celda in self.lista_celdas:
            if e_celda.rect.collidepoint(lista_posicion) and self.desbloqueado:
                if self.flag_bandera:
                    if self.bombas_restantes > 0 and e_celda.visible == False:
                        e_celda.bandera = BM_funciones.cambiar_flag(e_celda.bandera)
                elif e_celda.bomba == True:
                    self.explotar("play")
                    self.flag_play = False #Para parar el tiempo
                    self.flag_ganador = False
                    self.desbloqueado = False
                    self.mostrar_todas()

                elif e_celda.visible == False:
                    sonido_destapar.play()
                    self.destapar_celda(e_celda)
            
            if self.cantidad_visibles == (len(self.lista_celdas) - CANTIDAD_BOMBAS) and self.flag_play:
                sonido_ganador.play()
                self.flag_play = False
                self.flag_ganador = True
                self.desbloqueado = False


    def destapar_celda(self, e_celda):
        if e_celda.visible:
            return

        e_celda.visible = True
        self.cantidad_visibles += 1

        if e_celda.bombas_vecinas != 0:
            return

        # Destapar celdas adyacentes recursivamente
        for e_coord in e_celda.lista_coord_vecinos:
            if e_coord[0] > -1 and e_coord[0] < CANTIDAD_X and e_coord[1] > -1 and e_coord[1] < CANTIDAD_Y:
                    self.destapar_celda(self[(e_coord)])

    def actualizar_tablero(self, pantalla):
        for e_celda in self.lista_celdas:
            e_celda.dibujar(pantalla)  
        pygame.draw.rect(pantalla, colores.GRAY20, (POS_LEFT_TABLERO, POS_TOP_TABLERO, ANCHO_TABLERO,ALTO_TABLERO), 4)
        emoji.dibujar(pantalla)
        self.bombas_restantes = CANTIDAD_BOMBAS - self.contar_cantidad_banderas()
        

    
    def __getitem__(self,index:list) -> str:
        for e_celda in self.lista_celdas:
            index = tuple(index)
            if index == e_celda.coord:
                return e_celda

    def mostrar_todas(self):
        for e_celda in self.lista_celdas:
            e_celda.visible = True
   
    def explotar(self,comando):
        if comando == "stop":
            sonido_explosion.stop()
            sonido_explosion_final.stop()
        else:
            emoji.expresion = 3
            #sonido_explosion.play(CANTIDAD_BOMBAS-1)
            sonido_explosion_final.play()
            


    def contar_cantidad_banderas(self):
        cantidad_banderas = 0
        for e_celda in self.lista_celdas:
            if e_celda.bandera:
                cantidad_banderas += 1
        return cantidad_banderas
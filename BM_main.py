import pygame
import colores
from BM_funciones import *
from BM_constantes import *
from BM_tablero import Tablero
from BM_personaje import emoji


pygame.init()

#Pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("buscaminas")

#Imagen fondo
imagen_buscaminas = pygame.image.load("fondo_buscaminas.png")
imagen_buscaminas = pygame.transform.scale(imagen_buscaminas,(ANCHO_VENTANA, ALTO_VENTANA))

imagen_buscaminas_jugar = pygame.image.load("jugar_fondo_buscaminas.png")
imagen_buscaminas_jugar = pygame.transform.scale(imagen_buscaminas_jugar,(ANCHO_VENTANA, ALTO_VENTANA))

#Botones
imagen_jugar = pygame.image.load("jugar.png")
imagen_jugar = pygame.transform.scale(imagen_jugar,(ANCHO_BOTON, ALTO_BOTON))


imagen_volver = pygame.image.load("volver.png")
imagen_volver = pygame.transform.scale(imagen_volver,(ANCHO_BOTON, ALTO_BOTON))
rect_boton = imagen_volver.get_rect()
rect_boton.y = POS_TOP_BOTON
rect_boton.centerx = POS_CENTERX_BOTON

#Ranking
ruta = "Ranking.db"
crear_tabla_ranking(ruta)

#Ingreso nombre
font_input = pygame.font.SysFont(TIMES, 30)
font_titulo = pygame.font.SysFont(TIMES, 25)
ingreso = "Jugador"
ingreso_rect = pygame.Rect(POS_LEFT_INGRESO, POS_TOP_INGRESO, ANCHO_INGRESO, ALTO_INGRESO)
ingreso_rect.centerx = POS_XCENTER_INGRESO

#Evento creado por mi para manejar el tiempo/SCORE
tick = pygame.USEREVENT + 0
pygame.time.set_timer(tick, 1000)

JUGANDO = 0
flag_correr = True
flag_habilitar_ingreso = False
bandera_tick = False

while flag_correr:

    lista_posicion = [0,0]
    lista_evento = pygame.event.get()

    if JUGANDO == 0:
        #Codigo para la pantalla juego
        flag_poner_bandera = False
        tiempo = 0
        
        #fondo
        pantalla.blit(imagen_buscaminas,(0,0))

        
        #Creo el tablero 
        tablero = Tablero()

        #Actualizo la lista ranking
        lista_ranking = devolver_lista_ranking(ruta)

        #Dibujo rectangulo para ingresar el nombre
        pygame.draw.rect(pantalla, (colores.WHITE), ingreso_rect, 10)
        pygame.draw.rect(pantalla, (colores.PURPLE), ingreso_rect, 5)

        #INGRESO NOMBRE y TITULO ingreso nombre
        nombre_ingresado_render = font_input.render(ingreso, True, (colores.BLACK)) #transformar el texto a imagen
        titulo_nombre_render = font_titulo.render("INGRESE SU NOMBRE", True, colores.BLACK) #transformar el texto a imagen

        pantalla.blit(titulo_nombre_render, ((ingreso_rect.x, ingreso_rect.y - 30)))
        pantalla.blit(nombre_ingresado_render, (ingreso_rect.x + 15, ingreso_rect.y + 15))
        pantalla.blit(imagen_jugar, rect_boton)


        #EVENTOS
        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                flag_correr = False
            if evento.type == pygame.MOUSEBUTTONUP:
                lista_posicion = list(evento.pos)
                if (lista_posicion[0]> rect_boton[0] and lista_posicion[0] < (rect_boton[0]+rect_boton[2])):
                    if (lista_posicion[1]> rect_boton[1] and lista_posicion[1]< (rect_boton[1]+rect_boton[3])):
                        JUGANDO = 1
                        lista_posicion = [0,0]
                if ingreso_rect.collidepoint(lista_posicion) and ingreso == "Jugador":
                    ingreso = "|"

            if evento.type == pygame.KEYDOWN:
                    if flag_habilitar_ingreso == False and ingreso == "|":
                        ingreso = ""
                        flag_habilitar_ingreso = True
                    if flag_habilitar_ingreso:
                        if evento.key == pygame.K_BACKSPACE:  # Si se pulsa Retroceso, borra el último carácter
                            ingreso = ingreso[:-1]
                        elif evento.key == pygame.K_RETURN:
                            JUGANDO = 1
                        else:
                            valor = pygame.key.name(evento.key)  # Obtener el carácter asociado a la tecla
                            if len(valor) == 1:  # Asegurarse de que es un carácter imprimible
                                ingreso += valor
        
        for i in range(len(lista_ranking)):
            texto = "{0}º {1}".format(i, lista_ranking[i]["nombre"])
            if i == 0:
                color = colores.BLACK
                tamaño = 24
                texto = lista_ranking[i]["nombre"]
            elif i < 4:
                color = colores.ORANGE2
                tamaño = 24 - i
            else:
                color = colores.BLACK
                tamaño = 24 - i

            font_nombre = pygame.font.SysFont(LUDICA_GRANDE, tamaño)
            texto_nombre = font_nombre.render(texto, True, color)
            pantalla.blit(texto_nombre,(LEFT_TEXTO, TOP_TEXTO+(i*30)))

            font_tiempo= pygame.font.SysFont(LUDICA_GRANDE, tamaño)
            texto_tiempo = font_tiempo.render(str(lista_ranking[i]["score"]), True, color)
            pantalla.blit(texto_tiempo,((LEFT_TEXTO*2), TOP_TEXTO+(i*30)))

    #Cambia de pantalla a la del tablero
    elif JUGANDO == 1:
        
        for evento in lista_evento:

            #Salir con la cruz
            if evento.type == pygame.QUIT:
                flag_correr = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                #Guardo posicion del click inicial
                lista_posicion_inicial = list(evento.pos)
                if tablero.desbloqueado:
                    #Para que la primera celda este vacia y luego posiciono las bombitas
                    if tablero.flag_ditribucion:
                        emoji.expresion = 1
                    elif lista_posicion_inicial[0] > POS_LEFT_TABLERO and lista_posicion_inicial[0] < (POS_LEFT_TABLERO+ANCHO_TABLERO) and lista_posicion_inicial[1] > POS_TOP_TABLERO and lista_posicion_inicial[1] < (POS_TOP_TABLERO+ALTO_TABLERO):
                        print("entra")
                        tablero.definir_elementos_celdas(list(lista_posicion_inicial))
                        emoji.expresion = 1
                        tablero.flag_ditribucion = True
                    
            if evento.type == pygame.MOUSEBUTTONUP:

                #Guarda posicion del click
                lista_posicion = list(evento.pos)
                print(lista_posicion)

                if tablero.desbloqueado:
                    #Expresion de la cara cuando parece que el usuario va a ganar o normal
                    if tablero.bombas_restantes < 5:
                        emoji.expresion = 2
                    else:
                        emoji.expresion = 0
                    
                    #Click dentro de los limites para inicializar el juego
                    if lista_posicion[0] > 100 and lista_posicion[0] < 400 and lista_posicion[1] > 100 and lista_posicion[1] < 400 and tablero.flag_play == False:
                        tablero.flag_play = True

                    #Click derecho para marcar la bandera
                    if evento.button == 3:
                        tablero.flag_bandera = True
                    else:
                        tablero.flag_bandera = False
                
                #Cuando toca el boton de volver
                if rect_boton.collidepoint(lista_posicion):

                    #Guardo el SCORE solo si es ganador
                    if tablero.flag_ganador:
                        guardar_score(ruta, ingreso, tiempo)

                    #Para volver a la pantalla de inicio
                    JUGANDO = 0

                    #Reseteo las configuraciones iniciales
                    flag_habilitar_ingreso = False
                    ingreso = "Jugador"
                    emoji.expresion = 0
                    tablero.explotar("stop")
                
            #Evento creado por mi para marcar el tiempo/score
            if evento.type == tick and tablero.flag_play == True:
                    tiempo += 1

        #Fondo
        pantalla.blit(imagen_buscaminas_jugar,(0,0))

        #Boton para volver
        pantalla.blit(imagen_volver, rect_boton)

        #Texto del SCORE 
        fuente = pygame.font.SysFont(TIMES, 30)
        text_tiempo = fuente.render("TIEMPO: " + str(tiempo), True, colores.ALICEBLUE ,colores.GRAY1)
        pantalla.blit(text_tiempo, (POS_LEFT_SCORE,POS_TOP_SCORE))

        #Texto bombas restantes
        text_bombas = fuente.render("Bombas restantes: {0}".format(tablero.bombas_restantes), True, colores.ALICEBLUE, colores.GRAY1)
        pantalla.blit(text_bombas, (POS_LEFT_SCORE,POS_TOP_BANDERAS))


        #Analiza si el click es derecho o izquiero y si coincide con una bomba, si lo hace explota
        tablero.analizar_movimiento(lista_posicion)

        #Condicion de ganador
        if tablero.flag_play == False:
            if tablero.flag_ganador and emoji.expresion != 4:
                emoji.expresion = 4
                tablero.mostrar_todas()
       
        #Actualiza los cambios realizados en el codigo anterior
        tablero.actualizar_tablero(pantalla)

    pygame.display.flip()

pygame.quit()
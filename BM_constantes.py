#Pantalla
ANCHO_VENTANA = 700
ALTO_VENTANA = 700

ANCHO_BUSCAMINAS = ANCHO_VENTANA - (ANCHO_VENTANA/4)
ALTO_BUSCAMINAS = ANCHO_BUSCAMINAS/3

#Boton
ANCHO_BOTON = 150
ALTO_BOTON = 75
POS_TOP_BOTON = ALTO_VENTANA - (ALTO_BOTON*1.5)
POS_CENTERX_BOTON = ANCHO_VENTANA/2

#Ranking
LEFT_TEXTO = 200 
TOP_TEXTO = ALTO_BUSCAMINAS + 55

#Fuentes
DEJAVU = 'DejaVu Sans'
BITSTREAM_VERA_SANS = 'Bitstream Vera Sans'
BITSTREAM_CHARTER = 'Bitstream Charter'
LUDICA_GRANDE = 'Lucida Grande'
MS_SHELL = 'MS Shell Dlg 2'
CALIBRI = 'Calibri'
VERDANA = 'Verdana'
GENEVA = 'Geneva'
LUCID = 'Lucid'
ARIAL = 'Arial'
HELVETICA= 'Helvetica'
AVANT_GARDE = 'Avant Garde'
TIMES = 'Times'
SANS_SERIF = 'sans-serif'

#Celdas
TAMAÑO_CELDA = 30
CANTIDAD_X = 10
CANTIDAD_Y = 10
CANTIDAD_BOMBAS = 14

#Tablero
ANCHO_TABLERO = CANTIDAD_X*TAMAÑO_CELDA
ALTO_TABLERO = CANTIDAD_Y*TAMAÑO_CELDA
POS_TOP_TABLERO = ALTO_VENTANA/2 - ALTO_TABLERO/2
POS_LEFT_TABLERO = ANCHO_VENTANA/2 - ANCHO_TABLERO/2


#Ingreso

POS_XCENTER_INGRESO = ANCHO_VENTANA/2
ANCHO_INGRESO = 400
ALTO_INGRESO = 60
POS_TOP_INGRESO = ALTO_VENTANA - (ALTO_BOTON*2.5)
POS_LEFT_INGRESO = ANCHO_VENTANA/2 - ANCHO_INGRESO/2

#Score
POS_TOP_SCORE = 20
POS_LEFT_SCORE = 20

POS_TOP_BANDERAS = POS_TOP_SCORE + 40


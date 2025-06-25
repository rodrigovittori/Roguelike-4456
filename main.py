#pgzero

"""
Pack Kodland: https://kenney.nl/assets/roguelike-caves-dungeons (NO VIENE PRECORTADO)
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update (LO TIENEN QUE ESCALAR)

Pack escalado (drive del profe): https://drive.google.com/drive/folders/19obh4TK0RIBWlXOsaOq9uJ287jUHuLTn?usp=drive_link

> Página para redimensionar assets https://imageresizer.com/bulk-resize/

Link al Repositorio de GitHub: https://github.com/rodrigovittori/Roguelike-4456
Link al proyecto para remix: https://hub.kodland.org/project/309486
============================================================================================================================
Version actual: [M9.L2] - Actividades Nº 2 "Generando Enemigos"
Objetivo: Crear nuestro primer enemigo y generar variaciones del mismo con componentes random/aleatorios

NOTA: La actividad Nº 1 "Revisando nuestro mapa de sueños" NO involucra nuestro juego.

Pasos:
#1: Importar random
#2: Creamos una constante que determine la cantidad de enemigos a spawnear (5) y una lista de enemigos
#3: Creamos un bucle FOR donde calculamos la posición, la validamos,
    creamos los actores enemigos y les asignamos su salud y ataque con valores randomizados
#4: Agregamos un bucle FOR en nuestro draw() para mostrar los enemigos en pantalla

Nota: Pronto calcularemos las colisiones contra ellos
"""

import random

# Ventana de juego hecha de celdas
celda = Actor('border') # Celda que voy a utilizar como referencia para mi mapa
""" ******************************************************************* """
paleta_terrenos = [] # Paleta de terrenos
pared = Actor("border") # 0: Pared de bloques
paleta_terrenos.append(pared) 

piso = Actor("floor")   # 1: Suelo liso (sin decoración)
paleta_terrenos.append(piso)

crack =  Actor("crack") # 2: Suelo resquebrajado/quebradizo
paleta_terrenos.append(crack)

huesos = Actor("bones") # 3: Suelo con una pilita de huesos
paleta_terrenos.append(huesos)
""" ******************************************************************* """

# NOTA: El cambio de tamaño de las actividades Nº 9 y 10 se hace aquí

cant_celdas_ancho = 9 # Ancho del mapa (en celdas)
cant_celdas_alto = 10 # Altura del mapa (en celdas)

WIDTH  = celda.width  * cant_celdas_ancho # Ancho de la ventana (en píxeles)
HEIGHT = celda.height * cant_celdas_alto  # Alto de la ventana (en píxeles)

TITLE = "Rogue-like: Mazmorra Maldita" # Título de la ventana de juego
FPS = 60 # Número de fotogramas por segundo

# Personaje:
personaje = Actor("stand", size=(celda.width, celda.height)) # Creo mi PJ, y ajusto su tamaño al de las celdas

# Nota: si quieren llevar control de la vida, pueden crear dos atributos: "salud_max" y "salud_actual"
# personaje.salud = 100
personaje.salud_max = 100
personaje.salud_act = personaje.salud_max # El PJ empieza con la vida llena

# Nota: si quieren hacer más interesante el combate pueden agregar atributos para el valor mínimo de ataque y el máximo
# (también pueden implementar un sistema de miss y critical hits) Por ejemplo ataque de 2-5 de daño y crítico 2xMAX = 10
personaje.ataque = 5

################# ENEMIGOS ################

CANT_ENEMIGOS_A_SPAWNEAR = 5
lista_enemigos = []

# To-Do: migrar a función
while(len(lista_enemigos) < CANT_ENEMIGOS_A_SPAWNEAR):
    """ PASO 1: Generar coordenadas random """
    
    x = (random.randint(1, cant_celdas_ancho - 2) *  celda.width)
    y = (random.randint(1, cant_celdas_alto - 3)  * celda.height)
    # To-Do: Agregar variable para determinar tipo de enemigo a spawnear

    nvo_enemigo = Actor("enemy", topleft = (x, y))

    """ PASO 2: Validar posición / evitar enemigos superpuestos """
    # Validamos que los enemigos no spawneen uno sobre el otro
    posicion_duplicada = nvo_enemigo.collidelist(lista_enemigos) != -1
    
    if (posicion_duplicada):
        continue
        
    else:
        """ PASO 3: Generar atributos random """
        # Si NO hay conflicto: randomizamos salud, ataque y lo agregamos a lista_enemigos
        nvo_enemigo.salud = random.randint(10, 20)
        nvo_enemigo.ataque = random.randint(5, 10)
        
        """ FINALMENTE, lo agregamos a la lista """
        lista_enemigos.append(nvo_enemigo)

################## MAPAS ##################

mapa = [ [00, 00, 00, 00, 00, 00, 00, 00, 00],
         [00, 01, 01, 01, 01, 01, 01, 01, 00],
         [00, 01, 01, 02, 01, 03, 01, 01, 00],
         [00, 01, 01, 01, 02, 01, 01, 01, 00],
         [00, 01, 03, 02, 01, 01, 03, 01, 00],
         [00, 01, 01, 01, 01, 03, 01, 01, 00],
         [00, 01, 01, 03, 01, 01, 02, 01, 00],
         [00, 01, 01, 01, 01, 01, 01, 01, 00],
         [00, 00, 00, 00, 00, 00, 00, 00, 00],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1] ]

##########################################

mapa_actual = mapa # mapa a dibujar // cambiar valor si cambiamos de habitación
mostrar_valores = False

"""   #####################
     # FUNCIONES PROPIAS #
    #####################   """

def dibujar_mapa(mapa, mostrar_texto):

  for fila in range(len(mapa)):
    for columna in range(len(mapa[fila])):

      # https://pygame-zero.readthedocs.io/en/stable/builtins.html?highlight=anchor#positioning-actors

      if (mapa[fila][columna] != -1):
          """ NOTA: Yo podría multiplicar SIEMPRE por el tamaño de celda, PERO si hacemos eso,
                    ¿Cómo me daría cuenta si alguna casilla me quedó mal escalada? """

          paleta_terrenos[mapa[fila][columna]].left =  pared.width * columna    # POS EN X
          paleta_terrenos[mapa[fila][columna]].top  = pared.height * fila       # POS EN Y
          paleta_terrenos[mapa[fila][columna]].draw()
        
      if (mostrar_texto):
          screen.draw.text( str(mapa_actual[fila][columna]),
                            center=( ( (celda.width * columna) + int(celda.width/2) ), ( (celda.height * fila) + int(celda.height/2)) ),
                            color="black", fontsize=32 )

"""   #####################
     # FUNCIONES PG-ZERO #
    #####################   """

def draw():
    screen.fill((200,200,200))
    dibujar_mapa(mapa = mapa_actual, mostrar_texto = mostrar_valores)
    # Nota: Como el mapa en sí no se actualiza hasta terminar el nivel,
    #       podríamos simplemente dibujarlo UNA vez y no en cada frame
    #       Implementar este cambio cuando nuestro juego tenga lógica más compleja

    for enemigo in lista_enemigos:
        enemigo.draw()
    
    personaje.draw()
    
    # Mostramos valores personaje:
    screen.draw.text(("❤️: " + str(personaje.salud_act) + "/" + str(personaje.salud_act) ), midleft = (int(celda.width / 2), (HEIGHT - int(celda.height / 2))), color = 'black', fontsize = 36)
    screen.draw.text(("🗡️: " + str(personaje.ataque)), midright = ( (WIDTH - int(celda.width / 2)), (HEIGHT - int(celda.height / 2)) ), color = 'black', fontsize = 36)

def on_key_down(key):
    if ((keyboard.right or keyboard.d) and (personaje.x < (WIDTH - celda.width * 2))):
        # ¿Xq 2?: Una (a la que me voy a desplazar) y otra (por la pared, que NO puedo atravesar)
        personaje.x += celda.width
        personaje.image = "stand" # xq stand mira a la dcha
    
    elif ((keyboard.left or keyboard.a) and (personaje.x > (celda.width * 2))):
        personaje.x -= celda.width
        personaje.image = "left" # xq mira a la izq
        
    elif ((keyboard.down or keyboard.s) and (personaje.y < HEIGHT - celda.height * 3)):
        # A partir de la próxima actividad (9) deberían ser 3 celdas: a la que me muevo, la pared y el espacio para datos
        personaje.y += celda.height
    
    elif ((keyboard.up or keyboard.w) and (personaje.y > (celda.height * 2))):
        personaje.y -= celda.height
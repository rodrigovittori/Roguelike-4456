#pgzero

"""
Pack Kodland: https://kenney.nl/assets/roguelike-caves-dungeons (NO VIENE PRECORTADO)
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update (LO TIENEN QUE ESCALAR)

pack escalado (drive del profe): https://drive.google.com/drive/folders/19obh4TK0RIBWlXOsaOq9uJ287jUHuLTn?usp=drive_link

> Página para redimensionar assets https://imageresizer.com/bulk-resize/

Link al Repositorio de GitHub: https://github.com/rodrigovittori/Roguelike-4456
Link al proyecto para remix: https://hub.kodland.org/project/309486
============================================================================================================================
Version actual: [M9.L1] - Actividad #4: "Visualización del mapa en la pantalla"
Objetivo: En función del valor de cada celda, renderizar el terreno correspondiente

PASOS:

1º) Crear una paleta_terrenos = [] con los Actores que creamos previamente
2º) Modificar dibujar_mapa() para que dibuje cada casilla según el valor correspondiente de la paleta

NOTA: El texto en el for debe volver a center (top left no queda bien)
NOTA 2: En la tarea anterior explicar variable mapa actual y en la próxima eliminar mostrar_valores

"""

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
cant_celdas_ancho = 7 # Ancho del mapa (en celdas)
cant_celdas_alto =  7 # Altura del mapa (en celdas)

WIDTH  = celda.width  * cant_celdas_ancho # Ancho de la ventana (en píxeles)
HEIGHT = celda.height * cant_celdas_alto  # Alto de la ventana (en píxeles)

TITLE = "Rogue-like: Mazmorra Maldita" # Título de la ventana de juego
FPS = 60 # Número de fotogramas por segundo

################## MAPAS ##################

mapa = [ [0, 0, 0, 0, 0, 0, 0],
         [0, 1, 2, 1, 3, 1, 0],
         [0, 1, 1, 2, 1, 1, 0],
         [0, 3, 2, 1, 1, 3, 0],
         [0, 1, 1, 1, 3, 1, 0],
         [0, 1, 3, 1, 1, 2, 0],
         [0, 0, 0, 0, 0, 0, 0] ]

mapa_2 = [ [0, 0, 0, 0, 0, 0, 0],
           [0, 1, 1, 1, 1, 1, 0],
           [0, 1, 3, 1, 3, 1, 0],
           [0, 1, 1, 1, 1, 1, 0],
           [0, 3, 1, 1, 1, 3, 0],
           [0, 1, 3, 3, 3, 1, 0],
           [0, 0, 0, 0, 0, 0, 0] ]

##########################################

mapa_actual = mapa # mapa a dibujar // cambiar valor si cambiamos de habitación
mostrar_valores = True

"""   #####################
     # FUNCIONES PROPIAS #
    #####################   """

def dibujar_mapa(mapa, mostrar_texto):

  for fila in range(len(mapa)):
    for columna in range(len(mapa[fila])):

      """
      Lista códigos terrenos
      
      0: pared
      1: piso (sin nada)
      2: piso (roto/resquebrajado)
      3: piso (c/ huesitos)
      """

      # https://pygame-zero.readthedocs.io/en/stable/builtins.html?highlight=anchor#positioning-actors

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

    # Borrar después de la próxima tarea:
    screen.draw.text(("  Ventana de " + str(cant_celdas_ancho) + " x " + str(cant_celdas_alto) + "  "), center=(WIDTH/2, int(celda.height /2)), color = "white", background = "black", fontsize = int(celda.height /2))

    screen.draw.text("Pulse [Espacio] para alternar el diseño del mapa", center=(WIDTH/2, ((cant_celdas_alto * celda.height) - int(celda.height /2))), color = "white", background = "black", fontsize = int(celda.height /3))

def on_key_down(key):
    global mapa_actual, mostrar_valores
    
    if key == keys.SPACE:
        if mapa_actual == mapa:
            mapa_actual = mapa_2
        else:
            mapa_actual = mapa

    if key == keys.M:
        mostrar_valores = not mostrar_valores

    
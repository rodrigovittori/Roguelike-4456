#pgzero

"""
Pack Kodland: https://kenney.nl/assets/roguelike-caves-dungeons (NO VIENE PRECORTADO)
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update (LO TIENEN QUE ESCALAR)

pack escalado (drive del profe): https://drive.google.com/drive/folders/19obh4TK0RIBWlXOsaOq9uJ287jUHuLTn?usp=drive_link

> Página para redimensionar assets https://imageresizer.com/bulk-resize/

Link al Repositorio de GitHub: https://github.com/rodrigovittori/Roguelike-4456
Link al proyecto para remix: https://hub.kodland.org/project/309486
============================================================================================================================
Version actual: [M9.L1] - Actividad #3: "Bucles anidados"
Objetivo: Implementar un sistema de bucles anidados que recorra nuestro mapa y determine el valor de cada celda

NOTA: Ya lo implementamos en la tarea anterior pero vamos a migrar esa lógica de nuestro draw() a una función especial
      llamada dibujar_mapa(mapa, mostrar_texto)

PASOS:

1º) Modificar nuestro draw()
2º) Crear nuestra Función dibujar_mapa(mapa) que convierte los datos de una tabla (mapa) en los gráficos de nuestro nivel
3º) Implementar cambio de mapas desde on_key_down()

"""

# Ventana de juego hecha de celdas
celda = Actor('border') # Celda que voy a utilizar como referencia para mi mapa
""" ******************************************************************* """
# Paleta de terrenos:
pared =  Actor("border") # 0: Pared de bloques
piso =   Actor("floor")  # 1: Suelo liso (sin decoración)
crack =  Actor("crack")  # 2: Suelo resquebrajado/quebradizo
huesos = Actor("bones")  # 3: Suelo con una pilita de huesos
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

      # IMPLEMENTAR PALETA DE TERRENOS AQUÍ
        
      if (mostrar_texto):
          screen.draw.text( str(mapa_actual[fila][columna]),
                            topleft=( (celda.width * columna), (celda.height * fila) ),
                            color="black", fontsize=32 )

"""   #####################
     # FUNCIONES PG-ZERO #
    #####################   """

def draw():
    screen.fill((200,200,200))
    dibujar_mapa(mapa = mapa_actual, mostrar_texto = True)

    # Borrar después de la próxima tarea:
    screen.draw.text(("  Ventana de " + str(cant_celdas_ancho) + " x " + str(cant_celdas_alto) + "  "), center=(WIDTH/2, int(celda.height /2)), color = "white", background = "black", fontsize = int(celda.height /2))

    screen.draw.text("Pulse [Espacio] para alternar el diseño del mapa", center=(WIDTH/2, ((cant_celdas_alto * celda.height) - int(celda.height /2))), color = "white", background = "black", fontsize = int(celda.height /3))

def on_key_down(key):
    global mapa_actual
    
    if key == keys.SPACE:
        if mapa_actual == mapa:
            mapa_actual = mapa_2
        else:
            mapa_actual = mapa
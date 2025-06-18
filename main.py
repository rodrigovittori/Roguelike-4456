#pgzero

"""
Pack Kodland: https://kenney.nl/assets/roguelike-caves-dungeons (NO VIENE PRECORTADO)
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update (LO TIENEN QUE ESCALAR)

Pack escalado (drive del profe): https://drive.google.com/drive/folders/19obh4TK0RIBWlXOsaOq9uJ287jUHuLTn?usp=drive_link

> Página para redimensionar assets https://imageresizer.com/bulk-resize/

Link al Repositorio de GitHub: https://github.com/rodrigovittori/Roguelike-4456
Link al proyecto para remix: https://hub.kodland.org/project/309486
============================================================================================================================
Version actual: [M9.L1] - Actividad #6: "Desplazamiento a través de las celdas"
Objetivo: Implementar nuestro sistema de movimiento (por casillas/por turnos)

PASOS:
1º) Implementar el despalzamiento entre celdas por turnos con on_key_down(key)

NOTA 1: No olvidar el cambio de sprite
NOTA 2: No olvidar las notas de ejercicios adicionales
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

# Personaje:
personaje = Actor("stand", size=(celda.width, celda.height)) # Creo mi PJ, y ajusto su tamaño al de las celdas

# Nota: si quieren llevar control de la vida, pueden crear dos atributos: "salud_max" y "salud_actual"
# personaje.salud = 100
personaje.salud_max = 100
personaje.salud_act = personaje.salud_max # El PJ empieza con la vida llena

# Nota: si quieren hacer más interesante el combate pueden agregar atributos para el valor mínimo de ataque y el máximo
# (también pueden implementar un sistema de miss y critical hits) Por ejemplo ataque de 2-5 de daño y crítico 2xMAX = 10
personaje.ataque = 5

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
mostrar_valores = False

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

    personaje.draw()
    # Mostramos valores personaje:
    #screen.draw.text(("❤️: " + str(personaje.salud)), midright=((WIDTH - 15), 14), color = 'white', fontsize = 16)
    screen.draw.text(("❤️: " + str(personaje.salud_act) + "/" + str(personaje.salud_max)), midright=((WIDTH - 15), 14), color = 'white', fontsize = 16)
    screen.draw.text(("🗡️: " + str(personaje.ataque)), midright=((WIDTH - 15), 36), color = 'white', fontsize = 16)

def on_key_down(key):
    if ((keyboard.right or keyboard.d)):
        personaje.x += celda.width
        personaje.image = "stand" # xq stand mira a la dcha
    
    elif ((keyboard.left or keyboard.a)):
        personaje.x -= celda.width
        personaje.image = "left" # xq mira a la izq
        
    elif ((keyboard.down or keyboard.s)):
        personaje.y += celda.height
    
    elif ((keyboard.up or keyboard.w)):
        personaje.y -= celda.height
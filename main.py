#pgzero

"""
Pack Kodland: https://kenney.nl/assets/roguelike-caves-dungeons (NO VIENE PRECORTADO)
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update (LO TIENEN QUE ESCALAR)

pack escalado (drive del profe): https://drive.google.com/drive/folders/19obh4TK0RIBWlXOsaOq9uJ287jUHuLTn?usp=drive_link

> Página para redimensionar assets https://imageresizer.com/bulk-resize/

Link al Repositorio de GitHub: https://github.com/rodrigovittori/Roguelike-4456
Link al proyecto para remix: https://hub.kodland.org/project/309486
============================================================================================================================
Version actual: [M9.L1] - Actividad #2 "Creando un mapa"

Objetivo: Comprender como modificar el tamaño del mapa y como vamos a cargar nuestros mapas (tablas)

NOTA: Podríamos crear una función "cargar_mapa(mapa)" que se encargue de actualizar el tamaño y demas,
      pero lo ideal es que la pantalla sea desde el principio lo suficientemente grande para mostrar cada mapa

NOTA 2: Si quisiéramos mostrar mapas más grander podríamos desde draw() dibujar una "porción" del mapa

PASOS:

1º) Modificar las variables que definen la cant de casillas horiz y vert (7x7)
2º) Crear una "tabla" (lista de listas) que represente nuestro mapa

Nota: en el próximo ejercicio es que se crean los actores para dibujar
"""

# Ventana de juego hecha de celdas
celda = Actor('border') # Celda que voy a utilizar como referencia para mi mapa

cant_celdas_ancho = 7 # Ancho del mapa (en celdas)
cant_celdas_alto =  7 # Altura del mapa (en celdas)

WIDTH  = celda.width  * cant_celdas_ancho # Ancho de la ventana (en píxeles)
HEIGHT = celda.height * cant_celdas_alto  # Alto de la ventana (en píxeles)

TITLE = "Rogue-like: Mazmorra Maldita" # Título de la ventana de juego
FPS = 60 # Número de fotogramas por segundo

mapa = [ [0, 0, 0, 0, 0, 0, 0],
         [0, 1, 2, 1, 3, 1, 0],
         [0, 1, 1, 2, 1, 1, 0],
         [0, 3, 2, 1, 1, 3, 0],
         [0, 1, 1, 1, 3, 1, 0],
         [0, 1, 3, 1, 1, 2, 0],
         [0, 0, 0, 0, 0, 0, 0] ]

def draw():
    screen.fill((200,200,200))
    for fila in range(len(mapa)):
        for col in range(len(mapa[fila])):
            screen.draw.text( str(mapa[fila][col]),
                              center=( ( (celda.width * col) + int(celda.width/2) ), ( (celda.height * fila) + int(celda.height/2)) ),
                              color="black", fontsize=32)
"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *
from freegames import path

car = path('car.gif')

# Lista de símbolos usados en el juego de memoria (32 símbolos únicos para 64 fichas).
symbols = [
    '❤️', '🍀', '⭐', '🌈', '🌸', '🐶', '🐱', '🍉',
    '🍓', '🌼', '🚀', '🌏', '🎉', '🦄', '🎈', '🌻',
    '💎', '🍔', '🌙', '⚽', '🏆', '🎸', '📚', '💻',
    '🎨', '💼', '🌊', '🐳', '🎃', '🎭', '🐝', '🧊'
]

# Crear pares de símbolos y barajarlos.
tiles = symbols * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0

def square(x, y):
    """Dibuja un cuadrado blanco con un contorno negro en la posición (x, y) especificada."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Convierte las coordenadas (x, y) a un índice correspondiente en la cuadrícula de fichas."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convierte un contador de fichas a sus coordenadas (x, y) en la pantalla."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Actualiza la ficha seleccionada y la visibilidad de las fichas según un toque en (x, y)."""
    global tap_count
    spot = index(x, y)  # Determina la ficha tocada usando las coordenadas.
    mark = state['mark']  # Obtiene la ficha previamente marcada.

    tap_count += 1  # Incrementa el contador de toques.

    # Lógica para manejar el toque en la ficha actual.
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False  # Revela la ficha tocada.
        hide[mark] = False  # Revela la ficha previamente marcada.
        state['mark'] = None  # Reinicia la marca.

    # Verifica si todas las fichas han sido reveladas.
    if all(not h for h in hide):
        print("¡Todas las fichas han sido reveladas!")
        state['win'] = True  # Marca el estado de victoria.

def draw():
    """Dibuja el tablero de juego, las fichas y cualquier mensaje en la pantalla."""
    clear()  # Limpia la pantalla.
    goto(0, 0)  # Coloca la tortuga en el centro.
    shape(car)  # Establece la forma del coche.
    stamp()  # Imprime la forma del coche en la pantalla.

    # Dibuja las fichas ocultas.
    for count in range(64):
        if hide[count]:
            x, y = xy(count)  # Obtiene las coordenadas de la ficha.
            square(x, y)  # Dibuja la ficha.

    mark = state['mark']  # Obtiene la ficha actualmente marcada.

    # Dibuja la ficha marcada si está oculta.
    if mark is not None and hide[mark]:
        x, y = xy(mark)  # Obtiene las coordenadas de la ficha marcada.
        up()
        goto(x + 5, y + 5)  # Ajusta la posición para mostrar el símbolo.
        color('black')  # Cambia el color para el texto.
        write(tiles[mark], font=('Arial', 30, 'normal'))  # Escribe el símbolo de la ficha.

    up()
    goto(-200, 210)  # Posiciona el texto del contador de toques.
    color('black')
    write(f'Tap Count: {tap_count}', font=('Arial', 20, 'normal'))  # Muestra el contador de toques.

    # Muestra el mensaje de victoria si se ha ganado.
    if 'win' in state and state['win']:
        up()
        goto(0, 135)
        color('red')
        write('¡Has Ganado!', align='center', font=('Arial', 30, 'normal'))

    update()  # Actualiza la pantalla.
    ontimer(draw, 100)  # Programa la próxima actualización.

shuffle(tiles)
setup(520, 520, 370, 0)  
addshape(car)
hideturtle()  
tracer(False)  
onscreenclick(tap)
draw()
done()
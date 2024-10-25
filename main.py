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

symbols = [
    '❤️', '🍀', '⭐', '🌈', '🌸', '🐶', '🐱', '🍉',
    '🍓', '🌼', '🚀', '🌏', '🎉', '🦄', '🎈', '🌻',
    '💎', '🍔', '🌙', '⚽', '🏆', '🎸', '📚', '💻',
    '🎨', '💼', '🌊', '🐳', '🎃', '🎭', '🐝', '🧊'
]

tiles = symbols * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0  # Initialize tap count


def square(x, y):
    """Draw white square with black outline at (x, y)."""
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
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global tap_count  # Use the global variable for tap count
    spot = index(x, y)
    mark = state['mark']

    tap_count += 1  # Increment tap count

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    # Check if all tiles are revealed
    if all(not h for h in hide):
        print("All tiles have been revealed!")  # Print in console
        state['win'] = True  # Set win state


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 5, y + 5)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Display tap count
    up()
    goto(-200, 210)  # Position for the tap count
    color('black')
    write(f'Tap Count: {tap_count}', font=('Arial', 20, 'normal'))

    # Display win message if all tiles are revealed
    if 'win' in state and state['win']:
        up()
        goto(0, 135)  # Position for the win message
        color('red')
        write('You Win!', align='center', font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(520, 520, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
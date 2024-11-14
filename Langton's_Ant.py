import pygame
import sys

# Constante
WIDTH, HEIGHT = 800, 800  # Dimensiuni fereastra
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60  # Efectiv FPS

# Optiuni de configurare
size_options = {
    "1": 2,     # Dimensiune mare (CELL_SIZE mic)
    "2": 5,     # Dimensiune medie (CELL_SIZE mediu)
    "3": 8      # Dimensiune mica (CELL_SIZE mare)
}

speed_options = {
    "1": 10,    # Viteza mica
    "2": 100,   # Viteza medie
    "3": 1000   # Viteza mare
}

# Directii de mers (sus, dreapta, jos, stanga)
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

class LangtonsAnt:
    def __init__(self, grid_width, grid_height):
        # Initializam pozitia furnicii si directia (incepem din mijloc)
        self.x = grid_width // 2
        self.y = grid_height // 2
        self.direction = 0  # incepem cu directia "sus"

    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    def turn_left(self):
        self.direction = (self.direction - 1) % 4

    def move_forward(self, grid_width, grid_height):
        dx, dy = directions[self.direction]
        self.x = (self.x + dx) % grid_width
        self.y = (self.y + dy) % grid_height

def get_valid_input(prompt, valid_options):
    # Functie care cere un input valid de la utilizator
    while True:
        choice = input(prompt)
        if choice in valid_options:
            return choice
        else:
            print("Optiune invalida! Va rugam sa introduceti o optiune valida.")

def display_console_menu():
    # Afisam optiunile disponibile in consola si capturam inputul validat
    print("Alegeti dimensiunea grid-ului:")
    print("1 - Dimensiune mare")
    print("2 - Dimensiune medie")
    print("3 - Dimensiune mica")
    size_choice = get_valid_input("Introduceti alegerea (1, 2 sau 3): ", size_options.keys())

    print("\nAlegeti viteza simularii:")
    print("1 - Viteza mica")
    print("2 - Viteza medie")
    print("3 - Viteza mare")
    speed_choice = get_valid_input("Introduceti alegerea (1, 2 sau 3): ", speed_options.keys())

    # Returnam valorile CELL_SIZE si speed pe baza alegerii utilizatorului
    return size_options[size_choice], speed_options[speed_choice]

# Initializam pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Langton's Ant Simulator")
clock = pygame.time.Clock()

# Afisam meniul in consola si capturam optiunile utilizatorului
CELL_SIZE, speed = display_console_menu()
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Initializam grid-ul si furnica
grid = [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
ant = LangtonsAnt(GRID_WIDTH, GRID_HEIGHT)

# Codul principal (main)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Executam "speed" pasi per cadru pentru a controla viteza simularii
    for _ in range(speed):
        # Algoritmul pentru furnica
        if grid[ant.x][ant.y] == 0:  # Celula de culoare alba
            ant.turn_right()
            grid[ant.x][ant.y] = 1  # Schimbam culoarea celulei la negru
        else:  # Celula de culoare neagra
            ant.turn_left()
            grid[ant.x][ant.y] = 0  # Schimbam culoarea celulei la alb

        # Furnica se misca inainte cu o casuta
        ant.move_forward(GRID_WIDTH, GRID_HEIGHT)

    # Desenam grid-ul pentru reprezentarea vizuala
    screen.fill(WHITE)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            color = BLACK if grid[x][y] == 1 else WHITE
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Actualizare pentru display
    pygame.display.flip()
    clock.tick(FPS)

# Iesire din joc
pygame.quit()
sys.exit()

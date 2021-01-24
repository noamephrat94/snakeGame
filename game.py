import pygame
import pygame_menu
import sys
import random


class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * gridsize)) % screen_width), (cur[1]+(y * gridsize)) % screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            game_over(self.score)
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
        print(self.positions[0])

    def reset(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)


class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)


def drawGrid(surface):

    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (84, 194, 205), rr)


screen_width = 600
screen_height = 400

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)



def easy():
    game_loop(10)
def medium():
    game_loop(15)
def hard():
    game_loop(20)


def game_over(score):
    background = pygame.image.load("/Users/noame/Downloads/snake_game.jpg").convert_alpha()

    white = (255, 255, 255)
    display_surface = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Snake Game')
    font = pygame.font.Font('freesansbold.ttf', 35)
    text = font.render(("Game over your score was: {}".format(score)), True, white)
    textRect = text.get_rect()
    textRect.center = (screen_width // 2, screen_height // 2)
    display_surface.blit(background, (0, 0))
    display_surface.blit(text, textRect)
    pygame.display.update()
    pygame.time.wait(5000)
    main()


def game_loop(level):
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("monospace", 16)

    while (True):
        clock.tick(level)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0, 0, 0))
        screen.blit(text, (5, 10))
        pygame.display.update()


def main():
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    menu = pygame_menu.Menu(400, 600, 'Snake',
                            theme=pygame_menu.themes.THEME_BLUE)

    # menu.add_text_input('Name:', default='')
    # menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
    menu.add_button('Easy', easy)
    menu.add_button('Medium', medium)
    menu.add_button('Hard', hard)
    # menu.add_button('Level 1', game_loop)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)


main()


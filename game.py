import pygame
import pygame_menu
from snake import *
from food import *



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

    while snake.alive:
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

    game_over(snake.score)


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


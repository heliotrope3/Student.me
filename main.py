import pygame
from promptData import prompts
pygame.font.init()

WIDTH, HEIGHT = 600, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Student.me')

#background colour
BACKGROUND = (40, 45, 50)

TEXT_FONT = pygame.font.SysFont('comicsans', 80)

#drawing game screen
def draw_window(state):
    WIN.fill(BACKGROUND)
    if state == 'play':
        game_screen()
    pygame.display.update()

def game_screen():
    prompt = prompts["tests"][0]
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(WIDTH // 4 - 100, HEIGHT // 7 - 50, 500, 400))
    WIN.blit(TEXT_FONT.render(prompt.name, 1, (0, 0, 0)), (WIDTH // 2 - 130, HEIGHT // 3 - 25))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(WIDTH // 2 - 250, HEIGHT - 200, 200, 100))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(WIDTH - 250, HEIGHT - 200, 200, 100))
    WIN.blit(TEXT_FONT.render(prompt.opt1.name, 1, (0, 0, 0)), (WIDTH - 220, HEIGHT - 170))
    WIN.blit(TEXT_FONT.render(prompt.opt2.name, 1, (0, 0, 0)), (WIDTH // 2 - 190, HEIGHT - 170))

#run game
def main():
    state = 'play'
    run = True
    while run:

        #display game screen
        if state == 'play':
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if WIDTH // 2 - 100 <= mouse[0] <= WIDTH // 2 + 100 and HEIGHT // 2 - 50 <= mouse[1] <= HEIGHT // 2 + 50:
                        state = 'play'
            mouse = pygame.mouse.get_pos()
            draw_window(state)



if __name__ == "__main__":
    main()

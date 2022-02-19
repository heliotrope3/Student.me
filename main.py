import pygame


WIDTH, HEIGHT = 600, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Student.me')

#background colour
BACKGROUND = (40, 45, 50)

#drawing game screen
def draw_window(state):
    WIN.fill(BACKGROUND)
    if state == 'play':
        game_screen()
    pygame.display.update()

def game_screen():
    pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100))

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

import pygame
from promptData import prompts
from Student import Student
pygame.font.init()

WIDTH, HEIGHT = 600, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Student.me')

#background colour
BACKGROUND = (40, 45, 50)

TEXT_FONT = pygame.font.SysFont('arial', 60)
MEDIUM_FONT = pygame.font.SysFont('arial', 40)
SMALL_FONT = pygame.font.SysFont('arial', 30)

#drawing game screen
def draw_window(state, student):
    WIN.fill(BACKGROUND)
    if state == 'play':
        game_screen(student)
    pygame.display.update()

def game_screen(student):
    prompt = prompts["encounter"][2]
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(WIDTH // 4 - 100, HEIGHT // 4 + 50, 500, 200))
    display_text(TEXT_FONT, prompt.name, (WIDTH // 2, HEIGHT // 2), (0, 0, 0))

    pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(WIDTH // 2 - 260, HEIGHT - 260, 220, 100))
    pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(WIDTH - 260, HEIGHT - 260, 220, 100))
    display_text(MEDIUM_FONT, prompt.opt1.name, (WIDTH // 2 - 150, HEIGHT - 190), (255, 255, 255))
    display_text(MEDIUM_FONT, prompt.opt2.name, (WIDTH - 150, HEIGHT - 190), (255, 255, 255))

    WIN.blit(SMALL_FONT.render("HEALTH:", 1, (255, 255, 255)), (40, 25))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(220, 30, 350, 30))
    pygame.draw.rect(WIN, (0, 255, 0), pygame.Rect(220, 30, (350 * (student.health / student.maxes["health"])) // 1, 30))

    WIN.blit(SMALL_FONT.render("STRESS:", 1, (255, 255, 255)), (40, 75))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(220, 80, 350, 30))
    pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(220, 80, (350 * (student.stress / student.maxes["stress"])) // 1, 30))

    WIN.blit(SMALL_FONT.render("SMARTS:", 1, (255, 255, 255)), (40, 125))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(220, 130, 350, 30))
    pygame.draw.rect(WIN, (0, 0, 255), pygame.Rect(220, 130, (350 * (student.smarts / student.maxes["smarts"])) // 1, 30))

    WIN.blit(SMALL_FONT.render("HAPPINESS:", 1, (255, 255, 255)), (40, 175))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(220, 180, 350, 30))
    pygame.draw.rect(WIN, (255, 255, 0), pygame.Rect(220, 180, (350 * (student.happiness / student.maxes["happiness"])) // 1, 30))

    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(WIDTH//2 - 50, HEIGHT - 90, 100, 50))
    WIN.blit(SMALL_FONT.render("PAUSE", 1, (255, 255, 255)), (WIDTH // 2 - 40, HEIGHT - 85))

#run game
def main():
    student = Student("uni")
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
            draw_window(state, student)

def display_text(font, phrase, center, color):
    for index, chunk in enumerate(phrase):
        text = font.render(chunk, 1, color)
        rect = text.get_rect()
        rect.center = (center[0], (center[1] - (rect.height * len(phrase)//2) + (rect.height) * index))
        WIN.blit(text, rect)

if __name__ == "__main__":
    main()

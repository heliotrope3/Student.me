import pygame
from promptData import prompts
from Student import Student
pygame.font.init()

WIDTH, HEIGHT = 600, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Student.me')

#background colour
BACKGROUND = (40, 45, 50)

TEXT_FONT = pygame.font.SysFont('comicsans', 80)
SMALL_FONT = pygame.font.SysFont('comicsans', 40)

#drawing game screen
def draw_window(state, student):
    WIN.fill(BACKGROUND)
    if state == 'play':
        game_screen(student)
    pygame.display.update()

def game_screen(student):
    prompt = prompts["tests"][0]
    prompt_text = TEXT_FONT.render(prompt.name, 1, (0, 0, 0))
    prompt_rect = prompt_text.get_rect()
    prompt_rect.center = (WIDTH // 2, HEIGHT // 2)
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(WIDTH // 4 - 100, HEIGHT // 4 + 100, 500, 200))
    #WIN.blit(prompt_text, prompt_rect)
    display_text(TEXT_FONT, ["TEST", "TEXT"], (WIDTH // 2, HEIGHT // 2))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(WIDTH // 2 - 250, HEIGHT - 200, 200, 100))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(WIDTH - 250, HEIGHT - 200, 200, 100))
    WIN.blit(TEXT_FONT.render(prompt.opt1.name, 1, (0, 0, 0)), (WIDTH - 220, HEIGHT - 170))
    WIN.blit(TEXT_FONT.render(prompt.opt2.name, 1, (0, 0, 0)), (WIDTH // 2 - 190, HEIGHT - 170))

    WIN.blit(SMALL_FONT.render("HEALTH:", 1, (255, 255, 255)), (30, 30))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(220, 30, 350, 30))
    pygame.draw.rect(WIN, (0, 255, 0), pygame.Rect(220, 30, (350 * (student.health / student.maxes["health"])) // 1, 30))

    WIN.blit(SMALL_FONT.render("STRESS:", 1, (255, 255, 255)), (30, 80))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(220, 80, 350, 30))
    pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(220, 80, (350 * (student.stress / student.maxes["stress"])) // 1, 30))

    WIN.blit(SMALL_FONT.render("SMARTS:", 1, (255, 255, 255)), (30, 130))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(220, 130, 350, 30))
    pygame.draw.rect(WIN, (0, 0, 255), pygame.Rect(220, 130, (350 * (student.smarts / student.maxes["smarts"])) // 1, 30))

    WIN.blit(SMALL_FONT.render("HAPPINESS:", 1, (255, 255, 255)), (30, 180))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(220, 180, 350, 30))
    pygame.draw.rect(WIN, (255, 255, 0), pygame.Rect(220, 180, (350 * (student.happiness / student.maxes["happiness"])) // 1, 30))

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

def display_text(font, phrase, center):
    for index, chunk in enumerate(phrase):
        text = font.render(chunk, 1, (0, 0, 0))
        rect = text.get_rect()
        rect.center = (center[0], (center[1] - (rect.height * len(phrase)//2) + (rect.height) * index))
        WIN.blit(text, rect)

if __name__ == "__main__":
    main()

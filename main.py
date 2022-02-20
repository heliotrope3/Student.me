import pygame
from promptData import prompts
from Student import Student
pygame.font.init()

WIDTH, HEIGHT = 600, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Student.me')

TEXT_FONT = pygame.font.SysFont('arial', 60)
MEDIUM_FONT = pygame.font.SysFont('arial', 40)
SMALL_FONT = pygame.font.SysFont('arial', 30)

def draw_menu_screen():
    WIN.fill((237, 255, 238))
    WIN.blit(TEXT_FONT.render("STUDENT.me", 1, (0, 0, 0)), (WIDTH // 2 - 150, 200))
    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 - 20, 150, 70))
    pygame.draw.rect(WIN, (237, 255, 238), pygame.Rect(WIDTH // 2 - 70, HEIGHT // 2 - 15, 140, 60))
    WIN.blit(MEDIUM_FONT.render("START", 1, (0, 0, 0)), (WIDTH // 2 - 50, HEIGHT // 2 - 10))
    pygame.display.update()

def draw_select_screen():
    WIN.fill((255, 232, 238))
    WIN.blit(TEXT_FONT.render("Choose your level", 1, (0, 0, 0)), (WIDTH // 2 - 195, 200))
    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 - 20, 400, 70))
    pygame.draw.rect(WIN, (242, 237, 255), pygame.Rect(WIDTH // 2 - 195, HEIGHT // 2 - 15, 390, 60))
    WIN.blit(MEDIUM_FONT.render("High School (Regular)", 1, (0, 0, 0)), (WIDTH // 2 - 160, HEIGHT // 2 - 10))
    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 + 100, 400, 70))
    pygame.draw.rect(WIN, (230, 239, 255), pygame.Rect(WIDTH // 2 - 195, HEIGHT // 2 + 105, 390, 60))
    WIN.blit(MEDIUM_FONT.render("University (Hard)", 1, (0, 0, 0)), (WIDTH // 2 - 115, HEIGHT // 2 + 110))
    pygame.display.update() 

def draw_pause_screen(student):
    WIN.fill((237, 255, 238))
    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 - 110, 400, 70))
    pygame.draw.rect(WIN, (253, 255, 209), pygame.Rect(WIDTH // 2 - 195, HEIGHT // 2 - 105, 390, 60))
    WIN.blit(MEDIUM_FONT.render("Resume", 1, (0, 0, 0)), (WIDTH // 2 - 65, HEIGHT // 2 - 100))
    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 + 10, 400, 70))
    pygame.draw.rect(WIN, (255, 232, 238), pygame.Rect(WIDTH // 2 - 195, HEIGHT // 2 + 15, 390, 60))
    WIN.blit(MEDIUM_FONT.render("Restart", 1, (0, 0, 0)), (WIDTH // 2 - 55, HEIGHT // 2 + 20))
    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 + 130, 400, 70))
    pygame.draw.rect(WIN, (237, 255, 238), pygame.Rect(WIDTH // 2 - 195, HEIGHT // 2 + 135, 390, 60))
    WIN.blit(MEDIUM_FONT.render("Menu", 1, (0, 0, 0)), (WIDTH // 2 - 45, HEIGHT // 2 + 140))
    pygame.display.update()

def draw_end_screen(student):
    if student.stress == student.maxes["stress"]:
        WIN.fill((237, 255, 238))
        WIN.blit(TEXT_FONT.render("Game Over", 1, (0, 0, 0)), (WIDTH // 2 - 125, 100))
        display_text(MEDIUM_FONT, ["You became too stressed", "and dropped out"], (WIDTH // 2, HEIGHT // 2 - 10), (0, 0, 0))
    elif student.happiness == 0:
        WIN.fill((237, 255, 238))
        WIN.blit(TEXT_FONT.render("Game Over", 1, (0, 0, 0)), (WIDTH // 2 - 125, 100))
        display_text(MEDIUM_FONT, ["You became too depressed", "and dropped out"], (WIDTH // 2, HEIGHT // 2 - 10), (0, 0, 0))
    elif student.smarts == 0:
        WIN.fill((237, 255, 238))
        WIN.blit(TEXT_FONT.render("Game Over", 1, (0, 0, 0)), (WIDTH // 2 - 125, 100))
        display_text(MEDIUM_FONT, ["You got kicked out", "for not meeting the", "grade requirements"], (WIDTH // 2, HEIGHT // 2 - 10), (0, 0, 0))
    elif student.health == 0:
        WIN.fill((237, 255, 238))
        WIN.blit(TEXT_FONT.render("Game Over", 1, (0, 0, 0)), (WIDTH // 2 - 125, 100))
        display_text(MEDIUM_FONT, ["You got too sick and", "had to leave school :("], (WIDTH // 2, HEIGHT // 2 - 10), (0, 0, 0))
    else:
        WIN.fill((237, 255, 238))
        WIN.blit(TEXT_FONT.render("Congratulations", 1, (0, 0, 0)), (WIDTH // 2 - 175, 100))
        WIN.blit(TEXT_FONT.render("You survived school!", 1, (0, 0, 0)), (WIDTH // 2 - 225, 300))
    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 + 130, 400, 70))
    pygame.draw.rect(WIN, (230, 239, 255), pygame.Rect(WIDTH // 2 - 195, HEIGHT // 2 + 135, 390, 60))
    WIN.blit(MEDIUM_FONT.render("Menu", 1, (0, 0, 0)), (WIDTH // 2 - 45, HEIGHT // 2 + 140))
    pygame.display.update()

def draw_game_screen(student):
    WIN.fill((242, 237, 255))
    prompt = prompts["schoolwork"][0]
    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(WIDTH // 4 - 105, HEIGHT // 4 + 45, 510, 210))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(WIDTH // 4 - 100, HEIGHT // 4 + 50, 500, 200))
    display_text(TEXT_FONT, prompt.name, (WIDTH // 2, HEIGHT // 2 - 10), (0, 0, 0))

    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(WIDTH // 2 - 260, HEIGHT - 260, 220, 100))
    pygame.draw.rect(WIN, (237, 255, 238), pygame.Rect(WIDTH // 2 - 255, HEIGHT - 255, 210, 90))
    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(WIDTH - 260, HEIGHT - 260, 220, 100))
    pygame.draw.rect(WIN, (237, 255, 238), pygame.Rect(WIDTH - 255, HEIGHT - 255, 210, 90))
    display_text(MEDIUM_FONT, prompt.opt1.name, (WIDTH // 2 - 150, HEIGHT - 190), (0, 0, 0))
    display_text(MEDIUM_FONT, prompt.opt2.name, (WIDTH - 150, HEIGHT - 190), (0, 0, 0))

    WIN.blit(SMALL_FONT.render("HEALTH:", 1, (0, 0, 0)), (40, 25))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(220, 30, 350, 30))
    pygame.draw.rect(WIN, (149, 255, 112), pygame.Rect(220, 30, (350 * (student.health / student.maxes["health"])) // 1, 30))

    WIN.blit(SMALL_FONT.render("STRESS:", 1, (0, 0, 0)), (40, 75))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(220, 80, 350, 30))
    pygame.draw.rect(WIN, (255, 120, 120), pygame.Rect(220, 80, (350 * (student.stress / student.maxes["stress"])) // 1, 30))

    WIN.blit(SMALL_FONT.render("SMARTS:", 1, (0, 0, 0)), (40, 125))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(220, 130, 350, 30))
    pygame.draw.rect(WIN, (120, 125, 255), pygame.Rect(220, 130, (350 * (student.smarts / student.maxes["smarts"])) // 1, 30))

    WIN.blit(SMALL_FONT.render("HAPPINESS:", 1, (0, 0, 0)), (40, 175))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(220, 180, 350, 30))
    pygame.draw.rect(WIN, (255, 242, 120), pygame.Rect(220, 180, (350 * (student.happiness / student.maxes["happiness"])) // 1, 30))

    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(WIDTH//2 - 55, HEIGHT - 95, 110, 60))
    pygame.draw.rect(WIN, (253, 255, 209), pygame.Rect(WIDTH//2 - 50, HEIGHT - 90, 100, 50))
    WIN.blit(SMALL_FONT.render("PAUSE", 1, (0, 0, 0)), (WIDTH // 2 - 40, HEIGHT - 85))
    pygame.display.update()

#run game
def main():
    student = Student("uni")
    student.health = 0
    state = 'pause'
    run = True
    while run:

        #display game screen
        if state == 'menu':
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if WIDTH // 2 - 75 <= mouse[0] <= WIDTH // 2 + 75 and HEIGHT // 2 - 20 <= mouse[1] <= HEIGHT // 2 + 50:
                        state = 'select'
                mouse = pygame.mouse.get_pos()
            draw_menu_screen()

        elif state == 'select':
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if WIDTH // 2 - 200 <= mouse[0] <= WIDTH // 2 + 200 and HEIGHT // 2 - 20 <= mouse[1] <= HEIGHT // 2 + 50:
                        student = Student("high")
                        state = 'play'
                    if WIDTH // 2 - 200 <= mouse[0] <= WIDTH // 2 + 200 and HEIGHT // 2 + 100 <= mouse[1] <= HEIGHT // 2 + 170:
                        student = Student("uni")
                        state = 'play'
                mouse = pygame.mouse.get_pos()
            draw_select_screen()

        elif state == 'play':
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if WIDTH//2 - 55 <= mouse[0] <= WIDTH//2 + 55 and HEIGHT - 95 <= mouse[1] <= HEIGHT - 35:
                        state = 'pause'
                mouse = pygame.mouse.get_pos()
            draw_game_screen(student)

        elif state == 'pause':
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if WIDTH // 2 - 75 <= mouse[0] <= WIDTH // 2 + 75 and HEIGHT // 2 - 20 <= mouse[1] <= HEIGHT // 2 + 50:
                        state = 'select'
                mouse = pygame.mouse.get_pos()
            draw_pause_screen(student)
            
        elif state == 'end':
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if WIDTH // 2 - 75 <= mouse[0] <= WIDTH // 2 + 75 and HEIGHT // 2 - 20 <= mouse[1] <= HEIGHT // 2 + 50:
                        state = 'select'
                mouse = pygame.mouse.get_pos()
            draw_end_screen(student)

def display_text(font, phrase, center, color):
    for index, chunk in enumerate(phrase):
        text = font.render(chunk, 1, color)
        rect = text.get_rect()
        rect.center = (center[0], (center[1] - (rect.height * len(phrase)//2) + (rect.height) * index))
        WIN.blit(text, rect)

if __name__ == "__main__":
    main()

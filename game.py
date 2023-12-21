import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sankofa's Gift")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_COLOR = BLACK

# Load images
background_image = pygame.image.load("background.png")
female_player_image = pygame.image.load("female_player.png")
male_player_image = pygame.image.load("male_player.jpg")
tree_image = pygame.image.load("tree.jpg")
seed_image = pygame.image.load("seed.png")

# Initialize fonts
font = pygame.font.Font(None, 36)

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# display game instructions to user
def game_instructions():
    draw_text("Welcome to Sankofa's Gift!", FONT_COLOR, WIDTH // 4, HEIGHT // 2)
    draw_text("Press 'y' to confirm or 'n' to deny when prompted with choices.", FONT_COLOR, WIDTH // 4, HEIGHT // 2 + 50)
    draw_text("Use arrow keys for certain interactions.", FONT_COLOR, WIDTH // 4, HEIGHT // 2 + 100)
    pygame.display.flip()
    time.sleep(4)

# ask for username
def welcome():
    draw_text("Enter your name:", FONT_COLOR, WIDTH // 4, HEIGHT // 2)
    pygame.display.flip()
    time.sleep(1)
    return input()

# ask for user's gender
def ask_for_sex():
    draw_text("Choose your sex (press 'f' for female or 'm' for male):", FONT_COLOR, WIDTH // 4, HEIGHT // 2)
    pygame.display.flip()
    time.sleep(1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    return "female"
                elif event.key == pygame.K_m:
                    return "male"

# determine user's profile
def daily_life(player_name, sex):
    draw_text(f"Good morning, {player_name}!", FONT_COLOR, WIDTH // 4, HEIGHT // 2)
    if sex == "female":
        screen.blit(female_player_image, (WIDTH // 4, HEIGHT // 2 + 50))
    elif sex == "male":
        screen.blit(male_player_image, (WIDTH // 4, HEIGHT // 2 + 50))
    pygame.display.flip()
    time.sleep(2)


# begin game adventure
def explore_forest():
    draw_text("You hear about a mysterious forest. Do you want to explore it? (y/n)", FONT_COLOR, WIDTH // 4, HEIGHT // 2)
    pygame.display.flip()
    time.sleep(1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False


# build plot
def forest_encounter():
    draw_text("While exploring the forest, you encounter a wise elder.", FONT_COLOR, WIDTH // 4, HEIGHT // 2)
    pygame.display.flip()
    time.sleep(2)


# introduce a twist in storyline
def moral_dilemma():
    draw_text("The elder presents you with a magical seed. What will you do?", FONT_COLOR, WIDTH // 4, HEIGHT // 2)
    draw_text("Press '1' to plant the seed in the village center", FONT_COLOR, WIDTH // 4, HEIGHT // 2 + 50)
    draw_text("Press '2' to plant the seed in a hidden spot", FONT_COLOR, WIDTH // 4, HEIGHT // 2 + 100)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "center"
                elif event.key == pygame.K_2:
                    return "hidden"


# ending for players who make the right choice
def good_ending(player_name):
    draw_text(f"Congratulations, {player_name}! You planted the seed in the village center.", FONT_COLOR, WIDTH // 4, HEIGHT // 2)
    draw_text("The tree flourishes, bringing joy and prosperity to the entire village.", FONT_COLOR, WIDTH // 4, HEIGHT // 2 + 50)
    pygame.display.flip()
    time.sleep(4)

# ending for players who make the wrong choice
def not_so_good_ending(player_name):
    draw_text(f"Unfortunately, {player_name}, your choice has consequences.", FONT_COLOR, WIDTH // 4, HEIGHT // 2)
    draw_text("Challenges arise in the village due to your decision.", FONT_COLOR, WIDTH // 4, HEIGHT // 2 + 50)
    pygame.display.flip()
    time.sleep(4)

def main():
    game_instructions()
    player_name = welcome()
    sex = ask_for_sex()
    daily_life(player_name, sex)

    if explore_forest():
        forest_encounter()
        choice = moral_dilemma()

        if choice == "center":
            good_ending(player_name)
        elif choice == "hidden":
            not_so_good_ending(player_name)

    else:
        draw_text("You decide to stay in the village and continue with your daily activities.", FONT_COLOR, WIDTH // 4, HEIGHT // 2)
        draw_text("The game concludes with a reflection on the importance of choices.", FONT_COLOR, WIDTH // 4, HEIGHT // 2 + 50)
        pygame.display.flip()
        time.sleep(4)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


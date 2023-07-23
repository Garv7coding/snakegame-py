import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.alive = True

    def move(self, grow=False):
        if not self.alive:
            return

        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)

        # Check if the new head collides with the body or goes outside the grid
        if new_head in self.body[1:] or not (0 <= new_head[0] < GRID_WIDTH) or not (0 <= new_head[1] < GRID_HEIGHT):
            self.alive = False
            return

        self.body.insert(0, new_head)
        if not grow:
            self.body.pop()

    def change_direction(self, direction):
        if direction[0] * -1 != self.direction[0] or direction[1] * -1 != self.direction[1]:
            self.direction = direction

    def get_head(self):
        return self.body[0]

def draw_menu():
    font = pygame.font.Font(None, 36)
    title_text = font.render("Snake Game", True, WHITE)
    instruction_text = font.render("Press 'P' to Play", True, WHITE)
    instruction2_text = font.render("Press 'I' for Instructions", True, WHITE)

    window.fill(BLACK)
    window.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 50))
    window.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2))
    window.blit(instruction2_text, (WIDTH // 2 - instruction2_text.get_width() // 2, HEIGHT // 2 + 50))

    pygame.display.update()

def draw_instructions():
    font = pygame.font.Font(None, 30)
    text1 = font.render("Instructions:", True, WHITE)
    text2 = font.render("Use arrow keys to control the snake.", True, WHITE)
    text3 = font.render("Eat the red food to grow the snake.", True, WHITE)
    text4 = font.render("Avoid hitting the borders or yourself.", True, WHITE)
    text5 = font.render("Press 'P' to play the game.", True, WHITE)
    text6 = font.render("Press any other key to return to the menu.", True, WHITE)

    window.fill(BLACK)
    window.blit(text1, (WIDTH // 2 - text1.get_width() // 2, 50))
    window.blit(text2, (WIDTH // 2 - text2.get_width() // 2, 150))
    window.blit(text3, (WIDTH // 2 - text3.get_width() // 2, 200))
    window.blit(text4, (WIDTH // 2 - text4.get_width() // 2, 250))
    window.blit(text5, (WIDTH // 2 - text5.get_width() // 2, 350))
    window.blit(text6, (WIDTH // 2 - text6.get_width() // 2, 400))

    pygame.display.update()

# Initialize the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def main():
    menu = True
    game = False

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game = True
                    menu = False
                elif event.key == pygame.K_i:
                    draw_instructions()
                    waiting = True
                    while waiting:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                waiting = False
                    draw_menu()

        draw_menu()

    snake = Snake()
    food = [(random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))]

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))

        if snake.get_head() == food[0]:
            food[0] = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            snake.move(grow=True)
        else:
            snake.move()

        if not snake.alive:  # Check if the snake is not alive (game over)
            pygame.time.delay(1000)  # Pause for 1 second before quitting
            pygame.quit()
            quit()

        window.fill(BLACK)

        for segment in snake.body:
            pygame.draw.rect(window, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.draw.rect(window, RED, (food[0][0] * GRID_SIZE, food[0][1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

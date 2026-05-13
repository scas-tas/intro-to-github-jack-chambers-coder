"""
OOP Snake Game - Lesson 3: Abstraction & Multiple Objects
Demonstrates: abstraction, encapsulation, multiple class instances
"""


import pygame
import sys
import random

class Wall:
   """
   Represents food that the snake can eat.
  
   Demonstrates ABSTRACTION: randomize_position() hides the complex
   grid-aligned random positioning logic.
  
   This is a SEPARATE OBJECT from Snake - demonstrates creating multiple
   instances of different classes that interact.
   """
  
   def __init__(self, width, height):
       """
       Initialize food at a random position.
      
       Args:
           width: game window width
           height: game window height
       """
       self.size = 10
       self.length = 5
       # Calculate random position aligned to grid
       # (width - size) // size gives number of possible grid positions
       # Multiply by size to convert grid position back to pixel coordinates
       self.position = (random.randint(0, (width - self.size) // self.size) * self.size,
                       random.randint(0, (height - self.size) // self.size) * self.size)
  
   def spawn(self, width, height):
       """
       Move food to a new random position.
      
       ABSTRACTION: Simple method name hides grid alignment calculations.
       External code just calls spawn() - doesn't need to know the math.
      
       Args:
           width: game window width 
           height: game window height
       """
       self.position = (random.randint(0, (width - self.size) // self.size) * self.size,
                       random.randint(0, (height - self.size) // self.size) * self.size)
  
   def draw(self, surface):
       """
       Render the food on the given pygame surface.
      
       ENCAPSULATION: Food knows how to draw itself.
      
       Args:
           surface: pygame Surface to draw on
       """
       pygame.draw.rect(surface, (119, 111, 27),
                       pygame.Rect(self.position[0], self.position[1], self.size, self.size))


class Snake:
   """
   Represents the player-controlled snake.
  
   Demonstrates ENCAPSULATION: bundles snake data (body, direction) with
   snake behavior (move, grow, collision detection).
  
   Demonstrates ABSTRACTION: hides complex collision logic behind simple
   method names like check_collision().
   """
  
   def __init__(self):
       """
       Initialize the snake with default starting state.
      
       Instance variables:
       - size: dimensions of each snake segment (10x10 pixels)
       - body: list of (x, y) tuples representing snake segments
       - direction: current movement direction
       - change_to: pending direction change (prevents instant reversal)
       """
       self.size = 10
       self.body = [(100, 50), (90, 50), (80, 50)]  # Head at index 0
       self.direction = 'RIGHT'
       self.change_to = self.direction  # Buffer for direction changes
       self.colour = (0, 255, 0)  # default green
  
   def change_direction(self):
       """
       Update direction if the change is valid (not reversing into self).
      
       ABSTRACTION: External code just sets change_to; this method handles
       the complex logic of checking if the direction change is allowed.
      
       Uses any() with tuple of conditions to check all valid transitions.
       Prevents snake from immediately reversing (e.g., RIGHT → LEFT).
       """
       if any((self.change_to == 'UP' and not self.direction == 'DOWN',
               self.change_to == 'DOWN' and not self.direction == 'UP',
               self.change_to == 'LEFT' and not self.direction == 'RIGHT',
               self.change_to == 'RIGHT' and not self.direction == 'LEFT')):
           self.direction = self.change_to
  
   def move(self):
       """
       Move the snake one step in its current direction.
      
       ENCAPSULATION: Movement logic is bundled with the snake's data.
       External code doesn't need to know how the snake moves, just calls move().
      
       Algorithm:
       1. Get current head position
       2. Calculate new head position based on direction
       3. Add new head to front of body
       4. Remove tail (keeps snake same length unless growing)
       """
       x, y = self.body[0]  # Current head position
      
       # Calculate new head position (move by self.size pixels)
       if self.direction == 'UP':
           y -= self.size
       elif self.direction == 'DOWN':
           y += self.size
       elif self.direction == 'LEFT':
           x -= self.size
       elif self.direction == 'RIGHT':
           x += self.size
      
       # Update body: new head at front, remove tail
       self.body = [(x, y)] + self.body[:-1]
  
   def grow(self):
       """
       Increase snake length by one segment.
      
       ABSTRACTION: Simple interface hides implementation detail.
       Just appends a copy of the tail - when move() runs next, this
       segment stays in place while a new head is added.
       """
       self.body.append(self.body[-1])
  
   def change_colour(self):
    self.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
           


   def draw(self, surface):
       """
       Render the snake on the given pygame surface.
      
       ENCAPSULATION: Snake knows how to draw itself.
      x
       Args:
           surface: pygame Surface to draw on
       """
       for segment in self.body:
           pygame.draw.rect(surface, self.colour,
                          pygame.Rect(segment[0], segment[1], self.size, self.size))
  
   def check_collision(self, width, height):
       """
       Check if snake has collided with walls or itself.
      
       ABSTRACTION: Complex collision logic hidden behind simple method.
       External code just calls this and gets True/False - doesn't need
       to know how collision detection works.
      
       Args:
           width: game window width
           height: game window height
          
       Returns:
           True if collision detected, False otherwise
       """
       x, y = self.body[0]  # Head position
      
       # Check wall collision
       if x < 0 or x >= width or y < 0 or y >= height:
           return True
      
       # Check self-collision (head touching any other body segment)
       if (x, y) in self.body[1:]:
           return True
      
       return False




class Food:
   """
   Represents food that the snake can eat.
  
   Demonstrates ABSTRACTION: randomize_position() hides the complex
   grid-aligned random positioning logic.
  
   This is a SEPARATE OBJECT from Snake - demonstrates creating multiple
   instances of different classes that interact.
   """
  
   def __init__(self, width, height):
       """
       Initialize food at a random position.
      
       Args:
           width: game window width
           height: game window height
       """
       self.size = 10
       # Calculate random position aligned to grid
       # (width - size) // size gives number of possible grid positions
       # Multiply by size to convert grid position back to pixel coordinates
       self.position = (random.randint(0, (width - self.size) // self.size) * self.size,
                       random.randint(0, (height - self.size) // self.size) * self.size)
  
   def spawn(self, width, height):
       """
       Move food to a new random position.
      
       ABSTRACTION: Simple method name hides grid alignment calculations.
       External code just calls spawn() - doesn't need to know the math.
      
       Args:
           width: game window width 
           height: game window height
       """
       self.position = (random.randint(0, (width - self.size) // self.size) * self.size,
                       random.randint(0, (height - self.size) // self.size) * self.size)
  
   def draw(self, surface):
       """
       Render the food on the given pygame surface.
      
       ENCAPSULATION: Food knows how to draw itself.
      
       Args:
           surface: pygame Surface to draw on
       """
       pygame.draw.rect(surface, (255, 0, 0),
                       pygame.Rect(self.position[0], self.position[1], self.size, self.size))




def game_loop():
   """
   Main game loop - handles initialization, event processing, and game logic.
  
   Demonstrates using MULTIPLE OBJECTS:
   - snake: instance of Snake class
   - food: instance of Food class
  
   These are separate objects with their own data and methods.
   """
   # Initialize pygame and create window
   pygame.init()
   width, height = 640, 480
   window = pygame.display.set_mode((width, height))
   pygame.display.set_caption("Snake Game")
   clock = pygame.time.Clock()
  
   # Create game objects - two separate instances
   snake = Snake()          # Snake object
   food = Food(width, height)  # Food object
   wall = Wall(width, height)
  
   # Game state
   score = 0
   font = pygame.font.SysFont('Arial', 24)
  
   # Main game loop
   while True:
       # Event handling
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           elif event.type == pygame.KEYDOWN:
               # Set pending direction change (actual change happens in snake.change_direction())
               if event.key == pygame.K_UP or event.key == pygame.K_w:
                   snake.change_to = 'UP'
               elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                   snake.change_to = 'DOWN'
               elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                   snake.change_to = 'LEFT'
               elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                   snake.change_to = 'RIGHT'
      
       # Update snake direction and position
       snake.change_direction()
       snake.move()
      
       # Check for food collision
       if snake.body[0] == food.position:
           snake.grow()        # Make snake longer
           food.spawn(width, height)  # Move food to new position
           score += 1
           snake.change_colour()
        
       if snake.body[0] == wall.position:
           pygame.quit()
           sys.exit()
      
       # Check for game over (wall or self collision)
       if snake.check_collision(width, height):
           pygame.quit()
           sys.exit()
      
       # Render everything
       window.fill((0, 0, 0))  # Clear screen
       snake.draw(window)      # Snake draws itself
       food.draw(window)   
       wall.draw(window)    # Food draws itself
      
       # Draw score
       score_text = font.render(f'Score: {score}', True, (255, 255, 255))
       window.blit(score_text, (10, 10))
      
       pygame.display.flip()   # Update display
       keys = pygame.key.get_pressed() 
       clock.tick(30 if keys[pygame.K_SPACE] else 15)




if __name__ == "__main__":
   game_loop()

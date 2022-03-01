import pygame
import colors

from paddle import Paddle
from ball import Ball


pygame.init()

# Open a window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Font for text
font = pygame.font.Font(None, 74)

# Create the paddles A and B, like players
paddleA = Paddle(colors.WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(colors.WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

# Create a ball
ball = Ball(colors.WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# Create the storage for sprites
all_sprites_list = pygame.sprite.Group()

# Add paddles and ball to storage
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

quit_game = False

clock = pygame.time.Clock()

# Score
scoreA = 0
scoreB = 0
games_counter = 0


# Pause the game
def pause_game():
    status = True
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    quit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    status = False

        pygame.draw.rect(screen, colors.WHITE, (250, 345, 191, 60))
        pygame.draw.rect(screen, colors.GRAY, (250, 345, 191, 60), 3)
        text = font.render(str("Paused"), True, colors.RED)
        screen.blit(text, (255, 350))

        pygame.display.flip()
        clock.tick(15)


# New game
def new_game():
    status = True
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    quit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    status = False

        pygame.draw.rect(screen, colors.WHITE, (90, 345, 535, 60))
        pygame.draw.rect(screen, colors.GRAY, (90, 345, 535, 60), 3)
        text = font.render(str("Press 'SPACE' to play"), True, colors.RED)
        screen.blit(text, (95, 350))

        pygame.display.flip()
        clock.tick(15)


# Start new game
new_game()

# Game main loop
while not quit_game:
    # If player press X or close the window game will close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                quit_game = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE :
                pause_game()

    # Moving the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.move_up(5)
    if keys[pygame.K_s]:
        paddleA.move_down(5)
    if keys[pygame.K_UP]:
        paddleB.move_up(5)
    if keys[pygame.K_DOWN]:
        paddleB.move_down(5)

    all_sprites_list.update()

    # Moving the ball and adding points
    # If ball touches the bound add point to opponent and replace ball to start
    if ball.rect.x >= 690:
        scoreA += 1
        ball.rect.x = 345
        ball.rect.y = 195
    if ball.rect.x <= 0:
        scoreB += 1
        ball.rect.x = 345
        ball.rect.y = 195
    if scoreA == 10 or scoreB == 10:
        new_game()
        # Restart Score and Ball
        scoreA, scoreB = 0, 0
        ball.rect.x = 345
        ball.rect.y = 195
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 70:
        ball.velocity[1] = -ball.velocity[1]

    # Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    screen.fill(colors.BLACK)
    # Draw the GUI
    pygame.draw.line(screen, colors.WHITE, [349, 0], [349, 500], 5)
    pygame.draw.line(screen, colors.WHITE, [700, 70], [0, 70], 5)
    # Draw all the objects
    all_sprites_list.draw(screen)
    # Display the score
    text = font.render(str(scoreA), True, colors.WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), True, colors.WHITE)
    screen.blit(text, (420, 10))

    # Update the screen when everything is drawn
    pygame.display.flip()
    # FPS
    clock.tick(60)

pygame.quit()

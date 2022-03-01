import pygame
import colors


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(colors.BLACK)
        self.image.set_colorkey(colors.BLACK)
        # draw the paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def move_up(self, pixels):
        self.rect.y -= pixels
        # Screen out of bounds check
        if self.rect.y < 70:
            self.rect.y = 70

    def move_down(self, pixels):
        self.rect.y += pixels
        # Screen out of bounds check
        if self.rect.y > 400:
            self.rect.y = 400

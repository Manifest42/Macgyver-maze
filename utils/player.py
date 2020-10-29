import pygame


class Player(pygame.sprite.Sprite):
    """
    Loads image of the player
    """
    image = None
    rect = None
    screen = None

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('ressource/macgyver2.png').convert()
        # scale player image
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        # player starting location
        self.rect.centerx = 200
        self.rect.bottom = 200

        # other player attributes
        self.changex = 0
        self.changey = 0

    def move_left(self) -> None:
        '''move player left'''
        self.changex -= 30

    def move_right(self) -> None:
        '''move player right'''
        self.changex += 30

    def move_down(self) -> None:
        '''move player left'''
        self.changey += 30

    def move_up(self) -> None:
        '''move player right'''
        self.changey -= 30

    def update(self) -> None:
        # make player static in screen by default
        self.rect.x += self.changex
        self.rect.y += self.changey
        self.changex = 0
        self.changey = 0
        '''boundary checking'''
        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.y < 0:
            self.rect.y = 0

        if self.rect.x > 500 - self.rect.width:
            self.rect.x = 500 - self.rect.width

        if self.rect.y > 500 - self.rect.height:
            self.rect.y = 500 - self.rect.height

import pygame


class NonPlayerSprite(pygame.sprite.Sprite):
    """
    Loads images of the guard and objects
    """
    image = None
    rect = None
    screen = None

    def __init__(self, image: str, position: tuple) -> None:
        super().__init__()
        self.image = pygame.image.load('ressource/' + image).convert()
        # scale image
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        # starting location
        self.rect.centerx, self.rect.bottom = position

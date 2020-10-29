import pygame


class Labyrinthtile:
    """
    Loads images of the path and walls of the labyrinth
    """
    def __init__(self, filename: str):
        self.sheet = pygame.image.load(filename).convert()

    def image_at(self, rectangle: tuple) -> None:
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        image = pygame.transform.scale(image, (30, 30))
        return image

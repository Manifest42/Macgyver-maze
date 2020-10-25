import pygame


class Labyrinthtiles(object):
    def __init__(self, filename: str):
        self.sheet = pygame.image.load(filename).convert()

    def image_at(self, rectangle: tuple) -> None:
        """
        Loads image from x, y, x+offset, y+offset
        :param rectangle: format -> (x, y, offset_x, offset_y)
        """
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        image = pygame.transform.scale(image, (30, 30))
        return image

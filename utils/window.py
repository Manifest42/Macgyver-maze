import pygame
from utils.player import Player
from utils.labyrinthtiles import Labyrinthtiles
from utils.nonplayersprites import NonPlayerSprites


class Window:
    screen = None
    all_active_sprites = None

    def __init__(self, labyrinth) -> None:
        self.labyrinth = labyrinth
        pygame.init()
        size = 500, 500
        self.FPSCLOCK = pygame.time.Clock()  # frames per unit of time
        self.screen = pygame.display.set_mode(size)
        self.all_active_sprites = pygame.sprite.Group()
        self.player = Player()
        self.guardian = NonPlayerSprites('guard2.png', (0, 0))
        self.aiguille = NonPlayerSprites('aiguille.png', (0, 0))
        self.tube_plastique = NonPlayerSprites('tube_plastique.png', (0, 0))
        self.ether = NonPlayerSprites('ether.png', (0, 0))
        self.seringue = NonPlayerSprites('seringue.png', (0, 0))
        self.all_active_sprites.add(self.player,
                                    self.guardian,
                                    self.aiguille,
                                    self.tube_plastique,
                                    self.ether
                                    )
        # Load the terrain tiles
        self.tiles = Labyrinthtiles
        self.floor = pygame.image.load("ressource/path2.png")
        self.wall = pygame.image.load("ressource/wall.png")

    @staticmethod
    def text_objects(text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()

    def message_display(self, text):
        largeText = pygame.font.Font('freesansbold.ttf', 60)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = (250, 250)
        self.all_active_sprites = pygame.sprite.Group()
        self.screen.fill((0, 0, 0))
        self.screen.blit(TextSurf, TextRect)
        pygame.display.update()

    def refresh(self) -> None:
        self.all_active_sprites.update()
        self.screen.fill((0, 0, 0))
        for index_y, line in enumerate(self.labyrinth.layout):
            for index_x, column in enumerate(line):
                if column.lower() == 'x':
                    self.screen.blit(self.wall, (index_x * 30, index_y * 30))
                elif column == ' ':
                    self.screen.blit(self.floor, (index_x * 30, index_y * 30))
                elif column.lower() == "p":
                    self.player.rect.left = index_x * 30
                    self.player.rect.top = index_y * 30
                elif column.lower() == "e":
                    self.guardian.rect.left = index_x * 30
                    self.guardian.rect.top = index_y * 30
                elif column.lower() == "0":
                    self.aiguille.rect.left = index_x * 30
                    self.aiguille.rect.top = index_y * 30
                elif column.lower() == "1":
                    self.tube_plastique.rect.left = index_x * 30
                    self.tube_plastique.rect.top = index_y * 30
                elif column.lower() == "2":
                    self.ether.rect.left = index_x * 30
                    self.ether.rect.top = index_y * 30
        self.all_active_sprites.draw(self.screen)
        pygame.display.update()
        self.FPSCLOCK.tick(30)  # for each second at most 30 frames should pass

# Em desenvolvimento
import pygame
# Valores recomendados
LARGURA = 1280          # 1280
ALTURA = 720            # 720
FPS = 60                # 60
ESCALA = 2              # 2
TILESIZE = 16 * ESCALA  # 16 * ESCALA

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, surface, inflate_x=-8, inflate_y=-10, extend = 0):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)
        #reajuste do hitbox
        self.rect.width += extend
        self.hitbox = self.rect.inflate(inflate_x, inflate_y)
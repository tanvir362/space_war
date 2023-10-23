import math
import pygame
from os.path import join


def normalize_angle(angle):
    angle = angle % 360  # Convert angle to equivalent angle within 360 degrees
    if angle > 180:
        angle -= 360  # Subtract 360 to get the angle within the range of -180 to 180
    return angle

class SpaceShip:
    WIDTH, HEIGHT = 32, 32
    ROTATION_UNIT = 5
    count = 0

    def __init__(self, x, y, no=1):
        self.x = x
        self.y = y
        self.ang = 0 if no==1 else 180
        self.vx = 0
        self.vy = 0

        self.id = SpaceShip.count
        SpaceShip.count += 1

        self.clean_img = pygame.transform.scale(
            pygame.transform.rotate(
                pygame.image.load(join('assets', f"rocket{no}.png")).convert_alpha(),
                -90 if no==1 else 90
            ),
            (SpaceShip.WIDTH, SpaceShip.HEIGHT)
        )
        self._img = self.clean_img.copy()
        self._img_rect = self._img.get_rect(center=(self.x, self.y))


    def apply_thrust(self, a):
        ax = a*math.cos(math.radians(self.ang))
        ay = a*math.sin(math.radians(-self.ang))
        # print('angle', self.ang, 'a', a, 'ax', ax, 'ay', ay)

        self.vx += ax
        self.vy += ay

    def move(self):
        self.x += self.vx
        self.y += self.vy

        self.x %= 901
        self.y %= 701

        self._img_rect.center = (self.x, self.y)

    # dir: 1 means anti clock, -1 means clock
    def rotate(self, dir):
        self.ang += dir*SpaceShip.ROTATION_UNIT
        self.ang = normalize_angle(self.ang)

        self._img = pygame.transform.rotate(self.clean_img, self.ang)
        self._img_rect = self._img.get_rect(center=(self.x, self.y))


    def draw(self, surface:pygame.Surface):
        
        surface.blit(self._img, self._img_rect)
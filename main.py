import pygame
from space_ship import SpaceShip


WIDTH, HEIGHT = 900, 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space War")


def main():
    clock = pygame.time.Clock()
    space_ship1 = SpaceShip(100, 100, 1)

    run = True
    while run:
        clock.tick(FPS)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_w:
            #         space_ship1.apply_thrust(1)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a]:
            space_ship1.rotate(1)

        if key_pressed[pygame.K_d]:
            space_ship1.rotate(-1)

        if key_pressed[pygame.K_w]:
            space_ship1.apply_thrust(0.1)
        
        space_ship1.move()
        space_ship1.draw(screen)



        pygame.display.update()


    pygame.quit()


if __name__ == '__main__':
    main()
import pygame
from spaceship import Spaceship
from game_properties import HEIGHT, WIDTH, BLACK, WHITE, FPS



pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space War")


def main():
    clock = pygame.time.Clock()
    space_ship1 = Spaceship(100, 100, 1)
    space_ship2 = Spaceship(WIDTH-100, HEIGHT-100, 2)

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

        if key_pressed[pygame.K_LEFT]:
            space_ship2.rotate(1)

        if key_pressed[pygame.K_RIGHT]:
            space_ship2.rotate(-1)

        if key_pressed[pygame.K_UP]:
            space_ship2.apply_thrust(0.1)
        
        space_ship1.move()
        space_ship2.move()

        space_ship1.draw(screen)
        space_ship2.draw(screen)

        space_ship1.handle_collision(space_ship2)
        


        pygame.display.update()


    pygame.quit()


if __name__ == '__main__':
    main()
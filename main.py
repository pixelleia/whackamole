import pygame, sys
import random

def draw_grid(screen, color):
    screen.fill("light green")
    for i in range(1, 21):
        pygame.draw.line(screen, color, (0, i * 32), (640, i * 32))
    for i in range(1, 21):
        pygame.draw.line(screen, color, (i * 32, 0), (i * 32, 640))

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        #screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        color = (255,255,245)

        draw_grid(screen, color)

        mole_rect = mole_image.get_rect(topleft=(0,0))

        screen.blit(mole_image, mole_rect)



        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #i,j = event.pos
                    #print(f"mouse: {i}, {j} ... image: {mole_rect.x}, {mole_rect.y}")
                    #if mole_rect.collidepoint(event.pos):
                        #draw_grid(screen, color)
                    x = random.randrange(0, 20)  * 32
                    y = random.randrange(0, 16) * 32
                    mole_rect = mole_image.get_rect(topleft=(x, y))
                    screen.blit(mole_image, mole_rect)

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
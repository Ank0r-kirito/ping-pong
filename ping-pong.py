import pygame


WIN_WIDTH, WIN_HEIGHT = 600, 500
BACKGROUND = (80, 150, 255)
FPS = 60
RACKET_WIDTH, RACKET_HEIGHT = 50, 150
BALL_SIZE = 50
PLAYER_SPEED = 4
BALL_SPEED_X, BALL_SPEED_Y = 3, 3
FONT_SIZE = 35

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, speed, width, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_path), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)


class Player(GameSprite):
    def update(self, up_key, down_key, limit_top, limit_bottom):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.y > limit_top:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.y < limit_bottom - RACKET_HEIGHT:
            self.rect.y += self.speed

pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('CS 2')
clock = pygame.time.Clock()

racket1 = Player('racket.png',
                30,
                (WIN_HEIGHT - RACKET_HEIGHT) // 2,
                PLAYER_SPEED,
                RACKET_WIDTH,
                RACKET_HEIGHT
                )

racket2 = Player('racket.png', 
                WIN_WIDTH - (RACKET_WIDTH + 30),
                (WIN_HEIGHT - RACKET_HEIGHT) // 2,
                PLAYER_SPEED,
                RACKET_WIDTH,
                RACKET_HEIGHT
                )

ball = GameSprite('tenis_ball.png',
                 WIN_WIDTH // 2 - BALL_SIZE // 2,
                 WIN_HEIGHT // 2 - BALL_SIZE // 2,
                 0,
                 BALL_SIZE,
                 BALL_SIZE
                 )

game = True
finish = False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if not finish:
        window.fill(BACKGROUND)

        racket1.update(pygame.K_w, pygame.K_s, 5, WIN_HEIGHT)
        racket2.update(pygame.K_UP, pygame.K_DOWN, 5, WIN_HEIGHT)

        racket1.draw(window)
        racket2.draw(window)
        ball.draw(window)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
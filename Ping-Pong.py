import pygame
import sys
import random

# Настройки игры
WIDTH, HEIGHT = 1300, 800
PADDLE_SPEED = 8
BALL_SPEED = 7


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Мой Ping Pong")
clock = pygame.time.Clock()

# Загрузка и уменьшение спрайтов
try:
   
    original_paddle = pygame.image.load("paddle.png").convert_alpha()
    original_ball = pygame.image.load("ball.png").convert_alpha()
    
    
    paddle_img = pygame.transform.scale(original_paddle, 
                                      (original_paddle.get_width()//4, 
                                       original_paddle.get_height()//4))
    ball_img = pygame.transform.scale(original_ball, 
                                    (original_ball.get_width()//10, 
                                     original_ball.get_height()//10))
except:
    print("Ошибка загрузки спрайтов! Убедитесь, что файлы paddle.png и ball.png находятся в той же папке")
    sys.exit()

# Создание объектов
player1 = paddle_img.get_rect(left=10, centery=HEIGHT//2)  # Левая ракетка у края
player2 = paddle_img.get_rect(right=WIDTH-10, centery=HEIGHT//2)  # Правая ракетка у края
ball = ball_img.get_rect(center=(WIDTH//2, HEIGHT//2))

ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += PADDLE_SPEED
    
    # Движение мяча
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Отскоки от стен
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    
    
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1
    
   
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x = BALL_SPEED * random.choice((1, -1))
        ball_speed_y = BALL_SPEED * random.choice((1, -1))
    
    
    screen.fill((255, 255, 255))  # Белый фон
    screen.blit(paddle_img, player1)
    screen.blit(paddle_img, player2)
    screen.blit(ball_img, ball)
    
    pygame.display.flip()
    clock.tick(60)
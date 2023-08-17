#自機と1つの敵だけがいて、どちらかに弾が当たるとゲームオーバーの簡単なゲームを作りたいです。方針を教えてください。
#ふらふらと動く敵を表示したいです
import pygame
import random
import sys

# ゲームの設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# 色の定義
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
   def __init__(self):
       super().__init__()
       self.image = pygame.Surface((50, 50))
       self.image.fill(BLUE)  # 青の四角形
       self.rect = self.image.get_rect()
       self.rect.centerx = SCREEN_WIDTH // 2
       self.rect.bottom = SCREEN_HEIGHT - 10
       self.speed = 5

   def update(self):
       # プレイヤーの移動などの更新処理
       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT]:
           self.rect.x -= self.speed
       if keys[pygame.K_RIGHT]:
           self.rect.x += self.speed

class Enemy(pygame.sprite.Sprite):
   def __init__(self):
       super().__init__()
       self.image = pygame.Surface((50, 50))
       self.image.fill(RED)  # 赤の四角形
       self.rect = self.image.get_rect()
       self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)  # X座標をランダムに設定
       self.rect.y = 10
       self.speed = random.randint(1, 3)  # 移動速度をランダムに設定
       self.direction = random.choice([-1, 1])  # 移動方向をランダムに設定

   def update(self):
       # 敵の移動などの更新処理
       self.rect.x += self.speed * self.direction
       if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
           self.direction *= -1

class Bullet(pygame.sprite.Sprite):
   def __init__(self, x, y):
       super().__init__()
       self.image = pygame.Surface((10, 10))
       self.image.fill(WHITE)  # 白の四角形
       self.rect = self.image.get_rect()
       self.rect.centerx = x
       self.rect.centery = y
       self.speed = 10

   def update(self):
       # 弾の移動などの更新処理
       self.rect.y -= self.speed
       if self.rect.bottom < 0:
           self.kill()

def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   pygame.display.set_caption("シューティングゲーム")
   clock = pygame.time.Clock()

   player = Player()
   enemies = pygame.sprite.Group()

   all_sprites = pygame.sprite.Group()
   all_sprites.add(player)

   for _ in range(5):  # 5つの敵を生成
       enemy = Enemy()
       enemies.add(enemy)
       all_sprites.add(enemy)

   bullets = pygame.sprite.Group()

   game_over = False

   while not game_over:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                   bullet = Bullet(player.rect.centerx, player.rect.top)
                   bullets.add(bullet)
                   all_sprites.add(bullet)

       all_sprites.update()

       # 衝突判定
       if pygame.sprite.spritecollide(player, bullets, False):
           game_over = True
       if pygame.sprite.spritecollide(enemy, bullets, True):
           game_over = True

       screen.fill((0, 0, 0))  # 背景色を黒に設定
       all_sprites.draw(screen)

       pygame.display.flip()
       clock.tick(FPS)

   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

       # ゲームオーバー画面の表示
       font = pygame.font.Font(None, 36)
       text = font.render("Game Over", True, WHITE)
       text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
       screen.fill((0, 0, 0))
       screen.blit(text, text_rect)
       pygame.display.flip()

if __name__ == "__main__":
   main()

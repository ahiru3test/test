#ここにgtpへの指示を残す。↓にgtpのコードを張り付け。修正はコメント化？
#pygameで自分と敵が殴りあう格闘ゲームを作りたいです。


###1.Pygameのセットアップ:
import pygame
import random
import os

# Pygameの初期化
pygame.init()

# ゲームウィンドウのサイズ
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("格闘ゲーム")

###2.キャラクターの作成:
class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        
    def update(self):
        # キャラクターの移動などの更新処理
        pass

###2.1 add
# キャラクターの作成
player = Character(100, 200, os.path.join("gtp_etc", "player.png"))
enemy = Character(500, 200, os.path.join("gtp_etc", "enemy.png"))

###3.ゲームループの作成:
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)  # フレームレートを60に設定
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キャラクターの移動範囲の制約
    if player.rect.x < 0:
        player.rect.x = 0
    if player.rect.x > screen_width - player.rect.width:
        player.rect.x = screen_width - player.rect.width
    if player.rect.y < 0:
        player.rect.y = 0
    if player.rect.y > screen_height - player.rect.height:
        player.rect.y = screen_height - player.rect.height

    enemy_min_x = 0
    enemy_max_x = screen_width - enemy.rect.width

    # キーボード入力の処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= player.speed
    if keys[pygame.K_RIGHT]:
        player.rect.x += player.speed
    if keys[pygame.K_UP]:
        player.rect.y -= player.speed
    if keys[pygame.K_DOWN]:
        player.rect.y += player.speed

    # キャラクターの更新
    player.update()
    enemy.update()

    # ゲームループ内の適当な場所で敵キャラクターの座標を更新する
    if random.random() < 0.01:  # 1%の確率で座標を変更する例
        # 敵キャラクターの移動方向をランダムに選択（左: -1、右: 1）
        direction = random.choice([-1, 1])
        
        # 現在の座標に移動方向を加えて新しい座標を計算
        new_x = enemy.rect.x + direction * enemy.speed
        
        # 移動範囲の制約を適用
        new_x = max(enemy_min_x, min(new_x, enemy_max_x))
        
        # 新しい座標をセット
        enemy.rect.x = new_x

    # 衝突判定などのゲームロジック
    # ...
    
    # 画面の描画
    screen.fill((0, 0, 0))  # 黒で画面をクリア
    screen.blit(player.image, player.rect)
    screen.blit(enemy.image, enemy.rect)
    pygame.display.flip()

pygame.quit()

###4.キーボード入力の処理:
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player.rect.x -= player.speed
if keys[pygame.K_RIGHT]:
    player.rect.x += player.speed
if keys[pygame.K_UP]:
    player.rect.y -= player.speed
if keys[pygame.K_DOWN]:
    player.rect.y += player.speed


###5.衝突判定:
if pygame.sprite.collide_rect(player, enemy):
    # 自分と敵の衝突処理
    pass



import pygame
import random

pygame.init()

# 게임 화면 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# 게임 색깔 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 블록 종류와 색깔 설정
block_list = [
    [[1, 1, 1], [0, 1, 0]], # T 모양 블록
    [[1, 1, 1, 1]], # I 모양 블록
    [[1, 1, 0], [0, 1, 1]], # Z 모양 블록
    [[0, 1, 1], [1, 1, 0]], # S 모양 블록
    [[1, 1], [1, 1]], # O 모양 블록
    [[1, 1, 1], [1, 0, 0]] # L 모양 블록
]
color_list = [RED, GREEN, BLUE, WHITE, RED, GREEN]

# 게임 변수 설정
score = 0
fall_speed = 1
font = pygame.font.Font(None, 30)


# 블록 클래스 정의
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # 랜덤한 모양의 블록 선택
        self.block_type = random.randint(0, len(block_list) - 1)
        self.block = block_list[self.block_type]

        # 블록의 색깔 설정
        self.color = color_list[self.block_type]

        # 블록의 시작 위치 설정
        self.x = screen_width // 2 - len(self.block[0]) * 20 // 2
        self.y = 0

        # 블록의 현재 회전 상태 설정
        self.rotation = 0

    def rotate(self):
        # 블록 회전 함수
        self.rotation = (self.rotation + 1) % len(self.block)

    def move_left(self):
        # 블록 왼쪽으로 이동 함수
        self.x -= 20

    def move_right(self):
        # 블록 오른쪽으로 이동 함수
        self.x += 20

    def move_down(self):
        # 블록 아래로 이동 함수
        self.y += 20

    def draw(self):
        # 블록 그리기 함수
        for i in range(len(self.block[self.rotation])):
            for j in range(len(self.block[self.rotation][i])):
                if self.block[self.rotation][i][j] == 1:
                    pygame.draw.rect(screen, self.color, [self.x + j * 20, self.y + i * 20, 20, 20])

    def update(self):
        # 블록 이동 함수
        self.move_down()
        if self.check_collision():
            self.move_up()
            self.land()

    def check_collision(self):
        # 블록 충돌 검사 함수
        for i in range(len(self.block[self.rotation])):
            for j in range(len(self.block[self.rotation][i])):
                if self.block[self.rotation][i][j] == 1:
                    if self.y + i * 20 >= screen_height:
                        return True
                    if self.x + j * 20 < 0 or self.x + j * 20 >= screen_width:
                        return True
                    if pygame.sprite.spritecollide(self, block_group, False):
                        return True
        return False

    def move_up(self):
        # 블록 위로 이동 함수
        self.y -= 20

    def land(self):
        # 블록 착지 함수
        for i in range(len(self.block[self.rotation])):
            for j in range(len(self.block[self.rotation][i])):
                if self.block[self.rotation][i][j] == 1:
                    BlockSprite(self.x + j * 20, self.y + i * 20, self.color)
        remove_full_rows()
        new_block()

# 블록 스프라이트 클래스 정의
class BlockSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()

        # 스프라이트 설정
        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # 스프라이트 그룹에 추가
        all_sprites_group.add(self

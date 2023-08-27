import random
import os
import msvcrt
import time

# 화면 설정
width, height = 20, 10

# 초기화
snake = [(width // 2, height // 2)]
food = (random.randint(1, width), random.randint(1, height))
direction = (0, -1)
score = 0
game_over = False

# 게임 루프
while not game_over:
    os.system('cls' if os.name == 'nt' else 'clear')

    # 뱀과 음식 그리기
    for y in range(height + 1):
        for x in range(width + 1):
            if (x, y) == snake[0]:
                print('H', end='')
            elif (x, y) == food:
                print('F', end='')
            elif (x, y) in snake:
                print('o', end='')
            else:
                print('.', end='')
        print()
    
    # 입력 처리
    if msvcrt.kbhit():
        key = msvcrt.getch().decode()
        if key == 'w' and direction != (0, 1):
            direction = (0, -1)
        elif key == 's' and direction != (0, -1):
            direction = (0, 1)
        elif key == 'a' and direction != (1, 0):
            direction = (-1, 0)
        elif key == 'd' and direction != (-1, 0):
            direction = (1, 0)

    # 이동 처리
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    # 충돌 체크
    if new_head == food:
        food = (random.randint(1, width), random.randint(1, height))
        score += 1
    else:
        snake.pop()

    # 벽 충돌
    if new_head[0] < 0 or new_head[0] > width or new_head[1] < 0 or new_head[1] > height:
        game_over = True

    # 뱀 몸통 충돌
    if new_head in snake[1:]:
        game_over = True

    time.sleep(0.1)

# 게임 오버 메시지 출력
os.system('cls' if os.name == 'nt' else 'clear')
print("게임 오버!")
print(f"총 점수: {score}")

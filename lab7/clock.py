import pygame
import sys
import time
import datetime

# Инициализация Pygame
pygame.init()

# Размеры экрана
size = (770, 770)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mickey Clock")

# Загрузка изображений
clock_face = pygame.image.load("mainclock.png")
left_hand = pygame.image.load("leftarm.png")
right_hand = pygame.image.load("rightarm.png")

# Переворачивание изображений для удобства поворота
left_hand = pygame.transform.rotate(left_hand, 180)
right_hand = pygame.transform.rotate(right_hand, 180)

# Функция для отрисовки часов
def draw_clock():
    screen.blit(clock_face, ((size[0] - clock_face.get_width()) / 2, (size[1] - clock_face.get_height()) / 2))

# Функция для обновления позиции стрелок
def update_hands(minute_angle, second_angle):
    min_rot = pygame.transform.rotate(left_hand, minute_angle)
    sec_rot = pygame.transform.rotate(right_hand, second_angle)

    min_pos = ((size[0] - min_rot.get_width()) / 2, (size[1] - min_rot.get_height()) / 2)
    sec_pos = ((size[0] - sec_rot.get_width()) / 2, (size[1] - sec_rot.get_height()) / 2)

    screen.blit(min_rot, min_pos)  # Левая рука показывает минуты
    screen.blit(sec_rot, sec_pos)  # Правая рука показывает секунды

# Основной цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение текущего времени
    current_time = datetime.datetime.now()
    current_time += datetime.timedelta(minutes = 31)
    minute_angle = 360 - (current_time.minute * 6)
    second_angle = 360 - (current_time.second * 6)

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Отрисовка часов и обновление позиции стрелок
    draw_clock()
    update_hands(minute_angle, second_angle)

    # Обновление экрана
    pygame.display.flip()

    # Задержка для обновления времени
    time.sleep(0.5)

# Выход из Pygame
pygame.quit()
sys.exit()
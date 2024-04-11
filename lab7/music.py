import keyboard
import pygame
import os

# Инициализация pygame
pygame.init()

# Установка директории с музыкой
current_dir = os.path.dirname(__file__)  # Получаем текущую директорию
music_dir = os.path.join(current_dir, "musics")  # Объединяем текущую директорию с папкой "musics"

# Получение списка всех музыкальных файлов в директории
music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]

# Инициализация музыкального плеера
pygame.mixer.init()

# Установка начального индекса песни
current_song_index = 0

# Функция для проигрывания текущей песни
def play_song():
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_song_index]))
    pygame.mixer.music.play()

# Функция для остановки текущей песни
def stop_song():
    pygame.mixer.music.stop()

# Функция для проигрывания следующей песни
def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_song_index]))
    pygame.mixer.music.play()

# Функция для проигрывания предыдущей песни
def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_song_index]))
    pygame.mixer.music.play()

# Установка горячих клавиш
keyboard.add_hotkey('space', play_song)
keyboard.add_hotkey('s', stop_song)
keyboard.add_hotkey('n', next_song)
keyboard.add_hotkey('p', prev_song)

# Основной цикл (выход из программы осуществляется нажатием клавиши 'q')
print("Press 'q' to quit.")
keyboard.wait('q')

# пробел - воспроивести
# s - остановить
# n - след трек
# p - пред трек
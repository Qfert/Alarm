import datetime
import time
import pygame


musick=("musick.mp3")

a=input("Введите (Ч:М)  ")
print=(f"Вы установили будильник на {a}")
while True:
 current_time=datetime.datetime.now().strftime("%H:%M")
 if current_time==a:
  break
 time.sleep(5)

 pygame.mixer.init()
 pygame.mixer.music.load(musick)
 pygame.mixer.music.play()

print("Пора")
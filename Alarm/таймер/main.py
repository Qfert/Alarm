import datetime
import time
import pygame

Tic_Tic = "zvuk-chasov.mp3"   
musick = "musick.mp3"          

a = input("Введите (Ч:М)  ")
print(f"Вы установили будильник на {a}")   

pygame.mixer.init()


pygame.mixer.music.load(Tic_Tic)
pygame.mixer.music.play(-1)   

while True:
    current_time = datetime.datetime.now().strftime("%H:%M")
    if current_time == a:
        break
    time.sleep(5)


pygame.mixer.music.stop()
pygame.mixer.music.load(musick)
pygame.mixer.music.play()

print("Пора")


while pygame.mixer.music.get_busy():
    time.sleep(1)
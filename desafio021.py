#Programa que abra e reproduza um arquivo .mp3
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('beat2.mp3')
pygame.mixer.music.play()
pygame.event.wait()



import vlc
import time
import sys
import os
import random

instance = vlc.Instance()
player = instance.media_player_new()

root = input('Enter the absolute path of the directory that has your music: ')

if (len(root) <= 1):
    root = "/home/tom/Music/pomodoro/"

while True:
    try:
        pomodoro_length = int(input('Enter the length of the Pomodoro in minutes: ')) * 60
        break
    except:
        print('You have to enter an integer. Try again')
        continue

def countdown():
    for i in range(pomodoro_length,0,-1):
        sys.stdout.write("\r")
        sys.stdout.write("Pomodoro: {:2d} seconds remaining.".format(i))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\nPomodoro Complete\n")

def focus():
    print('Pomodoro will start with random song')
    songs = [root+song for song in os.listdir(root)]
    player.set_media(instance.media_new(random.choice(songs)))
    player.play()
    countdown()

focus()

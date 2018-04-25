import vlc
import time
import sys
import os
import random

instance = vlc.Instance()
player = instance.media_player_new()
root = "/home/tom/Music/pomodoro/"

def countdown():
    for i in range(2700,0,-1):
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

import vlc
import time
import sys

instance = vlc.Instance()
player = instance.media_player_new()

working = instance.media_new("electronic.mp3")
coding = instance.media_new("soundtrack.mp3")

def countdown():
    for i in range(2700,0,-1):
        sys.stdout.write("\r")
        sys.stdout.write("Pomodoro: {:2d} seconds remaining.".format(i))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\nPomodoro Complete\n")

def focus():
    print("Are you working or coding?")
    focus = input()
    
    if focus == 'working':
        player.set_media(working)
        player.play()
        countdown()

    elif focus == 'coding':
        player.set_media(coding)
        player.play()
        countdown()
focus()

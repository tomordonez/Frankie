import vlc
import time
import sys
import os
import random

instance = vlc.Instance()
player = instance.media_player_new()

print('             ')
print('### Frankie The Pomodoro ###')
print('             ')
print('[  x  x  x  ]')
print('| ......... |')
print('|  <0 | 0>  |')
print('  *|  o  |*  ')
print('   +++++++   ')
print('     ...     ')
print('             ')

# You have to hardcode your Music root here
root = "/home/tom/Music/pomodoro/"

while True:
    try:
        pomodoro_length = int(input('Enter Pomodoro in minutes: ')) * 60
        break
    except (KeyboardInterrupt, SystemExit):
        raise
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
    songs = [root+song for song in os.listdir(root)]
    song_mode = input('Do you want a random song? (y/n): ').lower()
    while True:
        try:
            if (song_mode == 'y') or (song_mode == 'yes'):
                print('Pomodoro will start with random song')
                player.set_media(instance.media_new(random.choice(songs)))
                player.play()
                countdown()
            elif (song_mode == 'n') or (song_mode == 'no'):
                counter = 0
                for song in os.listdir(root):
                    print('#', counter, song)
                    counter += 1
                while True:
                    try:
                        song_number = int(input('Enter a song number: '))
                        player.set_media(instance.media_new(songs[song_number]))
                        player.play()
                        countdown()
                        break
                    except (KeyboardInterrupt, SystemExit):
                        raise
                    except:
                        print("Please enter a number")
                        continue
            break
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            print('Please enter y or n')
            continue

focus()

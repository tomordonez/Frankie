import vlc
import time
import sys
import os
import random

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

def validate_int(input_string):
    while True:
        try:
            validated_int = int(input(input_string))
            break
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            print("Please enter an integer")
            continue
    return validated_int

def countdown(pomodoro_length):
    print('\n{}min Pomodoro'.format(pomodoro_length))

    for i in range(pomodoro_length*60, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("Pomodoro: {:2d}s remaining.".format(i))
        sys.stdout.flush()
        time.sleep(1)
    print("\nPomodoro Complete\n")

def play_song(song_selected, pomodoro_length):
    instance = vlc.Instance()
    player = instance.media_player_new()
    
    print('Playing song: {}'.format(song_selected))
    player.set_media(instance.media_new(song_selected))
    player.play()
    countdown(pomodoro_length)

def select_song():
    pomodoro_length = validate_int('Enter Pomodoro in minutes: ')

    songs = [root+song for song in os.listdir(root)]
    print('\nChoose Song Mode')
    print('1. Random song')
    print('2. View song list')
    
    song_mode = validate_int('Enter number: ')

    if song_mode == 1:
        song_selected = random.choice(songs)
        play_song(song_selected, pomodoro_length)

    elif song_mode == 2:
        counter = 0
        for song in os.listdir(root):
            print('# {} - {}'.format(counter,song))
            counter += 1
        
        song_number = validate_int('Enter a song number: ')
                
        song_selected = songs[song_number]
        play_song(song_selected, pomodoro_length)

    else:
        sys.exit()

    return(song_mode, song_selected, pomodoro_length)

def main():
    select_song()

if __name__ == '__main__':
    main()

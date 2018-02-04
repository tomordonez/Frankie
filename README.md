# Frankie

A Pomodoro timer with Music in Python.

This pomodoro timer runs from the command line and asks you for a task. Depending on the task, a different song is played and the timer starts counting down.

## Setup

Clone:

    $ git clone https://github.com/tomordonez/Frankie.git
    $ cd Frankie

Activate a `virtualenv`:

    $ virtualenv -p /usr/bin/python3 env
    $ source env/bin/activate

Install `VLC`:

    (env) $ pip install python-vlc

## Modify the Pomodoro Timer

The timer is currently set to 45 minutes (2700 seconds). Change this to your own Pomodoro interval.

Add `mp3` songs to your directory. And change the names in the program as needed.

    working = instance.media_new("electronic.mp3")
    coding= = instance.media_new("soundtrack.mp3")

## Creating a 45 minute song

I like to do my Pomodoros in 45m intervals. I took an album and joined all the songs.

    (env) $ cat *.mp3 > oneBigSong.mp3

This is not the best approach if the songs are not normalized to the same volume.

## Modify the task name

    if focus == 'working'
    if focus == 'coding'

You can modify the task names to anything you want.

## Running the Pomodoro timer

It's just a script:

    (env) $ python pomodoroTimer.py

## Why "Frankie"

I am getting this warning when running the program:

    Warning: Big change (MPEG version, layer, rate). Frankenstein stream?

I imagine is because I didn't normalize the volume of the joined mp3 file I am using. But I haven't been able to fix this. So I named this program `Frankie`.

## Future Version

I am thinking this could be a fun improvement.

Integrating the Pomodoro timer with TaskWarrior. Since I am such a fan of the command line. Use `task ID start` to start the timer and record how much time was spent on that task. Based on the task project, play a different song.

## Share/Comment

Tweet me at:

[Tom Ordonez](https://twitter.com/tomordonez)

Read my website:

[Data Science, Analytics, Growing Teams](https://www.tomordonez.com/)

Connect with me on:

[Linkedin](https://www.linkedin.com/in/tomordonez/)

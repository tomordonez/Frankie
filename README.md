# Frankie

A Pomodoro timer with Music in Python.

The pomodoro timer is evolving. In the previous version it asked for a task. The task was linked to a specific song.

Now it asks for a directory where your songs are. The length of your Pomodoro and it plays a random song from your music directory.

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

Add `mp3` songs to your directory.

Change the `root` variable with the absolute path of your directory.

It also asks for:

* Directory: Enter absolute path. If you don't enter anything it will default to your `root` variable.
* Length: Enter time in minutes as an integer. If you enter anything other than `int` it will ask again.



## Creating a 45 minute song

I like to do my Pomodoros in 45m intervals. I took an album and joined all the songs.

    (env) $ cat *.mp3 > oneBigSong.mp3

This is not the best approach if the songs are not normalized to the same volume.


## Running the Pomodoro timer

    (env) $ python pomodoroTimer.py

## Why "Frankie"

I am getting this warning when running the program:

    Warning: Big change (MPEG version, layer, rate). Frankenstein stream?

I imagine is because I didn't normalize the volume of the joined mp3 file I am using. But I haven't been able to fix this. So I named this program `Frankie`.

## Share/Comment

Tweet me at:

[Tom Ordonez](https://twitter.com/tomordonez)

Read my website:

[Data Science, Analytics, Growing Teams](https://www.tomordonez.com/)

Connect with me on:

[Linkedin](https://www.linkedin.com/in/tomordonez/)

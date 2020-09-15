import os
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from pygame import mixer
import time
import threading
from mutagen.mp3 import MP3

root = Tk()

menubar = Menu(root)
root.config(menu=menubar)


def openfile():
    global filename
    filename = tkinter.filedialog.askopenfilename()


submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=submenu)
submenu.add_command(label='Open', command=openfile)
submenu.add_command(label='Close', command=root.destroy)


def contact_us():
    tkinter.messagebox.showinfo('Akash Music Player - Help Section', 'Write To Us @akashpurushotham333@gmail.com')


submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=submenu)
submenu.add_command(label='Contact US', command=contact_us)


def about():
    tkinter.messagebox.showinfo('Akash Music Player - About Section',
                                'AKASH....Follow me on Instagram @snap_____dragon')


submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='About', menu=submenu)
submenu.add_command(label='About Develop', command=about)
mixer.init()

root.title("Akash Music Player")
root.iconbitmap(r'icon.ico')

fileLabel = Label(root, text="Lets Rock the Music...!")
fileLabel.pack(pady=10)

lengthLabel = Label(root, text='Go to File -> Open and Select a Music ')
lengthLabel.pack()

timeLabel = Label(root, text='--!|/Music Player With no Music is like Earth without Nature/|!--')
timeLabel.pack()


def show_details():
    fileLabel['text'] = "Playing" + ' - ' + os.path.basename(filename)

    file_data = os.path.splitext(filename)

    if file_data[1] == '.mp3':
        audio = MP3(filename)
        total_length = audio.info.length
    else:
        a = mixer.Sound(filename)
        total_length = a.get_length()

    # div - total_length/60, mod - total_length % 60
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthLabel['text'] = "Total Length" + ' - ' + timeformat

    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()


def start_count(t):
    global paused
    x = 0
    while x <= t and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(x, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            timeLabel['text'] = "Current Time" + ' - ' + timeformat
            time.sleep(1)
            x += 1


paused = False
mute = False
play = False


def play_fun():
    global play
    if paused:
        mixer.music.unpause()
        statusbar['text'] = 'Resumed -' + 'Now Playing' + '  - ' + os.path.basename(filename)
    else:
        try:
            if not play:
                mixer.music.load(filename)
                mixer.music.play()
                statusbar['text'] = 'Now Playing' + '  - ' + os.path.basename(filename)
                show_details()
                play = True
        except:
            tkinter.messagebox.showerror('File Not Found', 'Please Select a Valid Sound File and Try Again')


def stop_fun():
    global play
    mixer.music.stop()
    play = False
    statusbar['text'] = 'Music Stopped  - ' + os.path.basename(filename)


def pause_fun():
    global paused
    global play
    if play:
        paused = True
        mixer.music.pause()
        statusbar['text'] = 'Music Paused  - ' + os.path.basename(filename)
        play = False


def set_vol(val):
    global volume
    volume = int(val) / 100
    mixer.music.set_volume(volume)


def rewind_fun():
    mixer.music.play()
    global play
    play = True


def mute_fun():
    global mute
    if not mute:
        mixer.music.set_volume(0)
        mute = True
    elif mute:
        mixer.music.set_volume(volume)
        mute = False


middleFrame = Frame(root)
middleFrame.pack(padx=20, pady=30)

lowerFrame = Frame(root)
lowerFrame.pack(padx=10, pady=10)

playPhoto = PhotoImage(file='play.png')
playBtn = Button(middleFrame, image=playPhoto, command=play_fun)
playBtn.grid(row=0, column=0, padx=10)

pausePhoto = PhotoImage(file='pause.png')
pauseBtn = Button(middleFrame, image=pausePhoto, command=pause_fun)
pauseBtn.grid(row=0, column=1, padx=10)

stopPhoto = PhotoImage(file='stop.png')
stopBtn = Button(middleFrame, image=stopPhoto, command=stop_fun)
stopBtn.grid(row=0, column=2, padx=10)

rewindPhoto = PhotoImage(file='rewind.png')
rewindBtn = Button(lowerFrame, image=rewindPhoto, command=rewind_fun)
rewindBtn.grid(row=0, column=0)

scale = Scale(lowerFrame, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
scale.grid(row=0, column=2, padx=30)

mutePhoto = PhotoImage(file='mute.png')
muteBtn = Button(lowerFrame, image=mutePhoto, command=mute_fun)
muteBtn.grid(row=0, column=1, padx=10)

statusbar = Label(text='Welcome to Akash Music Player', relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()

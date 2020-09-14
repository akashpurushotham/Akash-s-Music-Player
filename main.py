import os
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from pygame import mixer

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

textlabel = Label(root, text="Lets Rock the Music...!")
textlabel.pack(pady=10)

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
lowerFrame.pack(padx=10,pady=10)

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

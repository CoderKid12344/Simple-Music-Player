from tkinter import *
from tkinter import filedialog
from pygame import mixer

def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()
def musicurl():
    dd = filedialog.askopenfilename()
    audiotrack.set(dd)
def pause():
    mixer.music.pause()
def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.1)
def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.1)
def stop():
    mixer.music.stop()
def resume():
    pass

def create_widgets():
    TrackLabel = Label(root, text='Select audio track: ', bg='lightskyblue', font=('arial', 15, 'italic bold'))
    TrackLabel.grid(row=0, column=0, padx=20, pady=20)
    TrackLabelEntry = Entry(root, font=('arial', 16, 'italic bold'), width=35, textvariable=audiotrack)
    TrackLabelEntry.grid(row=0, column=1, padx=20, pady=20)
    BrowseButton = Button(root, text='Browse Songs', bg='deeppink', font=('arial', 13, 'italic bold'), width=20, bd=5, activebackground='purple4', command=musicurl)
    BrowseButton.grid(row=0, column=2, padx=20, pady=20)


    PlayButton = Button(root, text='Play', bg='green2', font=('arial', 13, 'italic bold'), width=20, bd=5, activebackground='purple4', command=playmusic)
    PlayButton.grid(row=1, column=0, padx=20, pady=20)

    PauseButton = Button(root, text='Pause', bg='yellow', font=('arial', 13, 'italic bold'), width=20, bd=5, activebackground='purple4', command=pause)
    PauseButton.grid(row=1, column=1, padx=20, pady=20)

    VolumeUpButton = Button(root, text='Volume Up', bg='blue', font=('arial', 13, 'italic bold'), width=20, bd=5, activebackground='purple4', command=volumeup)
    VolumeUpButton.grid(row=1, column=2, padx=20, pady=20)

    VolumeDownButton = Button(root, text='Volume Down', bg='green2', font=('arial', 13, 'italic bold'), width=20, bd=5, activebackground='purple4', command=volumedown)
    VolumeDownButton.grid(row=4, column=0, padx=20, pady=20)

    StopButton = Button(root, text='Stop', bg='red', font=('arial', 13, 'italic bold'), width=20, bd=5, activebackground='purple4', command=stop)
    StopButton.grid(row=2, column=0, padx=20, pady=20)

    ResumeButton = Button(root, text='Resume', bg='red', font=('arial', 13, 'italic bold'), width=20, bd=5, activebackground='purple4', command=resume)
    ResumeButton.grid(row=3, column=0, padx=20, pady=20)
    ResumeButton.grid_remove()

    ExitButton = Button(root, text='Exit Player', bg='red2', font=('arial', 13, 'italic bold'), width=20, bd=5, activebackground='purple4', command=exit)
    ExitButton.grid(row=5, column=0, padx=20, pady=20)


root = Tk()
root.geometry('1100x500+200+50')
root.title('iSangeet')
root.iconbitmap('songs.jpg')
root.resizable(False, False)
root.configure(bg='lightskyblue')
audiotrack = StringVar()
ss = 'Devoloped by Debadrito Dutta'
count = 0
text = ''
SliderLabel = Label(root, text=ss, bg='lightskyblue', font=('arial', 40, 'italic bold'))
SliderLabel.grid(row=3, column=0, padx=20, pady=20, columnspan=3)
def IntroLabelTrick():
    global count, text
    if(count>=len(ss)):
        count = -1
        text = ''
        SliderLabel.configure(text=text)
    else:
        text = text+ss[count]
        SliderLabel.configure(text=text)
    count += 1
    SliderLabel.after(200, IntroLabelTrick)


IntroLabelTrick()
mixer.init()
create_widgets()
root.mainloop()


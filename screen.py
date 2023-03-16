from tkinter import *
import pyscreenrec
def starrec():
    file = fil.get()
    rec.start_recording(str(file+'.mp4'),5)
def pauserec():
 rec.pause_recording()
def resume():
    rec.resume_recording()

def stop():
    rec.stop_recording()
x = Tk()
x.title('screenrecorder')
rec = pyscreenrec.ScreenRecorder()
x.config(bg='#ffff33')
lbl = Label(x,text='screen rec')
lbl.pack(fill = X)
fil = StringVar()
ent = Entry(x,textvariable=fil)
fil.set('recoding25')
ent.pack()
but= Button(x,text='start',command=starrec,bg='#1aa3ff')
but.pack(fill=X)
but1= Button(x,text='pause',command=pauserec,bg='#1aa3ff')
but1.pack(fill=X)
but2 = Button(x,text='stop',command=stop,bg='#1aa3ff')
but2.pack(fill=X)
but3 = Button(text='resume',command=resume,bg='#1aa3ff')
but3.pack(fill=X)
x.mainloop()
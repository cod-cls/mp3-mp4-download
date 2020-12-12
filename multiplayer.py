from __future__ import unicode_literals
import youtube_dl
from tkinter import *
from moviepy.editor import *
import os
import sys


root = Tk()

class Functions():
    
    
    def downloadMP4(self):
        
        ydl_opts = {'format': 'best', 'outtmpl': 'mp4-%(title)s.%(ext)s'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.entry.get()])
        self.entry.delete(0,END)
    
    def downloadMP3(self):
        
        def etc(nameFile):
            path = os.path.dirname(os.path.abspath('multiplayer.py'))
            dir = os.listdir(path)
            for file in dir:
                if file == nameFile:
                    os.remove(file)
                    
                    
        ydl_opts = {'format': 'best', 'outtmpl': 'mp3-%(title)s.%(ext)s'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_video = ydl.extract_info(self.entry.get(),download = False)
            filename = ydl.prepare_filename(info_video)
            ydl.download([self.entry.get()])
            
            mp4_file = filename
            mp3_file = filename[:-3] + 'mp3'
                     
            videoClip = VideoFileClip(mp4_file)
            audioClip = videoClip.audio
            audioClip.write_audiofile(mp3_file)
            audioClip.close()
            videoClip.close()
            
            etc(filename)
            
        self.entry.delete(0,END)
     
        

       
                    
      

class Aplication(Functions):
    
    def __init__(self):
        self.root = root
        self.screen()
        self.frames()
        self.buttons()
        self.labels()
        self.entrys()
        self.root.mainloop()
        
    def screen(self):
        self.root.title("Video Downloader")
        self.root.configure(background = 'purple3')
        self.root.geometry("500x300")
        self.root.resizable(False,False)
        self.root.maxsize(width = 600, height = 400)
        self.root.minsize(300,200)
        
    def frames(self):
        self.frame1 = Frame(self.root, bd = 4, highlightbackground = "purple4", highlightthickness = 4)    
        self.frame1.place(relx = 0.125, rely = 0.2, relwidth = 0.75, relheight = 0.60) 
        
    def buttons(self):
        self.button1 = Button(self.frame1, text = "MP4", bd = 0.5, bg = "white",fg = "black",command = self.downloadMP4)
        self.button1.place(relx = 0.20,rely = 0.10, relwidth = 0.30, relheight = 0.20)
        
        self.button2 = Button(self.frame1, text = "MP3", bd = 0.5, bg = "white",fg = "black",command = self.downloadMP3)
        self.button2.place(relx = 0.5,rely = 0.10, relwidth = 0.30, relheight = 0.20)
        
    def labels(self):
        self.label = Label(self.frame1, text = "url",bg = "white",fg = "black")
        self.label.place(relx = 0.050,rely = 0.5, relwidth = 0.15, relheight = 0.20)
        
    def entrys(self):
        self.entry = Entry(self.frame1,bd = 3)
        self.entry.place(relx = 0.20,rely = 0.5, relwidth = 0.65, relheight = 0.20)
        x = self.entry.get()
        print(x)
        
  
Aplication()


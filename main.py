from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil

def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    get_link = link_field.get()
    user_path = path_label.cget('text')
    screen.title('Downloading.')
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete.')

screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

link_field = Entry(screen, width=50)
link_label = Label(screen, text='Enter Video Link: ', font=('MS Gothic', 15))

path_label = Label(screen, text='Select Path For Download', font=('MS Gothic', 15))
select_btn = Button(screen, text='Select', command=select_path)
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

download_btn = Button(screen, text='Download Video', command=download_file)
canvas.create_window(250, 390, window=download_btn)




screen.mainloop()
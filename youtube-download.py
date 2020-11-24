from tkinter import *
import pytube

def download():
    video_url = url.get()
    try:
        youtube = pytube.Youtube(video_url)
        video   = youtube.streams.first()
        video.download("C:/Users/Aethelwulf/Desktop/Videos")
        notif.config(fg="green",text="Downloaded complete")

    except Exception as e:
        print(e)
        notif.config(fg="red",text="Video could not be downloaded")

master = Tk()
master.title("Youtube video downloader")
Label(master, text="Youtube Video Converter",fg="red",font=("Calibri",15)).grid(sticky=N,padx=100,row=0)
Label(master, text="Enter the URL (Link) of your video below : ",fg="black",font=("Calibri",12)).grid(sticky=N,row=1,pady=15)
notif = Label(master,font=("Celibri",12))
notif.grid(sticky=N,pady=1,row=4)
url = StringVar()
Entry(master,width=50,textvariable=url).grid(sticky=N,row=2)
Button(master,width=20,text="Download",font=("Celibri",12),command=download).grid(sticky=N,row=3,pady=15)

master.mainloop()

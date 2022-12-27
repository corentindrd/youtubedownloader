import tkinter
import customtkinter
from pytube import YouTube
import urllib.request
from io import BytesIO
from PIL import Image, ImageTk


def getvideos():

#Récupération de l'url
    video_url = videourl.get()
    yt = YouTube(video_url)

#Récupération et affichage de la miniature
    thumbnail_url = yt.thumbnail_url
    response = urllib.request.urlopen(thumbnail_url)
    image_data = response.read()
    image = Image.open(BytesIO(image_data))
    image2 = customtkinter.CTkImage(image, size=(640,480))
    label = customtkinter.CTkLabel(master=root,text="", image= image2)
    label.place(relx=0.73, rely=0.3, anchor= tkinter.CENTER)

#Récupération et affichage du titre
    title = yt.title
    titlelabel = customtkinter.CTkLabel(master=root, text=title,font=("Helvetica",23, "bold"), wraplength=700)
    titlelabel.place(relx=0.73, rely=0.68, anchor= tkinter.CENTER)





root = customtkinter.CTk()
#root.iconbitmap('onair.ico')
root.title("Youtube Downloader")
root.geometry("1280x720")
root.resizable(width=False, height=False)


videourl = customtkinter.CTkEntry(root,width=400)
videourl.place(relx=0.2, rely=0.1, anchor= tkinter.CENTER)

validbutton = customtkinter.CTkButton(root, text="Valider", command=getvideos)
validbutton.place(relx=0.42, rely=0.1, anchor=tkinter.CENTER)

root.mainloop()


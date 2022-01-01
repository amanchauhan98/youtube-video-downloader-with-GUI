from tkinter import *
from tkinter import font
import tkinter.messagebox as tmsg
import time
from pytube import YouTube



def about_us():
    tmsg.showinfo("AboutUs","Here I am Aman chauhan who developed this  software. This is a version 1 of youtube video downloader")
def feedback():
    ask = tmsg.askquestion("Feedback","Do you Want to Give Feedback?")
    if ask == "yes":
        feedback11 = Tk()
        feedback11.title("Give Feedback")
        global feedback1 
        feedback1 = Text(feedback11, height=2, width=20)
        feedback1.grid(row=1, column=0)
        Button(feedback11, text="Submit", fg="green", command=Submit_feedback).grid(row=2, column=1)

        time.sleep(3)
        tmsg.showinfo("Received Feedback","Thank you for giving us a feedback! It means a lot")
        feedback11.mainloop()
    else :
        tmsg.showinfo("About Feedback","No worry about the You dont give us a feedback!")    
def submit():
    downloader = YouTube(text1.get())
    if choice.get() == 1:
        tmsg.showinfo("Title",downloader.title)
    elif choice.get() == 2:
        video = downloader.streams.get_highest_resolution()
        video.download(filename= "youtubevideo11.mp4")
        tmsg.showinfo("Youtube Downloader","Video Downloaded")
    elif choice.get() == 3:
        print("Thumbnail",downloader.thumbnail_url)
        tmsg.showinfo("Youtube Downloader","Thumbnail Downloaded")
    elif choice.get() == 4:
        tmsg.showinfo("Youtube Downloader",downloader.streams)
    elif choice.get() == 5:
        downloader.streams.get_audio_only().download("songs.mp3")
        tmsg.showinfo("Youtube Downloader","MP3 song is downloaded")
    else:
        tmsg.showerror("ERROR","There is some error in your input Please check once again!")    



def Submit_feedback():
    with open("youtubefeedback.txt","a") as f:
        f.write(str(feedback1.get(1.0, END)))



root = Tk()
# root.geometry("500x500")
root.title("Youtube Video DownLoader- Aman chauhan")
# for menu
mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="AboutUs", command=about_us)
m1.add_command(label="Exit",command=quit)
m1.add_command(label="Feedback",command=feedback)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Menu", menu=m1)

#for heading
Label(root, text="YOUTUBE VIDEO DOWNLOADER", font="comicsans 20 bold", fg="indigo", relief=SUNKEN).grid(row=0, column=2)
Label(root, text="Enter the URL of Youtube Video here:", font="comicsans 10 bold",pady=10).grid(row=1, column=0)
Label(root, text="Choose the Correct option what you want to do!  :", font= "comicsans 10 bold", pady=10).grid(row=2, column=0)

# for radio button:
choice = IntVar()
choice.set(2)
radio1 = Radiobutton(root, text="Title", variable=choice, value=1).grid(row=2, column=1)
radio2 = Radiobutton(root, text="Get Video", variable=choice, value=2).grid(row=3, column=1)
radio3 = Radiobutton(root, text="Thumbnail", variable=choice, value=3).grid(row=4, column=1)
radio4 = Radiobutton(root, text="Streams", variable=choice, value=4).grid(row=5, column=1)
radio5 = Radiobutton(root, text="Audio", variable=choice, value=5).grid(row=6, column=1)


# button
Button(root, text="Submit", fg="green", command=submit).grid(row=8, column=0)
Button(root, text="Exit", fg="red", command=quit).grid(row=8, column=1)

# for entry widget
text1 = StringVar()
txtval = Entry(root,textvariable=text1).grid(row=1, column=1)




root.mainloop()
from PIL import Image, ImageDraw, ImageFont
import csv
import os, sys
from tkinter import *
from tkinter import filedialog
import datetime

xdate = str(datetime.datetime.now())
date = xdate[8:10]+"/"+xdate[5:7]+"/"+xdate[0:4]
src = r'/Users/chiefpost/Desktop/python tests/clocksv1.csv'
dst = r'/Users/chiefpost/Desktop/python tests'
path = None

# defalt values
project = "32Red"
ratio = "Ratio: 16x9"
audio = "Stereo CH1 & CH2"

def setSrc():
    global src
    src = filedialog.askopenfilename(title="Select a folder")
    srcLabel = Label(gui, text="Selected source: " + src)
    srcLabel.grid(row=1, column=2)
    print(src)

def setDst():
    global dst
    dst = filedialog.askdirectory(title="Select a folder")
    dstLabel = Label(gui, text="Selected destination: " + dst)
    dstLabel.grid(row=2, column=2)
    print(dst)


def makeClocks():
    global src
    global dst
    global project
    global date
    global path
    global audio
    global ratio
    rxDate = "RX Date: " + date
    titles = []
    clocks = []
    times = []
    count = 0

    with open(src, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for lines in csv_reader:
            if not len(lines[1]) == 0:
                clock = lines[1]
                # adding a char into the clock name
                ######clock = clock[:7] + "I" + clock[7:]
                # ------
                clocks.append(clock)
                titles.append(lines[3])
                clocklen = len(lines[1])
                times.append(lines[1][-2:])
                count = count + 1

    print(titles)
    print(clocks)
    print(titles)

        #text placement
    tX = 900
    topY = 230
    padY = 60
    reCount = 0
    print(count)
    from PIL import Image, ImageDraw, ImageFont
    for no in range(count):

        duration = "Duration: 00:00:"+times[reCount]+":00"
        img = Image.new('RGBA', (1920, 1080), color=(0, 0, 0, 0))

        fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 42)
        d = ImageDraw.Draw(img)
        parts = titles[reCount].split("-",1)
        print(len(parts))

        aTitle = parts[0]
        d.text((tX, topY), project, font=fnt, fill=(255, 255, 255))
        d.text((tX, topY + padY * 1), aTitle, font=fnt, fill=(255, 255, 255))
        if len(parts) > 1:
            bTitle = parts[1]
            bTitle = bTitle[1:]
            d.text((tX, topY + padY * 2), bTitle, font=fnt, fill=(255, 255, 255))
        else:
            print(parts)

        d.text((tX, topY + padY * 4), clocks[reCount], font=fnt, fill=(255, 255, 255))
        d.text((tX, topY + padY * 6), duration, font=fnt, fill=(255, 255, 255))
        d.text((tX, topY + padY * 7), ratio, font=fnt, fill=(255, 255, 255))
        d.text((tX, topY + padY * 8), audio, font=fnt, fill=(255, 255, 255))
        d.text((tX, topY + padY * 9), rxDate, font=fnt, fill=(255, 255, 255))
        #saving image
        imgName2 = clocks[reCount].replace("/","-") + ".png"
        #print(imgName2)
        imgName = titles[reCount] + ".png"
        path = os.path.join(dst, imgName2)

        img.save(path)
        reCount = reCount + 1
        
def setAdv():
    print("testy def")

    global project
    global ratio
    global audio
    global projectLabel
    global projectEntry
    global setAdvBtn
    global ratioLabel
    global audioLabel
    hideAdvanced()

    if not len(projectEntry.get()) == 0:

        project = projectEntry.get()
    if not len(ratioEntry.get()) == 0:
        ratio = "Ratio: " + ratioEntry.get()
    if not len(audioEntry.get()) == 0:
        audio = audioEntry.get()

    projectLabel = Label(text="Project: " + project)
    ratioLabel = Label(text="Ratio: " + ratio)
    audioLabel = Label(text="Audio: " + audio)

    showAdvanced()


def showAdvanced():
    showAdvancedBtn.grid_forget()
    global hideAdvancedBtn
    hideAdvancedBtn.grid(row=4, column=1)
    global project
    global projectLabel
    global projectEntry
    global setAdvBtn
    global ratioLabel
    global audioLabel
    global audioEntry
    global ratio

    projectLabel.grid(row=5, column=1)
    projectEntry.grid(row=5, column=2)


    ratioLabel.grid(row=6, column=1)
    ratioEntry.grid(row=6, column=2)
    audioLabel.grid(row=7, column=1)
    audioEntry.grid(row=7, column=2)



    setAdvBtn.grid(row=10, column=1)

def hideAdvanced():
    print("test")
    global hideAdvancedBtn
    global projectLabel
    global projectEntry
    global setAdvBtn
    global ratioLabel
    global audioLabel
    hideAdvancedBtn.grid_forget()
    projectLabel.grid_forget()
    projectEntry.grid_forget()
    ratioLabel.grid_forget()
    ratioEntry.grid_forget()
    audioLabel.grid_forget()
    audioEntry.grid_forget()
    setAdvBtn.grid_forget()

    showAdvancedBtn.grid(row=4, column=1)


#UI section
gui = Tk()
gui.title("Jack's Clocker")
gui.geometry("420x420")

srcSelectBtn = Button(gui, text="browse src", command=setSrc)
srcSelectBtn.grid(row=1, column=1)

dstSelectBtn = Button(gui, text="browse dst", command=setDst)
dstSelectBtn.grid(row=2, column=1)

clockitBtn = Button(gui, text="Clock it", command=makeClocks)
clockitBtn.grid(row=3, column=1)

showAdvancedBtn = Button(gui, text="advanced", command=showAdvanced)
showAdvancedBtn.grid(row=4, column=1)


#ON ACTIVE BUTTONS
hideAdvancedBtn = Button(gui, text="hide advanced", command=hideAdvanced)
projectLabel = Label(text="User Name")

projectLabel = Label(text="Project: " + project)
ratioLabel = Label(text="Ratio: " + ratio)
audioLabel = Label(text="Audio: " + audio)

projectEntry = Entry()
ratioEntry = Entry()
audioEntry = Entry()
setAdvBtn = Button(gui, text="Set Avanced values", command=setAdv)

gui.mainloop()

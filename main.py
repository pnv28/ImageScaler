from PIL import Image, ImageEnhance, ImageFilter
from colorama import Fore as clr
import os

path = "./img"
pathOut = "./editedImg"

customPath = False

if len(os.listdir(path)) == 0:
    oFlag = input(f"There are no Images present in {path}\
        \nWould you like to manually enter the image path manually (y/n): ")
    if oFlag == 'y':
        path = input("Please enter the Global Image Path: ")
        customPath = True
    elif oFlag == 'n':
        exit()
    else:
        print(f"{clr.RED}Invalid Input{clr.RESET}")
        exit()


if customPath:
    newW = 0
    newH = 0
    img = Image.open(path)
    w, h = img.size
    print(f"Current size of the image in px is ({w}px,{h}px)")
    ch = input("Do you want to change the Height(h) or the Width(w) of the Image (h/w): ")
    if ch == 'h':
        newH = input("Input the New Height of the Image in px: ")
        newW = int(newH) * (w/h)
        print(f"The Width of the Image for the selected height will be {int(newW)}px")
    elif ch == 'w':
        newW = input("Input the New Width of the Image in px: ")
        newH = int(newW) * (h/w)
        print(f"The Height of the Image for the selected width will be {int(newH)}px")
    else:
        print(f"{clr.RED}Invalid Input{clr.RESET}")
    
    try:
        scaledImg = img.resize((int(newW),int(newH)), Image.LANCZOS)
        sharpenedImg = scaledImg.filter(ImageFilter.SHARPEN)
        filename = os.path.split(path)[1]
        cleanname, ext = os.path.splitext(filename)
        savePath = f"{os.path.abspath(f"./{pathOut}/{cleanname}")}_scaled{ext}"
        print(f"Saving the Image to {savePath}")
        sharpenedImg.save(savePath)
    except:
        print(f"{clr.RED}There was an error{clr.RESET}")
elif customPath == False:
    for filename in os.listdir(os.path.abspath(path)):
        newW = 0
        newH = 0
        img = Image.open(f"{os.path.abspath(path)}/{filename}")
        w, h = img.size
        print(f"Current size of {filename} in px is ({w}px,{h}px)")
        ch = input(f"Do you want to change the Height(h) or the Width(w) of the {filename} (h/w): ")
        if ch == 'h':
            newH = input(f"Input the New Height of the {filename} in px: ")
            newW = int(newH) * (w/h)
            print(f"The Width of the {filename} for the selected height will be {int(newW)}px")
        elif ch == 'w':
            newW = input(f"Input the New Width of the {filename} in px: ")
            newH = int(newW) * (h/w)
            print(f"The Height of the {filename} for the selected width will be {int(newH)}px")
        
        filen = os.path.split(f"{os.path.abspath(path)}/{filename}")[1]
        file, ext = os.path.splitext(f"{filen}")
        
        scaledImg = img.resize((int(newW),int(newH)), Image.LANCZOS)
        sharpenedImg = scaledImg.filter(ImageFilter.SHARPEN)
        savePath = f"{os.path.abspath(pathOut)}/{file}_scaled{ext}"
        print(f"Saving {filename} to {savePath}")
        sharpenedImg.save(savePath)

print(f"{clr.GREEN}Tool made by pnv28 ;)")
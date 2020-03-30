import tkinter as tk
from tkinter import *
import subprocess
from tkinter import filedialog, Text, messagebox
import os
from PIL import ImageTk, Image
import os
import time
import face_recognition as fr
#import FaceRecognition

#os.system( 'raspistill -o p.png')



#root = tk.Tk()
#img = ImageTk.PhotoImage(Image.open("image.png"))

#canvas = tk.Canvas(root, height = 700, width = 700, bg="#263D42")
#canvas.pack()
#canvas.create_image(20, 20, anchor = NW, image=img)
#panel = Label(image = img)
#panel.pack()
#frame = tk.Frame(root, image.png)
#frame.place(relwidth = 0.8, relheight = 0.8)"""


#root.mainloop()

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Facial Recognition")
        self.root.geometry('1080x720' )
        #self.canvas = tk.Canvas(self.root, height=700, width=700)
        #self.canvas.pack()
        #self.button1 = tk.Button(self.root, text = "Load Images", command = self.load)
        #self.button2 = tk.Button(self.root, text="Take Images", command = self.take)
        #self.button3 = tk.Button(self.root, text="Run Facial Recognition", command=self.fg)
        self.label =tk.Label(self.root, text = "Copyright 2020: Noah N.")
        self.label1 = tk.Label(self.root, text = "Image 1")
        self.label2 = tk.Label(self.root, text="Image 2")
        self.label3 = tk.Label(self.root, text="Image 3")
        self.label4 = tk.Label(self.root, text = "Results:")
        #self.root.filename=""
        self.besetzt = False
        self.counter = 0



    def load(self):
        self.besetzt = True
        if self.counter < 3:
            self.root.filename = filedialog.askopenfilename(initialdir = "/home/pi/PycharmProjects/GUI/venv", title = "Select a file", filetypes =(("png files", "*.png"), ("jpg files", "*.jpg"))) #all files "*.*"
            self.umwandlung = str(self.root.filename)
            self.counter = self.counter + 1
            self.display(self.umwandlung)
        else:
            self.msgerror()
            #self.errorbox()
            pass


    def take(self):
        if self.besetzt == False:
            self.msgbox()
            self.counter = 1
            os.system( 'raspistill -o /home/pi/PycharmProjects/GUI/venv/1.png')
            self.bild1 = "/home/pi/PycharmProjects/GUI/venv/1.png"
            self.display(self.bild1)
            time.sleep(1)
            self.counter = 2
            os.system('raspistill -o /home/pi/PycharmProjects/GUI/venv/2.png')
            self.bild2 = "/home/pi/PycharmProjects/GUI/venv/2.png"
            self.display(self.bild2)
            time.sleep(1)
            self.counter = 3
            os.system('raspistill -o /home/pi/PycharmProjects/GUI/venv/3.png')
            self.bild3 = "/home/pi/PycharmProjects/GUI/venv/3.png"
            self.display(self.bild3)
            #self.display(""
        else:
            self.msgerror2()
            pass




    def fg(self):
        self.stickpictures(self.img, self.img2, self.img3)
        #FaceRecognition.run()
        #print(self.root.filename)
        pass

    def stickpictures(self):        #a, b, c
        self.bilda = Image.open("/home/pi/Downloads/bild2.jpg")
        self.bildb = Image.open("/home/pi/Downloads/bild2.jpg")

        (self.width1, self.height1) = self.bilda.size
        (self.width2, self.height2) = self.bildb.size

        self.result_width = self.width1 + self.width2
        self.result_height = max(self.height1, self.height2)
        self.result_image = Image.new('RGB', (self.result_width, self.result_height))
        self.result_image.paste(im = self.bilda, box = (0, 0))
        self.result_image.paste(im = self.bildb, box = (self.width1, 0))

        self.result_image.save("ww.jpg")




    def loadbutton(self):
        self.button1 = tk.Button(self.root, text="Load Images", command=self.load)
        self.button1.place(x = 0, y = 0, anchor = "nw")

    def takeimagebutton(self):
        self.button2 = tk.Button(self.root, text="Take Images", command=self.take)
        self.button2.place(x = 0, y = 50, anchor = "nw")

    def facial_recognitionbutton(self):
        self.button3 = tk.Button(self.root, text="Run Facial Recognition", command=self.clear)
        self.button3.place(relx=1, rely=1, anchor="se")

    def clearbutton(self):
        self.button4 = tk.Button(self.root, text = "Clear all", command=self.clear)
        self.button4.place(x = 0, y = 100, anchor = "nw")

    def msgbox(self):
        tk.messagebox.showinfo \
            ("Info", "Es werden 3 Aufnahmen gemacht")

   # def errorbox(self):
    #    self.berror = tk.Button(self.root, text = "Fehler", command = self.msgerror)

    def msgerror(self):
        tk.messagebox.showerror \
            ("Fehler", "Es koennen nicht mehr als 3 Fotos hochgeladen werden!")

    def msgerror2(self):
        tk.messagebox.showerror \
            ("Fehler", "Entweder alle Fotos hochladen oder alle aufnehmen!")

    def layout(self):
        self.fr1 = tk.Frame(self.root, width=109, height=135, relief="sunken", bd=1)
        self.fr1.place(relx=0, rely=0, anchor="nw")
        #self.fr2 = tk.Frame(self.root, width=1720, height=400, relief="sunken", bg="white", bd=4)  # 2055
        #self.fr2.place(x=1825, y=0, anchor="ne")
        #self.fr3 = tk.Frame(self.root, width=573, height=400, relief="sunken", bg="white", bd=4)  # 685
        #self.fr3.place(x=1820, y=0, anchor="ne")  # 2160
        #self.fr4 = tk.Frame(self.root, width=573, height=400, relief="sunken", bg="white", bd=4)
        #self.fr4.place(x=1247, y=0, anchor="ne")
        #self.fr5 = tk.Frame(self.root, width = 1850, height = 425, relief = "sunken", bd = 4)
        #self.fr5.place(x=1825, y = 460, anchor = "ne")

    def display(self, x):
        #print(self.besetzt)
        if self.counter > 3:
            print("Es sind schon 3 Bilder hochgeladen")
            pass
        else:
            if self.counter == 1:
                #self.img = ImageTk.PhotoImage(Image.open(x))
                self.im = Image.open(x)
                self.new = self.im.resize((640, 480))
                self.img = ImageTk.PhotoImage(self.new)
                #self.img = tk.PhotoImage(file = "bild2.jpg")
                self.canvas.create_image(10, 10, anchor=tk.NW, image = self.img)

                #self.clear()
                #self.besetzt = True
                #self.counter = self.counter + 1
            if self.counter == 2:
                self.im2 = Image.open(x)
                self.new2 = self.im2.resize((640, 480))
                self.img2 = ImageTk.PhotoImage(self.new2)
                self.canvas2.create_image(10, 10, anchor=tk.NW, image=self.img2)
                #display daneben

            if self.counter == 3:
                self.im3 = Image.open(x)
                self.new3 = self.im3.resize((640, 480))
                self.img3 = ImageTk.PhotoImage(self.new3)
                self.canvas3.create_image(10, 10, anchor=tk.NW, image=self.img3)

    """def show(self):
        self.im = Image.open("kik.jpg")
        print(self.im.size)
        self.resize = self.im.resize((640, 480))
        print(self.resize)
        #self.resize.show() """



    def clear(self):

        self.img = None
        self.img2 = None
        self.img3 = None
        self.counter = 0
        self.besetzt = False
       # self.img.place(x = 1500, y = 0)

    def window(self):
        self.canvas = tk.Canvas(self.root, width = 550, height = 385, relief = "sunken", bd = 4, bg = "white")
        self.canvas.place(x=670, y=0, anchor="ne")
        self.canvas2 = tk.Canvas(self.root, width = 550, height = 385, relief = "sunken", bd = 4, bg = "white")
        self.canvas2.place(x=1240, y=0, anchor="ne")
        self.canvas3 = tk.Canvas(self.root, width=550, height=385, relief="sunken", bd=4, bg = "white")
        self.canvas3.place(x=1810, y=0, anchor="ne")
        self.canvas4 = tk.Canvas(self.root, width=1850, height=425, relief="sunken", bd=4, bg="white")
        self.canvas4.place(x=1825, y=460, anchor="ne")

    def run(self):
        self.layout()
        #self.button1.pack()
        self.loadbutton()
        self.takeimagebutton()
        self.clearbutton()
        self.facial_recognitionbutton()
        self.window()
        #self.display()
        #self.button2.pack()
        #self.button3.pack()
        #self.button3.place(relx = 1, rely = 1, anchor = "se")
        self.label1.place(x = 355, y = 400)
        self.label2.place(x=950, y=400)
        self.label3.place(x=1520, y=400)

        self.label4.place(x=930, y= 430)





        self.label.place(x = 0, rely = 1, anchor = "sw")
        #self.panel = Label(image=self.img)
        #self.panel.pack()
        self.root.mainloop()



Gui = GUI()
#Gui.show()
Gui.run()
#Gui.stickpictures()

import tkinter as tk
from tkinter import *
import subprocess
from tkinter import filedialog, Text, messagebox
import os
from PIL import ImageTk, Image
import os
import time
import face_recognition as fr
import FaceRecognition
#import cv2

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
        self.number = 0



    def load(self):
        self.besetzt = True
        if self.counter < 3:
            self.root.filename = filedialog.askopenfilename(initialdir = "../../img/unknown", title = "Select a file", filetypes =(("png files", "*.png"), ("jpg files", "*.jpg"))) #all files "*.*"
            if not self.root.filename:      #if not selecting image
                #self.counter = 0
                pass
            else:
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
            os.system( 'raspistill -o /home/pi/Facial_recognition/img/taken_pictures/1.png')
            self.bild1 = "/home/pi/Facial_recognition/img/taken_pictures/1.png"
            self.display(self.bild1)
            time.sleep(1)
            self.counter = 2
            os.system('raspistill -o /home/pi/Facial_recognition/img/taken_pictures/2.png')
            self.bild2 = "//home/pi/Facial_recognition/img/taken_pictures/2.png"
            self.display(self.bild2)
            time.sleep(1)
            self.counter = 3
            os.system('raspistill -o /home/pi/Facial_recognition/img/taken_pictures/3.png')
            self.bild3 = "/home/pi/Facial_recognition/img/taken_pictures/3.png"
            self.display(self.bild3)
            #self.stickpictures(self.bild1, self.bild2)
            #self.display(""
        else:
            self.msgerror2()
            pass




    def fg(self):
        #self.stickpictures(self.img, self.img2, self.img3)

        #print(self.root.filename)
        #self.image1 = self.img
        #self.image2 = str(self.img2)
        #print(self.image1)
        #print(self.image2)
        #print()
        #exception handling jenachdem wieviele bilder uebergeben werden
        self.path1 = "../../img/results/Resize1.jpg"
        if self.number == 1:
            # FaceRecognition.run()
            FaceRecognition.run(self.path1)
            
            self.displayresult()
            pass
        elif self.number == 2:
            self.path2 = "../../img/results/Resize2.jpg"
            self.stickpictures(self.path1, self.path2)
            FaceRecognition.run("/home/pi/Facial_recognition/GUI/venv/StickedImage.jpg")
            self.displayresult()

        elif self.number == 3:
            self.path2 = "../../img/results/Resize2.jpg"
            self.path3 = "../../img/results/Resize3.jpg"
            self.stickpictures(self.path1, self.path2)
            self.stickimage = "/home/pi/Facial_recognition/GUI/venv/StickedImage.jpg"
            self.stickpictures(self.stickimage, self.path3)
            FaceRecognition.run("/home/pi/Facial_recognition/GUI/venv/StickedImage.jpg")
            self.displayresult()

        else:
            self.msgerror3()
            pass


        #self.stickpictures(str(self.new), str(self.new2))

    #def saveresult(self):
        
        #self.face_recognition_image = cv2.imread("../../img/results/identify.jpg")
     #   self.face_recognition_image = cv2.imread("/home/pi/Facial_recognition/img/results/identify.jpg")
      #  self.edge = Image.fromarray(self.face_recognition_image)
       # self.tk_edge = ImageTk.PhotoImage(self.edge)
        #self.filename = filedialog.asksaveasfile(mode = "w", initialdir = "/../../img/results/", filetypes =(("png files", "*.png"), ("jpg files", "*.jpg")))
                                       
        #if not self.filename:
         #   pass
            
        #else:
         #   self.edge.save(self.filename)


        #

    def stickpictures(self, a, b):        #a, b, c
        self.bilda = Image.open(a)           #"/home/pi/Facial_recognition/GUI/venv/Resize1.jpg"


        self.bildb = Image.open(b)

        (self.width1, self.height1) = self.bilda.size
        (self.width2, self.height2) = self.bildb.size

        self.result_width = self.width1 + self.width2
        self.result_height = max(self.height1, self.height2)
        self.result_image = Image.new('RGB', (self.result_width, self.result_height))
        self.result_image.paste(im = self.bilda, box = (0, 0))
        self.result_image.paste(im = self.bildb, box = (self.width1, 0))

        self.result_image.save("StickedImage.jpg")
        #print("done")

    """def savebutton(self):
        self.button5 = tk.Button(self.root, text="Save Result", command=self.saveresult)
        self.button5.place(relx=0.5, rely=1, anchor="s")"""


    def loadbutton(self):
        self.button1 = tk.Button(self.root, text="Load Images", command=self.load)
        self.button1.place(x = 0, y = 0, anchor = "nw")

    def takeimagebutton(self):
        self.button2 = tk.Button(self.root, text="Take Images", command=self.take)
        self.button2.place(x = 0, y = 50, anchor = "nw")

    def facial_recognitionbutton(self):
        self.button3 = tk.Button(self.root, text="Run Facial Recognition", command=self.fg)
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

    def msgerror3(self):
        tk.messagebox.showerror \
            ("Fehler", "Es muss mindestens ein Bild geladen / gemacht werden!")

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
                self.new.save("../../img/results/Resize1.jpg")
                self.img = ImageTk.PhotoImage(self.new)
                #self.img = tk.PhotoImage(file = "bild2.jpg")
                self.canvas.create_image(10, 10, anchor=tk.NW, image = self.img)

                #self.clear()
                #self.besetzt = True
                #self.counter = self.counter + 1
                self.number = 1
            if self.counter == 2:
                self.im2 = Image.open(x)
                self.new2 = self.im2.resize((640, 480))
                self.new2.save("../../img/results/Resize2.jpg")
                self.img2 = ImageTk.PhotoImage(self.new2)
                self.canvas2.create_image(10, 10, anchor=tk.NW, image=self.img2)
                self.number = 2
                #display daneben

            if self.counter == 3:
                self.im3 = Image.open(x)
                self.new3 = self.im3.resize((640, 480))
                self.new3.save("../../img/results/Resize3.jpg")
                self.img3 = ImageTk.PhotoImage(self.new3)
                self.canvas3.create_image(10, 10, anchor=tk.NW, image=self.img3)
                self.number = 3

    def displayresult(self):
        if self.number == 1:
            self.endpicture = ImageTk.PhotoImage(Image.open("../../img/results/identify.jpg"))
            self.canvas4.create_image(10, 10, anchor=tk.NW, image=self.endpicture)

        else:
            self.endpicturepath = "../../img/results/identify.jpg"
            self.endpicture = ImageTk.PhotoImage(Image.open(self.endpicturepath))
            self.canvas4.create_image(10, 10, anchor=tk.NW, image=self.endpicture)


    



    def clear(self):

        self.img = None
        self.img2 = None
        self.img3 = None
        self.counter = 0
        self.besetzt = False
        self.number = 0
        self.endpicture = None
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
        #self.savebutton()
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

if __name__ == '__main__':

    Gui = GUI()
    #Gui.show()
    Gui.run()
    #Gui.stickpictures()

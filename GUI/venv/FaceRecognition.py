import face_recognition as fr
from PIL import Image, ImageDraw

class FaceRecognition:
    def __init__(self):
        self.image_of_bill = fr.load_image_file("/home/pi/Facial_recognition/img/known/bill.png")
        self.bill_face_encoding = fr.face_encodings(self.image_of_bill)[0]  # returns an array

        self.image_of_steve = fr.load_image_file("/home/pi/Facial_recognition/img/known/steve.png")
        self.steve_face_encoding = fr.face_encodings(self.image_of_steve)[0]

        self.image_of_noah = fr.load_image_file("/home/pi/Facial_recognition/img/known/Abschluss.png")
        self.noah_face_encoding = fr.face_encodings(self.image_of_noah)[0]

        # create an array with encodings and names
        self.known_face_encodings = [
            self.bill_face_encoding,
            self.steve_face_encoding,
            self.noah_face_encoding
            #self.minh_face_encoding,
            #self.mama_face_encoding,
            #self.papa_face_encoding

        ]

        self.known_face_names = [
            "Bill Gates",
            "Steve Jobs",
            "Noah",
            "Minh",
            "Mama",
            "Papa"
        ]

    # load test image to find faces
    def load(self):     #x uebergeben
        self.test_image = fr.load_image_file("/home/pi/Facial_recognition/img/unknown/bildjobs.png")

    # find faces in test image
    def findfaces(self):
        self.face_locations = fr.face_locations(self.test_image)
        self.face_encodings = fr.face_encodings(self.test_image, self.face_locations)

    # Convert to PIL format
    def convert(self):
        self.pil_image = Image.fromarray(self.test_image)

    # Create a ImageDraw
    def draw(self):
        self.draw = ImageDraw.Draw(self.pil_image)

    # loop through faces in test image
    def loop(self):
        for (top, right, bottom, left), self.face_encoding in zip(self.face_locations, self.face_encodings):
            self.matches = fr.compare_faces(self.known_face_encodings, self.face_encoding)

            self.name = "Unknown Person"

            if True in matches:
                self.first_match_index = self.matches.index(True)
                self.name = self.known_face_names[self.first_match_index]

            # Draw box around face
            self.draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))

            # draw text label
            self.text_width, self.text_height = self.draw.textsize(self.name)
            self.draw.rectangle(((left, bottom - self.text_height - 10), (right, bottom)), fill=(0, 0, 0), outline=(0, 0, 0))
            self.draw.text((left + 6, bottom - self.text_height - 5), self.name, fill=(255, 255, 255, 255))

    def delete(self):
        del self.draw

    def save(self):
    #pil_image.show()
        self.pil_image.save("identify.jpg")


    def run(self):
        self.load()
        self.findfaces()
        self.convert()
        self.draw()
        self.loop()
        self.delete()
        self.save()

FG = FaceRecognition()
FG.run()
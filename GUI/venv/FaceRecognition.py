import face_recognition as fr
from PIL import Image, ImageDraw




def run(x):
    image_of_bill = fr.load_image_file("/home/pi/Facial_recognition/img/known/bill.png")
    bill_face_encoding = fr.face_encodings(image_of_bill)[0]  # returns an array
    image_of_steve = fr.load_image_file("/home/pi/Facial_recognition/img/known/steve.png")
    steve_face_encoding = fr.face_encodings(image_of_steve)[0]

    image_of_noah = fr.load_image_file("/home/pi/Facial_recognition/img/known/Abschluss.png")
    noah_face_encoding = fr.face_encodings(image_of_noah)[0]

    known_face_encodings = [
        bill_face_encoding,
        steve_face_encoding,
        noah_face_encoding
        # self.Bruder_face_encoding,
        # self.mama_face_encoding,
        # self.papa_face_encoding

    ]

    known_face_names = [
        "Bill Gates",
        "Steve Jobs",
        "Noah",
        "Bruder",
        "Mama",
        "Papa"
    ] 
  
    # load test image to find faces / x uebergeben
    test_image = fr.load_image_file(x)

    # find faces in test image
    face_locations = fr.face_locations(test_image)
    face_encodings = fr.face_encodings(test_image, face_locations)

    # Convert to PIL format
    pil_image = Image.fromarray(test_image)

    # Create a ImageDraw
    draw = ImageDraw.Draw(pil_image)

    # loop through faces in test image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = fr.compare_faces(known_face_encodings, face_encoding)

            name = "Unknown Person"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            # Draw box around face
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))

            # draw text label
            text_width, text_height = draw.textsize(name)
            draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 0),
                                outline=(0, 0, 0))
            draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


    del draw
    
    pil_image.save("../../img/results/identify.jpg")
    #return pil_image
    # pil_image.show()
    #i = 0

    #for filename in os.listdir("../../img/results/"):
     #   dst = "identify" + str(i) + ".jpg"
      #  scr = '../../img/results/' + filename
       # dst = '../../img/results/' + dst

        #y = os.rename(src, dst)
        #pil_image.save(y)
        #i += 1
        #pil_image.save("../../img/results/identify.jpg")
    #return(pil_image)




#run()
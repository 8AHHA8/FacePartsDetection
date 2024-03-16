import numpy as np
import cv2
import customtkinter
from face_parts import eyes, mouth, nose
from PIL import Image, ImageTk

from display import app, custom_frame, camera_canvas

face_cascade = cv2.CascadeClassifier('.\opencv\data\haarcascades\haarcascade_frontalface_alt2.xml')

def button1_function():
    print("button1 pressed")
    
    cap = cv2.VideoCapture(0)

    while(True):
        ret, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 190, 0), 2)
        
        pil_img = Image.fromarray(img)
        tk_img = ImageTk.PhotoImage(image=pil_img)
        
        camera_canvas.create_image(0, 0, anchor="nw", image=tk_img)
        app.update()
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

button1 = customtkinter.CTkButton(master=custom_frame, text="Face detection", command=button1_function)
button1.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

eyes = customtkinter.CTkButton(master=custom_frame, text="Eyes", command=eyes)
eyes.place(relx=0.5, rely=0.4, anchor="center")

Mouth = customtkinter.CTkButton(master=custom_frame, text="Mouth", command=mouth)
Mouth.place(relx=0.5, rely=0.6, anchor="center")

nose = customtkinter.CTkButton(master=custom_frame, text="Nose", command=nose)
nose.place(relx=0.5, rely=0.8, anchor="center")

app.mainloop()

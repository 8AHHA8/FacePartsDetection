import numpy as np
import cv2
import customtkinter
from face_parts import eyes, mouth, nose, face
from PIL import Image, ImageTk

from display import app, custom_frame, camera_canvas

face = customtkinter.CTkButton(master=custom_frame, text="Face detection", command=face)
face.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

eyes = customtkinter.CTkButton(master=custom_frame, text="Eyes", command=eyes)
eyes.place(relx=0.5, rely=0.4, anchor="center")

Mouth = customtkinter.CTkButton(master=custom_frame, text="Mouth", command=mouth)
Mouth.place(relx=0.5, rely=0.6, anchor="center")

nose = customtkinter.CTkButton(master=custom_frame, text="Nose", command=nose)
nose.place(relx=0.5, rely=0.8, anchor="center")

app.mainloop()

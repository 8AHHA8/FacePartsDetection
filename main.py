import numpy as np
import cv2
import customtkinter
from face_parts import eyes, mouth, nose, face

from display import app, custom_frame, camera_canvas

face = customtkinter.CTkButton(master=custom_frame, text="Face detection", command=face, font=customtkinter.CTkFont(size=20, weight="bold", family="Papyrus"))
face.place(relx=0.5, rely=0.25, anchor="center")

eyes = customtkinter.CTkButton(master=custom_frame, text="Eyes", command=eyes, font=customtkinter.CTkFont(size=20, weight="bold", family="Papyrus"))
eyes.place(relx=0.5, rely=0.45, anchor="center")

Mouth = customtkinter.CTkButton(master=custom_frame, text="Mouth", command=mouth, font=customtkinter.CTkFont(size=20, weight="bold", family="Papyrus"))
Mouth.place(relx=0.5, rely=0.65, anchor="center")

nose = customtkinter.CTkButton(master=custom_frame, text="Nose", command=nose, font=customtkinter.CTkFont(size=20, weight="bold", family="Papyrus"))
nose.place(relx=0.5, rely=0.86, anchor="center")

app.mainloop()

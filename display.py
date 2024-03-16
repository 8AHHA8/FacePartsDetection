import cv2
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("942x440")

custom_frame = customtkinter.CTkFrame(master=app, width=300, height=240)
custom_frame.pack(side="left", fill="y")

camera_frame = customtkinter.CTkFrame(master=app)
camera_frame.pack(side="left", fill="both", expand=True)

camera_canvas = customtkinter.CTkCanvas(master=camera_frame, bg="#1b1b1b")
camera_canvas.pack(side="left", fill="both", expand=True)
import customtkinter
from face_parts import eyes, mouth, nose, face
from display import app, custom_frame, pressed_button, font_details
from filters import blurry_face, canny_edge, sobel_edge, general_blur, contour_detection, heat_vision

def reset_radio_buttons(exception=None):
    global pressed_button
    for button in [blur_face_filter, general_blur_filter, canny_checkbox, sobel_checkbox, contour_checkbox, heat_vision_checkbox]:
        if button != exception:
            button.deselect()
    pressed_button = exception
    
# FACE PARTS DETECTION________________________________________________________________________________________________________________________________________________________________________________________

face_button = customtkinter.CTkButton(
    master=custom_frame,
    text="Face", 
    command=lambda: [reset_radio_buttons(), face()], 
    font=font_details)
face_button.place(relx=0.25, rely=0.3, anchor="center")

eyes_button = customtkinter.CTkButton(
    master=custom_frame, 
    text="Eyes", 
    command=lambda: [reset_radio_buttons(), eyes()], 
    font=font_details)
eyes_button.place(relx=0.75, rely=0.3, anchor="center")

Mouth_button = customtkinter.CTkButton(
    master=custom_frame, 
    text="Mouth", 
    command=lambda: [reset_radio_buttons(), mouth()], 
    font=font_details)
Mouth_button.place(relx=0.75, rely=0.5, anchor="center")

nose_button = customtkinter.CTkButton(
    master=custom_frame, 
    text="Nose", 
    command=lambda: [reset_radio_buttons(), nose()], 
    font=font_details)
nose_button.place(relx=0.25, rely=0.5, anchor="center")

# FILTERS____________________________________________________________________________________________________________________________________________________________________________________________________

blur_face_filter = customtkinter.CTkRadioButton(
    master=custom_frame, 
    text="Blurry face", 
    command=lambda: [reset_radio_buttons(blur_face_filter), blurry_face()], 
    font=font_details)
blur_face_filter.place(relx=0.23, rely=0.7, anchor="center")

general_blur_filter = customtkinter.CTkRadioButton(
    master=custom_frame, 
    text="General blur", 
    command=lambda: [reset_radio_buttons(general_blur_filter), general_blur()], 
    font=font_details)
general_blur_filter.place(relx=0.24, rely=0.8, anchor="center")

canny_checkbox = customtkinter.CTkRadioButton(
    master=custom_frame, 
    text="Canny Edge", 
    command=lambda: [reset_radio_buttons(canny_checkbox), canny_edge()], 
    font=font_details)
canny_checkbox.place(relx=0.25, rely=0.9, anchor="center")

sobel_checkbox = customtkinter.CTkRadioButton(
    master=custom_frame, 
    text="Sobel Edge", 
    command=lambda: [reset_radio_buttons(sobel_checkbox), sobel_edge()], 
    font=font_details)
sobel_checkbox.place(relx=0.765, rely=0.7, anchor="center")

contour_checkbox = customtkinter.CTkRadioButton(
    master=custom_frame, 
    text="Contours", 
    command=lambda: [reset_radio_buttons(contour_checkbox), contour_detection()], 
    font=font_details)
contour_checkbox.place(relx=0.73, rely=0.8, anchor="center")

heat_vision_checkbox = customtkinter.CTkRadioButton(
    master=custom_frame, 
    text="Heat vision", 
    command=lambda: [reset_radio_buttons(heat_vision_checkbox), heat_vision()], 
    font=font_details)
heat_vision_checkbox.place(relx=0.75, rely=0.9, anchor="center")

app.mainloop()

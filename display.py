import customtkinter

app = customtkinter.CTk()
app.geometry("942x440")
app.title("General recognition")

pressed_button = None
font_details=customtkinter.CTkFont(size=20, weight="bold", family="Papyrus")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# LEFT FRAME WITH BUTTONS AND FILTERS______________________________________________________________________________________________________________________________________________________________

custom_frame = customtkinter.CTkFrame(master=app, height=440)
custom_frame.pack(side="left", fill="both", expand=True)
custom_frame.master.minsize(width=300, height=0)

title_label = customtkinter.CTkLabel(custom_frame, text="Face parts", font=customtkinter.CTkFont(size=50, weight="bold", family="Papyrus"))
title_label.place(relx=0.5, rely=0.0, anchor="n")

# RIGHT FRAME FOR CAMERA___________________________________________________________________________________________________________________________________________________________________________

camera_frame = customtkinter.CTkFrame(master=app)
camera_frame.pack(side="left", fill="both", expand=True)

camera_canvas = customtkinter.CTkCanvas(master=camera_frame, bg="#1b1b1b")
camera_canvas.pack(side="left", fill="both", expand=True)

app.resizable(False, False)

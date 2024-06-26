import cv2
from PIL import Image, ImageTk
from display import app, camera_canvas

face_cascade = cv2.CascadeClassifier('.\opencv\data\haarcascades\haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('.\opencv\data\haarcascades\haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('.\opencv\data\haarcascades\haarcascade_smile.xml')
nose_cascade = cv2.CascadeClassifier('.\opencv\data\haarcascades\haarcascade_mcs_nose.xml')

# __________________________________________________________________________________________________________________

def face():
    print("face button pressed")
    
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
pass

# __________________________________________________________________________________________________________________

def eyes():
    print("eyes button pressed")
    
    cap = cv2.VideoCapture(0)
    
    while(True):
        ret, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        eyes = eye_cascade.detectMultiScale(gray)
        
        # for (ex, ey, ew, eh) in eyes:
        #     cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (190, 190, 0), 2)
            
        for (x, y, w, h) in eyes:
            center_coordinates = x + w // 2, y + h // 2
            radius = w // 2 #pr h / 2
            cv2.circle(img, center_coordinates, radius, (0, 190, 0), 3)  
                
        pil_img = Image.fromarray(img)
        tk_img = ImageTk.PhotoImage(image=pil_img)
        
        camera_canvas.create_image(0, 0, anchor="nw", image=tk_img)
        app.update()
                
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
pass

# __________________________________________________________________________________________________________________

def mouth():
    print("mouth button pressed")
    
    cap = cv2.VideoCapture(0)
    
    while(True):
        ret, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        mouth = mouth_cascade.detectMultiScale(gray, 1.7, 11)
        
        for (sx, sy, sw, sh) in mouth:
            cv2.rectangle(img, (sx,sy),(sx+sw,sy+sh),(190, 190, 190),2)
            
        pil_img = Image.fromarray(img)
        tk_img = ImageTk.PhotoImage(image=pil_img)
        
        camera_canvas.create_image(0, 0, anchor="nw", image=tk_img)
        app.update()
                
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
pass

# __________________________________________________________________________________________________________________

def nose():
    print("nose button pressed")
    
    cap = cv2.VideoCapture(0)
    
    while(True):
        ret, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 
        nose = nose_cascade.detectMultiScale(gray, 1.3, 5)
        
        # for (x, y, w, h) in nose:
        #     cv2.rectangle(img, (x,y), (x+w,y+h), (190,190,190), 2)
        
        for (x, y, w, h) in nose:
            img = cv2.line(img, (x+50,y+75), (x,y), (190,190,190), 3)
            img = cv2.line(img, (x,y), (x,y), (190,190,190), 3)
            img = cv2.line(img, (x,y), (x,y), (190,190,190), 3)
            
        pil_img = Image.fromarray(img)
        tk_img = ImageTk.PhotoImage(image=pil_img)
        
        camera_canvas.create_image(0, 0, anchor="nw", image=tk_img)
        app.update()
                
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
pass

# __________________________________________________________________________________________________________________
import cv2
from PIL import Image, ImageTk
from display import app, camera_canvas

face_cascade = cv2.CascadeClassifier('.\opencv\data\haarcascades\haarcascade_frontalface_alt2.xml')

def blurry_face():
    cap = cv2.VideoCapture(0)
    
    while(True):
        ret, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    
        for (x,y,w,h) in faces:        
            face = img[y:y+h, x:x+w]
            face = cv2.blur(face,((w // 5),(h // 5)))
            img[y:y+h, x:x+w] = face
    
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

def general_blur():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.blur(img, (15, 15))
        
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

def canny_edge():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        edges = cv2.Canny(img, 100, 200)
        
        pil_img = Image.fromarray(edges)
        tk_img = ImageTk.PhotoImage(image=pil_img)
        
        camera_canvas.create_image(0, 0, anchor="nw", image=tk_img)
        app.update()
                
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
pass

# __________________________________________________________________________________________________________________

def sobel_edge():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
        edges = cv2.addWeighted(cv2.convertScaleAbs(sobelx), 0.5, cv2.convertScaleAbs(sobely), 0.5, 0)
        
        pil_img = Image.fromarray(edges)
        tk_img = ImageTk.PhotoImage(image=pil_img)
        
        camera_canvas.create_image(0, 0, anchor="nw", image=tk_img)
        app.update()
                
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
pass

# __________________________________________________________________________________________________________________

def contour_detection():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 127, 255, 0)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        img_with_contours = cv2.drawContours(img.copy(), contours, -1, (0, 255, 0), 3)
        
        pil_img = Image.fromarray(img_with_contours)
        tk_img = ImageTk.PhotoImage(image=pil_img)
        
        camera_canvas.create_image(0, 0, anchor="nw", image=tk_img)
        app.update()
                
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
pass

# __________________________________________________________________________________________________________________

def heat_vision():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, img = cap.read()
        img_colorized = cv2.applyColorMap(img, cv2.COLORMAP_JET)
        img_colorized_rgb = cv2.cvtColor(img_colorized, cv2.COLOR_BGR2RGB)
        
        pil_img = Image.fromarray(img_colorized_rgb)
        tk_img = ImageTk.PhotoImage(image=pil_img)
        
        camera_canvas.create_image(0, 0, anchor="nw", image=tk_img)
        app.update()
        
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
pass


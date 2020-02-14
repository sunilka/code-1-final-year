import cv2 
from gtts import gTTS 

import os 
mytext = 'Hello,,,,, You have choosen the option to convert the image to text. Please hold the image in front and wait. After few seconds tap key to capture the image'
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
file = open("C:\\Users\\Shruthi\\welcome.mp3")
file.close();
os.system("welcome.mp3") 
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
import time
time.sleep(3)

#implementing the image capture for the text to speech convertion
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(1)
while True:
    try:
        check, frame = webcam.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(gray,(500,500))
            print("Resized...")
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            #print(img_resized)
            print("Image saved!")
            mytext = 'Image captured... Converting the image to text. Please wait'
            language = 'en'
            
            myobj = gTTS(text=mytext, lang=language, slow=False) 
            myobj.save("welcome.mp3") 
            file = open("C:\\Users\\Shruthi\\welcome.mp3")
            file.close();
            os.system("welcome.mp3") 
            mytext = 'hello how are you doing'
            language = 'en'
            myobj = gTTS(text=mytext, lang=language, slow=False) 
            myobj.save("welcome.mp3") 
            webcam.release()
            import pytesseract       
           
            # adds image processing capabilities 
            from PIL import Image     
              
             # converts the text to speech   
            import pyttsx3            
              
            #translates into the mentioned language 
            from googletrans import Translator       
              
             # opening an image from the source path 
            img = Image.open('saved_img-final.jpg')      
              
            # describes image format in the output 
            print(img)                           
            # path where the tesseract module is installed 
            pytesseract.pytesseract.tesseract_cmd ='C:\\Users\\Shruthi\\Desktop\\TesseractOCR\\tesseract.exe'   
            # converts the image to result and saves it into result variable 
            result = pytesseract.image_to_string(img)    
            # write text in a text file and save it to source path    
            with open('abc.txt',mode ='w') as file:      
                  
                             file.write(result) 
                             print(result) 
                               
            p = Translator()                       
            # translates the text into german language 
            k = p.translate(result,dest='english')       
            print(k) 
            engine = pyttsx3.init() 
              
            # an audio will be played which speaks the test if pyttsx3 recognizes it 
            engine.say(k)                              
            engine.runAndWait() 
        
            break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            mytext = 'Image to text conversion program terminated'
            language = 'en'
            
            myobj = gTTS(text=mytext, lang=language, slow=False) 
            myobj.save("welcome.mp3") 
            file = open("C:\\Users\\Shruthi\\welcome.mp3")
            file.close();
            os.system("welcome.mp3") 
            mytext = 'hello how are you doing'
            language = 'en'
            myobj = gTTS(text=mytext, lang=language, slow=False) 
            myobj.save("welcome.mp3") 
            webcam.release()
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
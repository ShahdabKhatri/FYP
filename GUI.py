import tkinter as tk
import numpy as np
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
import tensorflow as tf
import keras
import cv2

#load the trained model to classify the images

from keras.models import load_model
model = load_model('sup.h5')
model1=load_model('sub1.h5')
model2=load_model('sub2.h5')
model3=load_model('sub3.h5')                  
model4=load_model('sub4.h5')
model5=load_model('sub5.h5')
model6=load_model('sub6.h5')
model7=load_model('sub7.h5')
model8=load_model('sub8.h5')
model9=load_model('sub9.h5')
model10=load_model('sub10.h5')
model11=load_model('sub11.h5')
model12=load_model('sub12.h5')
model13=load_model('sub13.h5')

                  
bay={1:'ٹ',2:'ت',3:'ٿ',4:'ٺ',5:'پ',6:'ث',7:'ٽ',8:'ٻ',9:'ڀ',10:'ب'}
jeem={1:'ح',2:'ج',3:'ڄ',4:'ڇ',5:'ڃ',6:'چ',7:'خ'}
daal={1:'ڌ',2:'ڊ',3:'ڍ',4:'ڈ',5:'د',6:'ذ',7:'ڏ'}
ra={1:'ر',2:'ز',3:'ڑ',4:'ڙ',5:'ژ'}
kaf={1:'ک',2:'گ',3:'ڳ',4:'ڱ'}
non={1:'ں',2:'ن',3:'ڻ',4:'ل'}
fa={1:'ف',2:'ڦ',3:'ق'}
jhay={1:'ھ',2:'جھ',3:'گھ'}
seen={1:'س',2:'ش'}
swad={2:'ض',1:'ص'}
twa={1:'ط',2:'ظ'}
ain={1:'ع',2:'غ'}
ya={1:'ی',2:'ي'}
classes={14:'و',15:'ء',16:'ڪ',17:'ے',18:'ا'}
#initialise GUI

top=tk.Tk()
top.geometry('800x600')
top.title('Offline Urdu and Sindhi Handwritten Character Recognition')
top.configure(background='#CDCDCD')
label=Label(top,background='#CDCDCD', font=('arial',100,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    path=file_path
    img  =cv2.imread(path,0)
    img2 =cv2.resize(img,(32,32))
    img3 = np.expand_dims(img2, axis=0)
    img4 = np.expand_dims(img3,axis=-1)
    prediction=np.argmax(model.predict(img4),axis=-1)
    sup=prediction[0]+1
    sign=0
    if sup == 1:
        prediction=np.argmax(model1.predict(img4),axis=-1)
        sign=bay[prediction[0]+1]
    elif sup == 2:
        prediction=np.argmax(model2.predict(img4),axis=-1)
        sign=jeem[prediction[0]+1]
    elif sup == 3:
        prediction=np.argmax(model3.predict(img4),axis=-1)
        sign=daal[prediction[0]+1]
    elif sup == 4:
        prediction=np.argmax(model4.predict(img4),axis=-1)
        sign=ra[prediction[0]+1]
    elif sup == 5:
        prediction=np.argmax(model5.predict(img4),axis=-1)
        sign=kaf[prediction[0]+1]
    elif sup == 6:
        prediction=np.argmax(model6.predict(img4),axis=-1)
        sign=non[prediction[0]+1]
    elif sup == 7:
        prediction=np.argmax(model7.predict(img4),axis=-1)
        sign=fa[prediction[0]+1]
    elif sup == 8:
        prediction=np.argmax(model8.predict(img4),axis=-1)
        sign=jhay[prediction[0]+1]
    elif sup == 9:
        prediction=np.argmax(model9.predict(img4),axis=-1)
        sign=seen[prediction[0]+1]
    elif sup == 10:
        prediction=np.argmax(model10.predict(img4),axis=-1)
        sign=swad[prediction[0]+1]
    elif sup == 11:
        prediction=np.argmax(model11.predict(img4),axis=-1)
        sign=twa[prediction[0]+1]
    elif sup == 12:
        prediction=np.argmax(model12.predict(img4),axis=-1)
        sign=ain[prediction[0]+1]
    elif sup == 13:
        prediction=np.argmax(model13.predict(img4),axis=-1)
        sign=ya[prediction[0]+1]
    elif sup == 14 or sup ==15 or sup==16 or sup==17 or sup==18:
        sign=classes[sup]

    print(sign)
    label.configure(foreground='#011638', text=sign) 

def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",
   command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',
font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded = uploaded.resize((200, 200), Image.ANTIALIAS)
        uploaded.thumbnail(((top.winfo_width()/2.25),
        (top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image,
  padx=10,pady=5)

upload.configure(background='#364156', foreground='white',
    font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Offline Urdu and Sindhi Handwritten Chracter Recognition",pady=20, font=('arial',20,'bold'))

heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()

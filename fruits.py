import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from keras.preprocessing import image
import os
from keras.models import load_model

model = load_model('filename.model')

classes = {0: 'Apple Braeburn', 1: 'Apple Golden1', 2: 'Apple Golden2', 3: 'Apple Golden3', 4: 'Apple GrannySmith',5: 'Apple Red', 6: 'Apple Red', 7: 'Apple Red', 8: 'Apple Red Delicious', 9: 'Apple Red Yellow', 10: 'Apricot', 11: 'Avocado', 12: 'Avocado Ripe', 13: 'Banana', 14: 'Banana Red', 15: 'Cactus Fruit', 16: 'Cantaloupe', 17: 'Cantaloupe', 18: 'Carambula', 19: 'Cherry 1', 20: 'Cherry 2', 21: 'Cherry Rainier', 22: 'Cherry Wax Black', 23: 'Cherry Wax Red', 24: 'Cherry Wax Yellow', 25: 'Clementine', 26: 'Cocos', 27: 'Dates', 28: 'Granadilla', 29: 'Grape fruit Pink', 30: 'Grape fruit White', 31: 'Grape Pink', 32: 'Grape White', 33: 'Grape White2', 34: 'Guava', 35: 'Huckle berry', 36: 'Kaki', 37: 'Kiwi', 38: 'Kumquats', 39: 'Lemon', 40: 'Lemon Meyer', 41: 'Limes', 42: 'Lychee', 43: 'Mandarine', 44: 'Mango',  45: 'Maracuja', 46: 'Melon Piel deSapo', 47: 'Mulberry', 48: 'Nectarine', 49: 'Orange', 50: 'Papaya', 51: 'Passion Fruit', 52: 'Peach', 53: 'Peach Flat', 54: 'Pear', 55: 'Pear Abate', 56: 'Pear Monster', 57: 'Pear Williams', 58: 'Pepino', 59: 'Physalis', 60: 'Physalis With Husk', 61: 'Pineapple', 62: 'Pineapple Mini', 63: 'Pitahaya Red', 64: 'Plum', 65: 'Pomegranate', 66: 'Quince', 67: 'Rambutan', 68: 'Raspberry', 69: 'Salak', 70: 'Strawberry', 71: 'Strawberry Wedge', 72: 'Tamarillo', 73: 'Tangelo', 74: 'Tomato', 75: 'Tomato', 76: 'Tomato', 77: 'Tomato', 78: 'Tomato Cherry Red', 79: 'Tomato Maroon', 80: 'Walnut' }

top = tk.Tk()
top.geometry('1200x900')
top.title('Fruit classification')
top.configure(background='#4EA24E')
label = Label(top, background='#4EA24E', font=('arial', 20, 'bold'))
sign_image = Label(top)


def classify(file_path):
    images = Image.open(file_path)
    images = images.resize((30, 30))
    images = np.expand_dims(images, axis=0)
    images = np.array(images)
    print(images.shape)
    predict = model.predict_classes([images])
    print(predict)
    sign = classes[predict[0]]
    print(sign)
    label.configure(foreground='black', text=sign)


def show_classify_button(file_path):
    classify_b = Button(top, text="Classify Image", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#4EA24E', foreground='white', font=('arial', 15, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 0.25), (top.winfo_height() / 0.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        print("ERROR")


upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
upload.configure(background='#4EA24E', foreground='white', font=('arial', 15, 'bold'))

upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Know Your Fruit", pady=20, font=('arial', 25, 'bold'))
heading.configure(background='#4EA24E', foreground='#164156')
heading.pack()
top.mainloop()

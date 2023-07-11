# Google Translate
# pip install googletrans
# pip install textblob
# pip install pillow

from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob
from PIL import Image, ImageTk

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)      # เป็นการเรียกให้ทำงานซ้ำๆ ทุก ๆ 1000 มิลลิวินาที หรือ 1วินาที

def translate_now():
    global language
    try:
        text_ = text1.get(1.0, END)
        c2 = combo1.get()
        c3 = combo2.get()
        if text_:
            words = textblob.TextBlob(text_)
            lan = words.detect_language()
            for i, j in language.items():
                if j == c3:
                    lan_ = i
            words = words.translate(from_lang=lan, to=str(lan_))
            text2.delete(1.0, END)
            text2.insert(END, words)
    except Exception as e:
        messagebox.showerror("googletrans", "please try again")

def label_clear():
    text1.delete('1.0', END)
    text2.delete('1.0', END)
    text1.focus()

root = Tk()
root.title("Google Translator")
root.geometry('1080x400')
root.configure(bg='white')

# icon
image_icon = PhotoImage(file="google.png")
root.iconphoto(False, image_icon)

# arrow image
image = Image.open("arrow.png")         # อ่านไฟล์รูปภาพ
resize_image = image.resize((120, 120))     # ปรับขนาดรูป

arrow_image = ImageTk.PhotoImage(resize_image)      # แปลงรูปเป็น PhotoImage
image_label = Label(root, image=arrow_image, width=120)     # สร้าง Label และนำรูปภาพไปใส่
image_label.place(x=475, y=53)      # วางรูปภาพ

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1 = ttk.Combobox(root, values=languageV, font=('Arial', 14), state="r")
combo1.place(x=110, y=20)
combo1.set("English")

label1 = Label(root, text="ENGLISH", font=('segoe', 30, 'bold'), bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=53)

# Frame
f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=120, width=444, height=210)

text1 = Text(f, font="Robot 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=433, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font=('Arial', 14), state="r")
combo2.place(x=730, y=20)
(combo2.set("SELECT LANGUAGE"))

label2 = Label(root, text="ENGLISH", font=('segoe', 30, 'bold'), bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=53)

# Frame1
f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=120, width=444, height=210)

text2 = Text(f1, font="Robot 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=433, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# translate Button
translateBtn = Button(root, text="Translate", font="Roboto 15 bold", width=10,
                      bg="mediumpurple", fg="white",
                      activebackground="indigo",
                      activeforeground="white",
                      cursor="hand2", bd=3,
                      command=translate_now)
translateBtn.place(x=470, y=240)

# clear Button
clearBtn = Button(root, text="Clear", font="Roboto 15 bold", width=10,
                      bg="red", fg="white",
                      activebackground="maroon",
                      activeforeground="white",
                      cursor="hand2", bd=3,
                      command=label_clear)
clearBtn.place(x=470, y=285)

label_change()

root.mainloop()
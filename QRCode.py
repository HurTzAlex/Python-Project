# QR Code generator
# pip install pyqrcode
# pip install pillow

import pyqrcode
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil

def generateQRCode(link, file_name):
    url = pyqrcode.create(link)
    url.png(file_name, scale=5)

def createQR():
    link = entry_link.get()
    if link == "":
        messagebox.showwarning("Error", "Please Enter QR Code name & URL")
    else:
        file_name = ".png"
        generateQRCode(link, file_name)

        canvas_qr.delete('all')

        image = ImageTk.PhotoImage(Image.open(file_name))
        canvas_qr.create_image(165, 130, image=image)
        canvas_qr.image = image

        os.remove(file_name)

def saveQR():
    name = entry_name.get()
    link = entry_link.get()
    file_name = name + ".png"

    if name == "" or link == "":
        messagebox.showwarning("Error", "Please Enter QR Code name & URL")
        return

    generateQRCode(link, file_name)

    path = filedialog.asksaveasfilename(defaultextension=".png")

    if path:
        directory = os.path.dirname(path)
        full_path = os.path.join(directory, file_name)
        shutil.move(file_name, full_path)

        if os.path.exists(file_name):
            os.remove(file_name)
            messagebox.showinfo("Success", "QR Code is Saved")

def clear():
    entry_name.delete(0, 'end')
    entry_link.delete(0, 'end')
    canvas_qr.delete('all')

# GUI
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("350x420")
root.config(bg="white")  # กำหนดสีของหน้าต่างหลัก
root.resizable(0, 0)  # กำหนดขนาดคงที่

# Top frame
frame_top = tk.Frame(root, bd=2, relief=tk.RAISED)  # RAISED กำหนด frame ให้แสดงเส้นขอบที่ยกขึ้น
frame_top.place(x=10, y=10, width=330, height=270)

canvas_qr = tk.Canvas(frame_top)
canvas_qr.pack(fill=tk.BOTH)

# Bottom frame
frame_bottom = tk.Frame(root, bd=2, relief=tk.SUNKEN)  # SUNKEN ทำให้จม
frame_bottom.place(x=10, y=290, width=330, height=120)

label_name = tk.Label(frame_bottom, text="QR Code name :")
label_name.place(x=7, y=10)

label_url = tk.Label(frame_bottom, text="URL :")
label_url.place(x=66, y=50)

# Entry
entry_name = ttk.Entry(frame_bottom, width=30, font=('arial', 10))
entry_name.place(x=100, y=10)

entry_link = ttk.Entry(frame_bottom, width=30, font=('arial', 10))
entry_link.place(x=100, y=50)

# Button
btn_create = ttk.Button(frame_bottom, text="Create", width=13, command=createQR)
btn_create.place(x=30, y=85)

btn_save = ttk.Button(frame_bottom, text="Save", width=13, command=saveQR)
btn_save.place(x=120, y=85)

btn_clear = ttk.Button(frame_bottom, text="Clear", width=13, command=clear)
btn_clear.place(x=210, y=85)

root.mainloop()
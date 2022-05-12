from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.geometry("700x700")
root.title("Photoshop 2.0")
root.config(background="#ff4e00")

image = Label(root, image="", bg="#a3f7b5", highlightthickness=2, highlightcolor="#3590f3")
image.place(relx=0.5, rely=0.1, anchor=CENTER)

button = Button(root, text="Open Image",foreground="#ff4e00", font=("Comic Sans MS", "12", "normal"), command=openimage)
button.place(relx=0.8, rely=0.5, anchor=CENTER)
img_path = ""

def openimage():
    global image_path
    image_path = filedialog.askopenfilename(title = "Scanning your computers for viruses and then opening your image",
                                            filetypes = (("png files", "*.png"),))
    print(image_file)
    print(image_path)
    image_file = ImageTk.PhotoImage(Image.open(image_path))
    image['image'] = str(image_file)
    image_path.close()
    
root.mainloop()
from tkinter import ttk, Tk, PhotoImage, Canvas
#from PIL import ImageTk, Image

root = Tk()

frame_header = ttk.Frame()
frame_header.pack()

ttk.Label(frame_header, text="my first tkinter").pack()

def click_button():
  print("I am clicked.")

ttk.Button(root, text="click me", command=click_button).pack()

logo = PhotoImage(file="sample.png").subsample(50,50)

canvas = Canvas(root, bg="grey", width=300, height=400)
canvas.pack()

canvas.create_image(300/2, 400/2, image=logo)

#ttk.Label(frame_header, image=logo).pack()

root.mainloop()
from tkinter import ttk, Tk, PhotoImage
#from PIL import ImageTk, Image

root = Tk()

ttk.Label(root, text="my first tkinter").pack()

def click_button():
  print("I am clicked.")

ttk.Button(root, text="click me", command=click_button).pack()

logo = PhotoImage(file="sample.png").subsample(10,10)

ttk.Label(root, image=logo).pack()

root.mainloop()
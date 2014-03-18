from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.minsize(500,500)

notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand='yes')

#Crear frames
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

#agregar los frames al notebook con el texto de la pestanna
notebook.add(frame1, text='Uno')
notebook.add(frame2, text='Dos')

#Label en el frame 1
etiquetatexto1 = Label(frame1, text = "Este es el frame 1", font = ("calibri","12"), bg = "#00ff04", fg = "#000b98", width= 28, height = 1)
etiquetatexto1.place(x = 20, y = 20)

#Label en el frame 2
etiquetatexto2 = Label(frame2, text = "Este es el frame 2", font = ("calibri","12"), bg = "#00ff04", fg = "#000b98", width= 28, height = 1)
etiquetatexto2.place(x = 20, y = 20)

ventana.mainloop()

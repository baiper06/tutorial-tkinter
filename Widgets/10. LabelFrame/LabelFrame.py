from tkinter import *

ventana = Tk()
ventana.minsize(500,500)

#Se crea el label frame con el texto respectivo ademas de su largo y ancho
labelframe = LabelFrame(ventana, text="Computadores CE", width = 400, height = 400)
labelframe.place(x = 50, y = 50)

#Se crea una etiqueta dentro del label frame
etiqueta = Label(labelframe, text="Este label esta contenido en el labelframe")
etiqueta.place(x = 20, y = 20)

ventana.mainloop()

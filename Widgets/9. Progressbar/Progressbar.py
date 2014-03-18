from tkinter import *
from tkinter import ttk

#esta funcion incrementa el progreso de la barra
def incrementar(event):
    barraprogreso.step(5)

ventana = Tk()
ventana.minsize(500,500)

#se crea la barra de progreso en donde se le asigna un largo
barraprogreso = ttk.Progressbar(ventana, length=300)
barraprogreso.place(x = 100, y = 10)

#se crea un boton que llama a la funcion incrementar
boton = Button(ventana, text="Avanzar")
boton.bind("<Button-1>", incrementar)
boton.place(x = 210, y = 100)

ventana.mainloop()

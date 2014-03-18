from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.minsize(500,500)

#se crea una lista de valores para agregarlos al combobox
valoresCombobox = ('Numero uno', 'Numero dos', 'Numero tres' )

#se crea una variable stringvar que contendra el dato seleccionado en el combobox
variableCombo = StringVar()
variableCombo.set('Elije un numero')

#Se crea el combobox
#Combobox(widgetcontenedor, lista valores iniciales, variable de texto, largo)
combobox = ttk.Combobox(ventana, values=valoresCombobox, textvariable=variableCombo, width = 20)
combobox.place(x = 10, y = 10)

#Se crea una funcion para mostrar el dato seleccionado en el dato seleccionado
def MostrarSeleccion():
    print(variableCombo.get())

#Se crea un boton para mostrar la informacion del combobox
boton = Button(ventana, text="Mostrar", command=MostrarSeleccion, bg = "#000000", fg = "#ffffff")
boton.place(x=10,y=150)

ventana.mainloop()

from tkinter import * 

ventana = Tk()

ventana.title("Computadores CE") 
ventana.minsize(500,500) 
ventana.maxsize(500,500)

#funcion que muestra lo ingresado en pantalla por medio de un message box
def mostrarValor():
    messagebox.showinfo("Titulo mensaje",str(entrada.get()))

#Funcion que inserta en el entry la frase "Hola Mundo"
def insertarValor():
    entrada.insert(0, "Hola Mundo")

#Funcion que borra lo ingresado en el entry
def borrarValor():
    #entrada.delete(inicioBorrar, finalBorrar)
    entrada.delete(0, END)
    
#crea el entry
#entrada = Entry(widgetContenedor, width)  
entrada = Entry(ventana, width=50)
entrada.place(x=100,y=100)

#Aqui se crean los botones

#Boton mostrar
#botonMostrar = Button(widgetContenedor, text=contenido, command=funcionLlamada, bg = colorDeFondo, fg = colorDeLetra)
botonMostrar = Button(ventana, text="Mostrar", command=mostrarValor, bg = "#000000", fg = "#ffffff")
botonMostrar.place(x=130,y=150)
#Boton insetar
botonHola = Button(ventana, text="Insertar", command=insertarValor, bg = "#000000", fg = "#ffffff")
botonHola.place(x=200,y=150)
#Boton borrar
botonBorrar = Button(ventana, text="Borrar", command=borrarValor, bg = "#000000", fg = "#ffffff")
botonBorrar.place(x=260,y=150)


ventana.mainloop()

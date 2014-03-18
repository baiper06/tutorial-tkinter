from tkinter import * 
#Label(etiqueta)

ventana = Tk()

ventana.title("Computadores CE") 
ventana.minsize(500,500) 
ventana.maxsize(500,500)

#Label con texto
#etiquetatexto = Label(WidgetContenedor, text=Contenido, font = (Tipo,Tamanno), bg=ColorDeFondo, fg=ColorDeLetra, width, height)
etiquetatexto = Label(ventana, text = "Bienvenidos Computadores", font = ("calibri","23"), bg = "#00ff04", fg = "#000b98", width= 28, height = 1)
etiquetatexto.place(x = 20, y = 20)

#Se crea el widget PhotoImage con la direccion de la imagen
imagen = PhotoImage(file="CE.gif")

#Label con una imagen
etiquetaimagen = Label(ventana, image = imagen, cursor="circle", bd=2, bg="#000000")
#asignarle la imagen
etiquetaimagen.image = imagen
etiquetaimagen.place(x = 120, y = 150)

ventana.mainloop()

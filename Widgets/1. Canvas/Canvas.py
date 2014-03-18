from tkinter import *

ventana = Tk()

ventana.title("Computadores CE") 
ventana.minsize(1000,500) 
ventana.maxsize(1100,500)

#Crear canvas
#canvas = Canvas(WidgetContenedor, Ancho, Alto, bg=colorDeFondo)
canvas = Canvas(ventana , width= 900, height = 500, bg = "#eeaa02")

#Dibujar lineas en el canvas
#canvas.create_line(Xinicio, Yinicio, Xfinal, Yfinal, fill=colorDeLinea)
canvas.create_line(50, 50, 50, 450, fill="#990000", dash=(4, 4))
canvas.create_line(100, 50, 100, 450, fill="#000000")

#Escribir en el canvas
#canvas.create_text(Xinicio, YInicio, text=Contenido, font = (TipoLetra, Tamanno), anchor=anclaje)
canvas.create_text(150,50,text="Somos ASEIC", font = ("Times New Roman","18"),anchor =NW)
canvas.create_text(150,100,text="Computadores", font = ("Times New Roman","18"),anchor =NW)

#Dibujar figuras en el canvas
#canvas.create_rectangle(Xinicio, Yinicio, Xfinal, Yfinal, fill=colorDeFondo)
canvas.create_rectangle(350, 50, 450, 150, fill="#ffffff")

#Mostrar una imagen en un canvas
imagen = PhotoImage(file = "computadores.gif")
canvas.create_image(150,175,anchor=NW,image = imagen)

#Reducir Tamanno Imagen
#En el ejemplo se divide el ancho y largo original entre dos
imagenreducida = imagen.subsample(x=2,y=2)
canvas.create_image(600,300,anchor=NW,image = imagenreducida)

#Ubicar canvas
canvas.place(x=0, y=0)

ventana.mainloop()

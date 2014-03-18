#aqui lo que se hace es importa la librería tkinter
from tkinter import * 

#Ventana

#se le asigna a la variable ventana dicho sea de paso la ventana
ventana = Tk()
#se le asigna el nombre que va a tener la ventana
ventana.title("Computadores CE")
#definimos el tamaño minimo que va a tener nuestra ventana especificamente corresponden al ancho x alto
ventana.minsize(300,300)
#definimos el tamaño maximo que va a tener nuestra ventana especificamente corresponden al ancho x alto
ventana.maxsize(600,700)

#Muestra las coordenadas donde se hace un click en el formato x,y
def mostrarCoordenada(event):
    x = event.x
    y = event.y
    print (x, y)

#se vincula la funcion mostrarCoordenada a la ventana, por medio del evento <Button-1>
ventana.bind("<Button-1>", mostrarCoordenada)

#esto lo que hace es mostrar la ventana en pantalla
ventana.mainloop()

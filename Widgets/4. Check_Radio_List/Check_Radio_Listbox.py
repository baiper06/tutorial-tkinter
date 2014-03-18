from tkinter import * 

ventana = Tk()

ventana.title("Computadores CE") 
ventana.minsize(500,500) 
ventana.maxsize(500,500)

#funcion llamada en el boton
def imprimirvalores():
    print("Elijio facebook : "+str(variableCheck1.get()))
    print("Elijio twitter  : "+str(variableCheck2.get()))
    print("Elijio el numero: "+str(variableRadio.get()))
    print("Elijio del listbox: "+lista.get(ACTIVE))

#variable modificadas por los checks
variableCheck1 = IntVar()
variableCheck2 = IntVar()
#crear CheckButton
check1 = Checkbutton(ventana, text="Facebook", variable=variableCheck1)
check1.place(x=20,y=20)
check2 = Checkbutton(ventana, text="Twitter", variable=variableCheck2)
check2.place(x=20,y=40)

#variable modificada por los radios
variableRadio = IntVar()
#crear rodioButton
radio1 = Radiobutton(ventana, text="Numero 1", variable=variableRadio, value=1)
radio1.place(x=150,y=20)
radio2 = Radiobutton(ventana, text="Numero 2", variable=variableRadio, value=2)
radio2.place(x=150,y=40)

#crear ListBox
lista = Listbox(ventana, width = 20, height = 10)
lista.place(x=300,y=20)
#insertar con un for
for numeros in ["Numero uno", "Numero dos", "Numero tres", "Numero cuatro"]:
    lista.insert(END, numeros) 
#insercion al incio
lista.insert(0,   "Este es el inicio")
#insercion al final
lista.insert(END, "Este es el final")
    
boton = Button(ventana, text="prueba", command=imprimirvalores)
boton.place(x=150,y=150)


ventana.mainloop()

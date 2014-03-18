from tkinter import *

ventana = Tk()
ventana.minsize(500,500)

def Opcion1():
    print ("click en: opcion uno")

def Opcion2():
    print ("click en: opcion dos") 

#se crea el widget menu
barramenu = Menu(ventana)
barramenu.add_command(label="Opcion uno", command=Opcion1)
barramenu.add_command(label="Opcion dos", command=Opcion2)

#Se le asigna el menu a la ventana
ventana.config(menu=barramenu)
ventana.mainloop()

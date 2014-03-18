from tkinter import * 
#Label(etiqueta)

ventana = Tk()

ventana.title("Computadores CE") 
ventana.minsize(700,600) 
ventana.maxsize(700,600)

#Cavas de fondo
canvasFondo = Canvas(ventana , width= 600, height = 600, bg = "#50328B")
canvasFondo.place( x = 0, y = 0)

#Canvas que contiene los scrolls y el canvas que se le hara scroll
canvasContenedor = Canvas(canvasFondo,width=100,height=100)
canvasContenedor.place(x = 100, y = 150)

#scrolly = Scrollbar(widgetContenedor,orient=horientacion)
scrolly = Scrollbar(canvasContenedor,orient=VERTICAL)
scrolly.grid(row=0, column=1, sticky=N+S)

##scrollx = Scrollbar(widgetContenedor,orient=horientacion)
scrollx = Scrollbar(canvasContenedor,orient=HORIZONTAL)
scrollx.grid(row=1, column=0, sticky=E+W)

#canvasScroll = Canvas(widgetContenedor,width,height,bg=colorDeFondo,relief = relieve,bd = tamanoBorde,
#                   yscrollcommand=scrollEnY.set,xscrollcommand=scrollEnX.set,scrollregion=(xinicial,yinicial,xfinal,yfinal))
canvasScroll = Canvas(canvasContenedor,width=350,height=400,bg="#058FE0",relief=RAISED,bd=0,yscrollcommand=scrolly.set,xscrollcommand=scrollx.set,scrollregion=(0,0,1000,1000))
canvasScroll.grid(row=0,column=0,sticky=N+S+E+W)

#Configuracion de el scroll
scrolly.config(command=canvasScroll.yview)
scrollx.config(command=canvasScroll.xview)

#Escribe texto en el cavas que se le hizo scroll
canvasScroll.create_text(40,20,text="Esto es un Cubo", font = ("Times New Roman","18"),anchor =NW,fill = "#ffffff")

#Dibuja el cubo en el canvas que se le hizo scroll
canvasScroll.create_line(40, 100, 200, 100, fill="#000000")
canvasScroll.create_line(40, 260, 200, 260, fill="#000000")
canvasScroll.create_line(40, 100, 40, 260, fill="#000000")
canvasScroll.create_line(200, 100, 200, 260, fill="#000000")

canvasScroll.create_line(90, 150, 250, 150, fill="#000000")
canvasScroll.create_line(90, 310, 250, 310, fill="#000000")
canvasScroll.create_line(90, 150, 90, 310, fill="#000000")
canvasScroll.create_line(250, 150, 250, 310, fill="#000000")

canvasScroll.create_line(40, 100, 90, 150, fill="#000000")
canvasScroll.create_line(200, 100, 250, 150, fill="#000000")
canvasScroll.create_line(40, 260, 90, 310, fill="#000000")
canvasScroll.create_line(200, 260, 250, 310, fill="#000000")

#Escribe texto en el canvas que esta de fondo
canvasFondo.create_text(100,50,text="Taller Tkinter", font = ("Times New Roman","18"),anchor =NW,fill = "#ffffff")
canvasFondo.create_text(100,100,text="Scroll Bar", font = ("Times New Roman","18"),anchor =NW, fill = "#ffffff")

ventana.mainloop()

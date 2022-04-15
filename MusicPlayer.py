#Importar las librerias necesarias
from tkinter import *
from pygame import mixer

#Definir las fuentes de texto que vamos a utilizar
fuente1=('Arial',20,"bold")
fuente2=('Arial',15)

#Crear una funcion especificando lo que deberan hacer los botones. Los parametros (a,b,c,d) se refiern a ('Archivo de la cancion','Imagen del artista','Nombre de la canción','Nombre del artista')
def boton(a,b,c,d):
    for i in range(1):
        #Reproducir la cancion que especifiquemos
        mixer.init()
        mixer.music.load (a)
        mixer.music.play()


        
        f1=Frame(ventana,bg='dimgray')
        f1.place(x=0,y=0,width=500,height=150)
        
        #Mostar imagen por pantalla
        global img
        img=PhotoImage(file=b)
        lbl_img=Label(ventana,image=img,bg='dimgray')
        lbl_img.place(x=350,y=20,width=100,height=100)
    
        #Mostrar el Nombre de la cancion y el Nombre del artista por pantalla
        Titulo=Label(ventana,text=c,bg='dimgray',fg='lime',font=fuente1)
        Titulo.place(x=50,y=35)
        Autor=Label(ventana,text=d,bg='dimgray',fg='white',font=fuente2)
        Autor.place(x=50,y=85)
       
#Estas son las funciones que ejecutan cada uno de los botones. Se ejecuta la función boton, especificando('Archivo de la cancion','Imagen del artista','Nombre de la canción','Nombre del artista')
def b1():
    boton('Song1.mp3','Image1.png','Song Name','Artist Name')
def b2():
    boton('Song2.mp3','Image2.png','Song Name','Artist Name')
def b3():
    boton('Song3.mp3','Image3.png','Song Name','Artist Name')
def b4():
    boton('Song4.mp3','Image4.png','Song Name','Artist Name')
def b5():
    boton('Song5.mp3','Image5.png','Song Name','Artist Name')
def b6():
    boton('Song6.mp3','Image6.png','Song Name','Artist Name')
def b7():
    boton('Song7.mp3','Image7.png','Song Name','Artist Name')
def b8():
    boton('Song8.mp3','Image8.png','Song Name','Artist Name')

#Funcion que se ejecuta al pulsar el boton de pausa
def pause():
    mixer.music.pause()

#Crear la ventana y los widgets
ventana=Tk()
ventana.geometry('500x600')
ventana.resizable(0,0)
ventana.config(bg='dimgray')


Boton1=Button(ventana,bg='Lime',fg='black',text='Song Name',command=b1)
Boton1.place(y=150,x=50,width=100,height=50)

Boton2=Button(ventana,bg='Lime',fg='black',text='SOng Name',command=b2)
Boton2.place(y=150,x=200,width=100,height=50)

Boton3=Button(ventana,bg='Lime',fg='black',text='Song Name',command=b3)
Boton3.place(y=150,x=350,width=100,height=50)

Boton4=Button(ventana,bg='Lime',fg='Black',text='Song Name',command=b4)
Boton4.place(y=300,x=50,width=100,height=50)


Boton5=Button(ventana,bg='Lime',fg='Black',text='Song Name',command=b5)
Boton5.place(x=350,y=300,width=100,height=50)

Boton6=Button(ventana,bg='Lime',fg='Black',text='Song Name',command=b6)
Boton6.place(x=50,y=450,width=100,height=50)

Boton7=Button(ventana,bg='Lime',fg='Black',text='Song Name',command=b7)
Boton7.place(x=200,y=450,width=100,height=50)

Boton8=Button(ventana,bg='Lime',fg='Black',text='Song Name',command=b8)
Boton8.place(x=350,y=450,width=100,height=50)  

BotonP=Button(ventana,bg='Lime',fg='Black',command=pause,text='| |')
BotonP.place(y=300,x=200,width=100,height=50)

f2=Frame(ventana,bg='lime')
f2.place(x=0,y=575,width=500,height=50)
ventana.mainloop()


from tkinter import *
from tkinter import messagebox
import tkinter
import webbrowser
import random
import pygame,sys
from pygame.locals import *

# Ventana Principal
class menu(tkinter.Tk):

    def __init__(menu):

        # La ventana del Menu Principal con sus respectivas caracteristicas.
        tkinter.Tk.__init__(menu)
        menu.title("KenKen")
        menu.geometry("900x720")
        menu.resizable(width = False, height = False)

        # Esta sera una variable global necesaria porque se utilizara en distintas funciones.
        global ImagenFondoMenu

        # Esta sera la imagen que aparecera en la ventanas.
        ImagenFondoMenu = PhotoImage(file = "Black-and-white-anime-wolves-29-cool-hd-wallpaper.png")
        FondoMenu = Label(menu, image = ImagenFondoMenu)
        FondoMenu.place(x = -2, y = -2) 
        
        # Estos seran todos los botones que apareceran en la ventana.
        menu.buttonJugar = Button(menu, text = "Jugar", activebackground = "#4285f4", fg = "white", bg = "#4285f4", font = ("Comic Sans Ms", 11), width = 20, heigh = 3, command = menu.JugarMenu)
        menu.buttonJugar.place(x = 10, y = 10)

        menu.buttonConfigurar = Button(menu, text = "Configurar", activebackground = "#4285f4", fg = "#4285f4", bg = "White", font = ("Comic Sans Ms", 11), width = 20, heigh = 3, command = menu.Configurar)
        menu.buttonConfigurar.place(x = 10, y = 100)

        # Esta sera la barra de menu que aparecera en la ventana con sus respectivas caracteristicas.
        menubar = Menu(menu)
        menubar.add_command(label = "Manual de Usuario", command = menu.ManualDeUsuario)
        menubar.add_command(label = "Acerca De", command = menu.AcercaDe)
        menubar.add_command(label = "Salir", command = menu.Salir)
        menu.config(menu = menubar)
        
    def JugarMenu(menu):
        # Se cerrara la ventana actual.
        menu.destroy()
        # Se abrira la nueva ventana solicitada.
        Jugar().mainloop()

    def Configurar(menu):
        # Se cerrara la ventana actual.
        menu.destroy()
        # Se abrira la nueva ventana solicitada.
        Configurar().mainloop()

    def ManualDeUsuario(menu):
        # Se abrira el PDF solicitado (Manual de Usuario).        
        webbrowser.open_new(r"manual_de_usuario_kenken.pdf")

    def AcercaDe(menu):
        # Se abrira una nueva ventana con la informacion general del proyecto.
        messagebox.showinfo("Acerca De", "Tecnológico de Costa Rica \nCurso: Taller de Programación \nProyecto 3: Kenken 2.0 \nEstudiantes: \nDaniel Camacho \nJose Ignacio Granados \nSemestre II \n2018")
        
    def Salir(menu):
        # Se abrira una nueva ventana con la opcion de salir del programa, si este es si, entonces el programa se finalizara.
        opcion = messagebox.askquestion("Salir", "¿Seguro que desea salir del programa?", icon = "warning")
        
        if opcion == "yes":
            # Se cerrara la ventana actual.
            menu.destroy()
            exit()

#####################################################################################################################################################################################################################

# Esta sera la ventana donde se encontrara la clase de Jugar.
global Jugador

class Jugar(tkinter.Tk):
    
    def __init__(self):

        # La ventana de Jugar con sus respectivas caracteristicas.
        tkinter.Tk.__init__(self)
        self.title("Jugar")
        self.geometry("1200x700")

        # Esta sera una variable global necesaria porque se utilizara en distintas funciones.
        global ImagenFondo

        # Esta sera la imagen que aparecera en la ventanas.
        ImagenFondo = PhotoImage(file = "710239_geometric-wallpaper-hd.png")
        Fondo = Label(self, image = ImagenFondo)
        Fondo.place(x = 0, y = 0)        

        # Esta sera una variable global necesaria porque se utilizara en distintas funciones.
        global ImagenKenKen

        # Esta sera la imagen que aparecera en la ventanas.
        ImagenKenKen = PhotoImage(file = "coollogo_com-5652650.png")
        KenKen = Label(self, image = ImagenKenKen)
        KenKen.place(x = 345, y = 100)

        self.labelNombre = Label(self, text = "Nombre del Jugador:", fg =  "#000000", font = ("Times New Roman", 17))
        self.labelNombre.place(x = 100, y = 567)

        # Estos seran todos los cuadros de texto que apareceran en la ventana.
        self.textBoxJugador = Entry(self, width = 30, font = ("Serif", 15))
        self.textBoxJugador.place(x = 100, y = 600)

        # Variable Nivel que se utilizara para indicar el nivel que se pulso y su respetiva condicion que determina cual label mostar.
        Nivel = StringVar()
        self.labelNivel = Label(self,textvariable = Nivel, width = 20, font = ("Serif", 17))
        self.labelNivel.place(x = 44, y = 20)

        if N == 1:

            Nivel.set("Nivel \nFácil")
            Nivel = "F"
            
        elif N == 2:

            Nivel.set("Nivel \nIntermedio")
            Nivel = "I"

        elif N == 3:

            Nivel.set("Nivel \nDifícil")
            Nivel = "D"
            
        # Variable Sonido que se utilizara para indicar si el nivel se completo con exito o no.
        Sonido = StringVar()
        self.labelSonido = Label(self,textvariable = Sonido, width = 20, font = ("Serif", 17))
        self.labelSonido.place(x = 44, y = 115)

        if S == 1:

            Sonido.set("Sonido \nSí")
            pygame.init()
            pygame.mixer.music.load("FlowNaruto.mp3")
            
        elif S == 2:

            Sonido.set("Sonido \nNo")
            pygame.mixer.music.stop()
            
        # Cuadricula con sus respectivas caracteristicas que se mostrara en pantalla la cual simbolizara las casillas del juego.
        cuadricula = Frame(self)
        cuadricula.grid(column = 6, row = 6, padx = (10,10), pady = (10,10))
        
        # Estas seran etiquetas vacias que se utilizaran para dar una mejor posicion a la cuadricula.
        label00 = Label(self, width = 7, font = ("Serif", 13))
        label00.grid(column = 0, row = 0)

        label10 = Label(self, width = 7, font = ("Serif", 13))
        label10.grid(column = 1, row = 0)

        label20 = Label(self, width = 7, font = ("Serif", 13))
        label20.grid(column = 2, row = 0)

        label30 = Label(self, width = 7, font = ("Serif", 13))
        label30.grid(column = 3, row = 0)

        label41 = Label(self, width = 7, font = ("Serif", 13)) 
        label41.grid(column = 4, row = 1)

        label42 = Label(self, width = 7, font = ("Serif", 13)) 
        label42.grid(column = 4, row = 2)

        label43 = Label(self, width = 7, font = ("Serif", 13)) 
        label43.grid(column = 4, row = 3)

        label44 = Label(self, width = 7, font = ("Serif", 13)) 
        label44.grid(column = 4, row = 4)

        label45 = Label(self, width = 7, font = ("Serif", 13)) 
        label45.grid(column = 4, row = 5)

        label46 = Label(self, width = 7, font = ("Serif", 13)) 
        label46.grid(column = 4, row = 6)

        label47 = Label(self, width = 7, font = ("Serif", 13)) 
        label47.grid(column = 4, row = 7)

        # Lectura del archivo que contiene las partidas.
        archivo = open("kenken_juegos.dat","r")

        # Variables globales
        global linea
        global listaTop
        global listaF
        global listaI
        global listaD
        global tamaño
        global rehacer
        global deshacer
        global puntero
        global T

        puntero = 0

        listaTop = []

        rehacer = []

        deshacer = []

        linea = archivo.readline()

        dic = archivo.readlines()

        listaF = []
        listaI = []
        listaD = []

        # Algoritmo para poder extraer una partida aleatoria del archivo segun el nivel elegido.
        try:
            
            if T == 1:

                tamaño = 3

                for letra in dic:

                    guia = letra[:2]

                    if guia[-1] == "3":
                        
                        if guia[0] == "F":

                            listaF.append(letra)

                        elif guia[0] == "I":

                            listaI.append(letra)

                        elif guia[0] == "D":

                            listaD.append(letra)

            elif T == 2:

                tamaño = 4

                for letra in dic:

                    guia = letra[:2]

                    if guia[-1] == "4":
                        
                        if guia[0] == "F":

                            listaF.append(letra)

                        elif guia[0] == "I":

                            listaI.append(letra)

                        elif guia[0] == "D":

                            listaD.append(letra)

            elif T == 3:

                tamaño = 5

                for letra in dic:

                    guia = letra[:2]

                    if guia[-1] == "5":
                        
                        if guia[0] == "F":

                            listaF.append(letra)

                        elif guia[0] == "I":

                            listaI.append(letra)

                        elif guia[0] == "D":

                            listaD.append(letra)

            elif T == 4:

                tamaño = 6

                for letra in dic:

                    guia = letra[:2]

                    if guia[-1] == "6":
                        
                        if guia[0] == "F":

                            listaF.append(letra)

                        elif guia[0] == "I":

                            listaI.append(letra)

                        elif guia[0] == "D":

                            listaD.append(letra)

            elif T == 5:

                tamaño = 7

                for letra in dic:

                    guia = letra[:2]

                    if guia[-1] == "7":
                        
                        if guia[0] == "F":

                            listaF.append(letra)

                        elif guia[0] == "I":

                            listaI.append(letra)

                        elif guia[0] == "D":

                            listaD.append(letra)

            elif T == 6:

                tamaño = 8

                for letra in dic:

                    guia = letra[:2]

                    if guia[-1] == "8":
                        
                        if guia[0] == "F":

                            listaF.append(letra)

                        elif guia[0] == "I":

                            listaI.append(letra)

                        elif guia[0] == "D":

                            listaD.append(letra)

            elif T == 7:

                tamaño = 9

                for letra in dic:

                    guia = letra[:2]

                    if guia[-1] == "9":
                        
                        if guia[0] == "F":

                            listaF.append(letra)

                        elif guia[0] == "I":

                            listaI.append(letra)

                        elif guia[0] == "D":

                            listaD.append(letra)

            """

            multitamano

            elif T == 8:

                for letra in dic:

                    guia = letra[:2]

                    if guia[-1] == "4":
                        
                        if guia[0] == "F":

                            listaF.append(letra)

                        elif guia[0] == "I":

                            listaI.append(letra)

                        elif guia[0] == "D":

                            listaD.append(letra)

            """

        except:

            pass

        if N == 1:

            linea = random.choice(listaF)

        elif N == 2:

            linea = random.choice(listaI)

        elif N == 3:

            linea = random.choice(listaD)

        for letra in archivo:

            if letra[0] == Nivel:

                linea = letra

                break
        
        # Valor que se le asignara a la siguiente variable y sus respectivas caracteristicas.
        labelPredicciones = Label(self, width = 12,text = "Predicciones", font = ("Serif", 16)) 
        labelPredicciones.place(x = 950, y = 15)
        
        self.p = StringVar()
        self.p.set("")
        self.Labelp = Label(self, textvariable = self.p, font = ("Serif", 16))
        self.Labelp.place(x = 980, y = 50)

        global a
                
        a = eval(linea[2:-1])
        
        nivel = linea[0]

        lista = []

        colores = []

        # Separa el dicionario por cada casilla.
        for e in range(1,len(a) + 1):

            tupla = a[e][1:]
            colores.append(tupla)

        # Definicion de los widgets para los cuadros texto.
        self.s11 = StringVar()
        self.s12 = StringVar()
        self.s13 = StringVar()
        self.s14 = StringVar()
        self.s15 = StringVar()
        self.s16 = StringVar()
        self.s17 = StringVar()
        self.s18 = StringVar()
        self.s19 = StringVar()
        
        self.s21 = StringVar()
        self.s22 = StringVar()
        self.s23 = StringVar()
        self.s24 = StringVar()
        self.s25 = StringVar()
        self.s26 = StringVar()
        self.s27 = StringVar()
        self.s28 = StringVar()
        self.s29 = StringVar()
        
        self.s31 = StringVar()
        self.s32 = StringVar()
        self.s33 = StringVar()
        self.s34 = StringVar()
        self.s35 = StringVar()
        self.s36 = StringVar()
        self.s37 = StringVar()
        self.s38 = StringVar()
        self.s39 = StringVar()
        
        self.s41 = StringVar()
        self.s42 = StringVar()
        self.s43 = StringVar()
        self.s44 = StringVar()
        self.s45 = StringVar()
        self.s46 = StringVar()
        self.s47 = StringVar()
        self.s48 = StringVar()
        self.s49 = StringVar()
        
        self.s51 = StringVar()
        self.s52 = StringVar()
        self.s53 = StringVar()
        self.s54 = StringVar()
        self.s55 = StringVar()
        self.s56 = StringVar()
        self.s57 = StringVar()
        self.s58 = StringVar()
        self.s59 = StringVar()
        
        self.s61 = StringVar()
        self.s62 = StringVar()
        self.s63 = StringVar()
        self.s64 = StringVar()
        self.s65 = StringVar()
        self.s66 = StringVar()
        self.s67 = StringVar()
        self.s68 = StringVar()
        self.s69 = StringVar()
        
        self.s71 = StringVar()
        self.s72 = StringVar()
        self.s73 = StringVar()
        self.s74 = StringVar()
        self.s75 = StringVar()
        self.s76 = StringVar()
        self.s77 = StringVar()
        self.s78 = StringVar()
        self.s79 = StringVar()

        self.s81 = StringVar()
        self.s82 = StringVar()
        self.s83 = StringVar()
        self.s84 = StringVar()
        self.s85 = StringVar()
        self.s86 = StringVar()
        self.s87 = StringVar()
        self.s88 = StringVar()
        self.s89 = StringVar()

        self.s91 = StringVar()
        self.s92 = StringVar()
        self.s93 = StringVar()
        self.s94 = StringVar()
        self.s95 = StringVar()
        self.s96 = StringVar()
        self.s97 = StringVar()
        self.s98 = StringVar()
        self.s99 = StringVar()

        """

        Solucion 6x6 Facil

        self.s11.set(3)
        self.s21.set(1)
        self.s31.set(5)
        self.s41.set(2)
        self.s51.set(4)
        self.s61.set(6)

        self.s12.set(5)
        self.s22.set(2)
        self.s32.set(1)
        self.s42.set(4)
        self.s52.set(6)
        self.s62.set(3)

        self.s13.set(4)
        self.s23.set(6)
        self.s33.set(2)
        self.s43.set(1)
        self.s53.set(3)
        self.s63.set(5)

        self.s14.set(1)
        self.s24.set(3)
        self.s34.set(6)
        self.s44.set(5)
        self.s54.set(2)
        self.s64.set(4)

        self.s15.set(2)
        self.s25.set(4)
        self.s35.set(3)
        self.s45.set(6)
        self.s55.set(5)
        self.s65.set(1)

        self.s16.set(6)
        self.s26.set(5)
        self.s36.set(4)
        self.s46.set(3)
        self.s56.set(1)
        self.s66.set(2)

        """

        # Lista que contendra todas las 36 casillas la cuadricula con un par de elementos para un mejor manejo de la lista.
        SV = [[],[0,self.s11,self.s12,self.s13,self.s14,self.s15,self.s16,self.s17,self.s18,self.s19],
                 [0,self.s21,self.s22,self.s23,self.s24,self.s25,self.s26,self.s27,self.s28,self.s29],
                 [0,self.s31,self.s32,self.s33,self.s34,self.s35,self.s36,self.s37,self.s38,self.s39],
                 [0,self.s41,self.s42,self.s43,self.s44,self.s45,self.s46,self.s47,self.s48,self.s49],
                 [0,self.s51,self.s52,self.s53,self.s54,self.s55,self.s56,self.s57,self.s58,self.s59],
                 [0,self.s61,self.s62,self.s63,self.s64,self.s65,self.s66,self.s67,self.s68,self.s69],
                 [0,self.s71,self.s72,self.s73,self.s74,self.s75,self.s76,self.s77,self.s78,self.s79],
                 [0,self.s81,self.s82,self.s83,self.s84,self.s85,self.s86,self.s87,self.s88,self.s89],
                 [0,self.s91,self.s92,self.s93,self.s94,self.s95,self.s96,self.s97,self.s98,self.s99]]

        # Lista de los colores que se pueden tomar para asignarselos a los cuadros de texto como fondo.
        c = ["salmon","yellow","green","brown","light blue","sienna3", "thistle2", "gray", "pink", "magenta", "medium purple", "khaki2", "aqua", "rosybrown", "tomato", "peru", "cornsilk2","goldenrod","slateblue", "maroon1", "cyan", "green3", "purple2", "gold3", "dodger blue", "light slate gray", "orange2", "brown3", "DarkOliveGreen3", "bisque2"]

        # Algoritmo para colocar los cuadros de texto segun la posicion de la cuadricula crada por el grid.
        for e in range(0,len(colores)):
            
            for i in range(0,len(colores[e])):

                n = str(colores[e][i][1]) + str(colores[e][i][0])

                parOrdenado = (colores[e][i][1],colores[e][i][0])
                
                string = SV[parOrdenado[0]][parOrdenado[1]]

                y = colores[e][i][0] * 23 + 200 - 23 
                x = colores[e][i][1] * 68 + 277 - 68 
            
                Entry(self, width = 7, font = ("Serif", 13), justify = RIGHT, bg = c[0], name = n, textvariable = string).place(x = x, y = y)
                
            c = c[1:]

        c = ["salmon","yellow","green","brown","light blue","sienna3", "thistle2", "gray", "pink", "magenta", "medium purple", "khaki2", "aqua", "rosybrown", "tomato", "peru", "cornsilk2","goldenrod","slateblue", "maroon1", "cyan", "green3", "purple2", "gold3", "dodger blue", "light slate gray", "orange2", "brown3", "DarkOliveGreen3", "bisque2"]

        cont = 0

        # Algoritmo para concatenar en una sola tupla, todos los pares ordenados que se relacion con la opericion matematica que se debe realizar.
        for e in range(1,len(a) + 1):

            tupla = (a[e][0],a[e][1])
            lista.append(tupla)

        # Algoritmo para crea las etiquetas que indicaran la operacion matematica dentro de las casillas de la cuadricula.
        for e in range(0,len(lista)):

            y = ((lista[e][1][0] * 23) + 201) - 23

            x = ((lista[e][1][1] * 68) + 278) - 68
            
            Label(self, text = lista[e][0], width = 3, font = ("Serif", 8), bg = c[cont]).place(x = x, y = y)
            
            cont = cont + 1

        # Estos seran todos los botones que apareceran en la ventana.
        self.buttonIniciar = Button(self, text = "Iniciar \nJuego", width = 6, activebackground = "#4285f4", command = self.Activar, fg = "White", bg = "#4285f4", font = ("Comic Sans Ms", 15))
        self.buttonIniciar.place(x = 483, y = 500)

        self.buttonValidar = Button(self, text = "Validar \nJuego", width = 6, activebackground = "#4285f4", command = self.Validar, fg = "#4285f4", bg = "White", font = ("Comic Sans Ms", 15))
        self.buttonValidar.place(x = 605, y = 500)

        self.buttonOtro = Button(self, text = "Otro \nJuego", width = 6, activebackground = "#4285f4", command = self.Otro, fg = "white", bg = "#4285f4", font = ("Comic Sans Ms", 15))
        self.buttonOtro.place(x = 715, y = 500)

        self.buttonReiniciar = Button(self, text = "Reiniciar \nJuego", width = 8, activebackground = "#4285f4",command = self.Reiniciar, fg = "#4285f4", bg = "White", font = ("Comic Sans Ms", 15))
        self.buttonReiniciar.place(x = 470, y = 600)        

        self.buttonTerminar = Button(self, text = "Terminar \nJuego", width = 8, activebackground = "#4285f4", command = self.Terminar, fg = "white", bg = "#4285f4", font = ("Comic Sans Ms", 15))
        self.buttonTerminar.place(x = 593, y = 600)        

        self.buttonPausa = Button(self, text = "Pausa", width = 5, activebackground = "#4285f4",command = self.Pausa, fg = "White", bg = "#4285f4", font = ("Comic Sans Ms", 15))
        self.buttonPausa.place(x = 785, y = 35)

        self.buttonPredicciones = Button(self, text = "Predicciones", width = 10, activebackground = "#4285f4",command = self.Predicciones, fg = "White", bg = "#4285f4", font = ("Comic Sans Ms", 15))
        self.buttonPredicciones.place(x = 755, y = 115)

        self.buttonDeshacer = Button(self, text = "Deshacer", width = 10, activebackground = "#4285f4",command = self.Deshacer, fg = "#4285f4", bg = "White", font = ("Comic Sans Ms", 15))
        self.buttonDeshacer.place(x = 813, y = 515)

        self.buttonRehacer = Button(self, text = "Rehacer", width = 10, activebackground = "#4285f4",command = self.Rehacer, fg = "White", bg = "#4285f4", font = ("Comic Sans Ms", 15))
        self.buttonRehacer.place(x = 813, y = 615)

        self.buttonTOP = Button(self, text = "TOP 10", width = 6, activebackground = "#4285f4", command = self.TOP, fg = "#4285f4", bg = "White", font = ("Comic Sans Ms", 15))
        self.buttonTOP.place(x = 715, y = 615)        

        self.buttonGuardarNombre = Button(self, text = "Guardar Nombre", width = 14, activebackground = "#4285f4", command = self.GuardarNombre, fg = "#4285f4", bg = "White", font= ("Comic Sans Ms", 15))
        self.buttonGuardarNombre.place(x = 100, y = 635)

        self.buttonBorrar = Button(self, text = "Borrar", width = 6, activebackground = "#4285f4", command = self.Borrar, fg = "#4285f4", bg = "White", font= ("Comic Sans Ms", 15))
        self.buttonBorrar.place(x = 131, y = 345)

        self.buttonRegresarMenu = Button(self, text = "Regresar al Menú", width = 15, activebackground = "#db4437", command = self.RegresarMenu, fg = "white", bg = "#db4437", font = ("Serif", 20))
        self.buttonRegresarMenu.place(x = 100, y = 500)

        self.button1 = Button(self, text = "1", width = 3, activebackground = "#9C661F", command = self.button1, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button1.place(x = 100, y = 200)

        self.button2 = Button(self, text = "2", width = 3, activebackground = "#9C661F", command = self.button2, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button2.place(x = 148, y = 200)

        self.button3 = Button(self, text = "3", width = 3, activebackground = "#9C661F", command = self.button3, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button3.place(x = 196, y = 200)

        self.button4 = Button(self, text = "4", width = 3, activebackground = "#9C661F", command = self.button4, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button4.place(x = 100, y = 245)

        self.button5 = Button(self, text = "5", width = 3, activebackground = "#9C661F", command = self.button5, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button5.place(x = 148, y = 245)

        self.button6 = Button(self, text = "6", width = 3, activebackground = "#9C661F", command = self.button6, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button6.place(x = 196, y = 245)

        self.button7 = Button(self, text = "7", width = 3, activebackground = "#9C661F", command = self.button7, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button7.place(x = 100, y = 290)

        self.button8 = Button(self, text = "8", width = 3, activebackground = "#9C661F", command = self.button8, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button8.place(x = 148, y = 290)

        self.button9 = Button(self, text = "9", width = 3, activebackground = "#9C661F", command = self.button9, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button9.place(x = 196, y = 290)

        # Condicion que determinara si el reloj aparecera o no segun lo solicitado por el usuario.
        try:
        
            if R == 1:
                
                # Etiquetas que apareceran en la ventana respectiva con sus caracteristicas.
                self.labelHoras = Label(self, text = "Horas", fg =  "#000000", font = ("Serif", 15))
                self.labelHoras.place(x = 280, y = 10)

                self.labelMinutos = Label(self, text = "Minutos", fg =  "#000000", font = ("Serif", 15))
                self.labelMinutos.place(x = 445, y = 10)

                self.labelSegundos = Label(self, text = "Segundos", fg =  "#000000", font = ("Serif", 15))
                self.labelSegundos.place(x = 600, y = 10)

                self.labelDosPuntos1 = Label(self, text = ":", fg =  "#000000", font = ("Serif", 15))
                self.labelDosPuntos1.place(x = 385, y = 60)

                self.labelDosPuntos2 = Label(self, text = ":", fg =  "#000000", font = ("Serif", 15))
                self.labelDosPuntos2.place(x = 560, y = 60)

                # Valores que se les asignaran a las siguientes variables junto con sus características.
                self.TiempoHoras = IntVar()
                self.TiempoHoras.set(0)
                self.labelTimepoHorasActivo = Label(self, textvariable = self.TiempoHoras, font = ("Serif", 15 ))
                self.labelTimepoHorasActivo.place(x = 300, y = 60)

                self.TiempoMinutos = IntVar()
                self.TiempoMinutos.set(0)
                self.labelTimepoMinutosActivo = Label(self, textvariable = self.TiempoMinutos, font = ("Serif", 15 ))
                self.labelTimepoMinutosActivo.place(x = 475, y = 60)

                self.TiempoSegundos = IntVar()
                self.TiempoSegundos.set(0)
                self.labelTimepoSegundosActivo = Label(self, textvariable = self.TiempoSegundos, font = ("Serif", 15 ))
                self.labelTimepoSegundosActivo.place(x = 640, y = 60)

            elif R == 2:

                # Valores que se les asignaran a las siguientes variables junto con sus características.
                self.TiempoHoras = IntVar()
                self.TiempoHoras.set(0)
                self.labelTimepoHorasActivo = Label(self, textvariable = self.TiempoHoras, font = ("Serif", 15 ))
                self.labelTimepoHorasActivo.place(x = 300, y = 2000)

                self.TiempoMinutos = IntVar()
                self.TiempoMinutos.set(0)
                self.labelTimepoMinutosActivo = Label(self, textvariable = self.TiempoMinutos, font = ("Serif", 15 ))
                self.labelTimepoMinutosActivo.place(x = 475, y = 2000)

                self.TiempoSegundos = IntVar()
                self.TiempoSegundos.set(0)
                self.labelTimepoSegundosActivo = Label(self, textvariable = self.TiempoSegundos, font = ("Serif", 15 ))
                self.labelTimepoSegundosActivo.place(x = 640, y = 2000)

            elif R == 3:

                # Etiquetas que apareceran en la ventana respectiva con sus caracteristicas.
                self.labelHoras = Label(self, text = "Horas", fg =  "#000000", font = ("Serif", 15))
                self.labelHoras.place(x = 280, y = 10)

                self.labelMinutos = Label(self, text = "Minutos", fg =  "#000000", font = ("Serif", 15))
                self.labelMinutos.place(x = 445, y = 10)

                self.labelSegundos = Label(self, text = "Segundos", fg =  "#000000", font = ("Serif", 15))
                self.labelSegundos.place(x = 600, y = 10)

                self.labelDosPuntos1 = Label(self, text = ":", fg =  "#000000", font = ("Serif", 15))
                self.labelDosPuntos1.place(x = 385, y = 60)

                self.labelDosPuntos2 = Label(self, text = ":", fg =  "#000000", font = ("Serif", 15))
                self.labelDosPuntos2.place(x = 560, y = 60)

                # Valores que se les asignaran a las siguientes variables junto con sus características.
                self.TiempoHoras = IntVar()
                self.TiempoHoras.set(Horas)
                self.labelTimepoHorasActivo = Label(self, textvariable = self.TiempoHoras, font = ("Serif", 15 ))
                self.labelTimepoHorasActivo.place(x = 300, y = 60)

                self.TiempoMinutos = IntVar()
                self.TiempoMinutos.set(Minutos)
                self.labelTimepoMinutosActivo = Label(self, textvariable = self.TiempoMinutos, font = ("Serif", 15 ))
                self.labelTimepoMinutosActivo.place(x = 475, y = 60)

                self.TiempoSegundos = IntVar()
                self.TiempoSegundos.set(Segundos)
                self.labelTimepoSegundosActivo = Label(self, textvariable = self.TiempoSegundos, font = ("Serif", 15 ))
                self.labelTimepoSegundosActivo.place(x = 640, y = 60)

        # Manejor de errores mediante la utilizacion del metodo try - except.
        except NameError:

            messagebox.showinfo("Aviso", "Debe de configurar el modo de juego que desea.", icon = "warning")

            # Se cerrara la ventana actual.
            self.destroy()
            # Se abrira la nueva ventana solicitada.
            Configurar().mainloop()

    # Funcion del boton asignado.
    def button1(self):

        n = 1
        self.CuadroDeTexto(n)

    # Funcion del boton asignado.
    def button2(self):

        n = 2
        self.CuadroDeTexto(n)

    # Funcion del boton asignado.
    def button3(self):

        n = 3
        self.CuadroDeTexto(n)

    # Funcion del boton asignado.
    def button4(self):

        n = 4
        self.CuadroDeTexto(n)

    # Funcion del boton asignado.
    def button5(self):

        n = 5
        self.CuadroDeTexto(n)

    # Funcion del boton asignado.
    def button6(self):

        n = 6
        self.CuadroDeTexto(n)

    # Funcion del boton asignado.
    def button7(self):

        n = 7
        self.CuadroDeTexto(n)

    # Funcion del boton asignado.
    def button8(self):

        n = 8
        self.CuadroDeTexto(n)

    # Funcion del boton asignado.
    def button9(self):

        n = 9
        self.CuadroDeTexto(n)

    # Funcion del boton asignado.
    def Borrar(self):

        global hacer
        global puntero

        posicion = self.focus_get()
        Cuadro = posicion.winfo_name()

        if Cuadro == "11" or Cuadro == "12" or Cuadro == "13" or Cuadro == "14" or Cuadro == "15" or Cuadro == "16" or Cuadro == "17" or Cuadro == "18" or Cuadro == "19" or\
           Cuadro == "21" or Cuadro == "22" or Cuadro == "23" or Cuadro == "24" or Cuadro == "25" or Cuadro == "26" or Cuadro == "27" or Cuadro == "28" or Cuadro == "29" or\
           Cuadro == "31" or Cuadro == "32" or Cuadro == "33" or Cuadro == "34" or Cuadro == "35" or Cuadro == "36" or Cuadro == "37" or Cuadro == "38" or Cuadro == "39" or\
           Cuadro == "41" or Cuadro == "42" or Cuadro == "43" or Cuadro == "44" or Cuadro == "45" or Cuadro == "46" or Cuadro == "47" or Cuadro == "48" or Cuadro == "49" or\
           Cuadro == "51" or Cuadro == "52" or Cuadro == "53" or Cuadro == "54" or Cuadro == "55" or Cuadro == "56" or Cuadro == "57" or Cuadro == "58" or Cuadro == "59" or\
           Cuadro == "61" or Cuadro == "62" or Cuadro == "63" or Cuadro == "64" or Cuadro == "65" or Cuadro == "66" or Cuadro == "67" or Cuadro == "68" or Cuadro == "69" or\
           Cuadro == "71" or Cuadro == "72" or Cuadro == "73" or Cuadro == "74" or Cuadro == "75" or Cuadro == "76" or Cuadro == "77" or Cuadro == "78" or Cuadro == "79" or\
           Cuadro == "81" or Cuadro == "82" or Cuadro == "83" or Cuadro == "84" or Cuadro == "85" or Cuadro == "86" or Cuadro == "87" or Cuadro == "88" or Cuadro == "89" or\
           Cuadro == "91" or Cuadro == "92" or Cuadro == "93" or Cuadro == "94" or Cuadro == "95" or Cuadro == "96" or Cuadro == "97" or Cuadro == "98" or Cuadro == "99":
            
            posicion.delete(0,END)
            
    # Funcion que determinara la posicion del cursor para poder colocar el numero en dicho cuadro de texto.
    def CuadroDeTexto(self,num):

        global hacer
        global puntero

        posicion = self.focus_get()
        Cuadro = posicion.winfo_name()

        if Cuadro == "11" or Cuadro == "12" or Cuadro == "13" or Cuadro == "14" or Cuadro == "15" or Cuadro == "16" or Cuadro == "17" or Cuadro == "18" or Cuadro == "19" or\
           Cuadro == "21" or Cuadro == "22" or Cuadro == "23" or Cuadro == "24" or Cuadro == "25" or Cuadro == "26" or Cuadro == "27" or Cuadro == "28" or Cuadro == "29" or\
           Cuadro == "31" or Cuadro == "32" or Cuadro == "33" or Cuadro == "34" or Cuadro == "35" or Cuadro == "36" or Cuadro == "37" or Cuadro == "38" or Cuadro == "39" or\
           Cuadro == "41" or Cuadro == "42" or Cuadro == "43" or Cuadro == "44" or Cuadro == "45" or Cuadro == "46" or Cuadro == "47" or Cuadro == "48" or Cuadro == "49" or\
           Cuadro == "51" or Cuadro == "52" or Cuadro == "53" or Cuadro == "54" or Cuadro == "55" or Cuadro == "56" or Cuadro == "57" or Cuadro == "58" or Cuadro == "59" or\
           Cuadro == "61" or Cuadro == "62" or Cuadro == "63" or Cuadro == "64" or Cuadro == "65" or Cuadro == "66" or Cuadro == "67" or Cuadro == "68" or Cuadro == "69" or\
           Cuadro == "71" or Cuadro == "72" or Cuadro == "73" or Cuadro == "74" or Cuadro == "75" or Cuadro == "76" or Cuadro == "77" or Cuadro == "78" or Cuadro == "79" or\
           Cuadro == "81" or Cuadro == "82" or Cuadro == "83" or Cuadro == "84" or Cuadro == "85" or Cuadro == "86" or Cuadro == "87" or Cuadro == "88" or Cuadro == "89" or\
           Cuadro == "91" or Cuadro == "92" or Cuadro == "93" or Cuadro == "94" or Cuadro == "95" or Cuadro == "96" or Cuadro == "97" or Cuadro == "98" or Cuadro == "99":

            posicion.insert(END,num)
            deshacer.append([Cuadro,""])
            rehacer.append([Cuadro,posicion.get()])
            puntero = puntero + 1

    def Predicciones(self):

        global tamaño

        posicion = self.focus_get()
        Cuadro = posicion.winfo_name()

        fila = Cuadro[1]
        columna = Cuadro[0]
        
        lista = []

        for i in a:

            s = a[i][0]

            final = [int(s[:-1]),s[-1],a[i][1:]]

            lista.append(final)
            for e in range(0,len(final[2])):
                if str(final[2][e][0]) == fila and str(final[2][e][1])==columna:
                    op = final

        resultado = "\n"

        if op[1] == "+":

            if len(op[2]) == 2:

                for e in range(1,tamaño + 1):
                    for i in range(1,tamaño + 1):
                        suma = e + i
                        if suma == op[0]:
                            resultado = resultado + str(e) + " + " + str(i) + "\n"

            if len(op[2]) == 3:

                for e in range(1,tamaño + 1):
                    for i in range(1,tamaño + 1):
                        for j in range(1,tamaño + 1):
                            suma = e + i + j
                            if suma == op[0]:
                                resultado = resultado + str(e) + " + " + str(i) +  " + "  + str(j) + "\n"

        if op[1] == "-":

            if len(op[2]) == 2:

                for e in range(1,tamaño + 1):
                    for i in range(1,tamaño + 1):
                        resta = abs(e - i)
                        if resta == op[0]:
                            resultado = resultado + str(e) + " - "  + str(i) + "\n"

            if len(op[2]) == 3:

                for e in range(1,tamaño + 1):
                    for i in range(1,tamaño + 1):
                        for j in range(1,tamaño + 1):
                            resta = abs(e - i - j)
                            if resta == op[0]:
                                resultado = resultado + str(e) + " - " + str(i)  +  " - " + str(j) + "\n"

        if op[1] == "x":

            if len(op[2]) == 2:

                for e in range(1,tamaño + 1):
                    for i in range(1,tamaño + 1):
                        resta = e * i
                        if resta == op[0]:
                            resultado = resultado  + str(e) + " x " + str(i) + "\n"

            if len(op[2]) == 3:

                for e in range(1,tamaño + 1):
                    for i in range(1,tamaño + 1):
                        for j in range(1,tamaño + 1):
                            resta = e * i * j
                            if resta == op[0]:
                                resultado = resultado + str(e)  + " x " + str(i)  +  " x " + str(j) + "\n"

        if op[1] == "/":

            if len(op[2]) == 2:

                for e in range(1,tamaño + 1):
                    for i in range(1,tamaño + 1):

                        if e > i:
                            div = e / i
                        else:
                            div = i / e
                            
                        if div == op[0]:

                            if e > i:
                                resultado = resultado  + str(e) + " / " + str(i) + "\n"
                            else:
                                resultado = resultado  + str(i) + " / " + str(e) + "\n"

        self.p.set(resultado)

    # Funcion que determinara la posicion del cursor para poder colocar el numero en dicho cuadro de texto.
    def Deshacer(self):

        global deshacer
        global puntero
        global rehacer

        if puntero >= 0:

            puntero = puntero - 1

            if puntero < 0:
                
                messagebox.showinfo("Aviso", "No existen más jugadas.", icon = "warning")

        if puntero < len(deshacer):

            lista = deshacer[puntero]

            if lista[0] == "11":

                self.s11.set(lista[1])

            elif lista[0] == "12":

                self.s12.set(lista[1])

            elif lista[0] == "13":

                self.s13.set(lista[1])

            elif lista[0] == "14":

                self.s14.set(lista[1])

            elif lista[0] == "15":

                self.s15.set(lista[1])

            elif lista[0] == "16":

                self.s16.set(lista[1])

            elif lista[0] == "17":

                self.s17.set(lista[1])

            elif lista[0] == "18":

                self.s18.set(lista[1])

            elif lista[0] == "19":

                self.s19.set(lista[1])

            elif lista[0] == "21":

                self.s21.set(lista[1])

            elif lista[0] == "22":

                self.s22.set(lista[1])

            elif lista[0] == "23":

                self.s23.set(lista[1])

            elif lista[0] == "24":

                self.s24.set(lista[1])

            elif lista[0] == "25":

                self.s25.set(lista[1])

            elif lista[0] == "26":

                self.s26.set(lista[1])

            elif lista[0] == "27":

                self.s27.set(lista[1])

            elif lista[0] == "28":

                self.s28.set(lista[1])

            elif lista[0] == "29":

                self.s29.set(lista[1])

            elif lista[0] == "31":

                self.s31.set(lista[1])

            elif lista[0] == "32":

                self.s32.set(lista[1])

            elif lista[0] == "33":

                self.s33.set(lista[1])

            elif lista[0] == "34":

                self.s34.set(lista[1])

            elif lista[0] == "35":

                self.s35.set(lista[1])

            elif lista[0] == "36":

                self.s36.set(lista[1])

            elif lista[0] == "37":

                self.s37.set(lista[1])

            elif lista[0] == "38":

                self.s38.set(lista[1])

            elif lista[0] == "39":

                self.s39.set(lista[1])

            elif lista[0] == "41":

                self.s41.set(lista[1])

            elif lista[0] == "42":

                self.s42.set(lista[1])

            elif lista[0] == "43":

                self.s43.set(lista[1])

            elif lista[0] == "44":

                self.s44.set(lista[1])

            elif lista[0] == "45":

                self.s45.set(lista[1])

            elif lista[0] == "46":

                self.s46.set(lista[1])

            elif lista[0] == "47":

                self.s47.set(lista[1])

            elif lista[0] == "48":

                self.s48.set(lista[1])

            elif lista[0] == "49":

                self.s49.set(lista[1])

            elif lista[0] == "51":

                self.s51.set(lista[1])

            elif lista[0] == "52":

                self.s52.set(lista[1])

            elif lista[0] == "53":

                self.s53.set(lista[1])

            elif lista[0] == "54":

                self.s54.set(lista[1])

            elif lista[0] == "55":

                self.s55.set(lista[1])

            elif lista[0] == "56":

                self.s56.set(lista[1])

            elif lista[0] == "57":

                self.s57.set(lista[1])

            elif lista[0] == "58":

                self.s58.set(lista[1])

            elif lista[0] == "59":

                self.s59.set(lista[1])

            elif lista[0] == "61":

                self.s61.set(lista[1])

            elif lista[0] == "62":

                self.s62.set(lista[1])

            elif lista[0] == "63":

                self.s63.set(lista[1])

            elif lista[0] == "64":

                self.s64.set(lista[1])

            elif lista[0] == "65":

                self.s65.set(lista[1])

            elif lista[0] == "66":

                self.s66.set(lista[1])

            elif lista[0] == "67":

                self.s67.set(lista[1])

            elif lista[0] == "68":

                self.s68.set(lista[1])

            elif lista[0] == "69":

                self.s69.set(lista[1])

            elif lista[0] == "71":

                self.s71.set(lista[1])

            elif lista[0] == "72":

                self.s72.set(lista[1])

            elif lista[0] == "73":

                self.s73.set(lista[1])

            elif lista[0] == "74":

                self.s74.set(lista[1])

            elif lista[0] == "75":

                self.s75.set(lista[1])

            elif lista[0] == "76":

                self.s76.set(lista[1])

            elif lista[0] == "77":

                self.s77.set(lista[1])

            elif lista[0] == "78":

                self.s78.set(lista[1])

            elif lista[0] == "79":

                self.s79.set(lista[1])

            elif lista[0] == "81":

                self.s81.set(lista[1])

            elif lista[0] == "82":

                self.s82.set(lista[1])

            elif lista[0] == "83":

                self.s83.set(lista[1])

            elif lista[0] == "84":

                self.s84.set(lista[1])

            elif lista[0] == "85":

                self.s85.set(lista[1])

            elif lista[0] == "86":

                self.s86.set(lista[1])

            elif lista[0] == "87":

                self.s87.set(lista[1])

            elif lista[0] == "88":

                self.s88.set(lista[1])

            elif lista[0] == "89":

                self.s89.set(lista[1])

            elif lista[0] == "91":

                self.s91.set(lista[1])

            elif lista[0] == "92":

                self.s92.set(lista[1])

            elif lista[0] == "93":

                self.s93.set(lista[1])

            elif lista[0] == "94":

                self.s94.set(lista[1])

            elif lista[0] == "95":

                self.s95.set(lista[1])

            elif lista[0] == "96":

                self.s96.set(lista[1])

            elif lista[0] == "97":

                self.s97.set(lista[1])

            elif lista[0] == "98":

                self.s98.set(lista[1])

            elif lista[0] == "99":

                self.s99.set(lista[1])

    # Funcion que determinara la posicion del cursor para poder colocar el numero en dicho cuadro de texto.
    def Rehacer(self):

        global rehacer
        global deshacer
        global puntero

        try:

            puntero = puntero + 1

            if puntero >= 0:

                lista = rehacer[puntero]

                if lista[0] == "11":

                    self.s11.set(lista[1])

                elif lista[0] == "12":

                    self.s12.set(lista[1])

                elif lista[0] == "13":

                    self.s13.set(lista[1])

                elif lista[0] == "14":

                    self.s14.set(lista[1])

                elif lista[0] == "15":

                    self.s15.set(lista[1])

                elif lista[0] == "16":

                    self.s16.set(lista[1])

                elif lista[0] == "17":

                    self.s17.set(lista[1])

                elif lista[0] == "18":

                    self.s18.set(lista[1])

                elif lista[0] == "19":

                    self.s19.set(lista[1])

                elif lista[0] == "21":

                    self.s21.set(lista[1])

                elif lista[0] == "22":

                    self.s22.set(lista[1])

                elif lista[0] == "23":

                    self.s23.set(lista[1])

                elif lista[0] == "24":

                    self.s24.set(lista[1])

                elif lista[0] == "25":

                    self.s25.set(lista[1])

                elif lista[0] == "26":

                    self.s26.set(lista[1])

                elif lista[0] == "27":

                    self.s27.set(lista[1])

                elif lista[0] == "28":

                    self.s28.set(lista[1])

                elif lista[0] == "29":

                    self.s29.set(lista[1])

                elif lista[0] == "31":

                    self.s31.set(lista[1])

                elif lista[0] == "32":

                    self.s32.set(lista[1])

                elif lista[0] == "33":

                    self.s33.set(lista[1])

                elif lista[0] == "34":

                    self.s34.set(lista[1])

                elif lista[0] == "35":

                    self.s35.set(lista[1])

                elif lista[0] == "36":

                    self.s36.set(lista[1])

                elif lista[0] == "37":

                    self.s37.set(lista[1])

                elif lista[0] == "38":

                    self.s38.set(lista[1])

                elif lista[0] == "39":

                    self.s39.set(lista[1])

                elif lista[0] == "41":

                    self.s41.set(lista[1])

                elif lista[0] == "42":

                    self.s42.set(lista[1])

                elif lista[0] == "43":

                    self.s43.set(lista[1])

                elif lista[0] == "44":

                    self.s44.set(lista[1])

                elif lista[0] == "45":

                    self.s45.set(lista[1])

                elif lista[0] == "46":

                    self.s46.set(lista[1])

                elif lista[0] == "47":

                    self.s47.set(lista[1])

                elif lista[0] == "48":

                    self.s48.set(lista[1])

                elif lista[0] == "49":

                    self.s49.set(lista[1])

                elif lista[0] == "51":

                    self.s51.set(lista[1])

                elif lista[0] == "52":

                    self.s52.set(lista[1])

                elif lista[0] == "53":

                    self.s53.set(lista[1])

                elif lista[0] == "54":

                    self.s54.set(lista[1])

                elif lista[0] == "55":

                    self.s55.set(lista[1])

                elif lista[0] == "56":

                    self.s56.set(lista[1])

                elif lista[0] == "57":

                    self.s57.set(lista[1])

                elif lista[0] == "58":

                    self.s58.set(lista[1])

                elif lista[0] == "59":

                    self.s59.set(lista[1])

                elif lista[0] == "61":

                    self.s61.set(lista[1])

                elif lista[0] == "62":

                    self.s62.set(lista[1])

                elif lista[0] == "63":

                    self.s63.set(lista[1])

                elif lista[0] == "64":

                    self.s64.set(lista[1])

                elif lista[0] == "65":

                    self.s65.set(lista[1])

                elif lista[0] == "66":

                    self.s66.set(lista[1])

                elif lista[0] == "67":

                    self.s67.set(lista[1])

                elif lista[0] == "68":

                    self.s68.set(lista[1])

                elif lista[0] == "69":

                    self.s69.set(lista[1])

                elif lista[0] == "71":

                    self.s71.set(lista[1])

                elif lista[0] == "72":

                    self.s72.set(lista[1])

                elif lista[0] == "73":

                    self.s73.set(lista[1])

                elif lista[0] == "74":

                    self.s74.set(lista[1])

                elif lista[0] == "75":

                    self.s75.set(lista[1])

                elif lista[0] == "76":

                    self.s76.set(lista[1])

                elif lista[0] == "77":

                    self.s77.set(lista[1])

                elif lista[0] == "78":

                    self.s78.set(lista[1])

                elif lista[0] == "79":

                    self.s79.set(lista[1])

                elif lista[0] == "81":

                    self.s81.set(lista[1])

                elif lista[0] == "82":

                    self.s82.set(lista[1])

                elif lista[0] == "83":

                    self.s83.set(lista[1])

                elif lista[0] == "84":

                    self.s84.set(lista[1])

                elif lista[0] == "85":

                    self.s85.set(lista[1])

                elif lista[0] == "86":

                    self.s86.set(lista[1])

                elif lista[0] == "87":

                    self.s87.set(lista[1])

                elif lista[0] == "88":

                    self.s88.set(lista[1])

                elif lista[0] == "89":

                    self.s89.set(lista[1])

                elif lista[0] == "91":

                    self.s91.set(lista[1])

                elif lista[0] == "92":

                    self.s92.set(lista[1])

                elif lista[0] == "93":

                    self.s93.set(lista[1])

                elif lista[0] == "94":

                    self.s94.set(lista[1])

                elif lista[0] == "95":

                    self.s95.set(lista[1])

                elif lista[0] == "96":

                    self.s96.set(lista[1])

                elif lista[0] == "97":

                    self.s97.set(lista[1])

                elif lista[0] == "98":

                    self.s98.set(lista[1])

                elif lista[0] == "99":

                    self.s99.set(lista[1])

        except IndexError:

            messagebox.showinfo("Aviso", "No existen más jugadas.", icon = "warning")

    # Funcion del boton asignado.
    def Validar(self):

        # Se le asignara un valor especifico a las siguientes variables.
        guia = 1
        espacio = False

        # Algoritmo que determinara si el usuario no ha rellenado toda la cuadricula.
        while guia == 1:

            if T == 1:
                
                # Obtencion de todos los valores presentes en los cuadros de texto de la cuadricula.
                t11 = self.s11.get()
                t12 = self.s12.get()
                t13 = self.s13.get()

                t21 = self.s21.get()
                t22 = self.s22.get()
                t23 = self.s23.get()

                t31 = self.s31.get()
                t32 = self.s32.get()
                t33 = self.s33.get()

                # Lista que contendra los valores ordenados por filas.
                lista1 = [t11,t21,t31]
                lista2 = [t12,t22,t32]
                lista3 = [t13,t23,t33]

                # Lista que contendra los valores ordenados por columnas.
                lista4 = [t11,t12,t13]
                lista5 = [t21,t22,t23]
                lista6 = [t31,t32,t33]
                
                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista1) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 1.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista2) == True:
                    
                    messagebox.showinfo("Error", "Espacios en blanco en la fila 2.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista3) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 3.", icon = "warning")
                    espacio = True

                # Si existe algun espacio en blanco en la cuadricula, se cerrara el ciclo while.
                if espacio == True:

                    break

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista1 != []:

                        e = lista1[0]
                        lista1.remove(e)

                        if (str(e) in lista1) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 1.", icon = "warning")                        

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista2 != []:

                        e = lista2[0]
                        lista2.remove(e)

                        if (str(e) in lista2) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 2.", icon = "warning")                        

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista3 != []:

                        e = lista3[0]
                        lista3.remove(e)

                        if (str(e) in lista3) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 3.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista4 != []:

                        e = lista4[0]
                        lista4.remove(e)

                        if (str(e) in lista4) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 1.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista5 != []:

                        e = lista5[0]
                        lista5.remove(e)

                        if (str(e) in lista5) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 2.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.            
                if guia == 1:

                    while lista6 != []:

                        e = lista6[0]
                        lista6.remove(e)

                        if (str(e) in lista6) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 3.", icon = "warning")

                # Algoritmo que determinara si las casillas relacionas con la operacion matematica respectiva, dan el resultado correcto.
                for e in range(1,len(a) + 1):

                    tupla = a[e]

                    string = tupla[0]

                    paresOrdenados = tupla[1:]

                    nuevos = []

                    # Se determinaran cuales pares ordenados deben ir juntos con respecto al dicciorio utilizado.
                    for i in tupla[1:]:

                        p = str(i[0]) + str(i[1])

                        nuevos.append(p)

                    valores = []

                    # Algoritmo para identificar cuales valores se encuentran en las casillas respectivas.
                    for i in nuevos:

                        if i == "11":

                            valores.append(t11)

                        elif i == "21":

                            valores.append(t12)
                            
                        elif i == "31":

                            valores.append(t13)
                            
                        elif i == "12":

                            valores.append(t21)

                        elif i == "22":

                            valores.append(t22)

                        elif i == "32":

                            valores.append(t23)

                        elif i == "13":

                            valores.append(t31)

                        elif i == "23":

                            valores.append(t32)

                        elif i == "33":

                            valores.append(t33)

                    # Se ordenara la lista de mayor a menor
                    valores.sort(reverse = True)

                    # Se asignara el string de la operacion matematica a la siguiente variable.
                    resultado = int(string[:-1])

                    # Simbolo de la operacion matematica.
                    s = string[-1]

                    resta = 0

                    # Condiciones necesarias para retornar el resultado correcto.
                    if s == "x":

                        final = 1

                    elif s == "+" or s == "-":

                        final = 0

                    if s == "+" or s == "-" or s == "x":
                        
                        for i in valores:

                            if s == "+":

                                final = final + int(i)

                            elif s == "-":

                                if resta == 0:

                                    final = final - int(i)
                                    resta = resta + 1

                                else:

                                    final = final + int(i)

                            elif s == "x":

                                final = final * int(i)

                        if s == "-":

                            final = abs(final)

                    else:

                        final = int(int(valores[0]) / int(valores[1]))

                    # Condicion que determina si el resultado indicado por la etiqueta es el mismo resultado obtenido segun los valores digitados por el usuario.
                    if final != resultado:

                        messagebox.showinfo("Error", "Revise las casillas de la operación " + string + ".", icon = "warning")
                        guia = 0

                    # Se reinicia esta variable para no tenes todos los pares ordenados en una misma lista.
                    valores = []

                # Condicion que reproducira el sondio cuando se gane la partida.
                if guia == 1:

                    # Condicion que determina si el usuario quiere reproducir el sonido o no.
                    if S == 1:
                        
                        pygame.init()

                        zelda = pygame.mixer.music.load("You win sound effect 5.mp3")

                        pygame.mixer.music.play(1)

                    messagebox.showinfo("Aviso", " Felicidades!!!\n Completaste el kenken.")

                    break

            if T == 2:

                # Obtencion de todos los valores presentes en los cuadros de texto de la cuadricula.
                t11 = self.s11.get()
                t12 = self.s12.get()
                t13 = self.s13.get()
                t14 = self.s14.get()

                t21 = self.s21.get()
                t22 = self.s22.get()
                t23 = self.s23.get()
                t24 = self.s24.get()

                t31 = self.s31.get()
                t32 = self.s32.get()
                t33 = self.s33.get()
                t34 = self.s34.get()

                t41 = self.s41.get()
                t42 = self.s42.get()
                t43 = self.s43.get()
                t44 = self.s44.get()

                t51 = self.s51.get()
                t52 = self.s52.get()
                t53 = self.s53.get()
                t54 = self.s54.get()

                t61 = self.s61.get()
                t62 = self.s62.get()
                t63 = self.s63.get()
                t64 = self.s64.get()

                # Lista que contendra los valores ordenados por filas.
                lista1 = [t11,t21,t31,t41]
                lista2 = [t12,t22,t32,t42]
                lista3 = [t13,t23,t33,t43]
                lista4 = [t14,t24,t34,t44]

                # Lista que contendra los valores ordenados por columnas.
                lista5 = [t11,t12,t13,t14]
                lista6 = [t21,t22,t23,t24]
                lista7 = [t31,t32,t33,t34]
                lista8 = [t41,t42,t43,t44]

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista1) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 1.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista2) == True:
                    
                    messagebox.showinfo("Error", "Espacios en blanco en la fila 2.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista3) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 3.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista4) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 4.", icon = "warning")
                    espacio = True

                # Si existe algun espacio en blanco en la cuadricula, se cerrara el ciclo while.
                if espacio == True:

                    break

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista1 != []:

                        e = lista1[0]
                        lista1.remove(e)

                        if (str(e) in lista1) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 1.", icon = "warning")                        

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista2 != []:

                        e = lista2[0]
                        lista2.remove(e)

                        if (str(e) in lista2) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 2.", icon = "warning")                        

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista3 != []:

                        e = lista3[0]
                        lista3.remove(e)

                        if (str(e) in lista3) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 3.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista4 != []:

                        e = lista4[0]
                        lista4.remove(e)

                        if (str(e) in lista4) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 4.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista5 != []:

                        e = lista5[0]
                        lista5.remove(e)

                        if (str(e) in lista5) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 1.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 6:

                    while lista6 != []:

                        e = lista6[0]
                        lista6.remove(e)

                        if (str(e) in lista6) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 2.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.            
                if guia == 1:

                    while lista7 != []:

                        e = lista7[0]
                        lista7.remove(e)

                        if (str(e) in lista7) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 3.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista8 != []:

                        e = lista8[0]
                        lista8.remove(e)

                        if (str(e) in lista8) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 4.", icon = "warning")

                # Algoritmo que determinara si las casillas relacionas con la operacion matematica respectiva, dan el resultado correcto.
                for e in range(1,len(a) + 1):

                    tupla = a[e]

                    string = tupla[0]

                    paresOrdenados = tupla[1:]

                    nuevos = []

                    # Se determinaran cuales pares ordenados deben ir juntos con respecto al dicciorio utilizado.
                    for i in tupla[1:]:

                        p = str(i[0]) + str(i[1])

                        nuevos.append(p)

                    valores = []

                    # Algoritmo para identificar cuales valores se encuentran en las casillas respectivas.
                    for i in nuevos:

                        if i == "11":

                            valores.append(t11)

                        elif i == "21":

                            valores.append(t12)
                            

                        elif i == "31":

                            valores.append(t13)

                        elif i == "41":

                            valores.append(t14)
                            
                        elif i == "12":

                            valores.append(t21)

                        elif i == "22":

                            valores.append(t22)

                        elif i == "32":

                            valores.append(t23)

                        elif i == "42":

                            valores.append(t24)

                        elif i == "13":

                            valores.append(t31)

                        elif i == "23":

                            valores.append(t32)

                        elif i == "33":

                            valores.append(t33)

                        elif i == "43":

                            valores.append(t34)

                        elif i == "14":

                            valores.append(t41)

                        elif i == "24":

                            valores.append(t42)

                        elif i == "34":

                            valores.append(t43)

                        elif i == "44":

                            valores.append(t44)

                    # Se ordenara la lista de mayor a menor
                    valores.sort(reverse = True)

                    # Se asignara el string de la operacion matematica a la siguiente variable.
                    resultado = int(string[:-1])

                    # Simbolo de la operacion matematica.
                    s = string[-1]

                    resta = 0

                    # Condiciones necesarias para retornar el resultado correcto.
                    if s == "x":

                        final = 1

                    elif s == "+" or s == "-":

                        final = 0

                    if s == "+" or s == "-" or s == "x":
                        
                        for i in valores:

                            if s == "+":

                                final = final + int(i)

                            elif s == "-":

                                if resta == 0:

                                    final = final - int(i)
                                    resta = resta + 1

                                else:

                                    final = final + int(i)

                            elif s == "x":

                                final = final * int(i)

                        if s == "-":

                            final = abs(final)

                    else:

                        final = int(int(valores[0]) / int(valores[1]))

                    # Condicion que determina si el resultado indicado por la etiqueta es el mismo resultado obtenido segun los valores digitados por el usuario.
                    if final != resultado:

                        messagebox.showinfo("Error", "Revise las casillas de la operación " + string + ".", icon = "warning")
                        guia = 0

                    # Se reinicia esta variable para no tenes todos los pares ordenados en una misma lista.
                    valores = []

                # Condicion que reproducira el sondio cuando se gane la partida.
                if guia == 1:

                    # Condicion que determina si el usuario quiere reproducir el sonido o no.
                    if S == 1:
                        
                        pygame.init()

                        zelda = pygame.mixer.music.load("You win sound effect 5.mp3")

                        pygame.mixer.music.play(1)

                    messagebox.showinfo("Aviso", " Felicidades!!!\n Completaste el kenken.")

                    break

            if T == 3:

                # Obtencion de todos los valores presentes en los cuadros de texto de la cuadricula.
                t11 = self.s11.get()
                t12 = self.s12.get()
                t13 = self.s13.get()
                t14 = self.s14.get()
                t15 = self.s15.get()
                
                t21 = self.s21.get()
                t22 = self.s22.get()
                t23 = self.s23.get()
                t24 = self.s24.get()
                t25 = self.s25.get()

                t31 = self.s31.get()
                t32 = self.s32.get()
                t33 = self.s33.get()
                t34 = self.s34.get()
                t35 = self.s35.get()

                t41 = self.s41.get()
                t42 = self.s42.get()
                t43 = self.s43.get()
                t44 = self.s44.get()
                t45 = self.s45.get()

                t51 = self.s51.get()
                t52 = self.s52.get()
                t53 = self.s53.get()
                t54 = self.s54.get()
                t55 = self.s55.get()

                # Lista que contendra los valores ordenados por filas.
                lista1 = [t11,t21,t31,t41,t51]
                lista2 = [t12,t22,t32,t42,t52]
                lista3 = [t13,t23,t33,t43,t53]
                lista4 = [t14,t24,t34,t44,t54]
                lista5 = [t15,t25,t35,t45,t55]

                # Lista que contendra los valores ordenados por columnas.
                lista6 = [t11,t12,t13,t14,t15]
                lista7 = [t21,t22,t23,t24,t25]
                lista8 = [t31,t32,t33,t34,t35]
                lista9 = [t41,t42,t43,t44,t45]
                lista10 = [t51,t52,t53,t54,t55]
                
                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista1) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 1.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista2) == True:
                    
                    messagebox.showinfo("Error", "Espacios en blanco en la fila 2.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista3) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 3.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista4) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 4.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista5) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 5.", icon = "warning")
                    espacio = True

                # Si existe algun espacio en blanco en la cuadricula, se cerrara el ciclo while.
                if espacio == True:

                    break

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista1 != []:

                        e = lista1[0]
                        lista1.remove(e)

                        if (str(e) in lista1) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 1.", icon = "warning")                        

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista2 != []:

                        e = lista2[0]
                        lista2.remove(e)

                        if (str(e) in lista2) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 2.", icon = "warning")                        

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista3 != []:

                        e = lista3[0]
                        lista3.remove(e)

                        if (str(e) in lista3) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 3.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista4 != []:

                        e = lista4[0]
                        lista4.remove(e)

                        if (str(e) in lista4) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 4.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista5 != []:

                        e = lista5[0]
                        lista5.remove(e)

                        if (str(e) in lista5) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 5.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista6 != []:

                        e = lista6[0]
                        lista6.remove(e)

                        if (str(e) in lista6) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 1.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista7 != []:

                        e = lista7[0]
                        lista7.remove(e)

                        if (str(e) in lista7) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 2.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.            
                if guia == 1:

                    while lista8 != []:

                        e = lista8[0]
                        lista8.remove(e)

                        if (str(e) in lista8) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 3.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista9 != []:

                        e = lista9[0]
                        lista9.remove(e)

                        if (str(e) in lista9) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 4.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista10 != []:

                        e = lista10[0]
                        lista10.remove(e)

                        if (str(e) in lista10) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 5.", icon = "warning")

                # Algoritmo que determinara si las casillas relacionas con la operacion matematica respectiva, dan el resultado correcto.
                for e in range(1,len(a) + 1):

                    tupla = a[e]

                    string = tupla[0]

                    paresOrdenados = tupla[1:]

                    nuevos = []

                    # Se determinaran cuales pares ordenados deben ir juntos con respecto al dicciorio utilizado.
                    for i in tupla[1:]:

                        p = str(i[0]) + str(i[1])

                        nuevos.append(p)

                    valores = []

                    # Algoritmo para identificar cuales valores se encuentran en las casillas respectivas.
                    for i in nuevos:

                        if i == "11":

                            valores.append(t11)

                        elif i == "21":

                            valores.append(t12)
                            

                        elif i == "31":

                            valores.append(t13)

                        elif i == "41":

                            valores.append(t14)

                        elif i == "51":

                            valores.append(t15)

                        elif i == "61":

                            valores.append(t16)
                            
                        elif i == "12":

                            valores.append(t21)

                        elif i == "22":

                            valores.append(t22)

                        elif i == "32":

                            valores.append(t23)

                        elif i == "42":

                            valores.append(t24)

                        elif i == "52":

                            valores.append(t25)

                        elif i == "62":

                            valores.append(t26)

                        elif i == "13":

                            valores.append(t31)

                        elif i == "23":

                            valores.append(t32)

                        elif i == "33":

                            valores.append(t33)

                        elif i == "43":

                            valores.append(t34)

                        elif i == "53":

                            valores.append(t35)

                        elif i == "63":

                            valores.append(t36)

                        elif i == "14":

                            valores.append(t41)

                        elif i == "24":

                            valores.append(t42)

                        elif i == "34":

                            valores.append(t43)

                        elif i == "44":

                            valores.append(t44)

                        elif i == "54":

                            valores.append(t45)

                        elif i == "64":

                            valores.append(t46)

                        elif i == "15":

                            valores.append(t51)

                        elif i == "25":

                            valores.append(t52)

                        elif i == "35":

                            valores.append(t53)

                        elif i == "45":

                            valores.append(t54)

                        elif i == "55":

                            valores.append(t55)

                        elif i == "65":

                            valores.append(t56)

                        elif i == "16":

                            valores.append(t61)

                        elif i == "26":

                            valores.append(t62)

                        elif i == "36":

                            valores.append(t63)

                        elif i == "46":

                            valores.append(t64)

                        elif i == "56":

                            valores.append(t65)

                        elif i == "66":

                            valores.append(t66)

                    # Se ordenara la lista de mayor a menor
                    valores.sort(reverse = True)

                    # Se asignara el string de la operacion matematica a la siguiente variable.
                    resultado = int(string[:-1])

                    # Simbolo de la operacion matematica.
                    s = string[-1]

                    resta = 0

                    # Condiciones necesarias para retornar el resultado correcto.
                    if s == "x":

                        final = 1

                    elif s == "+" or s == "-":

                        final = 0

                    if s == "+" or s == "-" or s == "x":
                        
                        for i in valores:

                            if s == "+":

                                final = final + int(i)

                            elif s == "-":

                                if resta == 0:

                                    final = final - int(i)
                                    resta = resta + 1

                                else:

                                    final = final + int(i)

                            elif s == "x":

                                final = final * int(i)

                        if s == "-":

                            final = abs(final)

                    else:

                        final = int(int(valores[0]) / int(valores[1]))

                    # Condicion que determina si el resultado indicado por la etiqueta es el mismo resultado obtenido segun los valores digitados por el usuario.
                    if final != resultado:

                        messagebox.showinfo("Error", "Revise las casillas de la operación " + string + ".", icon = "warning")
                        guia = 0

                    # Se reinicia esta variable para no tenes todos los pares ordenados en una misma lista.
                    valores = []

                # Condicion que reproducira el sondio cuando se gane la partida.
                if guia == 1:

                    # Condicion que determina si el usuario quiere reproducir el sonido o no.
                    if S == 1:
                        
                        pygame.init()

                        zelda = pygame.mixer.music.load("You win sound effect 5.mp3")

                        pygame.mixer.music.play(1)

                    messagebox.showinfo("Aviso", " Felicidades!!!\n Completaste el kenken.")

                    break

            if T == 4:

                # Obtencion de todos los valores presentes en los cuadros de texto de la cuadricula.
                t11 = self.s11.get()
                t12 = self.s12.get()
                t13 = self.s13.get()
                t14 = self.s14.get()
                t15 = self.s15.get()
                t16 = self.s16.get()

                t21 = self.s21.get()
                t22 = self.s22.get()
                t23 = self.s23.get()
                t24 = self.s24.get()
                t25 = self.s25.get()
                t26 = self.s26.get()

                t31 = self.s31.get()
                t32 = self.s32.get()
                t33 = self.s33.get()
                t34 = self.s34.get()
                t35 = self.s35.get()
                t36 = self.s36.get()

                t41 = self.s41.get()
                t42 = self.s42.get()
                t43 = self.s43.get()
                t44 = self.s44.get()
                t45 = self.s45.get()
                t46 = self.s46.get()

                t51 = self.s51.get()
                t52 = self.s52.get()
                t53 = self.s53.get()
                t54 = self.s54.get()
                t55 = self.s55.get()
                t56 = self.s56.get()

                t61 = self.s61.get()
                t62 = self.s62.get()
                t63 = self.s63.get()
                t64 = self.s64.get()
                t65 = self.s65.get()
                t66 = self.s66.get()

                # Lista que contendra los valores ordenados por filas.
                lista1 = [t11,t21,t31,t41,t51,t61]
                lista2 = [t12,t22,t32,t42,t52,t62]
                lista3 = [t13,t23,t33,t43,t53,t63]
                lista4 = [t14,t24,t34,t44,t54,t64]
                lista5 = [t15,t25,t35,t45,t55,t65]
                lista6 = [t16,t26,t36,t46,t56,t66]

                # Lista que contendra los valores ordenados por columnas.
                lista7 = [t11,t12,t13,t14,t15,t16]
                lista8 = [t21,t22,t23,t24,t25,t26]
                lista9 = [t31,t32,t33,t34,t35,t36]
                lista10 = [t41,t42,t43,t44,t45,t46]
                lista11 = [t51,t52,t53,t54,t55,t56]
                lista12 = [t61,t62,t63,t64,t65,t66]

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista1) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 1.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista2) == True:
                    
                    messagebox.showinfo("Error", "Espacios en blanco en la fila 2.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista3) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 3.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista4) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 4.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista5) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 5.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista6) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 6.", icon = "warning")
                    espacio = True

                # Si existe algun espacio en blanco en la cuadricula, se cerrara el ciclo while.
                if espacio == True:

                    break

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista1 != []:

                        e = lista1[0]
                        lista1.remove(e)

                        if (str(e) in lista1) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 1.", icon = "warning")                        

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista2 != []:

                        e = lista2[0]
                        lista2.remove(e)

                        if (str(e) in lista2) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 2.", icon = "warning")                        

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista3 != []:

                        e = lista3[0]
                        lista3.remove(e)

                        if (str(e) in lista3) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 3.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista4 != []:

                        e = lista4[0]
                        lista4.remove(e)

                        if (str(e) in lista4) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 4.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista5 != []:

                        e = lista5[0]
                        lista5.remove(e)

                        if (str(e) in lista5) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 5.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista6 != []:

                        e = lista6[0]
                        lista6.remove(e)

                        if (str(e) in lista6) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 6.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista7 != []:

                        e = lista7[0]
                        lista7.remove(e)

                        if (str(e) in lista7) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 1.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista8 != []:

                        e = lista8[0]
                        lista8.remove(e)

                        if (str(e) in lista8) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 2.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.            
                if guia == 1:

                    while lista9 != []:

                        e = lista9[0]
                        lista9.remove(e)

                        if (str(e) in lista9) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 3.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista10 != []:

                        e = lista10[0]
                        lista10.remove(e)

                        if (str(e) in lista10) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 4.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista11 != []:

                        e = lista11[0]
                        lista11.remove(e)

                        if (str(e) in lista11) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 5.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista12 != []:

                        e = lista12[0]
                        lista12.remove(e)

                        if (str(e) in lista12) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 6.", icon = "warning")

                # Algoritmo que determinara si las casillas relacionas con la operacion matematica respectiva, dan el resultado correcto.
                for e in range(1,len(a) + 1):

                    tupla = a[e]

                    string = tupla[0]

                    paresOrdenados = tupla[1:]

                    nuevos = []

                    # Se determinaran cuales pares ordenados deben ir juntos con respecto al dicciorio utilizado.
                    for i in tupla[1:]:

                        p = str(i[0]) + str(i[1])

                        nuevos.append(p)

                    valores = []

                    # Algoritmo para identificar cuales valores se encuentran en las casillas respectivas.
                    for i in nuevos:

                        if i == "11":

                            valores.append(t11)

                        elif i == "21":

                            valores.append(t12)
                            

                        elif i == "31":

                            valores.append(t13)

                        elif i == "41":

                            valores.append(t14)

                        elif i == "51":

                            valores.append(t15)

                        elif i == "61":

                            valores.append(t16)
                            
                        elif i == "12":

                            valores.append(t21)

                        elif i == "22":

                            valores.append(t22)

                        elif i == "32":

                            valores.append(t23)

                        elif i == "42":

                            valores.append(t24)

                        elif i == "52":

                            valores.append(t25)

                        elif i == "62":

                            valores.append(t26)

                        elif i == "13":

                            valores.append(t31)

                        elif i == "23":

                            valores.append(t32)

                        elif i == "33":

                            valores.append(t33)

                        elif i == "43":

                            valores.append(t34)

                        elif i == "53":

                            valores.append(t35)

                        elif i == "63":

                            valores.append(t36)

                        elif i == "14":

                            valores.append(t41)

                        elif i == "24":

                            valores.append(t42)

                        elif i == "34":

                            valores.append(t43)

                        elif i == "44":

                            valores.append(t44)

                        elif i == "54":

                            valores.append(t45)

                        elif i == "64":

                            valores.append(t46)

                        elif i == "15":

                            valores.append(t51)

                        elif i == "25":

                            valores.append(t52)

                        elif i == "35":

                            valores.append(t53)

                        elif i == "45":

                            valores.append(t54)

                        elif i == "55":

                            valores.append(t55)

                        elif i == "65":

                            valores.append(t56)

                        elif i == "16":

                            valores.append(t61)

                        elif i == "26":

                            valores.append(t62)

                        elif i == "36":

                            valores.append(t63)

                        elif i == "46":

                            valores.append(t64)

                        elif i == "56":

                            valores.append(t65)

                        elif i == "66":

                            valores.append(t66)

                    # Se ordenara la lista de mayor a menor
                    valores.sort(reverse = True)

                    # Se asignara el string de la operacion matematica a la siguiente variable.
                    resultado = int(string[:-1])

                    # Simbolo de la operacion matematica.
                    s = string[-1]

                    resta = 0

                    # Condiciones necesarias para retornar el resultado correcto.
                    if s == "x":

                        final = 1

                    elif s == "+" or s == "-":

                        final = 0

                    if s == "+" or s == "-" or s == "x":
                        
                        for i in valores:

                            if s == "+":

                                final = final + int(i)

                            elif s == "-":

                                if resta == 0:

                                    final = final - int(i)
                                    resta = resta + 1

                                else:

                                    final = final + int(i)

                            elif s == "x":

                                final = final * int(i)

                        if s == "-":

                            final = abs(final)

                    else:

                        final = int(int(valores[0]) / int(valores[1]))

                    # Condicion que determina si el resultado indicado por la etiqueta es el mismo resultado obtenido segun los valores digitados por el usuario.
                    if final != resultado:

                        messagebox.showinfo("Error", "Revise las casillas de la operación " + string + ".", icon = "warning")
                        guia = 0

                    # Se reinicia esta variable para no tenes todos los pares ordenados en una misma lista.
                    valores = []

                # Condicion que reproducira el sondio cuando se gane la partida.
                if guia == 1:

                    # Condicion que determina si el usuario quiere reproducir el sonido o no.
                    if S == 1:
                        
                        pygame.init()

                        zelda = pygame.mixer.music.load("You win sound effect 5.mp3")

                        pygame.mixer.music.play(1)

                    messagebox.showinfo("Aviso", " Felicidades!!!\n Completaste el kenken.")

                    break

            if T == 5:

                # Obtencion de todos los valores presentes en los cuadros de texto de la cuadricula.
                t11 = self.s11.get()
                t12 = self.s12.get()
                t13 = self.s13.get()
                t14 = self.s14.get()
                t15 = self.s15.get()
                t16 = self.s16.get()
                t17 = self.s17.get()

                t21 = self.s21.get()
                t22 = self.s22.get()
                t23 = self.s23.get()
                t24 = self.s24.get()
                t25 = self.s25.get()
                t26 = self.s26.get()
                t27 = self.s27.get()

                t31 = self.s31.get()
                t32 = self.s32.get()
                t33 = self.s33.get()
                t34 = self.s34.get()
                t35 = self.s35.get()
                t36 = self.s36.get()
                t37 = self.s37.get()

                t41 = self.s41.get()
                t42 = self.s42.get()
                t43 = self.s43.get()
                t44 = self.s44.get()
                t45 = self.s45.get()
                t46 = self.s46.get()
                t47 = self.s47.get()

                t51 = self.s51.get()
                t52 = self.s52.get()
                t53 = self.s53.get()
                t54 = self.s54.get()
                t55 = self.s55.get()
                t56 = self.s56.get()
                t57 = self.s57.get()

                t61 = self.s61.get()
                t62 = self.s62.get()
                t63 = self.s63.get()
                t64 = self.s64.get()
                t65 = self.s65.get()
                t66 = self.s66.get()
                t67 = self.s67.get()

                t71 = self.s71.get()
                t72 = self.s72.get()
                t73 = self.s73.get()
                t74 = self.s74.get()
                t75 = self.s75.get()
                t76 = self.s76.get()
                t77 = self.s77.get()

                # Lista que contendra los valores ordenados por filas.
                lista1 = [t11,t21,t31,t41,t51,t61,t71]
                lista2 = [t12,t22,t32,t42,t52,t62,t72]
                lista3 = [t13,t23,t33,t43,t53,t63,t73]
                lista4 = [t14,t24,t34,t44,t54,t64,t74]
                lista5 = [t15,t25,t35,t45,t55,t65,t75]
                lista6 = [t16,t26,t36,t46,t56,t66,t76]
                lista7 = [t17,t27,t37,t47,t57,t67,t77]

                # Lista que contendra los valores ordenados por columnas.
                lista8 = [t11,t12,t13,t14,t15,t16,t17]
                lista9 = [t21,t22,t23,t24,t25,t26,t27]
                lista10 = [t31,t32,t33,t34,t35,t36,t37]
                lista11 = [t41,t42,t43,t44,t45,t46,t47]
                lista12 = [t51,t52,t53,t54,t55,t56,t57]
                lista13 = [t61,t62,t63,t64,t65,t66,t67]
                lista14 = [t71,t72,t73,t74,t75,t76,t77]

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista1) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 1.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista2) == True:
                    
                    messagebox.showinfo("Error", "Espacios en blanco en la fila 2.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 3.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 4.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista5) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 5.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista6) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 6.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista7) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 7.", icon = "warning")
                    espacio = True

                # Si existe algun espacio en blanco en la cuadricula, se cerrara el ciclo while.
                if espacio == True:

                    break

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista1 != []:

                        e = lista1[0]
                        lista1.remove(e)

                        if (str(e) in lista1) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 1.", icon = "warning")                        

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista2 != []:

                        e = lista2[0]
                        lista2.remove(e)

                        if (str(e) in lista2) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 2.", icon = "warning")                        

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista3 != []:

                        e = lista3[0]
                        lista3.remove(e)

                        if (str(e) in lista3) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 3.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista4 != []:

                        e = lista4[0]
                        lista4.remove(e)

                        if (str(e) in lista4) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 4.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista5 != []:

                        e = lista5[0]
                        lista5.remove(e)

                        if (str(e) in lista5) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 5.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista6 != []:

                        e = lista6[0]
                        lista6.remove(e)

                        if (str(e) in lista6) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 6.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista7 != []:

                        e = lista7[0]
                        lista7.remove(e)

                        if (str(e) in lista7) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 7.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista8 != []:

                        e = lista8[0]
                        lista8.remove(e)

                        if (str(e) in lista8) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 1.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista9 != []:

                        e = lista9[0]
                        lista9.remove(e)

                        if (str(e) in lista9) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 2.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.            
                if guia == 1:

                    while lista10 != []:

                        e = lista10[0]
                        lista10.remove(e)

                        if (str(e) in lista10) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 3.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista11 != []:

                        e = lista11[0]
                        lista11.remove(e)

                        if (str(e) in lista11) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 4.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista12 != []:

                        e = lista12[0]
                        lista12.remove(e)

                        if (str(e) in lista12) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 5.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista13 != []:

                        e = lista13[0]
                        lista13.remove(e)

                        if (str(e) in lista13) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 6.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista14 != []:

                        e = lista14[0]
                        lista14.remove(e)

                        if (str(e) in lista14) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 7.", icon = "warning")

                # Algoritmo que determinara si las casillas relacionas con la operacion matematica respectiva, dan el resultado correcto.
                for e in range(1,len(a) + 1):

                    tupla = a[e]

                    string = tupla[0]

                    paresOrdenados = tupla[1:]

                    nuevos = []

                    # Se determinaran cuales pares ordenados deben ir juntos con respecto al dicciorio utilizado.
                    for i in tupla[1:]:

                        p = str(i[0]) + str(i[1])

                        nuevos.append(p)

                    valores = []

                    # Algoritmo para identificar cuales valores se encuentran en las casillas respectivas.
                    for i in nuevos:

                        if i == "11":

                            valores.append(t11)

                        elif i == "21":

                            valores.append(t12)
                            

                        elif i == "31":

                            valores.append(t13)

                        elif i == "41":

                            valores.append(t14)

                        elif i == "51":

                            valores.append(t15)

                        elif i == "61":

                            valores.append(t16)

                        elif i == "71":

                            valores.append(t17)
                            
                        elif i == "12":

                            valores.append(t21)

                        elif i == "22":

                            valores.append(t22)

                        elif i == "32":

                            valores.append(t23)

                        elif i == "42":

                            valores.append(t24)

                        elif i == "52":

                            valores.append(t25)

                        elif i == "62":

                            valores.append(t26)

                        elif i == "72":

                            valores.append(t27)

                        elif i == "13":

                            valores.append(t31)

                        elif i == "23":

                            valores.append(t32)

                        elif i == "33":

                            valores.append(t33)

                        elif i == "43":

                            valores.append(t34)

                        elif i == "53":

                            valores.append(t35)

                        elif i == "63":

                            valores.append(t36)

                        elif i == "73":

                            valores.append(t37)

                        elif i == "14":

                            valores.append(t41)

                        elif i == "24":

                            valores.append(t42)

                        elif i == "34":

                            valores.append(t43)

                        elif i == "44":

                            valores.append(t44)

                        elif i == "54":

                            valores.append(t45)

                        elif i == "64":

                            valores.append(t46)

                        elif i == "74":

                            valores.append(t47)

                        elif i == "15":

                            valores.append(t51)

                        elif i == "25":

                            valores.append(t52)

                        elif i == "35":

                            valores.append(t53)

                        elif i == "45":

                            valores.append(t54)

                        elif i == "55":

                            valores.append(t55)

                        elif i == "65":

                            valores.append(t56)

                        elif i == "75":

                            valores.append(t57)

                        elif i == "16":

                            valores.append(t61)

                        elif i == "26":

                            valores.append(t62)

                        elif i == "36":

                            valores.append(t63)

                        elif i == "46":

                            valores.append(t64)

                        elif i == "56":

                            valores.append(t65)

                        elif i == "66":

                            valores.append(t66)

                        elif i == "76":

                            valores.append(t67)

                        elif i == "17":

                            valores.append(t71)

                        elif i == "27":

                            valores.append(t72)

                        elif i == "37":

                            valores.append(t73)

                        elif i == "47":

                            valores.append(t74)

                        elif i == "57":

                            valores.append(t75)

                        elif i == "67":

                            valores.append(t76)

                        elif i == "77":

                            valores.append(t77)

                    # Se ordenara la lista de mayor a menor
                    valores.sort(reverse = True)

                    # Se asignara el string de la operacion matematica a la siguiente variable.
                    resultado = int(string[:-1])

                    # Simbolo de la operacion matematica.
                    s = string[-1]

                    resta = 0

                    # Condiciones necesarias para retornar el resultado correcto.
                    if s == "x":

                        final = 1

                    elif s == "+" or s == "-":

                        final = 0

                    if s == "+" or s == "-" or s == "x":
                        
                        for i in valores:

                            if s == "+":

                                final = final + int(i)

                            elif s == "-":

                                if resta == 0:

                                    final = final - int(i)
                                    resta = resta + 1

                                else:

                                    final = final + int(i)

                            elif s == "x":

                                final = final * int(i)

                        if s == "-":

                            final = abs(final)

                    else:

                        final = int(int(valores[0]) / int(valores[1]))

                    # Condicion que determina si el resultado indicado por la etiqueta es el mismo resultado obtenido segun los valores digitados por el usuario.
                    if final != resultado:

                        messagebox.showinfo("Error", "Revise las casillas de la operación " + string + ".", icon = "warning")
                        guia = 0

                    # Se reinicia esta variable para no tenes todos los pares ordenados en una misma lista.
                    valores = []

                # Condicion que reproducira el sondio cuando se gane la partida.
                if guia == 1:

                    # Condicion que determina si el usuario quiere reproducir el sonido o no.
                    if S == 1:
                        
                        pygame.init()

                        zelda = pygame.mixer.music.load("You win sound effect 5.mp3")

                        pygame.mixer.music.play(1)

                    messagebox.showinfo("Aviso", " Felicidades!!!\n Completaste el kenken.")

                    break

            if T == 6:

                # Obtencion de todos los valores presentes en los cuadros de texto de la cuadricula.
                t11 = self.s11.get()
                t12 = self.s12.get()
                t13 = self.s13.get()
                t14 = self.s14.get()
                t15 = self.s15.get()
                t16 = self.s16.get()
                t17 = self.s17.get()
                t18 = self.s18.get()

                t21 = self.s21.get()
                t22 = self.s22.get()
                t23 = self.s23.get()
                t24 = self.s24.get()
                t25 = self.s25.get()
                t26 = self.s26.get()
                t27 = self.s27.get()
                t28 = self.s28.get()

                t31 = self.s31.get()
                t32 = self.s32.get()
                t33 = self.s33.get()
                t34 = self.s34.get()
                t35 = self.s35.get()
                t36 = self.s36.get()
                t37 = self.s37.get()
                t38 = self.s38.get()

                t41 = self.s41.get()
                t42 = self.s42.get()
                t43 = self.s43.get()
                t44 = self.s44.get()
                t45 = self.s45.get()
                t46 = self.s46.get()
                t47 = self.s47.get()
                t48 = self.s48.get()

                t51 = self.s51.get()
                t52 = self.s52.get()
                t53 = self.s53.get()
                t54 = self.s54.get()
                t55 = self.s55.get()
                t56 = self.s56.get()
                t57 = self.s57.get()
                t58 = self.s58.get()

                t61 = self.s61.get()
                t62 = self.s62.get()
                t63 = self.s63.get()
                t64 = self.s64.get()
                t65 = self.s65.get()
                t66 = self.s66.get()
                t67 = self.s67.get()
                t68 = self.s68.get()

                t71 = self.s71.get()
                t72 = self.s72.get()
                t73 = self.s73.get()
                t74 = self.s74.get()
                t75 = self.s75.get()
                t76 = self.s76.get()
                t77 = self.s77.get()
                t78 = self.s78.get()

                t81 = self.s81.get()
                t82 = self.s82.get()
                t83 = self.s83.get()
                t84 = self.s84.get()
                t85 = self.s85.get()
                t86 = self.s86.get()
                t87 = self.s87.get()
                t88 = self.s88.get()

                # Lista que contendra los valores ordenados por filas.
                lista1 = [t11,t21,t31,t41,t51,t61,t71,t81]
                lista2 = [t12,t22,t32,t42,t52,t62,t72,t82]
                lista3 = [t13,t23,t33,t43,t53,t63,t73,t83]
                lista4 = [t14,t24,t34,t44,t54,t64,t74,t84]
                lista5 = [t15,t25,t35,t45,t55,t65,t75,t85]
                lista6 = [t16,t26,t36,t46,t56,t66,t76,t86]
                lista7 = [t17,t27,t37,t47,t57,t67,t77,t87]
                lista8 = [t18,t28,t38,t48,t58,t68,t78,t88]

                # Lista que contendra los valores ordenados por columnas.
                lista9 = [t11,t12,t13,t14,t15,t16,t17,t18]
                lista10 = [t21,t22,t23,t24,t25,t26,t27,t28]
                lista11 = [t31,t32,t33,t34,t35,t36,t37,t38]
                lista12 = [t41,t42,t43,t44,t45,t46,t47,t48]
                lista13 = [t51,t52,t53,t54,t55,t56,t57,t58]
                lista14 = [t61,t62,t63,t64,t65,t66,t67,t68]
                lista15 = [t71,t72,t73,t74,t75,t76,t77,t78]
                lista16 = [t81,t82,t83,t84,t85,t86,t87,t88]

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista1) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 1.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista2) == True:
                    
                    messagebox.showinfo("Error", "Espacios en blanco en la fila 2.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 3.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 4.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista5) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 5.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista6) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 6.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista7) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 7.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista8) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 8.", icon = "warning")
                    espacio = True

                # Si existe algun espacio en blanco en la cuadricula, se cerrara el ciclo while.
                if espacio == True:

                    break

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista1 != []:

                        e = lista1[0]
                        lista1.remove(e)

                        if (str(e) in lista1) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 1.", icon = "warning")                        

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista2 != []:

                        e = lista2[0]
                        lista2.remove(e)

                        if (str(e) in lista2) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 2.", icon = "warning")                        

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista3 != []:

                        e = lista3[0]
                        lista3.remove(e)

                        if (str(e) in lista3) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 3.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista4 != []:

                        e = lista4[0]
                        lista4.remove(e)

                        if (str(e) in lista4) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 4.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista5 != []:

                        e = lista5[0]
                        lista5.remove(e)

                        if (str(e) in lista5) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 5.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista6 != []:

                        e = lista6[0]
                        lista6.remove(e)

                        if (str(e) in lista6) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 6.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista7 != []:

                        e = lista7[0]
                        lista7.remove(e)

                        if (str(e) in lista7) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 7.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista8 != []:

                        e = lista8[0]
                        lista8.remove(e)

                        if (str(e) in lista8) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 8.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista9 != []:

                        e = lista9[0]
                        lista9.remove(e)

                        if (str(e) in lista9) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 1.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista10 != []:

                        e = lista10[0]
                        lista10.remove(e)

                        if (str(e) in lista10) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 2.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.            
                if guia == 1:

                    while lista11 != []:

                        e = lista11[0]
                        lista11.remove(e)

                        if (str(e) in lista11) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 3.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista12 != []:

                        e = lista12[0]
                        lista12.remove(e)

                        if (str(e) in lista12) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 4.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista13 != []:

                        e = lista13[0]
                        lista12.remove(e)

                        if (str(e) in lista13) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 5.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista14 != []:

                        e = lista14[0]
                        lista14.remove(e)

                        if (str(e) in lista14) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 6.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista15 != []:

                        e = lista15[0]
                        lista15.remove(e)

                        if (str(e) in lista15) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 7.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista16 != []:

                        e = lista16[0]
                        lista15.remove(e)

                        if (str(e) in lista16) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 8.", icon = "warning")

                # Algoritmo que determinara si las casillas relacionas con la operacion matematica respectiva, dan el resultado correcto.
                for e in range(1,len(a) + 1):

                    tupla = a[e]

                    string = tupla[0]

                    paresOrdenados = tupla[1:]

                    nuevos = []

                    # Se determinaran cuales pares ordenados deben ir juntos con respecto al dicciorio utilizado.
                    for i in tupla[1:]:

                        p = str(i[0]) + str(i[1])

                        nuevos.append(p)

                    valores = []

                    # Algoritmo para identificar cuales valores se encuentran en las casillas respectivas.
                    for i in nuevos:

                        if i == "11":

                            valores.append(t11)

                        elif i == "21":

                            valores.append(t12)
                            

                        elif i == "31":

                            valores.append(t13)

                        elif i == "41":

                            valores.append(t14)

                        elif i == "51":

                            valores.append(t15)

                        elif i == "61":

                            valores.append(t16)

                        elif i == "71":

                            valores.append(t17)

                        elif i == "81":

                            valores.append(t18)
                            
                        elif i == "12":

                            valores.append(t21)

                        elif i == "22":

                            valores.append(t22)

                        elif i == "32":

                            valores.append(t23)

                        elif i == "42":

                            valores.append(t24)

                        elif i == "52":

                            valores.append(t25)

                        elif i == "62":

                            valores.append(t26)

                        elif i == "72":

                            valores.append(t27)

                        elif i == "82":

                            valores.append(t28)

                        elif i == "13":

                            valores.append(t31)

                        elif i == "23":

                            valores.append(t32)

                        elif i == "33":

                            valores.append(t33)

                        elif i == "43":

                            valores.append(t34)

                        elif i == "53":

                            valores.append(t35)

                        elif i == "63":

                            valores.append(t36)

                        elif i == "73":

                            valores.append(t37)

                        elif i == "83":

                            valores.append(t38)

                        elif i == "14":

                            valores.append(t41)

                        elif i == "24":

                            valores.append(t42)

                        elif i == "34":

                            valores.append(t43)

                        elif i == "44":

                            valores.append(t44)

                        elif i == "54":

                            valores.append(t45)

                        elif i == "64":

                            valores.append(t46)

                        elif i == "74":

                            valores.append(t47)

                        elif i == "84":

                            valores.append(t48)

                        elif i == "15":

                            valores.append(t51)

                        elif i == "25":

                            valores.append(t52)

                        elif i == "35":

                            valores.append(t53)

                        elif i == "45":

                            valores.append(t54)

                        elif i == "55":

                            valores.append(t55)

                        elif i == "65":

                            valores.append(t56)

                        elif i == "75":

                            valores.append(t57)

                        elif i == "85":

                            valores.append(t58)

                        elif i == "16":

                            valores.append(t61)

                        elif i == "26":

                            valores.append(t62)

                        elif i == "36":

                            valores.append(t63)

                        elif i == "46":

                            valores.append(t64)

                        elif i == "56":

                            valores.append(t65)

                        elif i == "66":

                            valores.append(t66)

                        elif i == "76":

                            valores.append(t67)

                        elif i == "86":

                            valores.append(t68)

                        elif i == "17":

                            valores.append(t71)

                        elif i == "27":

                            valores.append(t72)

                        elif i == "37":

                            valores.append(t73)

                        elif i == "47":

                            valores.append(t74)

                        elif i == "57":

                            valores.append(t75)

                        elif i == "67":

                            valores.append(t76)

                        elif i == "77":

                            valores.append(t77)

                        elif i == "87":

                            valores.append(t78)

                        elif i == "18":

                            valores.append(t81)

                        elif i == "28":

                            valores.append(t82)

                        elif i == "38":

                            valores.append(t83)

                        elif i == "48":

                            valores.append(t84)

                        elif i == "58":

                            valores.append(t85)

                        elif i == "68":

                            valores.append(t86)

                        elif i == "78":

                            valores.append(t87)

                        elif i == "88":

                            valores.append(t88)

                    # Se ordenara la lista de mayor a menor
                    valores.sort(reverse = True)

                    # Se asignara el string de la operacion matematica a la siguiente variable.
                    resultado = int(string[:-1])

                    # Simbolo de la operacion matematica.
                    s = string[-1]

                    resta = 0

                    # Condiciones necesarias para retornar el resultado correcto.
                    if s == "x":

                        final = 1

                    elif s == "+" or s == "-":

                        final = 0

                    if s == "+" or s == "-" or s == "x":
                        
                        for i in valores:

                            if s == "+":

                                final = final + int(i)

                            elif s == "-":

                                if resta == 0:

                                    final = final - int(i)
                                    resta = resta + 1

                                else:

                                    final = final + int(i)

                            elif s == "x":

                                final = final * int(i)

                        if s == "-":

                            final = abs(final)

                    else:

                        final = int(int(valores[0]) / int(valores[1]))

                    # Condicion que determina si el resultado indicado por la etiqueta es el mismo resultado obtenido segun los valores digitados por el usuario.
                    if final != resultado:

                        messagebox.showinfo("Error", "Revise las casillas de la operación " + string + ".", icon = "warning")
                        guia = 0

                    # Se reinicia esta variable para no tenes todos los pares ordenados en una misma lista.
                    valores = []

                # Condicion que reproducira el sondio cuando se gane la partida.
                if guia == 1:

                    # Condicion que determina si el usuario quiere reproducir el sonido o no.
                    if S == 1:
                        
                        pygame.init()

                        zelda = pygame.mixer.music.load("You win sound effect 5.mp3")

                        pygame.mixer.music.play(1)

                    messagebox.showinfo("Aviso", " Felicidades!!!\n Completaste el kenken.")

                    break




















                

            if T == 7:

                # Obtencion de todos los valores presentes en los cuadros de texto de la cuadricula.
                t11 = self.s11.get()
                t12 = self.s12.get()
                t13 = self.s13.get()
                t14 = self.s14.get()
                t15 = self.s15.get()
                t16 = self.s16.get()
                t17 = self.s17.get()
                t18 = self.s18.get()
                t19 = self.s19.get()

                t21 = self.s21.get()
                t22 = self.s22.get()
                t23 = self.s23.get()
                t24 = self.s24.get()
                t25 = self.s25.get()
                t26 = self.s26.get()
                t27 = self.s27.get()
                t28 = self.s28.get()
                t29 = self.s29.get()

                t31 = self.s31.get()
                t32 = self.s32.get()
                t33 = self.s33.get()
                t34 = self.s34.get()
                t35 = self.s35.get()
                t36 = self.s36.get()
                t37 = self.s37.get()
                t38 = self.s38.get()
                t39 = self.s39.get()

                t41 = self.s41.get()
                t42 = self.s42.get()
                t43 = self.s43.get()
                t44 = self.s44.get()
                t45 = self.s45.get()
                t46 = self.s46.get()
                t47 = self.s47.get()
                t48 = self.s48.get()
                t49 = self.s49.get()

                t51 = self.s51.get()
                t52 = self.s52.get()
                t53 = self.s53.get()
                t54 = self.s54.get()
                t55 = self.s55.get()
                t56 = self.s56.get()
                t57 = self.s57.get()
                t58 = self.s58.get()
                t59 = self.s59.get()

                t61 = self.s61.get()
                t62 = self.s62.get()
                t63 = self.s63.get()
                t64 = self.s64.get()
                t65 = self.s65.get()
                t66 = self.s66.get()
                t67 = self.s67.get()
                t68 = self.s68.get()
                t69 = self.s69.get()

                t71 = self.s71.get()
                t72 = self.s72.get()
                t73 = self.s73.get()
                t74 = self.s74.get()
                t75 = self.s75.get()
                t76 = self.s76.get()
                t77 = self.s77.get()
                t78 = self.s78.get()
                t79 = self.s79.get()

                t81 = self.s81.get()
                t82 = self.s82.get()
                t83 = self.s83.get()
                t84 = self.s84.get()
                t85 = self.s85.get()
                t86 = self.s86.get()
                t87 = self.s87.get()
                t88 = self.s88.get()
                t89 = self.s89.get()

                t91 = self.s81.get()
                t92 = self.s82.get()
                t93 = self.s83.get()
                t94 = self.s84.get()
                t95 = self.s85.get()
                t96 = self.s86.get()
                t97 = self.s87.get()
                t98 = self.s88.get()
                t99 = self.s89.get()

                # Lista que contendra los valores ordenados por filas.
                lista1 = [t11,t21,t31,t41,t51,t61,t71,t81,t91]
                lista2 = [t12,t22,t32,t42,t52,t62,t72,t82,t92]
                lista3 = [t13,t23,t33,t43,t53,t63,t73,t83,t93]
                lista4 = [t14,t24,t34,t44,t54,t64,t74,t84,t94]
                lista5 = [t15,t25,t35,t45,t55,t65,t75,t85,t95]
                lista6 = [t16,t26,t36,t46,t56,t66,t76,t86,t96]
                lista7 = [t17,t27,t37,t47,t57,t67,t77,t87,t97]
                lista8 = [t18,t28,t38,t48,t58,t68,t78,t88,t98]
                lista9 = [t19,t29,t39,t49,t59,t69,t79,t89,t99]

                # Lista que contendra los valores ordenados por columnas.
                lista10 = [t11,t12,t13,t14,t15,t16,t17,t18,t19]
                lista11 = [t21,t22,t23,t24,t25,t26,t27,t28,t29]
                lista12 = [t31,t32,t33,t34,t35,t36,t37,t38,t39]
                lista13 = [t41,t42,t43,t44,t45,t46,t47,t48,t49]
                lista14 = [t51,t52,t53,t54,t55,t56,t57,t58,t59]
                lista15 = [t61,t62,t63,t64,t65,t66,t67,t68,t69]
                lista16 = [t71,t72,t73,t74,t75,t76,t77,t78,t79]
                lista17 = [t81,t82,t83,t84,t85,t86,t87,t88,t89]
                lista18 = [t91,t92,t93,t94,t95,t96,t97,t98,t99]

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista1) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 1.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista2) == True:
                    
                    messagebox.showinfo("Error", "Espacios en blanco en la fila 2.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 3.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 4.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista5) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 5.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista6) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 6.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista7) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 7.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista8) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 8.", icon = "warning")
                    espacio = True

                # Condicion que determina si se hna rellenado los cuadros de texto especificos o no.
                if ("" in lista9) == True:

                    messagebox.showinfo("Error", "Espacios en blanco en la fila 9.", icon = "warning")
                    espacio = True

                # Si existe algun espacio en blanco en la cuadricula, se cerrara el ciclo while.
                if espacio == True:

                    break

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista1 != []:

                        e = lista1[0]
                        lista1.remove(e)

                        if (str(e) in lista1) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 1.", icon = "warning")                        

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista2 != []:

                        e = lista2[0]
                        lista2.remove(e)

                        if (str(e) in lista2) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 2.", icon = "warning")                        

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista3 != []:

                        e = lista3[0]
                        lista3.remove(e)

                        if (str(e) in lista3) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 3.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista4 != []:

                        e = lista4[0]
                        lista4.remove(e)

                        if (str(e) in lista4) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 4.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista5 != []:

                        e = lista5[0]
                        lista5.remove(e)

                        if (str(e) in lista5) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 5.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista6 != []:

                        e = lista6[0]
                        lista6.remove(e)

                        if (str(e) in lista6) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 6.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista7 != []:

                        e = lista7[0]
                        lista7.remove(e)

                        if (str(e) in lista7) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 7.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista8 != []:

                        e = lista8[0]
                        lista8.remove(e)

                        if (str(e) in lista8) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 8.", icon = "warning")

                # Condicion que determina si en la fila especifica existen valores repetidos.
                if guia == 1:

                    while lista9 != []:

                        e = lista9[0]
                        lista9.remove(e)

                        if (str(e) in lista9) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la fila 9.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista10 != []:

                        e = lista10[0]
                        lista10.remove(e)

                        if (str(e) in lista10) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 1.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista11 != []:

                        e = lista11[0]
                        lista11.remove(e)

                        if (str(e) in lista11) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 2.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.            
                if guia == 1:

                    while lista12 != []:

                        e = lista12[0]
                        lista12.remove(e)

                        if (str(e) in lista12) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 3.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista13 != []:

                        e = lista13[0]
                        lista13.remove(e)

                        if (str(e) in lista13) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 4.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista14 != []:

                        e = lista14[0]
                        lista14.remove(e)

                        if (str(e) in lista14) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 5.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista15 != []:

                        e = lista15[0]
                        lista15.remove(e)

                        if (str(e) in lista15) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 6.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista16 != []:

                        e = lista16[0]
                        lista16.remove(e)

                        if (str(e) in lista16) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 7.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista17 != []:

                        e = lista17[0]
                        lista17.remove(e)

                        if (str(e) in lista17) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 8.", icon = "warning")

                # Condicion que determina si en la colunma especifica existen valores repetidos.
                if guia == 1:

                    while lista18 != []:

                        e = lista18[0]
                        lista18.remove(e)

                        if (str(e) in lista18) == True:

                            guia = 0
                            messagebox.showinfo("Error", "Errores en la columna 9.", icon = "warning")

                # Algoritmo que determinara si las casillas relacionas con la operacion matematica respectiva, dan el resultado correcto.
                for e in range(1,len(a) + 1):

                    tupla = a[e]

                    string = tupla[0]

                    paresOrdenados = tupla[1:]

                    nuevos = []

                    # Se determinaran cuales pares ordenados deben ir juntos con respecto al dicciorio utilizado.
                    for i in tupla[1:]:

                        p = str(i[0]) + str(i[1])

                        nuevos.append(p)

                    valores = []

                    # Algoritmo para identificar cuales valores se encuentran en las casillas respectivas.
                    for i in nuevos:

                        if i == "11":

                            valores.append(t11)

                        elif i == "21":

                            valores.append(t12)
                            

                        elif i == "31":

                            valores.append(t13)

                        elif i == "41":

                            valores.append(t14)

                        elif i == "51":

                            valores.append(t15)

                        elif i == "61":

                            valores.append(t16)

                        elif i == "71":

                            valores.append(t17)

                        elif i == "81":

                            valores.append(t18)

                        elif i == "91":

                            valores.append(t19)
                            
                        elif i == "12":

                            valores.append(t21)

                        elif i == "22":

                            valores.append(t22)

                        elif i == "32":

                            valores.append(t23)

                        elif i == "42":

                            valores.append(t24)

                        elif i == "52":

                            valores.append(t25)

                        elif i == "62":

                            valores.append(t26)

                        elif i == "72":

                            valores.append(t27)

                        elif i == "82":

                            valores.append(t28)

                        elif i == "92":

                            valores.append(t29)

                        elif i == "13":

                            valores.append(t31)

                        elif i == "23":

                            valores.append(t32)

                        elif i == "33":

                            valores.append(t33)

                        elif i == "43":

                            valores.append(t34)

                        elif i == "53":

                            valores.append(t35)

                        elif i == "63":

                            valores.append(t36)

                        elif i == "73":

                            valores.append(t37)

                        elif i == "83":

                            valores.append(t38)

                        elif i == "93":

                            valores.append(t39)

                        elif i == "14":

                            valores.append(t41)

                        elif i == "24":

                            valores.append(t42)

                        elif i == "34":

                            valores.append(t43)

                        elif i == "44":

                            valores.append(t44)

                        elif i == "54":

                            valores.append(t45)

                        elif i == "64":

                            valores.append(t46)

                        elif i == "74":

                            valores.append(t47)

                        elif i == "84":

                            valores.append(t48)

                        elif i == "94":

                            valores.append(t49)

                        elif i == "15":

                            valores.append(t51)

                        elif i == "25":

                            valores.append(t52)

                        elif i == "35":

                            valores.append(t53)

                        elif i == "45":

                            valores.append(t54)

                        elif i == "55":

                            valores.append(t55)

                        elif i == "65":

                            valores.append(t56)

                        elif i == "75":

                            valores.append(t57)

                        elif i == "85":

                            valores.append(t58)

                        elif i == "95":

                            valores.append(t59)

                        elif i == "16":

                            valores.append(t61)

                        elif i == "26":

                            valores.append(t62)

                        elif i == "36":

                            valores.append(t63)

                        elif i == "46":

                            valores.append(t64)

                        elif i == "56":

                            valores.append(t65)

                        elif i == "66":

                            valores.append(t66)

                        elif i == "76":

                            valores.append(t67)

                        elif i == "86":

                            valores.append(t68)

                        elif i == "96":

                            valores.append(t69)

                        elif i == "17":

                            valores.append(t71)

                        elif i == "27":

                            valores.append(t72)

                        elif i == "37":

                            valores.append(t73)

                        elif i == "47":

                            valores.append(t74)

                        elif i == "57":

                            valores.append(t75)

                        elif i == "67":

                            valores.append(t76)

                        elif i == "77":

                            valores.append(t77)

                        elif i == "87":

                            valores.append(t78)

                        elif i == "97":

                            valores.append(t79)

                        elif i == "18":

                            valores.append(t81)

                        elif i == "28":

                            valores.append(t82)

                        elif i == "38":

                            valores.append(t83)

                        elif i == "48":

                            valores.append(t84)

                        elif i == "58":

                            valores.append(t85)

                        elif i == "68":

                            valores.append(t86)

                        elif i == "78":

                            valores.append(t87)

                        elif i == "88":

                            valores.append(t88)

                        elif i == "98":

                            valores.append(t89)

                        elif i == "19":

                            valores.append(t91)

                        elif i == "29":

                            valores.append(t92)

                        elif i == "39":

                            valores.append(t93)

                        elif i == "49":

                            valores.append(t94)

                        elif i == "59":

                            valores.append(t95)

                        elif i == "69":

                            valores.append(t96)

                        elif i == "79":

                            valores.append(t97)

                        elif i == "89":

                            valores.append(t98)

                        elif i == "99":

                            valores.append(t99)

                    # Se ordenara la lista de mayor a menor
                    valores.sort(reverse = True)

                    # Se asignara el string de la operacion matematica a la siguiente variable.
                    resultado = int(string[:-1])

                    # Simbolo de la operacion matematica.
                    s = string[-1]

                    resta = 0

                    # Condiciones necesarias para retornar el resultado correcto.
                    if s == "x":

                        final = 1

                    elif s == "+" or s == "-":

                        final = 0

                    if s == "+" or s == "-" or s == "x":
                        
                        for i in valores:

                            if s == "+":

                                final = final + int(i)

                            elif s == "-":

                                if resta == 0:

                                    final = final - int(i)
                                    resta = resta + 1

                                else:

                                    final = final + int(i)

                            elif s == "x":

                                final = final * int(i)

                        if s == "-":

                            final = abs(final)

                    else:

                        final = int(int(valores[0]) / int(valores[1]))

                    # Condicion que determina si el resultado indicado por la etiqueta es el mismo resultado obtenido segun los valores digitados por el usuario.
                    if final != resultado:

                        messagebox.showinfo("Error", "Revise las casillas de la operación " + string + ".", icon = "warning")
                        guia = 0

                    # Se reinicia esta variable para no tenes todos los pares ordenados en una misma lista.
                    valores = []

                # Condicion que reproducira el sondio cuando se gane la partida.
                if guia == 1:

                    # Condicion que determina si el usuario quiere reproducir el sonido o no.
                    if S == 1:
                        
                        pygame.init()

                        zelda = pygame.mixer.music.load("You win sound effect 5.mp3")

                        pygame.mixer.music.play(1)

                    messagebox.showinfo("Aviso", " Felicidades!!!\n Completaste el kenken.")

                    break

    # Funcion del boton asignado.
    def Otro(self):
        opcion1 = messagebox.askquestion("Otro juego", "¿Está seguro de empezar otro juego?", icon = "warning")
        if opcion1 == "yes":
            # Se cerrara la ventana actual.
            self.destroy()
            # Se abrira la nueva ventana solicitada.
            Jugar().mainloop()

    # Funcion del boton asignado.
    def Reiniciar(self):

        global Activo
        global R

        Activo = False

        # Se abrira una nueva ventana con la opcion de reiniciar la partida, si este es si, entonces la partida se reiniciara.
        opcion = messagebox.askquestion("Reiniciar", "¿Está seguro de empezar nuevamente este mismo juego?", icon = "warning")

        # Si el usuario desea reiniciar la partida, entonces se eliminaran todos los valores de los cuadros de texto y se reiniciara el reloj en caso de haber habilitado esa opcion.
        if opcion == "yes":

            t11 = self.s11.set("")
            t12 = self.s12.set("")
            t13 = self.s13.set("")
            t14 = self.s14.set("")
            t15 = self.s15.set("")
            t16 = self.s16.set("")

            t21 = self.s21.set("")
            t22 = self.s22.set("")
            t23 = self.s23.set("")
            t24 = self.s24.set("")
            t25 = self.s25.set("")
            t26 = self.s26.set("")

            t31 = self.s31.set("")
            t32 = self.s32.set("")
            t33 = self.s33.set("")
            t34 = self.s34.set("")
            t35 = self.s35.set("")
            t36 = self.s36.set("")

            t41 = self.s41.set("")
            t42 = self.s42.set("")
            t43 = self.s43.set("")
            t44 = self.s44.set("")
            t45 = self.s45.set("")
            t46 = self.s46.set("")

            t51 = self.s51.set("")
            t52 = self.s52.set("")
            t53 = self.s53.set("")
            t54 = self.s54.set("")
            t55 = self.s55.set("")
            t56 = self.s56.set("")

            t61 = self.s61.set("")
            t62 = self.s62.set("")
            t63 = self.s63.set("")
            t64 = self.s64.set("")
            t65 = self.s65.set("")
            t66 = self.s66.set("")

            if R == 1 or R == 2:
                
                self.TiempoHoras.set(0)
                self.TiempoMinutos.set(0)
                self.TiempoSegundos.set(0)

            elif R == 3:

                self.TiempoHoras.set(PronosticoH)
                self.TiempoMinutos.set(PronosticoM)
                self.TiempoSegundos.set(PronosticoS)        

    # Funcion del boton asignado.
    def Terminar(self):

        global Jugador
        global listaTop
        global Activo

        Activo = False

        # Se guardaran todos los datos que sean necesarios para otra funciones.
        horasjugador =  self.TiempoHoras.get()
        minutosjugador = self.TiempoMinutos.get()
        segundosjugador = self.TiempoSegundos.get()

        listaTop = listaTop + [horasjugador, minutosjugador, segundosjugador, Jugador]

        # Se abrira una nueva ventana con la opcion de terminar la partida, si este es si, entonces la partida se terminara.
        opcion = messagebox.askquestion("Terminar Juego", "¿Está seguro de terminar juego?", icon = "warning")
        
        if opcion == "yes":
            pygame.mixer.music.stop()
            Jugador = ""
            # Se cerrara la ventana actual.
            Jugar.destroy(self)
            # Se abrira la nueva ventana solicitada.
            menu().mainloop()

    def Pausa(self):
        # Se definira esta variale como global para un buen procesamiento de la funcion.
        global Activo
        # Valor que se le asignara a la variable global.
        Activo = False

    # Funcion del boton asignado.
    def TOP(self):
     
        # Se abrira la nueva ventana solicitada.
        Top().mainloop()

    # Funcion del boton asignado.
    global Jugador
    
    Jugador = ""
    
    def GuardarNombre(self):

        global Jugador

        # Se guardara el nombre del jugador en la siguiente variable.
        Jugador = self.textBoxJugador.get()

        # Restriccion que debe tener el nombre del jugador.
        if len(Jugador) < 3 or len(Jugador)> 30:

            messagebox.showinfo("Error", "El nombre del jugador debe contener de 3 a 30 caracteres.", icon = "warning")
            self.textBoxJugador.delete(0,END)

    def RegresarMenu(self):
        # Se cerrara la ventana actual.
        self.destroy()
        # Se abrira la nueva ventana solicitada.
        menu().mainloop()
    
#####################################################################################################################################################################################################################

# Esta sera la ventana donde se encontrara la clase de Reloj.   

    # Funcion del boton asignado.
    def Activar(self):
        
        # Se definiran estas variables como globales para un buen procesamiento de la funcion.
        global Activo
        global Jugador
        global SegundosTime

        SegundosTime = int(self.TiempoSegundos.get())
        # Valor que se le asignara a la variable global.
        Activo = True

        # Si no se ha digitado el nombre del jugador, aparecera el siguiente aviso.
        if Jugador == "":

            messagebox.showinfo("Error", "Por favor introduzca el nombre del jugador.", icon = "warning")

        else:

            # Se llamara la funcion solicitada.
            self.Iniciar()
            if SegundosTime == 0 and S == 1:
                pygame.mixer.music.play(-1)

    # Funcion del boton asignado.
    def Iniciar(self):

        # Se definira esta variale como global para un buen procesamiento de la funcion.
        global Activo
        global Jugador
        global HorasT
        global MinutosT
        global SegundosT
        global R

        try:

            # Si no se ha digitado el nombre del jugador, aparecera el siguiente aviso.
            if Jugador == "":

                messagebox.showinfo("Error", "Por favor introduzca un nombre.", icon = "warning")

            else:
                # Se llamara la funcion solicitada.
                self.Cronometrar()
                
        except:

            pass

    # Funcion del boton asignado.
    def Cronometro(self):
                
        # Se cerrara la ventana actual.
        self.destroy()
        # Se abrira la nueva ventana solicitada.
        Cronometro().mainloop()

    # Funcion del boton asignado.
    def Cronometrar(self):

        # Se definiran estas variables como globales para un buen procesamiento de la funcion.
        global Activo
        global HorasT
        global MinutosT
        global SegundosT
        global R
        
        """
        Este sera el cronometro. Para esta funcion se utilizo el metodo .arter() para lograr que el programa espere la cantidad de milisegundos digitados como el primer parametro del metodo
        para poder ejecutar la funcion del segundo parametro. Lo que se programo fue un tipo de ciclo a traves de funciones, sin utilizar ninguna estructura de iteracion. Cuando se ejecute
        la primera funcion, esta ejecutara todas las lineas dentro de ella y luego pasara a otra funcion y ejecutara sus respectivas lineas y se devolvera a la funcion anteriory asi
        sucesivamente, formando un ciclo tomando en cuenta el valor de la variable Activo, si este es True entonces es cronometro se encontrara en movimiento y si pose el valor de
        False, entonces se detendra el tiempo hasta que el usuario desee continuarlo.
        """
        
        if Activo == True:
            
            HorasT = int(self.TiempoHoras.get())
            MinutosT = int(self.TiempoMinutos.get())
            SegundosT = int(self.TiempoSegundos.get())

            if R == 1 or R == 2:

                if SegundosT < 59:
                        
                    SegundosT = SegundosT + 1
                        
                elif SegundosT == 59:
                        
                    SegundosT = 0
                        
                    if MinutosT < 59:
                            
                        MinutosT = MinutosT + 1
                            
                    elif MinutosT == 59:

                        MinutosT = 0
                            
                        HorasT = HorasT + 1

                        if HorasT == 24:

                            HorasT = 0
                            MinutosT = 0
                            SegundosT = 0

                # Se enviaran los siguientes valores a los IntVar de cada parte del cronometro.
                self.TiempoHoras.set(HorasT)
                self.TiempoMinutos.set(MinutosT)
                self.TiempoSegundos.set(SegundosT)

            elif R == 3:

                if SegundosT > 0:
                        
                    SegundosT = SegundosT - 1
                        
                elif SegundosT == 0:
                        
                    SegundosT = 59
                        
                    if MinutosT > 0:
                            
                        MinutosT = MinutosT - 1
                            
                    elif MinutosT == 0:

                        MinutosT = 59
                            
                        HorasT = HorasT - 1

                        if HorasT == 0:

                            HorasT = 59
                            MinutosT = 59
                            SegundosT = 59
                        
                # Se enviaran los siguientes valores a los IntVar de cada parte del cronometro.
                self.TiempoHoras.set(HorasT)
                self.TiempoMinutos.set(MinutosT)
                self.TiempoSegundos.set(SegundosT)

                # Condicion que determina si se ha pasado del pronostico.
                if HorasT == 0 and MinutosT == 0 and SegundosT == 0:

                    R = 1
                    
                    self.TiempoHoras.set(str(PronosticoH))
                    self.TiempoMinutos.set(str(PronosticoM))
                    self.TiempoSegundos.set(str(PronosticoS))

            # Se ejecutara el metodo .after()
            self.after(930,self.Iniciar)                        

#####################################################################################################################################################################################################################

#Ventana Configurar
        
class Configurar(tkinter.Tk):
    
    def __init__(self):

        # Ventana de configurar con sus respectivas caracteristicas.        
        tkinter.Tk.__init__(self)
        self.title("Configurar")
        self.geometry("845x615")
        self.resizable(width = False, height = False)

        # Esta sera una variable global necesaria porque se utilizara en distintas funciones.
        global ImagenFondo

        # Esta sera la imagen que aparecera en la ventanas.
        ImagenFondo = PhotoImage(file = "710239_geometric-wallpaper-hd - copia.png")
        Fondo = Label(self, image = ImagenFondo)
        Fondo.place(x = 0, y = 0) 

        global guiaN

        guiaN = IntVar()

        # Etiqueta que aparecera en la ventana.
        self.labelNivel = Label(self, text = "¿Cuál dificultad desea jugar?", fg =  "#000000", font = ("Serif", 17))
        self.labelNivel.place(x = 100, y = 50)

        # Botones que apareceran en la ventana.
        self.buttonNivelFacil = Radiobutton(self, text = "Fácil", value = 1, font = ("Serif", 17), variable = guiaN, command = self.DeterminarNivel)
        self.buttonNivelFacil.place(x = 60, y = 100)
        
        self.buttonNivelIntermedio = Radiobutton(self, text = "Intermedio", value = 2, font = ("Serif", 17), variable = guiaN, command = self.DeterminarNivel)
        self.buttonNivelIntermedio.place(x = 170, y = 100)
        
        self.buttonNivelDificil = Radiobutton(self, text = "Difícil", width = 7, value = 3, font = ("Serif", 17), variable = guiaN, command = self.DeterminarNivel)
        self.buttonNivelDificil.place(x = 320, y = 100)

        global guiaR

        guiaR = IntVar()

        # Etiqueta que aparecera en la ventana.
        self.labelReloj = Label(self, text = "¿Necesita reloj?", fg =  "#000000", font = ("Serif", 17))
        self.labelReloj.place(x = 160, y = 200)

        # Botones que apareceran en la ventana.
        self.buttonRelojSi = Radiobutton(self, text = "Sí", value = 1, font = ("Serif", 17), variable = guiaR, command = self.DeterminarReloj)
        self.buttonRelojSi.place(x = 120, y = 250)

        self.buttonRelojNo = Radiobutton(self, text = "No", value = 2, font = ("Serif", 17), variable = guiaR, command = self.DeterminarReloj)
        self.buttonRelojNo.place(x = 205, y = 250)

        self.buttonRelojTimer = Radiobutton(self, text = "Timer", value = 3, font = ("Serif", 17), variable = guiaR, command = self.DeterminarReloj)
        self.buttonRelojTimer.place(x = 300, y = 250)

        global guiaS

        guiaS = IntVar()

        # Etiqueta que aparecera en la ventana.
        self.labelSonido = Label(self, text = "¿Desea un sonido al finalizar con éxito?", fg =  "#000000", font = ("Serif", 17))
        self.labelSonido.place(x = 60, y = 350)

        # Botones que apareceran en la ventana.
        self.buttonSonidoSi = Radiobutton(self, text = "Sí", value = 1, font = ("Serif", 17), variable = guiaS, command = self.DeterminarSonido)
        self.buttonSonidoSi.place(x = 185, y = 400)

        self.buttonSonidoNo = Radiobutton(self, text = "No", value = 2, font = ("Serif", 17), variable = guiaS, command = self.DeterminarSonido)
        self.buttonSonidoNo.place(x = 270, y = 400)

        global guiaT

        guiaT = IntVar()

        # Etiqueta que aparecera en la ventana.
        self.labelSonido = Label(self, text = "¿Cuál tamaño desea jugar?", fg =  "#000000", font = ("Serif", 17))
        self.labelSonido.place(x = 500, y = 50)

        # Botones que apareceran en la ventana.
        self.button3x3 = Radiobutton(self, text = "3x3", value = 1, font = ("Serif", 17), variable = guiaT, command = self.DeterminarTamaño)
        self.button3x3.place(x = 610, y = 100)

        self.button4x4 = Radiobutton(self, text = "4x4", value = 2, font = ("Serif", 17), variable = guiaT, command = self.DeterminarTamaño)
        self.button4x4.place(x = 610, y = 150)

        self.button5x5 = Radiobutton(self, text = "5x5", value = 3, font = ("Serif", 17), variable = guiaT, command = self.DeterminarTamaño)
        self.button5x5.place(x = 610, y = 200)

        self.button6x6 = Radiobutton(self, text = "6x6", value = 4, font = ("Serif", 17), variable = guiaT, command = self.DeterminarTamaño)
        self.button6x6.place(x = 610, y = 250)

        self.button7x7 = Radiobutton(self, text = "7x7", value = 5, font = ("Serif", 17), variable = guiaT, command = self.DeterminarTamaño)
        self.button7x7.place(x = 610, y = 300)

        self.button8x8 = Radiobutton(self, text = "8x8", value = 6, font = ("Serif", 17), variable = guiaT, command = self.DeterminarTamaño)
        self.button8x8.place(x = 610, y = 350)

        self.button9x9 = Radiobutton(self, text = "9x9", value = 7, font = ("Serif", 17), variable = guiaT, command = self.DeterminarTamaño)
        self.button9x9.place(x = 610, y = 400)

        self.buttonMultitamaño = Radiobutton(self, text = "Multitamaño", value = 8, font = ("Serif", 17), variable = guiaT, command = self.DeterminarTamaño)
        self.buttonMultitamaño.place(x = 610, y = 450)

        # Botones que apareceran en la ventana.
        self.buttonJugar = Button(self, text = "Jugar", width = 8, activebackground = "#db4437", command = self.Jugar, fg = "white", bg = "#66CD00", font = ("Serif", 20))
        self.buttonJugar.place(x = 190, y = 500)  

        self.buttonRegresarMenu = Button(self, text = "Regresar al Menú", width = 15, activebackground = "#db4437", command = self.RegresarMenu, fg = "white", bg = "#db4437", font = ("Serif", 20))
        self.buttonRegresarMenu.place(x = 500, y = 500)

    # Funcion del boton asignado.
    def DeterminarNivel(self):

        global N

        N = guiaN.get()

    # Funcion del boton asignado.
    def DeterminarReloj(self):

        global R

        R = guiaR.get()

    # Funcion del boton asignado.
    def DeterminarSonido(self):

        global S

        S = guiaS.get()

    # Funcion del boton asignado.
    def DeterminarTamaño(self):

        global T

        T = guiaT.get()

    # Funcion del boton asignado.
    def Jugar(self):

        # Condicion que determina si se puede abrir la ventana de jugar o no
        try:
            
            if (N == 1 or N == 2 or N == 3) and (S == 1 or S == 2) and (T == 1 or T == 2 or T == 3 or T == 4 or T == 5 or T == 6 or T == 7 or T == 8):

                    if R == 1:
                        # Se cerrara la ventana actual.
                        self.destroy()
                        # Se abrira la nueva ventana solicitada.
                        Jugar().mainloop()

                    elif R == 2:
                        # Se cerrara la ventana actual.
                        self.destroy()
                        # Se abrira la nueva ventana solicitada.
                        Jugar().mainloop()

                    elif R == 3:
                        # Se cerrara la ventana actual.
                        self.destroy()
                        # Se abrira la nueva ventana solicitada.
                        Timer().mainloop()
                        
            else:

                messagebox.showinfo("Aviso", "Debe de configurar el modo de juego que desea.", icon = "warning")

        except NameError:

            messagebox.showinfo("Aviso", "Debe de configurar el modo de juego que desea.", icon = "warning")

    # Funcion del boton asignado.
    def RegresarMenu(self):
        # Se cerrara la ventana actual.
        self.destroy()
        # Se abrira la nueva ventana solicitada.
        menu().mainloop()
        
#####################################################################################################################################################################################################################

# Ventana Timer

class Timer(tkinter.Tk):

    # Estas seran variables globales necesarias porque se utilizaran en las distintas ventanas.
    global cont
    global guia
    global Horas
    global Minutos
    global Segundos
    global PronosticoH
    global PronosticoM
    global PronosticoS

    # Valor que se les asignara a las variables globales.
    cont = 1
    guia = 0
    Horas = 0
    Minutos = 0
    Segundos = 0
    
    def __init__(self):

        # La ventana de Pronosticar Tiempo con sus respectivas caracteristicas.
        tkinter.Tk.__init__(self)
        self.title("Timer")
        self.geometry("750x500")
        self.resizable(width = False, height = False)

        # Esta sera una variable global necesaria porque se utilizara en distintas funciones.
        global ImagenFondo

        # Esta sera la imagen que aparecera en la ventanas.
        ImagenFondo = PhotoImage(file = "710239_geometric-wallpaper-hd - copia - copia.png")
        Fondo = Label(self, image = ImagenFondo)
        Fondo.place(x = 0, y = 0)   

        # Estas seran todas las etiquetas que apareceran en la ventana.
        self.titulo = Label(self, text = "TIMER", fg =  "#4285f4", font = ("Serif", 18))
        self.titulo.place(x = 339, y = 7)

        self.labelPronostico = Label(self, text = "Pronóstico", fg =  "#000000", font = ("Serif", 15))
        self.labelPronostico.place(x = 15, y = 120)

        self.labelHoras = Label(self, text = "Horas", fg =  "#000000", font = ("Serif", 15))
        self.labelHoras.place(x = 173, y = 70)

        self.labelMinutos = Label(self, text = "Minutos", fg =  "#000000", font = ("Serif", 15))
        self.labelMinutos.place(x = 340, y = 70)

        self.labelSegundos = Label(self, text = "Segundos", fg =  "#000000", font = ("Serif", 15))
        self.labelSegundos.place(x = 505, y = 70)

        self.labelCursor = Label(self, text = "Cursor en:", fg =  "#000000", font = ("Serif", 18))
        self.labelCursor.place(x = 115, y = 260)

        # Valor que se le asignara a la siguiente variable y sus respectivas caracteristicas.
        self.Cursor = StringVar()
        self.Cursor.set("Horas")
        self.labelCursorActivo = Label(self, textvariable = self.Cursor, font = ("Serif", 16))
        self.labelCursorActivo.place(x = 115, y = 307)

        # Estos seran todos los cuadros de texto que apareceran en la ventana.
        self.textBoxHoras = Entry(self, width = 7, font = ("times new roman", 35))
        self.textBoxHoras.place(x = 115, y = 105)

        self.textBoxMinutos = Entry(self, width = 7, font = ("times new roman", 35))
        self.textBoxMinutos.place(x = 290, y = 105)

        self.textBoxSegundos = Entry(self, width = 7, font = ("times new roman", 35))
        self.textBoxSegundos.place(x = 465, y = 105)

        # Estos seran todos los botones que apareceran en la ventana.
        self.button1 = Button(self, text = "1", width = 7, activebackground = "#9C661F", command = self.button1, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button1.place(x = 335, y = 195)

        self.button2 = Button(self, text = "2", width = 7, activebackground = "#9C661F", command = self.button2, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button2.place(x = 435, y = 195)

        self.button3 = Button(self, text = "3", width = 7, activebackground = "#9C661F", command = self.button3, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button3.place(x = 535, y = 195)

        self.button4 = Button(self, text = "4", width = 7, activebackground = "#9C661F", command = self.button4, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button4.place(x = 335, y = 240)

        self.button5 = Button(self, text = "5", width = 7, activebackground = "#9C661F", command = self.button5, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button5.place(x = 435, y = 240)

        self.button6 = Button(self, text = "6", width = 7, activebackground = "#9C661F", command = self.button6, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button6.place(x = 535, y = 240)

        self.button7 = Button(self, text = "7", width = 7, activebackground = "#9C661F", command = self.button7, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button7.place(x = 335, y = 285)

        self.button8 = Button(self, text = "8", width = 7, activebackground = "#9C661F", command = self.button8, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button8.place(x = 435, y = 285)

        self.button9 = Button(self, text = "9", width = 7, activebackground = "#9C661F", command = self.button9, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button9.place(x = 535, y = 285)

        self.button0 = Button(self, text = "0", width = 7, activebackground = "#9C661F", command = self.button0, fg = "white", bg = "#7F7F7F", font = ("Serif", 17))
        self.button0.place(x = 435, y = 330)

        self.buttonSiguiente = Button(self, text = "Siguiente", width = 13, activebackground = "#FF6103", command = self.Siguiente, fg = "white", bg = "#FF6103", font = ("Serif", 17))
        self.buttonSiguiente.place(x = 115, y = 195)

        self.buttonRegresarMenu = Button(self, text = "Jugar", width = 15, activebackground = "#db4437", command = self.JugarTimer, fg = "white", bg = "#db4437", font = ("Serif", 20))
        self.buttonRegresarMenu.place(x = 385, y = 409)

        self.buttonGuardar = Button(self, text = "Guardar Pronóstico", width = 15, activebackground = "#66CD00", command = self.Guardar, fg = "white", bg = "#66CD00", font = ("Serif", 20))
        self.buttonGuardar.place(x = 115, y = 409)

    # Funcion del boton asignado.
    def Siguiente(self):

        # Estas seran variables globales necesarias para un buen procesamiento de la funcion.
        global cont
        global guia

        # Valor que se les asignara a las variables globales.
        cont = cont + 1
        guia = 0

        # Estas condiciones altualizaran el varlor de self.Cursor dependiendo de donde se vaya a introducir el texto segun el boton Siguiente.
        if cont > 3:

            cont = 1

        if cont == 1:

            self.Cursor.set("Horas")

        elif cont == 2:

            self.Cursor.set("Minutos")

        elif cont == 3:

            self.Cursor.set("Segundos")

    # Funcion del boton asignado.
    def button1(self):

        # Se definira esta variable como global para un buen procesamiento de la funcion.
        global guia

        # Dependiendo del valor que tenga la variable cont, se colocara el numero del boton en el respectivo cuadro de texto.
        if cont == 1:
            self.textBoxHoras.insert(guia,"1")
            guia = guia + 1
        elif cont == 2:
            self.textBoxMinutos.insert(guia,"1")
            guia = guia + 1
        elif cont == 3:
            self.textBoxSegundos.insert(guia,"1")
            guia = guia + 1

    # Funcion del boton asignado.
    def button2(self):

        # Se definira esta variable como global para un buen procesamiento de la funcion.
        global guia

        # Dependiendo del valor que tenga la variable cont, se colocara el numero del boton en el respectivo cuadro de texto.
        if cont == 1:
            self.textBoxHoras.insert(guia,"2")
            guia = guia + 1
        elif cont == 2:
            self.textBoxMinutos.insert(guia,"2")
            guia = guia + 1
        elif cont == 3:
            self.textBoxSegundos.insert(guia,"2")
            guia = guia + 1

    # Funcion del boton asignado.
    def button3(self):

        # Se definira esta variable como global para un buen procesamiento de la funcion.
        global guia

        # Dependiendo del valor que tenga la variable cont, se colocara el numero del boton en el respectivo cuadro de texto.
        if cont == 1:
            self.textBoxHoras.insert(guia,"3")
            guia = guia + 1
        elif cont == 2:
            self.textBoxMinutos.insert(guia,"3")
            guia = guia + 1
        elif cont == 3:
            self.textBoxSegundos.insert(guia,"3")
            guia = guia + 1

    # Funcion del boton asignado.
    def button4(self):

        # Se definira esta variable como global para un buen procesamiento de la funcion.
        global guia

        # Dependiendo del valor que tenga la variable cont, se colocara el numero del boton en el respectivo cuadro de texto.
        if cont == 1:
            self.textBoxHoras.insert(guia,"4")
            guia = guia + 1
        elif cont == 2:
            self.textBoxMinutos.insert(guia,"4")
            guia = guia + 1
        elif cont == 3:
            self.textBoxSegundos.insert(guia,"4")
            guia = guia + 1

    # Funcion del boton asignado.
    def button5(self):

        # Se definira esta variable como global para un buen procesamiento de la funcion.
        global guia

        # Dependiendo del valor que tenga la variable cont, se colocara el numero del boton en el respectivo cuadro de texto.
        if cont == 1:
            self.textBoxHoras.insert(guia,"5")
            guia = guia + 1
        elif cont == 2:
            self.textBoxMinutos.insert(guia,"5")
            guia = guia + 1
        elif cont == 3:
            self.textBoxSegundos.insert(guia,"5")
            guia = guia + 1

    # Funcion del boton asignado.
    def button6(self):

        # Se definira esta variable como global para un buen procesamiento de la funcion.
        global guia

        # Dependiendo del valor que tenga la variable cont, se colocara el numero del boton en el respectivo cuadro de texto.
        if cont == 1:
            self.textBoxHoras.insert(guia,"6")
            guia = guia + 1
        elif cont == 2:
            self.textBoxMinutos.insert(guia,"6")
            guia = guia + 1
        elif cont == 3:
            self.textBoxSegundos.insert(guia,"6")
            guia = guia + 1

    # Funcion del boton asignado.
    def button7(self):

        # Se definira esta variable como global para un buen procesamiento de la funcion.
        global guia

        # Dependiendo del valor que tenga la variable cont, se colocara el numero del boton en el respectivo cuadro de texto.
        if cont == 1:
            self.textBoxHoras.insert(guia,"7")
            guia = guia + 1
        elif cont == 2:
            self.textBoxMinutos.insert(guia,"7")
            guia = guia + 1
        elif cont == 3:
            self.textBoxSegundos.insert(guia,"7")
            guia = guia + 1

    # Funcion del boton asignado.
    def button8(self):

        # Se definira esta variable como global para un buen procesamiento de la funcion.
        global guia

        # Dependiendo del valor que tenga la variable cont, se colocara el numero del boton en el respectivo cuadro de texto.
        if cont == 1:
            self.textBoxHoras.insert(guia,"8")
            guia = guia + 1
        elif cont == 2:
            self.textBoxMinutos.insert(guia,"8")
            guia = guia + 1
        elif cont == 3:
            self.textBoxSegundos.insert(guia,"8")
            guia = guia + 1

    # Funcion del boton asignado.
    def button9(self):

        # Se definira esta variable como global para un buen procesamiento de la funcion.
        global guia

        # Dependiendo del valor que tenga la variable cont, se colocara el numero del boton en el respectivo cuadro de texto.
        if cont == 1:
            self.textBoxHoras.insert(guia,"9")
            guia = guia + 1
        elif cont == 2:
            self.textBoxMinutos.insert(guia,"9")
            guia = guia + 1
        elif cont == 3:
            self.textBoxSegundos.insert(guia,"9")
            guia = guia + 1

    # Funcion del boton asignado.
    def button0(self):

        # Se definira esta variable como global para un buen procesamiento de la funcion.
        global guia

        # Dependiendo del valor que tenga la variable cont, se colocara el numero del boton en el respectivo cuadro de texto.
        if cont == 1:
            self.textBoxHoras.insert(guia,"0")
            guia = guia + 1
        elif cont == 2:
            self.textBoxMinutos.insert(guia,"0")
            guia = guia + 1
        elif cont == 3:
            self.textBoxSegundos.insert(guia,"0")
            guia = guia + 1

    # Funcion del boton asignado.
    def Guardar(self):

        # Se definiran estas variables como globaesl para un buen procesamiento de la funcion.
        global Horas
        global Minutos
        global Segundos
        global PronosticoH
        global PronosticoM
        global PronosticoS
        global cont

        # Se guardara el valor introducido en las variables respectivas para luego mostrarlas como el pronostico en la ventana del Cronometro.
        
        entryHoras = self.textBoxHoras.get()

        # La siguiente estructutra validara las restricciones necesarias para que el cronometro pueda funcionar correctamente.
        try:
            
            entryHoras = int(entryHoras)
            
            if isinstance(entryHoras,int) == True:

                if entryHoras >= 0 and entryHoras <= 3:

                    Horas = entryHoras
                    PronosticoH = Horas

                else:

                    messagebox.showinfo("Error", "Dato Inválido \nPor favor digite las horas correctas.")
                    self.textBoxHoras.delete(0,END)
                    
            else:

                messagebox.showinfo("Error", "Dato Inválido \nPor favor digite las horas correctas.")
                self.textBoxHoras.delete(0,END)
                    
        except:

            pass

        entryMinutos = self.textBoxMinutos.get()  

        # La siguiente estructutra validara las restricciones necesarias para que el cronometro pueda funcionar correctamente.
        try:
            
            entryMinutos = int(entryMinutos)
            
            if isinstance(entryMinutos,int) == True:

                if entryMinutos >= 0 and entryMinutos <= 59:

                    Minutos = entryMinutos
                    PronosticoM = Minutos

                else:

                    messagebox.showinfo("Error", "Dato Inválido \nPor favor digite los minutos correctos.")
                    self.textBoxMinutos.delete(0,END)
                    
            else:

                messagebox.showinfo("Error", "Dato Inválido \nPor favor digite los minutos correctos.")
                self.textBoxMinutos.delete(0,END)

        except:

            pass

        entrySegundos = self.textBoxSegundos.get()

        # La siguiente estructutra validara las restricciones necesarias para que el cronometro pueda funcionar correctamente.  
        try:
            
            entrySegundos = int(entrySegundos)
            
            if isinstance(entrySegundos,int) == True:

                if entrySegundos >= 0 and entrySegundos <= 59:

                    Segundos = entrySegundos
                    PronosticoS = Segundos

                else:

                    messagebox.showinfo("Error", "Dato Inválido \nPor favor digite los segundos correctos.")
                    self.textBoxSegundos.delete(0,END)
                    
            else:

                messagebox.showinfo("Error", "Dato Inválido \nPor favor digite los segundos correctos.")
                self.textBoxSegundos.delete(0,END)

        except:

            pass
            
    # Funcion del boton asignado.
    def JugarTimer(self):

        # Se definira esta variale como global para un buen procesamiento de la funcion.
        global cont
        # Valor que se le asignara a la variable global.
        cont = 1
        
        # Se cerrara la ventana actual.
        self.destroy()
        # Se abrira la nueva ventana solicitada.
        Jugar().mainloop()

#####################################################################################################################################################################################################################

# Ventana Top 10

class Top(tkinter.Tk):
    
    def __init__(self):

        # Ventana del Top 10 con respectivas caracteristicas.
        tkinter.Tk.__init__(self)
        self.title("TOP 10")
        self.geometry("500x400")

        # Se definiran estas variables como globaesl para un buen procesamiento de la funcion.
        global Jugador
        global listaTop
        global horasjugador
        global minutosjugador
        global segundosjugador

        # Se ordenara la siguiente lista de mayor a menor.
        listaTop.sort(reverse = True)

        # Etiquetas que apareceran en la ventana
        self.labelJugador= Label(self, text = "Jugador", fg =  "#4285f4", font = ("Serif", 16))
        self.labelJugador.place(x = 100, y = 5)

        self.labelNivel= Label(self, text = "Nivel 6x6", fg =  "#4285f4", font = ("Serif", 16))
        self.labelNivel.place(x = 200, y = 5)

        self.labelTiempo= Label(self, text= "Tiempo", fg =  "#4285f4", font = ("Serif", 16))
        self.labelTiempo.place(x = 300, y = 5)

        y = 100

        # Algoritmo que creara las etiquetas de los nombres de los jugadores.
        for s in listaTop:

            Label(self, text = s[3], font = ("Serif", 15)).place(x = 100, y = y)

            y = y + 100

        y = 100

        # Algoritmo que creara las etiquetas del tiempo de los jugadores
        for s in listaTop:

            t = str(s[0]) + ":" + str(s[1]) + ":" + str(s[2])

            Label(self, text = t, font = ("Serif", 15)).place(x = 300, y = y)

            y = y + 100

#Loop de la ventana
menu().mainloop()

from ast import Global
from calendar import c
from cgi import print_form
from codecs import latin_1_decode
from copyreg import pickle
from ctypes.wintypes import HLOCAL
from doctest import FAIL_FAST
from faulthandler import disable
from msilib.schema import ComboBox
from nntplib import NNTP
import selectors 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from turtle import back, left, position
from types import CellType
from webbrowser import BackgroundBrowser
from PIL import ImageTk, Image
from numpy import true_divide
from pip import main
import random

def on_click(Boton,PB_ready,PB_select,ready,Pokemon_name):
    global C_ready
    global S_ready
    global P_ready
    global B_ready
    global Seleccion_Pokemon
    global Nombre_pokemon

    if (Pokemon_name == "Charmander" and not S_ready and not P_ready and not B_ready): 
        if ready:
            Boton['image'] = PB_select
            Boton['bd'] = 1
            C_ready = not ready
            Seleccion_Pokemon = False
            Nombre_pokemon = "null"
        else:
            Boton['image'] = PB_ready
            Boton['bd'] = 20
            C_ready = not ready
            Seleccion_Pokemon = TRUE
            Nombre_pokemon = Pokemon_name


    elif (Pokemon_name == "Squirtle" and not C_ready and not P_ready and not B_ready):
        if ready:
            Boton['image'] = PB_select
            Boton['bd'] = 1
            S_ready = not ready
            Seleccion_Pokemon = False
            Nombre_pokemon = "null"
        else:
            Boton['image'] = PB_ready
            Boton['bd'] = 20
            S_ready = not ready
            Seleccion_Pokemon = TRUE
            Nombre_pokemon = Pokemon_name

    elif (Pokemon_name == "Pikachu" and not C_ready and not S_ready and not B_ready):
        if ready:
            Boton['image'] = PB_select
            Boton['bd'] = 1
            P_ready = not ready
            Seleccion_Pokemon = False
            Nombre_pokemon = "null"
        else:
            Boton['image'] = PB_ready
            Boton['bd'] = 20
            P_ready = not ready
            Seleccion_Pokemon = TRUE
            Nombre_pokemon = Pokemon_name
    
    elif (Pokemon_name == "Bulbasaur" and not C_ready and not P_ready and not S_ready):
        if ready:
            Boton['image'] = PB_select
            Boton['bd'] = 1
            B_ready = not ready
            Seleccion_Pokemon = False
            Nombre_pokemon = "null"
        else:
            Boton['image'] = PB_ready
            Boton['bd'] = 20
            B_ready = not ready
            Seleccion_Pokemon = TRUE
            Nombre_pokemon = Pokemon_name

def on_click_rival(Boton,PB_ready,PB_select,ready,Pokemon_name):
    global C_ready_rival
    global S_ready_rival
    global P_ready_rival
    global B_ready_rival
    global Selecccion_Rival
    global Nombre_rival

    if (Pokemon_name == "Charmander" and not S_ready_rival and not P_ready_rival and not B_ready_rival): 
        if ready:
            Boton['image'] = PB_select
            Boton['bd'] = 1
            C_ready_rival = not ready
            Selecccion_Rival = False
            Nombre_rival = "null"
        else:
            Boton['image'] = PB_ready
            Boton['bd'] = 20
            C_ready_rival = not ready
            Selecccion_Rival = True
            Nombre_rival = Pokemon_name

    elif (Pokemon_name == "Squirtle" and not C_ready_rival and not P_ready_rival and not B_ready_rival):
        if ready:
            Boton['image'] = PB_select
            Boton['bd'] = 1
            S_ready_rival = not ready
            Selecccion_Rival = False
            Nombre_rival = "null"
        else:
            Boton['image'] = PB_ready
            Boton['bd'] = 20
            S_ready_rival = not ready
            Selecccion_Rival = True
            Nombre_rival = Pokemon_name

    elif (Pokemon_name == "Pikachu" and not S_ready_rival and not C_ready_rival and not B_ready_rival):
        if ready:
            Boton['image'] = PB_select
            Boton['bd'] = 1
            P_ready_rival = not ready
            Selecccion_Rival = False
            Nombre_rival = "null"
        else:
            Boton['image'] = PB_ready
            Boton['bd'] = 20
            P_ready_rival = not ready
            Selecccion_Rival = True
            Nombre_rival = Pokemon_name
    
    elif (Pokemon_name == "Bulbasaur" and not S_ready_rival and not P_ready_rival and not C_ready_rival):
        if ready:
            Boton['image'] = PB_select
            Boton['bd'] = 1
            B_ready_rival = not ready
            Selecccion_Rival = False
            Nombre_rival = "null"
        else:
            Boton['image'] = PB_ready
            Boton['bd'] = 20
            B_ready_rival = not ready
            Selecccion_Rival = True
            Nombre_rival = Pokemon_name

def error_seleccion(Pokemon, Rival):

    def terminar():
        root.destroy()

    root=Tk()
    root.title("Error de selccion:")
    root.geometry("480x150")
    root.configure(background='')
    root.resizable(False,False)
    
    #BOTÓN ACEPTAR
    B1=Button(root, text="Aceptar",command=lambda:terminar(),background="white",foreground="black",font=('Times New Roman bold',10),border=2)
    B1.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    #ENTRY 
    if Pokemon and not Rival:
        l1 = Label(root, text = "Por favor elije un rival para comenzar la batalla... ",background="white",foreground="black",font=('Times New Roman bold',12))
        l1.grid(row=0,column=0,padx=5, pady=35)

    elif not Pokemon and not Rival:
        l1 = Label(root, text = "Por favor elije a tu pokemon y a un rival para comenzar la batalla... ",background="white",foreground="black",font=('Times New Roman bold',12))
        l1.grid(row=0,column=0,padx=5, pady=35)
    elif not Pokemon and Rival:
        l1 = Label(root, text = "Por favor elije a tu pokemon para comenzar la batalla... ",background="white",foreground="black",font=('Times New Roman bold',12))
        l1.grid(row=0,column=0,padx=5, pady=35)
    else:
        l1 = Label(root, text = "Tu rival no puede ser el mismo pokemon... escoge un rival diferente ",background="white",foreground="black",font=('Times New Roman bold',12))
        l1.grid(row=0,column=0,padx=5, pady=35)

def Curacion(nombre):
    #global pikachu
    #global charmander
    #global bulbasaur
    #global squirtle

    def terminar():
        Croot.destroy()
        Seleccion(nombre)

    Croot=Tk()
    Croot.title("Modulo de curacion:")
    Croot.geometry("340x400")
    Croot.configure(background='')
    Croot.resizable(False,False)

    pikachu.centro_pokemon()
    charmander.centro_pokemon()
    squirtle.centro_pokemon()
    bulbasaur.centro_pokemon()

    pikachu_rival.centro_pokemon()
    charmander_rival.centro_pokemon()
    squirtle_rival.centro_pokemon()
    bulbasaur_rival.centro_pokemon()

    #Pc = pikachu.stats.copy()
    #pikachu.current_stats =  Pc
    #Cc = charmander.stats.copy()
    #charmander.current_stats = Cc
    #Sc = squirtle.stats.copy()
    #squirtle.current_stats = Sc
    #Bc = bulbasaur.stats.copy()
    #bulbasaur.current_stats = Bc
    

    Enfermera=ImageTk.PhotoImage(Image.open("enfermera.png")) 

    #Mensaje
    l1 = Label(Croot, text = "Tus pokemones han sido curados vuelve pronto",background="white",foreground="black",font=('Times New Roman bold',12))
    l1.grid(row=0,column=0,padx=5, pady=35)

    l2 = Label(Croot,image=Enfermera)
    l2.grid(row=1,column=0,padx=5, pady=35)


    
    #BOTÓN ACEPTAR
    B1=Button(Croot, text="Regresar",command=lambda:terminar(),background="white",foreground="black",font=('Times New Roman bold',10),border=2)
    B1.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

    Croot.mainloop()

def add_attack(NN,Npokemon,selecctor):
    def add_end():
        if selecctor == 1:
            if Npokemon == "Charmander":
                TC1=E1.get()
                TC2=E2.get()
                charmander.add(TC1,TC2)
            elif Npokemon == "Bulbasaur":
                TC1=E1.get()
                TC2=E2.get()
                bulbasaur.add(TC1,TC2)
            elif Npokemon == "Pikachu":
                TC1=E1.get()
                TC2=E2.get()
                pikachu.add(TC1,TC2)
            else:
                TC1=E1.get()
                TC2=E2.get()
                squirtle.add(TC1,TC2)
            adroot.destroy()
            estadisticas_Usuario(NN)
        else:
            if Npokemon == "Charmander":
                TC1=E1.get()
                TC2=E2.get()
                charmander_rival.add(TC1,TC2)
            elif Npokemon == "Bulbasaur":
                TC1=E1.get()
                TC2=E2.get()
                bulbasaur_rival.add(TC1,TC2)
            elif Npokemon == "Pikachu":
                TC1=E1.get()
                TC2=E2.get()
                pikachu_rival.add(TC1,TC2)
            else:
                TC1=E1.get()
                TC2=E2.get()
                squirtle_rival.add(TC1,TC2)
            adroot.destroy()
            estadisticas_rival(NN)

        

    adroot=Tk()
    adroot.title("Nombre del Jugador")
    P = ImageTk.PhotoImage(Image.open("Poke.jpeg"))
    adroot.iconphoto(False,P)
    adroot.geometry("500x300")
    adroot.configure(background='black')
    adroot.resizable(False,False)
    #Vroot.overrideredirect(True)
    

    texto=StringVar()
    #ENTRY 
    l1 = Label(adroot, text = "Nombre del ataque:",background="black",foreground="white",font=('Times New Roman bold',12))
    l1.grid(row=0,column=0,padx=5, pady=35)
    E1=Entry(adroot)
    E1.grid(row=0,column=1,padx=5, pady=35)
    l2 = Label(adroot, text = "Poder del ataque:",background="black",foreground="white",font=('Times New Roman bold',12))
    l2.grid(row=1,column=0,padx=5, pady=35)
    E2=Entry(adroot)
    E2.grid(row=1,column=1,padx=5, pady=35)

    #Open Image
    Pimg = ImageTk.PhotoImage(Image.open("Pokebola.png"))
    #place image in menu
    Label(adroot, image = Pimg,border=0,anchor= N).grid(row = 0, column = 2,columnspan = 2, rowspan = 2, padx = 5, pady = 5)

    #BOTÓN ACEPTAR

    B1=Button(adroot, text="Aceptar",command=lambda:add_end(),background="Black",foreground="white",font=('Times New Roman bold',10),border=2)
    B1.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

    adroot.mainloop()

def estadisticas_Usuario(nombre):
    
    variable = nombre
    def devolverDatos1():
       Eroot.destroy()
       Seleccion(nombre)
    
    def Ataque(NN,pokemon,selecctor):
        Eroot.destroy()
        add_attack(NN,pokemon,selecctor)


    Eroot=Tk()
    Eroot.title("Estadisticas...")
    Eroot.geometry("1600x650")
    Eroot.configure(background='black')
    #Eroot.resizable(False,False)
        
    #Estadisticas Charmander
    if charmander.current_stats['hp']>0:
        EPB1 = ImageTk.PhotoImage(Image.open("Charmander_S.png")) 
    else:
        EPB1 = ImageTk.PhotoImage(Image.open("Charmander_debil.png")) 
    EB1 = Button(Eroot, image= EPB1, anchor=CENTER,)
    EB1.grid(row=2,column=0,padx=35, pady=35)

    EL1 = Label(Eroot, text = "Nombre: " + str(charmander.especie)  ,background="black",foreground="Red",font=('Times New Roman bold',14))
    EL1.grid(row=4,column=0,padx=40, pady=1,sticky="WN")
    EL2 = Label(Eroot, text = "Velocidad: " + str(charmander.current_stats["velocidad"])  ,background="black",foreground="red",font=('Times New Roman bold',14))
    EL2.grid(row=5,column=0,padx=40, pady=1,sticky="WN")
    EL3 = Label(Eroot, text = "HP: " + str(charmander.current_stats["hp"])  ,background="black",foreground="red",font=('Times New Roman bold',14))
    EL3.grid(row=6,column=0,padx=40, pady=1,sticky="WN")
    EL4 = Label(Eroot, text = "Ataque: " + str(charmander.current_stats["ataque"])  ,background="black",foreground="red",font=('Times New Roman bold',14))
    EL4.grid(row=7,column=0,padx=40, pady=1,sticky="WN")
    EL5 = Label(Eroot, text = "Defensa: " + str(charmander.current_stats["defensa"])  ,background="black",foreground="red",font=('Times New Roman bold',14))
    EL5.grid(row=8,column=0,padx=40, pady=1,sticky="WN")
    EL6 = Label(Eroot, text = "Tipo: " + str(charmander.tipo)  ,background="black",foreground="red",font=('Times New Roman bold',14))
    EL6.grid(row=9,column=0,padx=40, pady=1,sticky="WN")
    EL7 = Label(Eroot, text = "Fortaleza: " + str(charmander.fortalezas[0])  ,background="black",foreground="red",font=('Times New Roman bold',14))
    EL7.grid(row=10,column=0,padx=40, pady=1,sticky="WN")
    EL8 = Label(Eroot, text = "Debilidad: " + str(charmander.debilidades[0])  ,background="black",foreground="red",font=('Times New Roman bold',14))
    EL8.grid(row=11,column=0,padx=40, pady=1,sticky="WN")
    y=""
    for x in charmander.ataques:
        y +=  str(x)+" "

    EL9 = Label(Eroot, text = "ataques: " + y,background="black",foreground="red",font=('Times New Roman bold',14))
    EL9.grid(row=12,column=0,padx=40, pady=1,sticky="WN")

    Char_add = Button(Eroot, text="Agregar ataque",command=lambda:Ataque(variable,"Charmander",1),background="Black",foreground="red",font=('Times New Roman bold',10),border=2)
    Char_add.grid(row=13, column=0, sticky="nsew", padx=5, pady=5)

    if bulbasaur.current_stats['hp']>0:
        EPB2 = ImageTk.PhotoImage(Image.open("Bulbasaur_S.png")) 
    else:
        EPB2 = ImageTk.PhotoImage(Image.open("Bulbasaur_debil.png"))
    EB2 = Button(Eroot, image= EPB2, anchor=CENTER)
    EB2.grid(row=2,column=1,padx=35, pady=35)

    EL1 = Label(Eroot, text = "Nombre: " + str(bulbasaur.especie)  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL1.grid(row=4,column=1,padx=40, pady=1,sticky="WN")
    EL2 = Label(Eroot, text = "Velocidad: " + str(bulbasaur.current_stats["velocidad"])  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL2.grid(row=5,column=1,padx=40, pady=1,sticky="WN")
    EL3 = Label(Eroot, text = "HP: " + str(bulbasaur.current_stats["hp"])  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL3.grid(row=6,column=1,padx=40, pady=1,sticky="WN")
    EL4 = Label(Eroot, text = "Ataque: " + str(bulbasaur.current_stats["ataque"])  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL4.grid(row=7,column=1,padx=40, pady=1,sticky="WN")
    EL5 = Label(Eroot, text = "Defensa: " + str(bulbasaur.current_stats["defensa"])  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL5.grid(row=8,column=1,padx=40, pady=1,sticky="WN")
    EL6 = Label(Eroot, text = "Tipo: " + str(bulbasaur.tipo)  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL6.grid(row=9,column=1,padx=40, pady=1,sticky="WN")
    EL7 = Label(Eroot, text = "Fortaleza: " + str(bulbasaur.fortalezas[0])  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL7.grid(row=10,column=1,padx=40, pady=1,sticky="WN")
    EL8 = Label(Eroot, text = "Debilidad: " + str(bulbasaur.debilidades[0])  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL8.grid(row=11,column=1,padx=40, pady=1,sticky="WN")
    y=""
    for x in bulbasaur.ataques:
        y +=  str(x)+" "
    EL9 = Label(Eroot, text = "ataques: " + y,background="black",foreground="green",font=('Times New Roman bold',14))
    EL9.grid(row=12,column=1,padx=40, pady=1,sticky="WN")

    BUl_add = Button(Eroot, text="Agregar ataque",command=lambda:Ataque(variable,"Bulbasaur",1),background="Black",foreground="green",font=('Times New Roman bold',10),border=2)
    BUl_add.grid(row=13, column=1, sticky="nsew", padx=5, pady=5)

   
    if pikachu.current_stats['hp']>0:
        EPB3 = ImageTk.PhotoImage(Image.open("Pikachu_S.png")) 
    else:
        EPB3 = ImageTk.PhotoImage(Image.open("Pikachu_debil.png"))

    EB3 = Button(Eroot, image= EPB3, anchor=CENTER)
    EB3.grid(row=2,column=2,padx=35, pady=35)

    EL1 = Label(Eroot, text = "Nombre: " + str(pikachu.especie)  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL1.grid(row=4,column=2,padx=40, pady=1,sticky="WN")
    EL2 = Label(Eroot, text = "Velocidad: " + str(pikachu.current_stats["velocidad"])  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL2.grid(row=5,column=2,padx=40, pady=1,sticky="WN")
    EL3 = Label(Eroot, text = "HP: " + str(pikachu.current_stats["hp"])  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL3.grid(row=6,column=2,padx=40, pady=1,sticky="WN")
    EL4 = Label(Eroot, text = "Ataque: " + str(pikachu.current_stats["ataque"])  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL4.grid(row=7,column=2,padx=40, pady=1,sticky="WN")
    EL5 = Label(Eroot, text = "Defensa: " + str(pikachu.current_stats["defensa"])  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL5.grid(row=8,column=2,padx=40, pady=1,sticky="WN")
    EL6 = Label(Eroot, text = "Tipo: " + str(pikachu.tipo)  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL6.grid(row=9,column=2,padx=40, pady=1,sticky="WN")
    EL7 = Label(Eroot, text = "Fortaleza: " + str(pikachu.fortalezas[0])  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL7.grid(row=10,column=2,padx=40, pady=1,sticky="WN")
    EL8 = Label(Eroot, text = "Debilidad: " + str(pikachu.debilidades[0])  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL8.grid(row=11,column=2,padx=40, pady=1,sticky="WN")
    y=""
    for x in pikachu.ataques:
        y +=  str(x)+" "
    EL9 = Label(Eroot, text = "ataques: " + y ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL9.grid(row=12,column=2,padx=40, pady=1,sticky="WN")

    Pik_add = Button(Eroot, text="Agregar ataque",command=lambda:Ataque(variable,"Pikachu",1),background="Black",foreground="yellow",font=('Times New Roman bold',10),border=2)
    Pik_add.grid(row=13, column=2, sticky="nsew", padx=5, pady=5)

    if squirtle.current_stats['hp']>0:
        EPB4 = ImageTk.PhotoImage(Image.open("Squirtle_S.png")) 
    else:
        EPB4 = ImageTk.PhotoImage(Image.open("Squirtle_debil.png")) 
    EB4 = Button(Eroot, image= EPB4, anchor=CENTER)
    EB4.grid(row=2,column=3,padx=35, pady=35)

    EL1 = Label(Eroot, text = "Nombre: " + str(squirtle.especie)  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL1.grid(row=4,column=3,padx=40, pady=1,sticky="WN")
    EL2 = Label(Eroot, text = "Velocidad: " + str(squirtle.current_stats["velocidad"])  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL2.grid(row=5,column=3,padx=40, pady=1,sticky="WN")
    EL3 = Label(Eroot, text = "HP: " + str(squirtle.current_stats["hp"])  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL3.grid(row=6,column=3,padx=40, pady=1,sticky="WN")
    EL4 = Label(Eroot, text = "Ataque: " + str(squirtle.current_stats["ataque"])  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL4.grid(row=7,column=3,padx=40, pady=1,sticky="WN")
    EL5 = Label(Eroot, text = "Defensa: " + str(squirtle.current_stats["defensa"])  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL5.grid(row=8,column=3,padx=40, pady=1,sticky="WN")
    EL6 = Label(Eroot, text = "Tipo: " + str(squirtle.tipo)  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL6.grid(row=9,column=3,padx=40, pady=1,sticky="WN")
    EL7 = Label(Eroot, text = "Fortaleza: " + str(squirtle.fortalezas[0])  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL7.grid(row=10,column=3,padx=40, pady=1,sticky="WN")
    EL8 = Label(Eroot, text = "Debilidad: " + str(squirtle.debilidades[0])  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL8.grid(row=11,column=3,padx=40, pady=1,sticky="WN")
    y=""
    for x in squirtle.ataques:
        y +=  str(x)+" "
    EL9 = Label(Eroot, text = "ataques: " + y ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL9.grid(row=12,column=3,padx=40, pady=1,sticky="WN")

    Squ_add = Button(Eroot, text="Agregar ataque",command=lambda:Ataque(variable,"Squirtle",1),background="Black",foreground="blue",font=('Times New Roman bold',10),border=2)
    Squ_add.grid(row=13, column=3, sticky="nsew", padx=5, pady=5)

    #-----------------------------------------------------------------------------------------
    #BOTÓN ACEPTAR
    EB10=Button(Eroot, text="Regresar",command=lambda:devolverDatos1(),background="Black",foreground="white",font=('Times New Roman bold',10),border=2)
    EB10.grid(row=14, column=0,columnspan = 4, sticky="nsew", padx=5, pady=5)

    Eroot.mainloop()

def estadisticas_rival(nombre):
    
    variable = nombre
    def devolverDatos1():
       Eroot.destroy()
       Seleccion(nombre)
    
    def Ataque(NN,pokemon,Selecctor):
        Eroot.destroy()
        add_attack(NN,pokemon,Selecctor)


    Eroot=Tk()
    Eroot.title("Estadisticas de los rivales...")
    Eroot.geometry("1600x650")
    Eroot.configure(background='black')
    #Eroot.resizable(False,False)
        
    #Estadisticas Charmander
    if charmander_rival.current_stats['hp']>0:
        EPB1 = ImageTk.PhotoImage(Image.open("Charmander_S.png")) 
    else:
        EPB1 = ImageTk.PhotoImage(Image.open("Charmander_debil.png")) 
    EB1 = Button(Eroot, image= EPB1, anchor=CENTER,)
    EB1.grid(row=2,column=0,padx=35, pady=35)

    EL1 = Label(Eroot, text = "Nombre: " + str(charmander_rival.especie)  ,background="black",foreground="Red",font=('Times New Roman bold',14))
    EL1.grid(row=4,column=0,padx=40, pady=1,sticky="WN")
    EL2 = Label(Eroot, text = "Velocidad: " + str(charmander_rival.current_stats["velocidad"])  ,background="black",foreground="red",font=('Times New Roman bold',14))
    EL2.grid(row=5,column=0,padx=40, pady=1,sticky="WN")
    EL3 = Label(Eroot, text = "HP: " + str(charmander_rival.current_stats["hp"])  ,background="black",foreground="red",font=('Times New Roman bold',14))
    EL3.grid(row=6,column=0,padx=40, pady=1,sticky="WN")
    EL4 = Label(Eroot, text = "Ataque: " + str(charmander_rival.current_stats["ataque"])  ,background="black",foreground="red",font=('Times New Roman bold',14))
    EL4.grid(row=7,column=0,padx=40, pady=1,sticky="WN")
    EL5 = Label(Eroot, text = "Defensa: " + str(charmander_rival.current_stats["defensa"])  ,background="black",foreground="red",font=('Times New Roman bold',14))
    EL5.grid(row=8,column=0,padx=40, pady=1,sticky="WN")
    EL6 = Label(Eroot, text = "Tipo: " + str(charmander_rival.tipo)  ,background="black",foreground="red",font=('Times New Roman bold',14))
    EL6.grid(row=9,column=0,padx=40, pady=1,sticky="WN")
    EL7 = Label(Eroot, text = "Fortaleza: " + str(charmander_rival.fortalezas[0])  ,background="black",foreground="red",font=('Times New Roman bold',14))
    EL7.grid(row=10,column=0,padx=40, pady=1,sticky="WN")
    EL8 = Label(Eroot, text = "Debilidad: " + str(charmander_rival.debilidades[0])  ,background="black",foreground="red",font=('Times New Roman bold',14))
    EL8.grid(row=11,column=0,padx=40, pady=1,sticky="WN")
    y=""
    for x in charmander_rival.ataques:
        y +=  str(x)+" "

    EL9 = Label(Eroot, text = "ataques: " + y,background="black",foreground="red",font=('Times New Roman bold',14))
    EL9.grid(row=12,column=0,padx=40, pady=1,sticky="WN")

    Char_add = Button(Eroot, text="Agregar ataque",command=lambda:Ataque(variable,"Charmander",2),background="Black",foreground="red",font=('Times New Roman bold',10),border=2)
    Char_add.grid(row=13, column=0, sticky="nsew", padx=5, pady=5)

    if bulbasaur_rival.current_stats['hp']>0:
        EPB2 = ImageTk.PhotoImage(Image.open("Bulbasaur_S.png")) 
    else:
        EPB2 = ImageTk.PhotoImage(Image.open("Bulbasaur_debil.png"))
    EB2 = Button(Eroot, image= EPB2, anchor=CENTER)
    EB2.grid(row=2,column=1,padx=35, pady=35)

    EL1 = Label(Eroot, text = "Nombre: " + str(bulbasaur_rival.especie)  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL1.grid(row=4,column=1,padx=40, pady=1,sticky="WN")
    EL2 = Label(Eroot, text = "Velocidad: " + str(bulbasaur_rival.current_stats["velocidad"])  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL2.grid(row=5,column=1,padx=40, pady=1,sticky="WN")
    EL3 = Label(Eroot, text = "HP: " + str(bulbasaur_rival.current_stats["hp"])  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL3.grid(row=6,column=1,padx=40, pady=1,sticky="WN")
    EL4 = Label(Eroot, text = "Ataque: " + str(bulbasaur_rival.current_stats["ataque"])  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL4.grid(row=7,column=1,padx=40, pady=1,sticky="WN")
    EL5 = Label(Eroot, text = "Defensa: " + str(bulbasaur_rival.current_stats["defensa"])  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL5.grid(row=8,column=1,padx=40, pady=1,sticky="WN")
    EL6 = Label(Eroot, text = "Tipo: " + str(bulbasaur_rival.tipo)  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL6.grid(row=9,column=1,padx=40, pady=1,sticky="WN")
    EL7 = Label(Eroot, text = "Fortaleza: " + str(bulbasaur_rival.fortalezas[0])  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL7.grid(row=10,column=1,padx=40, pady=1,sticky="WN")
    EL8 = Label(Eroot, text = "Debilidad: " + str(bulbasaur_rival.debilidades[0])  ,background="black",foreground="green",font=('Times New Roman bold',14))
    EL8.grid(row=11,column=1,padx=40, pady=1,sticky="WN")
    y=""
    for x in bulbasaur_rival.ataques:
        y +=  str(x)+" "
    EL9 = Label(Eroot, text = "ataques: " + y,background="black",foreground="green",font=('Times New Roman bold',14))
    EL9.grid(row=12,column=1,padx=40, pady=1,sticky="WN")

    BUl_add = Button(Eroot, text="Agregar ataque",command=lambda:Ataque(variable,"Bulbasaur",2),background="Black",foreground="green",font=('Times New Roman bold',10),border=2)
    BUl_add.grid(row=13, column=1, sticky="nsew", padx=5, pady=5)

   
    if pikachu_rival.current_stats['hp']>0:
        EPB3 = ImageTk.PhotoImage(Image.open("Pikachu_S.png")) 
    else:
        EPB3 = ImageTk.PhotoImage(Image.open("Pikachu_debil.png"))

    EB3 = Button(Eroot, image= EPB3, anchor=CENTER)
    EB3.grid(row=2,column=2,padx=35, pady=35)

    EL1 = Label(Eroot, text = "Nombre: " + str(pikachu_rival.especie)  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL1.grid(row=4,column=2,padx=40, pady=1,sticky="WN")
    EL2 = Label(Eroot, text = "Velocidad: " + str(pikachu_rival.current_stats["velocidad"])  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL2.grid(row=5,column=2,padx=40, pady=1,sticky="WN")
    EL3 = Label(Eroot, text = "HP: " + str(pikachu_rival.current_stats["hp"])  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL3.grid(row=6,column=2,padx=40, pady=1,sticky="WN")
    EL4 = Label(Eroot, text = "Ataque: " + str(pikachu_rival.current_stats["ataque"])  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL4.grid(row=7,column=2,padx=40, pady=1,sticky="WN")
    EL5 = Label(Eroot, text = "Defensa: " + str(pikachu_rival.current_stats["defensa"])  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL5.grid(row=8,column=2,padx=40, pady=1,sticky="WN")
    EL6 = Label(Eroot, text = "Tipo: " + str(pikachu_rival.tipo)  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL6.grid(row=9,column=2,padx=40, pady=1,sticky="WN")
    EL7 = Label(Eroot, text = "Fortaleza: " + str(pikachu_rival.fortalezas[0])  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL7.grid(row=10,column=2,padx=40, pady=1,sticky="WN")
    EL8 = Label(Eroot, text = "Debilidad: " + str(pikachu_rival.debilidades[0])  ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL8.grid(row=11,column=2,padx=40, pady=1,sticky="WN")
    y=""
    for x in pikachu_rival.ataques:
        y +=  str(x)+" "
    EL9 = Label(Eroot, text = "ataques: " + y ,background="black",foreground="yellow",font=('Times New Roman bold',14))
    EL9.grid(row=12,column=2,padx=40, pady=1,sticky="WN")

    Pik_add = Button(Eroot, text="Agregar ataque",command=lambda:Ataque(variable,"Pikachu",2),background="Black",foreground="yellow",font=('Times New Roman bold',10),border=2)
    Pik_add.grid(row=13, column=2, sticky="nsew", padx=5, pady=5)

    if squirtle_rival.current_stats['hp']>0:
        EPB4 = ImageTk.PhotoImage(Image.open("Squirtle_S.png")) 
    else:
        EPB4 = ImageTk.PhotoImage(Image.open("Squirtle_debil.png")) 
    EB4 = Button(Eroot, image= EPB4, anchor=CENTER)
    EB4.grid(row=2,column=3,padx=35, pady=35)

    EL1 = Label(Eroot, text = "Nombre: " + str(squirtle_rival.especie)  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL1.grid(row=4,column=3,padx=40, pady=1,sticky="WN")
    EL2 = Label(Eroot, text = "Velocidad: " + str(squirtle_rival.current_stats["velocidad"])  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL2.grid(row=5,column=3,padx=40, pady=1,sticky="WN")
    EL3 = Label(Eroot, text = "HP: " + str(squirtle_rival.current_stats["hp"])  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL3.grid(row=6,column=3,padx=40, pady=1,sticky="WN")
    EL4 = Label(Eroot, text = "Ataque: " + str(squirtle_rival.current_stats["ataque"])  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL4.grid(row=7,column=3,padx=40, pady=1,sticky="WN")
    EL5 = Label(Eroot, text = "Defensa: " + str(squirtle_rival.current_stats["defensa"])  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL5.grid(row=8,column=3,padx=40, pady=1,sticky="WN")
    EL6 = Label(Eroot, text = "Tipo: " + str(squirtle_rival.tipo)  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL6.grid(row=9,column=3,padx=40, pady=1,sticky="WN")
    EL7 = Label(Eroot, text = "Fortaleza: " + str(squirtle_rival.fortalezas[0])  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL7.grid(row=10,column=3,padx=40, pady=1,sticky="WN")
    EL8 = Label(Eroot, text = "Debilidad: " + str(squirtle_rival.debilidades[0])  ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL8.grid(row=11,column=3,padx=40, pady=1,sticky="WN")
    y=""
    for x in squirtle_rival.ataques:
        y +=  str(x)+" "
    EL9 = Label(Eroot, text = "ataques: " + y ,background="black",foreground="blue",font=('Times New Roman bold',14))
    EL9.grid(row=12,column=3,padx=40, pady=1,sticky="WN")

    Squ_add = Button(Eroot, text="Agregar ataque",command=lambda:Ataque(variable,"Squirtle",2),background="Black",foreground="blue",font=('Times New Roman bold',10),border=2)
    Squ_add.grid(row=13, column=3, sticky="nsew", padx=5, pady=5)

    #-----------------------------------------------------------------------------------------
    #BOTÓN ACEPTAR
    EB10=Button(Eroot, text="Regresar",command=lambda:devolverDatos1(),background="Black",foreground="white",font=('Times New Roman bold',10),border=2)
    EB10.grid(row=14, column=0,columnspan = 4, sticky="nsew", padx=5, pady=5)

    Eroot.mainloop()

def Pelea(nombre,n_pokemon,n_rival):

    def terminar():
        global Selecccion_Rival
        global Seleccion_Pokemon
        global P_ready
        global S_ready
        global C_ready
        global B_ready
        global P_ready_rival
        global S_ready_rival
        global C_ready_rival
        global B_ready_rival
        Proot.destroy()
        P_ready = False
        S_ready = False
        C_ready = False
        B_ready = False
        C_ready_rival = False
        S_ready_rival = False
        P_ready_rival = False
        B_ready_rival = False
        Seleccion_Pokemon = False
        Selecccion_Rival = False
        Seleccion(nombre)

    Proot=Tk()
    Proot.title("Arena de pelea:")
    Proot.geometry("1200x700")
    Proot.configure(background='white')
    #Proot.resizable(False,False)

    #Configuracion Peleas
    if ((n_pokemon=="Charmander") and (n_rival =="Bulbasaur")):
        Pelea=ImageTk.PhotoImage(Image.open("BVSC.png")) 
        PMensaje = charmander.pelea(bulbasaur_rival)
    elif ((n_pokemon=="Charmander") and (n_rival =="Pikachu")):
        print("entro")
        Pelea=ImageTk.PhotoImage(Image.open("PVSC.png"))
        PMensaje = charmander.pelea(pikachu_rival)
    elif ((n_pokemon=="Charmander") and (n_rival =="Squirtle")):
        Pelea=ImageTk.PhotoImage(Image.open("SVSC.png"))
        PMensaje = charmander.pelea(squirtle_rival)
    elif ((n_pokemon=="Charmander") and (n_rival =="Charmander")):
        Pelea=ImageTk.PhotoImage(Image.open("CVSC.png"))
        PMensaje = charmander.pelea(charmander_rival)
        #------------------------------------------------------------
    elif ((n_pokemon=="Pikachu") and (n_rival =="Bulbasaur")):
        Pelea=ImageTk.PhotoImage(Image.open("PVSB.png"))
        PMensaje = pikachu.pelea(bulbasaur_rival)
    elif ((n_pokemon=="Pikachu") and (n_rival =="Squirtle")):
        Pelea=ImageTk.PhotoImage(Image.open("PVSS.png"))
        PMensaje = pikachu.pelea(squirtle_rival)
    elif ((n_pokemon=="Pikachu") and (n_rival =="Charmander")):
        Pelea=ImageTk.PhotoImage(Image.open("PVSC.png"))
        PMensaje = pikachu.pelea(charmander_rival)
    elif ((n_pokemon=="Pikachu") and (n_rival =="Pikachu")):
        Pelea=ImageTk.PhotoImage(Image.open("PVSP.png"))
        PMensaje = pikachu.pelea(pikachu_rival)
        #------------------------------------------------------------
    elif ((n_pokemon=="Bulbasaur") and (n_rival =="Squirtle")):
        Pelea=ImageTk.PhotoImage(Image.open("SVSB.png"))
        PMensaje = bulbasaur.pelea(squirtle_rival)
    elif ((n_pokemon=="Bulbasaur") and (n_rival =="Bulbasaur")):
        Pelea=ImageTk.PhotoImage(Image.open("BVSB.png"))
        PMensaje = bulbasaur.pelea(bulbasaur_rival)
    elif ((n_pokemon=="Bulbasaur") and (n_rival =="Pikachu")):
        Pelea=ImageTk.PhotoImage(Image.open("PVSB.png"))
        PMensaje = bulbasaur.pelea(pikachu_rival)
    elif ((n_pokemon=="Bulbasaur") and (n_rival =="Charmander")):
        Pelea=ImageTk.PhotoImage(Image.open("PVSC.png"))
        PMensaje = bulbasaur.pelea(charmander_rival)
    #------------------------------------------------------------
    elif ((n_pokemon=="Squirtle") and (n_rival =="Charmander")):
        Pelea=ImageTk.PhotoImage(Image.open("SVSC.png"))
        PMensaje = squirtle.pelea(charmander_rival)
    elif ((n_pokemon=="Squirtle") and (n_rival =="Pikachu")):
        Pelea=ImageTk.PhotoImage(Image.open("PVSS.png"))
        PMensaje = squirtle.pelea(pikachu_rival)
    elif ((n_pokemon=="Squirtle") and (n_rival =="Bulbasaur")):
        Pelea=ImageTk.PhotoImage(Image.open("SVSB.png"))
        PMensaje = squirtle.pelea(bulbasaur_rival)
    else:
        Pelea=ImageTk.PhotoImage(Image.open("SVSS.png"))
        PMensaje = squirtle.pelea(squirtle_rival)

    #Mensaje
    l1 = Label(Proot, text = "la pelea pokemon a comenzado",background="white",foreground="black",font=('Times New Roman bold',12))
    l1.grid(row=0,column=0,padx=5, pady=35)

    l2 = Label(Proot,image=Pelea)
    l2.grid(row=1,column=0,padx=5, pady=35)

    l3 = Label(Proot, text = PMensaje,background="white",foreground="black",font=('Times New Roman bold',8))
    l3.grid(row=1,column=3,padx=5, pady=35)
    
    #BOTÓN regresar
    B1=Button(Proot, text="Regresar",command=lambda:terminar(),background="white",foreground="black",font=('Times New Roman bold',10),border=2)
    B1.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

    Proot.mainloop()

def Seleccion(nombre):

    def devolverDatos1():

        print(Selecccion_Rival)
        print(Seleccion_Pokemon)
        if (Seleccion_Pokemon == True and Selecccion_Rival == True) and (Nombre_pokemon != Nombre_rival) :
            root.destroy()
            Pelea(nombre,Nombre_pokemon,Nombre_rival)
        else:
          error_seleccion(Seleccion_Pokemon,Selecccion_Rival)

    def Stats():
        root.destroy()
        estadisticas_Usuario(nombre)
    
    def Stats_rival():
        root.destroy()
        estadisticas_rival(nombre)

    def Curar():
        root.destroy()
        Curacion(nombre)
    
    def salir():
        root.destroy()
       

    root=Tk()
    root.title("Hola " +str(nombre))
    P = ImageTk.PhotoImage(Image.open("Poke.jpeg"))
    root.iconphoto(False,P)
    root.geometry("1250x900")
    root.configure(background='black')
    root.resizable(False,False)
    
    #Texto de bienvenida
    L1 = Label(root, text = "Hola " + str(nombre) + " estas a punto de comenzar una emocionante aventura" ,background="black",foreground="white",font=('Times New Roman bold',14))
    L1.grid(row=0,column=0,padx=1,columnspan = 3, pady=1,sticky="WN")
    L1 = Label(root, text = "Por favor elige tu Pokemon..." ,background="black",foreground="white",font=('Times New Roman bold',14))
    L1.grid(row=1,column=0,padx=1, pady=1,sticky="WN")
    
    #Pokemones a elegir por el entrenador
    if charmander.current_stats["hp"]>0:
        PB1 = ImageTk.PhotoImage(Image.open("Charmander.png"))
        B1 = Button(root, image= PB1, anchor=CENTER,activebackground="pink",state=NORMAL) 
    else:
        PB1 = ImageTk.PhotoImage(Image.open("Charmander_debil.png")) 
        B1 = Button(root, image= PB1, anchor=CENTER,activebackground="pink",state=DISABLED)

    PB11 = ImageTk.PhotoImage(Image.open("Charmander_ready.png")) 

    B1.grid(row=2,column=0,padx=35, pady=35)
    B1['command'] = lambda arg=B1:on_click(arg,PB11,PB1,C_ready,"Charmander")

    if bulbasaur.current_stats["hp"]>0:
        PB2 = ImageTk.PhotoImage(Image.open("Bulbasaur.png")) 
        B2 = Button(root, image= PB2, anchor=CENTER,state=NORMAL)
    else:
        PB2 = ImageTk.PhotoImage(Image.open("Bulbasaur_debil.png")) 
        B2 = Button(root, image= PB2, anchor=CENTER,state=DISABLED)

    PB12 = ImageTk.PhotoImage(Image.open("Bulbasaur_ready.png")) 
    
    B2.grid(row=2,column=1,padx=35, pady=35)
    B2['command'] = lambda arg=B2:on_click(arg,PB12,PB2,B_ready,"Bulbasaur")

    if pikachu.current_stats["hp"]>0:
        PB3 = ImageTk.PhotoImage(Image.open("Pikachu.png")) 
        B3 = Button(root, image= PB3, anchor=CENTER,state=NORMAL)
    else:
        PB3 = ImageTk.PhotoImage(Image.open("Pikachu_debil.png")) 
        B3 = Button(root, image= PB3, anchor=CENTER,state=DISABLED)

    PB13 = ImageTk.PhotoImage(Image.open("Pikachu_ready.png")) 
    
    B3.grid(row=2,column=2,padx=35, pady=35)
    B3['command'] = lambda arg=B3:on_click(arg,PB13,PB3,P_ready,"Pikachu")

    if squirtle.current_stats["hp"]>0:
        PB4 = ImageTk.PhotoImage(Image.open("Squirtle.png")) 
        B4 = Button(root, image= PB4, anchor=CENTER,state=NORMAL)
    else:
        PB4 = ImageTk.PhotoImage(Image.open("Squirtle_debil.png")) 
        B4 = Button(root, image= PB4, anchor=CENTER,state=DISABLED)

    PB14 = ImageTk.PhotoImage(Image.open("Squirtle_ready.png")) 
    
    B4.grid(row=2,column=3,padx=35, pady=35)
    B4['command'] = lambda arg=B4:on_click(arg,PB14,PB4,S_ready,"Squirtle")

    #-----------------------------------------------------------------------------------------

    #Texto seleccion de rival
    L2 = Label(root, text = "Elige a tu rival..." ,background="black",foreground="white",font=('Times New Roman bold',14))
    L2.grid(row=3,column=0,padx=1,columnspan = 3, pady=1,sticky="WN")

    #Pokemones a elegir por el entrenador para pelear y entrenar a su pokemon
    if charmander_rival.current_stats["hp"]>0:
        PB6 = ImageTk.PhotoImage(Image.open("Charmander.png"))
        B6 = Button(root, image= PB6, anchor=CENTER,state=NORMAL) 
    else:
        PB6 = ImageTk.PhotoImage(Image.open("Charmander_debil.png")) 
        B6 = Button(root, image= PB6, anchor=CENTER,state=DISABLED)
    
    PB16 = ImageTk.PhotoImage(Image.open("Charmander_ready.png")) 
    B6.grid(row=4,column=3,padx=35, pady=35)
    B6['command'] = lambda arg=B6:on_click_rival(arg,PB16,PB6,C_ready_rival,"Charmander")

    if bulbasaur_rival.current_stats["hp"]>0:
        PB7 = ImageTk.PhotoImage(Image.open("Bulbasaur.png"))
        B7 = Button(root, image= PB7, anchor=CENTER,state=NORMAL) 
    else:
        PB7 = ImageTk.PhotoImage(Image.open("Bulbasaur_debil.png")) 
        B7= Button(root, image= PB7, anchor=CENTER,state=DISABLED)
    PB17 = ImageTk.PhotoImage(Image.open("Bulbasaur_ready.png")) 
    B7.grid(row=4,column=2,padx=35, pady=35)
    B7['command'] = lambda arg=B7:on_click_rival(arg,PB17,PB7,B_ready_rival,"Bulbasaur")

    if pikachu_rival.current_stats["hp"]>0:
        PB8 = ImageTk.PhotoImage(Image.open("Pikachu.png"))
        B8 = Button(root, image= PB8, anchor=CENTER,state=NORMAL) 
    else:
        PB7 = ImageTk.PhotoImage(Image.open("Pikachu_debil.png")) 
        B7= Button(root, image= PB8, anchor=CENTER,state=DISABLED)

    PB18 = ImageTk.PhotoImage(Image.open("Pikachu_ready.png")) 
    B8.grid(row=4,column=1,padx=35, pady=35)
    B8['command'] = lambda arg=B8:on_click_rival(arg,PB18,PB8,P_ready_rival,"Pikachu")

    if squirtle_rival.current_stats["hp"]>0:
        PB9 = ImageTk.PhotoImage(Image.open("Squirtle.png"))
        B9 = Button(root, image= PB9, anchor=CENTER,state=NORMAL) 
    else:
        PB9 = ImageTk.PhotoImage(Image.open("Squirtle_debil.png")) 
        B9= Button(root, image= PB9, anchor=CENTER,state=DISABLED)
   
    PB19 = ImageTk.PhotoImage(Image.open("Squirtle_ready.png")) 
    B9.grid(row=4,column=0,padx=35, pady=35)
    B9['command'] = lambda arg=B9:on_click_rival(arg,PB19,PB9,S_ready_rival,"Squirtle")
    #----------------------------------------------------------------------------------------------------------

    #BOTÓN ACEPTAR
    B10=Button(root, text="A pelear!!!!!",command=lambda:devolverDatos1(),background="Black",foreground="white",font=('Times New Roman bold',10),border=2)
    B10.grid(row=5, column=0,columnspan = 4, sticky="nsew", padx=5, pady=5)

    #Boton stats
    B11=Button(root, text=" Stats Usuario ",command=lambda:Stats(),background="Black",foreground="white",font=('Times New Roman bold',10),border=2)
    B11.grid(row=6, column=1, sticky="nsew", padx=5, pady=5)

    #Boton stats
    B15=Button(root, text=" Stats Rival ",command=lambda:Stats_rival(),background="Black",foreground="white",font=('Times New Roman bold',10),border=2)
    B15.grid(row=6, column=0, sticky="nsew", padx=5, pady=5)
    #Boton curar
    if ((pikachu.current_stats["hp"]>0) and (charmander.current_stats["hp"]>0) and (squirtle.current_stats["hp"]>0) and (bulbasaur.current_stats["hp"]>0)):
        B12=Button(root, text=" Curar ",command=lambda:Curar(),background="Black",foreground="white",font=('Times New Roman bold',10),border=2,state=DISABLED)
    else:
        B12=Button(root, text=" Curar ",command=lambda:Curar(),background="Black",foreground="white",font=('Times New Roman bold',10),border=2,state=NORMAL)
    B12.grid(row=6, column=2, sticky="nsew", padx=5, pady=5)

    B13=Button(root, text=" Salir ",command=lambda:salir(),background="Black",foreground="white",font=('Times New Roman bold',10),border=2)
    B13.grid(row=6, column=3, sticky="nsew", padx=5, pady=5)

    root.mainloop()

def ventanaCapturaDatos():

    def devolverDatos():
        textoCaja=E1.get()
        texto.set(textoCaja)
        Vroot.destroy()
        texto2=Seleccion(textoCaja)

    Vroot=Tk()
    Vroot.title("Nombre del Jugador")
    P = ImageTk.PhotoImage(Image.open("Poke.jpeg"))
    Vroot.iconphoto(False,P)
    Vroot.geometry("300x150")
    Vroot.configure(background='black')
    Vroot.resizable(False,False)
    #Vroot.overrideredirect(True)
    

    texto=StringVar()
    #ENTRY 
    l1 = Label(Vroot, text = "Nombre:",background="black",foreground="white",font=('Times New Roman bold',12))
    l1.grid(row=0,column=0,padx=5, pady=35)
    E1=Entry(Vroot)
    E1.grid(row=0,column=1,padx=5, pady=35)

    #Open Image
    Pimg = ImageTk.PhotoImage(Image.open("Pokebola.png"))
    #place image in menu
    Label(Vroot, image = Pimg,border=0,anchor= N).grid(row = 0, column = 2,columnspan = 2, rowspan = 2, padx = 5, pady = 5)

    #BOTÓN ACEPTAR

    B1=Button(Vroot, text="Aceptar",command=lambda:devolverDatos(),background="Black",foreground="white",font=('Times New Roman bold',10),border=2)
    B1.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

    Vroot.mainloop()


    def devolverDatos():
        Aroot.destroy()
        

    Aroot=Tk()
    Aroot.title("Ataque")
    P = ImageTk.PhotoImage(Image.open("Poke.jpeg"))
    Aroot.iconphoto(False,P)
    Aroot.geometry("300x150")
    Aroot.configure(background='black')
    Aroot.resizable(False,False)
    #Vroot.overrideredirect(True)
    
    #ENTRY 
    l1 = Label(Aroot, text = "Escoge tu ataque:",background="black",foreground="white",font=('Times New Roman bold',12))
    l1.grid(row=0,column=0,padx=5, pady=35)
    E1=Entry(Aroot)
    E1.grid(row=0,column=1,padx=5, pady=35)

    #Open Image
    Pimg = ImageTk.PhotoImage(Image.open("Pokebola.png"))
    #place image in menu
    Label(Aroot, image = Pimg,border=0,anchor= N).grid(row = 0, column = 2,columnspan = 2, rowspan = 2, padx = 5, pady = 5)

    #BOTÓN ACEPTAR
    B1=Button(Aroot, text="Aceptar",command=lambda:devolverDatos(),background="Black",foreground="white",font=('Times New Roman bold',10),border=2)
    B1.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

    return E1.get()

class Pokemon:
    dano_base = 10

    def __init__(self, especie, stats,ataques, tipo, fortalezas, debilidades): #caracteristicas definidas dentro de un diccionario
        self.especie = especie
        self.stats = stats
        self.ataques = ataques
        self.current_stats = self.stats.copy()
        self.tipo = tipo
        self.debilidades = debilidades
        self.fortalezas = fortalezas

    def add(self,attack_name,poder):
        self.ataques.update({str(attack_name): str(poder)})

    def centro_pokemon(self): #restablecer la vida del pokemon
        aux = self.stats.copy()
        self.current_stats = aux #reiniciar las estadisticas
        

    def pelea(self, rival):
        # Tu rival es furte o debil a ti?
        mensaje_pelea = ""
        if self.tipo in rival.fortalezas:
            modificador_ataque = 1/2
            mensaje_pelea = f"{rival.especie} es fuerte a los ataques de {self.especie} \n\n"
        elif self.tipo in rival.debilidades:
            modificador_ataque = 2
            mensaje_pelea = f"{rival.especie} es debil a los ataques de {self.especie} \n\n"
        else:
            modificador_ataque = 1
        
        #eres fuerte o debil a tu rival?
        if rival.tipo in self.fortalezas:
            modificador_defensa = 1/2
            mensaje_pelea += f"{self.especie} es fuerte a los ataques de {rival.especie} \n\n"
        elif rival.tipo in self.debilidades:
            modificador_defensa = 2
            mensaje_pelea += f"{self.especie} es debil a los ataques de {rival.especie} \n\n"
        else:
            modificador_defensa = 1

        # quien ataca primero
        if self.current_stats["velocidad"] >= rival.current_stats["velocidad"]:
            mi_turno = True
        else:
            mi_turno = False
        
        # combate por turnos
        while (self.current_stats["hp"] > 0) & (rival.current_stats["hp"] > 0):
            if mi_turno:
                #Ataque_elegido

                att, power = random.choice(list(self.ataques.items()))
              
                dano = int(self.dano_base * (power/ rival.current_stats["defensa"]) * modificador_ataque) 
                rival.current_stats["hp"] -= dano
                mensaje_pelea += f"{self.especie} uso {att} e hizo {dano} de daño a {rival.especie}\n"
                mensaje_pelea += f"A {rival.especie} le quedan {rival.current_stats['hp']} puntos de vida\n"
        
            else:
                # defendiendo
                attr, powerr = random.choice(list(rival.ataques.items()))
                dano = int(rival.dano_base *(powerr / self.current_stats["defensa"]) * modificador_defensa)
                self.current_stats["hp"] -= dano
                mensaje_pelea += f"{rival.especie} uso {attr} e hizo {dano} de daño a {self.especie}\n"
                mensaje_pelea += f"A {self.especie} le quedan {self.current_stats['hp']} puntos de vida\n"
            mi_turno = not mi_turno
        else:
            if self.current_stats["hp"] <= 0:
                mensaje_pelea += f'{rival.especie} ha ganado la pelea \n'
            else:
                mensaje_pelea += f'{self.especie} ha ganado la pelea \n'
        
        return mensaje_pelea


#Pokemos Usuario
squirtle = Pokemon(
    especie = "Squirtle",
    ataques = {
        "Chorro de agua" :20,
        "Embestida" :30},
    stats = {
        "velocidad": 43,
        "hp": 44,
        "ataque": 48,
        "defensa": 65},
    tipo = "agua",
    fortalezas = ["fuego"],
    debilidades = ["planta"])

charmander = Pokemon(
    especie = "Charmander",
    ataques = {
        "Lanza llamas" :27,
        "Embestida" :36},
    stats = {
        "velocidad": 65,
        "hp": 39,
        "ataque": 52,
        "defensa": 43},
    tipo = "fuego",
    fortalezas = ["planta"],
    debilidades = ["agua"])

bulbasaur = Pokemon(
    especie = "Bulbasaur",
    ataques = {
        "Latigazo" :29,
        "Embestida" :37},
    stats = {
        "velocidad": 45,
        "hp": 45,
        "ataque": 49,
        "defensa": 49},
    tipo = "planta",
    fortalezas = ["agua"],
    debilidades = ["fuego"])

pikachu = Pokemon(
    especie = "Pikachu",
    ataques = {
        "Ataque trueno" :25,
        "Embestida" :40},
    stats = {
        "velocidad": 76,
        "hp": 98,
        "ataque": 62,
        "defensa": 80},
    tipo = "Rayo",
    fortalezas = ["Rayo"],
    debilidades = ["Agua"])

#Pokemones Rivales
squirtle_rival = Pokemon(
    especie = "Squirtle",
    ataques = {
        "Chorro de agua" :18,
        "Embestida" :27},
    stats = {
        "velocidad": 49,
        "hp": 44,
        "ataque": 48,
        "defensa": 65},
    tipo = "agua",
    fortalezas = ["fuego"],
    debilidades = ["planta"])

charmander_rival = Pokemon(
    especie = "Charmander",
    ataques = {
        "Lanza llamas" :31,
        "Embestida" :26},
    stats = {
        "velocidad": 70,
        "hp": 39,
        "ataque": 52,
        "defensa": 43},
    tipo = "fuego",
    fortalezas = ["planta"],
    debilidades = ["agua"])

bulbasaur_rival = Pokemon(
    especie = "Bulbasaur",
    ataques = {
        "Latigazo" :39,
        "Embestida" :27},
    stats = {
        "velocidad": 55,
        "hp": 45,
        "ataque": 49,
        "defensa": 49},
    tipo = "planta",
    fortalezas = ["agua"],
    debilidades = ["fuego"])

pikachu_rival = Pokemon(
    especie = "Pikachu",
    ataques = {
        "Ataque trueno" :35,
        "Embestida" :23},
    stats = {
        "velocidad": 46,
        "hp": 98,
        "ataque": 62,
        "defensa": 80},
    tipo = "Rayo",
    fortalezas = ["Rayo"],
    debilidades = ["Agua"])

#Variable global para elegir solo un pokemon bolean
P_ready = False
S_ready = False
C_ready = False
B_ready = False

#Variable global para elegir solo un pokemon para pelear
C_ready_rival = False
S_ready_rival = False
P_ready_rival = False
B_ready_rival = False

#Seleccion de rival y Pokemon
Selecccion_Rival = False
Nombre_pokemon = "null"
Nombre_rival = "null"
Seleccion_Pokemon = False
Ataque_elegido="null"

texto=ventanaCapturaDatos()


from tkinter import *
import time
import pygame
import random

#Actualisation de la fenetre
def up():
    fenetre.update()

#Mise a 0 de la fenetre
def delete_page():
    for widget in fenetre.winfo_children():
        widget.destroy()

#Jou un son aleatoir
def robot_son():
    liste_son = ["son/Robot.ogg","son/Robot1.ogg","son/Robot2.ogg","son/Robot3.ogg","son/Robot4.ogg"]
    son = random.choice(liste_son)
    son_robot = pygame.mixer.Sound(son)
    son_robot.play()

#activer le son
#def on_son():
#def off_son():

#Fonction de la premiere etape
def commencer():
    liste_dialogue = ["1", "2", "3", "4"]
    btn_commencer.destroy()
    up()
    y = 50
    for i in range(4):
        dialogue1 = Label(fenetre, text=liste_dialogue[i], font=("Arial", 32))
        dialogue1.grid(row=0, column=0, columnspan=2, pady=y, padx=40, sticky="nw")
        y = y + 100
        robot_son()
        up()
        time.sleep(2.5)
    btn_suivant1 = Button(fenetre, text="SUIVANT", font=("Arial", 16),command=entrenom)
    btn_suivant1.grid(row=0, column=0, columnspan=2, pady=400, padx=400, sticky="nw")

#Fonction de la 2eme etape
def entrenom():
    delete_page()
    liste_dialogue = ["Mais pardonnez moi mes bonne magniere", "Comment vous vous appelez ?"]
    y = 100
    x = 350
    for i in range(2):
        dialogue = Label(fenetre, text=liste_dialogue[i], font=("Arial", 20))
        dialogue.grid(row=0, column=0, columnspan=2,pady=y,padx= x,sticky="nw")
        y = y + 100
        x = x + 55
        robot_son()
        up()
        time.sleep(2.5)
    entre = Entry(fenetre, font=("Arial", 13))
    entre.place(y= 450, x=470)
    btn_ok = Button(fenetre, text="OK", font=("Arial", 10), command=le_nom(entre))
    btn_ok.place(y= 450, x=670)
    
def le_nom(entre):
    nom = entre.get()
    print(nom)
    
    
pygame.init()
fenetre = Tk()
fenetre.title("super CC")
fenetre.iconbitmap("img\logo.ico")
fenetre.geometry("1200x900")
fenetre.minsize(1200,900)
fenetre.maxsize(1200,900)
fenetre.config(background="#474747")

btn_commencer = Button(fenetre, text="COMMENCER !", font=("Arial", 32), command=commencer)
btn_commencer.grid(row=0, column=0, columnspan=2, pady=350, padx=440, sticky="we")

#btn_on_son = Button(fenetre, text="ACTIVER", font=("Arial", 16),command=off_son)
#btn_on_son.grid(row=1, column=0, columnspan=2, pady=20, padx=40, sticky="nw")
#btn_off_son = Button(fenetre, text="DESACTIVER", font=("Arial", 16),command=on_son)
#btn_off_son.grid(row=1, column=0, columnspan=2, pady=20, padx=180, sticky="nw")

fenetre.mainloop()





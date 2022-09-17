from interfaz import main
from random import randint
inter = main()#Creo una instancia de la clase "main" del modulo "interfaz" en este modulo decidí guardar los dibujos "ascii"
inter.welcome()#Esta funcion llama al titulo y a las opciones(Revisar modulo interfaz)

pl = int()
bt = randint(1, 3)
pl_win = bool()
bt_win = bool()
draw = bool()

inter.choose_rock_paper_scissors()
#Entrada de datos
pl = int(input("Elija una opcion: "))
print("EL bot elijió", bt)

#Proceso
if pl > 0 and pl <= 3:
    #Condiciones de victoria
    if pl == 1 and bt == 3:
        pl_win = True
    
    elif pl == 2 and bt == 1:
        pl_win = True
    
    elif pl == 3 and bt == 2:
        pl_win = True
    #Condicones de Perdida 
    elif pl == 3 and bt == 1:
        pl_win = False
        bt_win = True
    
    elif pl == 1 and bt == 2:
        pl_win = False
        bt_win = True 
    
    elif pl == 2 and bt == 3:
        pl_win = False
        bt_win = True

    #Si ninguna se cumple es por que es un empate
    else:
        draw = True
        
else:
    print("Ingrese una opcion correcta")

if pl_win:
    print("El jugador es el ganador")

elif bt_win and not draw:
    print("El bot es el ganador")

if draw:
    print("Empate")



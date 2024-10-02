import random as rn
import cowsay as cs
print('''

                ╔════╗╔╗          ╔═══╗        ╔═╗         ╔╗     ╔═══╗                     ╔═══╗
                ║╔╗╔╗║║║          ║╔═╗║        ║╔╝        ╔╝╚╗    ║╔═╗║                     ║╔═╗║
                ╚╝║║╚╝║╚═╗╔══╗    ║╚═╝║╔══╗╔═╗╔╝╚╗╔══╗╔══╗╚╗╔╝    ║║ ╚╝╔╗╔╗╔══╗╔══╗╔══╗     ╚╝╔╝║
                  ║║  ║╔╗║║╔╗║    ║╔══╝║╔╗║║╔╝╚╗╔╝║╔╗║║╔═╝ ║║     ║║╔═╗║║║║║╔╗║║══╣║══╣       ║╔╝
                 ╔╝╚╗ ║║║║║║═╣    ║║   ║║═╣║║  ║║ ║║═╣║╚═╗ ║╚╗    ║╚╩═║║╚╝║║║═╣╠══║╠══║       ╔╗ 
                 ╚══╝ ╚╝╚╝╚══╝    ╚╝   ╚══╝╚╝  ╚╝ ╚══╝╚══╝ ╚═╝    ╚═══╝╚══╝╚══╝╚══╝╚══╝       ╚╝ 
                                                                            
                                                                            

''')
X= rn.randint(1,100)
print(X)
def PERFECT():
    while True:
        GUESS = int(input("CAN YOU GUESS THE NUMBER?    NOOO YOU DON'T :"))
        if GUESS==X:
            cs.daemon(f"OHHH SHITT YOU DID IT ......THAT'S THE ACTUAL NUMBER  {X}")
            break

        elif(X<GUESS):
            cs.dragon("THE NUMBER IS TOO HIGHHH!")
        else:
            cs.cow("THE NUMBER IS TOO LOOOOO!")
            

PERFECT()

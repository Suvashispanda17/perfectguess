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

def PERFECT():
    guess=1
    while True:
        GUESS = int(input("CAN YOU GUESS THE NUMBER?    NOOO YOU DON'T :"))
        if GUESS==X:
            cs.daemon(f"OHHH SHITT YOU DID IT ......THAT'S THE ACTUAL NUMBER  {X}")
            print(f"NUMBER OF ATTEMPTS {guess} ")
            break

        elif(X<GUESS):
            cs.dragon("THE NUMBER IS TOO HIGHHH!")
            guess +=1
        else:
            cs.cow("THE NUMBER IS TOO LOOOOO!")
            guess +=1
            


PERFECT()



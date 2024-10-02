import random as rn
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
    while True:
        GUESS = int(input("CAN YOU GUESS THE NUMBER?    NOOO YOU DON'T :"))
        if GUESS==X:
            print(f"OHHH SHITT YOU DID IT ......THAT'S THE ACTUAL NUMBER  {X}")
            break

        elif(X<GUESS):
            print("THE NUMBER IS TOO HIGHHH!")
        else:
            print("THE NUMBER IS TOO LOOOOO!")
            

PERFECT()
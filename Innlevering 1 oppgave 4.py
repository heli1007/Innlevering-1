#Oppgave 4 Positivt heltall


import math #Importerer matte for å bruke fakultet

while True :
    n=float(input("Skriv inn et positivt heltall."))
    if n%1==0: #Sjekker om tallet er et heltall
        N=math.factorial(n)
        print("Fakultetet av",n,"er",N)
        break
    elif n<0: 
        print("Dette her er da ikke et positivt heltall! Prøv igjen") #Presiserer at tallet må være positivt      
    else:
        print("Dette her er da ikke et heltall! Prøv igjen") #Presiserer at tallet må være positivt og helt
        
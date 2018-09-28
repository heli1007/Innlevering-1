#Oppgave 1 pH

a=float(input("Dette er et program som regner ut pH-en til en løsning og forteller deg om den er sur, basisk eller nøytral. \n Skriv inn løsningens antall H+-ioner i mol/l 5*10^(-3) skrives 5E-3."))
#Definerer antall H+-ioner

import math #Importerer matte for å kunne bruke logaritme i formel

b=-math.log10(a) #Bruker formelen for pH

if 0<b<7:
    print("Denne løsningen har pH",b,"og er derfor sur.")
   
elif b==7:
    print("Denne løsningen har pH",b,"og er derfor nøytral.")
        
elif 7<b<=14:
    print("Denne løsningen har pH",b,"og er derfor basisk.")
else:
    print("Dette er dessverre ikke en godkjent mengde mol/l.")
#Velger en betingelse for å skille mellom sur, basisk, nøytral eller ikke godkjent
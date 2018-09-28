#Oppgave 3 Populasjonsendringer innenfor et område


print("Dette er et program som  regner ut populasjonsendringer innenfor et habitat")

B_n=int(input("Hvor mange dyr bor i habitatet nå?")) #Finner ut nåverende populasjon og antall år som har gått
t=int(input("Hvor mange år har gått?"))

while True: #Bruker en while-løkke
    
    s=input("Vil du at populasjonen skal stige eller synke?") #Finner ut omp populasjonen stiger eller synker
    if s=="stige":
        p=float(input("Skriv inn antall prosent dyrebefolkningen stiger, for eksempel 12."))
        B_ny=int(B_n*(1+p/100)**t) #Ved stigende populasjon er prosenten positiv
        print("Nå bor det",B_ny,"dyr i habitatet.")
        break
    
    elif s=="synke":
        p=float(input("Skriv inn antall prosent dyrebefolkningen synker."))
        B_ny=int(B_n*(1-p/100)**t) #Ved synkende populasjon er prosenten negativ
        print("Nå bor det",B_ny,"dyr i habitatet.")
        break
    else:
        print("Skriv inn et av ordene: stige eller synke") #Hvis du ikke skriver riktig ord, må du prøve på nytt
        
        
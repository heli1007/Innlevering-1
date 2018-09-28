#Oppgave 2 Kinetisk energi


a=input("Dette programmet bruker formelen for kinetisk energi. \n Vil du regne ut energien (E), massen (m), eller farten (v)?")
#Bestemmer om brukeren vil regne ut energien, massen eller farten

if a=="E":
    print("Du har valgt å regne ut energien.")
    m=float(input("Skriv inn massen i kg.")) #Ved energi, setter fart og masse som input
    v=float(input("Skriv inn farten i m/s."))
    E=1/2*m*v**2 #Bruker formelen for kinetisk energi
    print("Energien er",E,"Joule")
    
elif a=="m":
    print("Du har valgt å regne ut massen.") #Ved masse, setter energi og fart som input
    v=float(input("Skriv inn farten i m/s."))
    E=float(input("Skriv inn energien i Joule."))
    m=2*E/(v**2) #Bruker formelen for kinetisk energi, snudd, for å finne massen
    print("Massen er",m,"kg.")
    
elif a=="v":
    print("Du har valgt å regne ut farten.") #Ved fart, setter energi og masse som input
    m=float(input("Skriv inn massen i kg."))
    E=float(input("Skriv inn energien i Joule."))
    v=(2*E/m)**(1/2) #Bruker formelen for kinetisk energi, snudd, for å finne farten
    print("Farten er",v,"m/s.")
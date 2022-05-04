Die_liste = [] #La lista
Die_Hilfsliste = [] #La lista auxiliar
flagge = 0 #0 normal - 1 comentario - 2 caracter especial
Hilfs = '' #Auxiliar
#Torschlusspanik
#Innerer schweinehund    
Worterbuch = {'else':1,'if':2,'int':3,'return':4,'void':5,'while':6,'+':9,'-':10,'*':11,
'/':12,'<':13,'<=':14,'>':15,'>=':16,'==':17,'!=':18,'=':19,';':20,',':21,'(':22,')':23,
'[':24,']':25,'{':26,'}':27}
# def Nachverfolgen(lex,Aktivator):
#     global flagge,Hilfs
#     flagge = 2
#     if Aktivator == 0:
#         Hilfs+=lex
#         flagge = 1
#     elif Aktivator == 1 and ord(lex) == 42:
#         Hilfs+=lex
#         Die_liste.append(Hilfs)
#         flagge = 1
#     elif Aktivator == 1 and ord(lex) != 42:
#         Die_liste.append(lex)
#         flagge = 0

def Kommentator(lex,Aktivator):
    global flagge, Hilfs
    if lex == '/*':
        flagge = 1
    elif lex == '*/':
        flagge = 0


#Continuador del 
def Anhanger(Aktivator):
    global flagge, Hilfs
    
    for n in range(len(Die_liste)):
        Kommentator(Die_liste[n],Aktivator)
        if Aktivator == 0:
            at=Die_liste[n]
            print(Die_liste+" "+Worterbuch.get("at"))
            #print(Die_liste+" "+Worterbuch.values(Die_liste[n]))
        elif Aktivator == 1:
            flagge = 1


#--------------------------------------------------------------------------------------------------------------------------------------------------------------           

def analysator(lex,flagge):
    global Hilfs
    for n in range(len(Die_Hilfsliste)):
        #Mayusculas
        if ord(Die_Hilfsliste[n]) >= 65 and ord(Die_Hilfsliste[n]) <= 90:
            Hilfs+=Die_Hilfsliste[n]

            #Minusculas
        elif ord(Die_Hilfsliste[n]) >= 97 and ord(Die_Hilfsliste[n]) <= 122:
            Hilfs+=Die_Hilfsliste[n]

            # Numeros    
        elif ord(Die_Hilfsliste[n])>= 48 and ord(Die_Hilfsliste[n]) <= 57:
            Hilfs+=Die_Hilfsliste[n]
                
            #Espacios    
        elif ord(Die_Hilfsliste[n]) == 32: 
            if Hilfs != '':          
                Die_liste.append(Hilfs)
                Die_liste.append(Die_Hilfsliste[n])
            Hilfs = ""

            #Salto de linea
        elif ord(Die_Hilfsliste[n]) == 10:            
            if Hilfs != '':          
                Die_liste.append(Hilfs)
                Die_liste.append(Die_Hilfsliste[n])
            Hilfs = ""

            #Llaves
        elif ord(Die_Hilfsliste[n]) == 123 or ord(Die_Hilfsliste[n]) == 125:            
            if Hilfs != '':          
                Die_liste.append(Hilfs)
                Die_liste.append(Die_Hilfsliste[n])
            Hilfs = ''
                
            #Corchetes 
        elif ord(Die_Hilfsliste[n]) == 91 or ord(Die_Hilfsliste[n]) ==93:            
            if Hilfs != '':          
                Die_liste.append(Hilfs)
                Die_liste.append(Die_Hilfsliste[n])
            Hilfs = ""
            
            #Punto y coma
        elif ord(Die_Hilfsliste[n]) == 59:            
            if Hilfs != '':          
                Die_liste.append(Hilfs)
                Die_liste.append(Die_Hilfsliste[n])
            Hilfs = ""

            #Asterisco
        elif ord(Die_Hilfsliste[n]) == 42:
            if ord(Die_Hilfsliste[n-1]) == 47:
                Hilfs += Die_Hilfsliste[n]
                Die_liste.append(Hilfs)
                Hilfs = ""
            elif ord(Die_Hilfsliste[n+1]) ==47:
                Hilfs = Die_Hilfsliste[n] 

            # Caracteres especiales complejos < = >
        elif ord(Die_Hilfsliste[n]) >=60 and ord(Die_Hilfsliste[n]) <=62: 
            if Hilfs != '':          
                Die_liste.append(Hilfs)
                Die_liste.append(Die_Hilfsliste[n])
            Hilfs = ""

            # Caracter especial /
        elif ord(Die_Hilfsliste[n]) == 47:
            if ord(Die_Hilfsliste[n+1]) == 42:
                Hilfs = Die_Hilfsliste[n]
            elif ord(Die_Hilfsliste[n-1]) == 42:
                Hilfs += Die_Hilfsliste[n]
                Die_liste.append(Hilfs)
                Hilfs = ''

            #Caracteres especiales ( ) 
        elif ord(Die_Hilfsliste[n]) >= 40 and ord(Die_Hilfsliste[n]) <=41: 
            if Hilfs != '':          
                Die_liste.append(Hilfs)
                Die_liste.append(Die_Hilfsliste[n])
                Hilfs = ''
            else:
                Die_liste.append(Die_Hilfsliste[n])
            
            #Caracteres especiales  + , -
        elif ord(Die_Hilfsliste[n]) >= 43 and ord(Die_Hilfsliste[n]) <=45: 
            if Hilfs != '':          
                Die_liste.append(Hilfs)
                Die_liste.append(Die_Hilfsliste[n])
                Hilfs = ''
            else:
                Die_liste.append(Die_Hilfsliste[n])
            
        else:
            print(ord(Die_Hilfsliste[n]))
            print("Error: No se encontro el simbolo" + lex)

# try:
#     archivo = "/home/ulrich/DocumentosPython/prog1.tc"
#     file = open("./prog1.tc", "r")

#     while True:
        
#         lex = file.read(1)
#         if not lex:
#             print ("End of file")
#             break
#         else:
#             Die_Hilfsliste.append(lex)

#     file.close()
#     analysator(lex,flagge)
#     print(Die_liste)
#     Anhanger(flagge)
# except:
#     print('Error')




archivo = "/home/ulrich/DocumentosPython/prog1.tc"
file = open("./prog1.tc", "r")
while True:
        
    lex = file.read(1)
    if not lex:
        print ("End of file")
        break
    else:
        Die_Hilfsliste.append(lex)
file.close()
analysator(lex,flagge)
print(Die_liste)
Anhanger(flagge)





# tam = 5
# for i in range(tam):
#     token = input()
#     Die_liste.append(token)

# for n in Die_liste:
#     print(n)


# for n in range(len(Die_liste)):
#     print(Die_liste[n])


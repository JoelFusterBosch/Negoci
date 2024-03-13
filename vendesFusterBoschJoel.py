#Joel Fuster Bosch
#Inicialització dels vectors
noms=[]
preus=[]
qVenudes=[]
while True:
    #Menú
    print("-----------")
    print("1. Introduir un article nou")
    print("2. Fer una venda")
    print("3. Mostrar informació")
    print("4. Esborrar un article")
    print("5. Esborrar tots els articles")
    print("6. Eixir")
    print("-----------")
    #Elecció del menú
    opcio=int(input("Quina opcio agarres?"))
    print("-----------")
    if opcio==1:
        quantitat=0
        #Pregunta nom i preu del article i afig eixos valors als vectors
        article=input("Quin article vols afegir?")
        noms.append(article)
        preu=float(input("Quin preu té?"))
        preus.append(preu)   
        qVenudes.append(quantitat)
    elif opcio==2:
        triar=input("Dis-me quin producte vols:")
        produtrobat=False
        #Bucle per a trobar que eixe producte existisca
        for i in range(len(noms)):
            if triar==noms[i]:
                produtrobat=True
                break
        if produtrobat:
            #Si existeix el producte es suma la quntitat que compres
            quantitat=int(input("Quants compres?"))
            qVenudes[i]+=quantitat
        else:
            #Si no existeix dona error
            print("Error")        
    elif opcio==3:
        #iniciem les variables de la llista dels més venuts, més ingressos i el total 
        total=0
        mesvenut=0
        nomesvenut=""
        mesingressos=0
        nomesingressos=""
        #Preguntem si volem la llista inversa o no
        invers=input("Vols vore la llista en inversa?")
        print("NOM\tQUANTITAT\tPREU\tIMPORT")
        if invers=="s" or invers=="S":
            #For per a fer calculs i mostrar els productes
            for i in range(len(noms),0,-1):
                print(noms[i-1],end="\t")
                print(qVenudes[i-1],end="\t")
                print(preus[i-1],end="\t")
                print(preus[i-1]*qVenudes[i-1])
                mitja=preus[i-1]*qVenudes[i-1]
                total+=mitja
                if qVenudes[i-1]>=mesvenut:
                    mesvenut=qVenudes[i-1]
                    nomesvenut=noms[i-1] 
                if (preus[i-1]*qVenudes[i-1])>=mesingressos:
                    nomesingressos=noms[i-1]
                    mesingressos=preus[i-1]*qVenudes[i-1]
            print("TOTAL:",total)  
            print("Article més venut: ",nomesvenut, " amb ",mesvenut," unitats")
            print("Article amb més ingressos: ",nomesingressos," amb ",mesingressos)      
        else:
            #For per a fer calculs i mostrar els productes
            for i in range(len(noms)):
                print(noms[i],end="\t")
                print(qVenudes[i],end="\t")
                print(preus[i],end="\t")
                print(preus[i]*qVenudes[i])
                mitja=preus[i]*qVenudes[i]
                total+=mitja 
                if qVenudes[i]>=mesvenut:
                    mesvenut=qVenudes[i]
                    nomesvenut=noms[i] 
                if (preus[i]*qVenudes[i])>=mesingressos:
                    nomesingressos=noms[i]
                    mesingressos=preus[i]*qVenudes[i]
            print("TOTAL:",total)  
            print("Article més venut: ",nomesvenut, " amb ",mesvenut," unitats")
            print("Article amb més ingressos: ",nomesingressos," amb ",mesingressos)  
    elif opcio==4:
        #Iniciem la variable per a borrar el producte que li preguntem i si existeix
        produborrat=False
        produeliminar=input("Quin producte vols borrar?:")
        #Bucle per a vore si existeix el producte que volem borrar
        for i in range(len(noms)):
            if produeliminar==noms[i]:
                produborrat=True
                break
        for i in range(len(preus)):
            if preus[i]==noms[i]:
                break
        for i in range(len(qVenudes)):
            if qVenudes[i]==noms[i]:
                break
        if produborrat:
            #Si existeix el producte el borrem i deixem lliure el lloc que ocupava
            noms.remove(produeliminar)
            preus.remove(preus[i-1])
            qVenudes.remove(qVenudes[i-1])
            print("Producte eliminat")
        else:
            #Si no existeix dona un missatge de error
            print("Article no trobat")
    elif opcio==5:
        #Borrem i tornem a fer des de 0 més el missatge que han sigut borrats exitosament
        noms=[]
        preus=[]
        qVenudes=[]
        print("Borrats tots els articles")
    elif opcio==6:
        #Ens dona la opció de eixir i acabar
        eixir=input("Estas segur de que vols eixir?(s/n)(S/N)")
        if eixir=="s" or  eixir=="S":
            break
        else:
            continue
    else:
        print("Sols pots agarrar les opcions de l'1 al 6")
#Última llista per a quan acabé tot mostre el total a pagar més el que més ha venut i el que més ingressos ha generat
for i in range(len(noms)):
    print(noms[i],end="\t")
    print(qVenudes[i],end="\t")
    print(preus[i],end="\t")
    print(preus[i]*qVenudes[i])
    mitja=preus[i]*qVenudes[i]
    total+=mitja 
    if qVenudes[i]>=mesvenut:
            mesvenut=qVenudes[i]
            nomesvenut=noms[i] 
    if (preus[i]*qVenudes[i])>=mesingressos:
            nomesingressos=noms[i]
            mesingressos=preus[i]*qVenudes[i]
print("TOTAL:",total)  
print("Article més venut: ",nomesvenut, " amb ",mesvenut," unitats")
print("Article amb més ingressos: ",nomesingressos," amb ",mesingressos)  
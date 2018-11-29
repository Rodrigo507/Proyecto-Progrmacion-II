import random
nomb=["Alan","Aron","Pietra","Pilian","Quilina","Rey","Regis","Regino","Romulo","Yasmila","Yako","Zane","Zahirah","Abril","Rodrigo","Jose","Marina","Jesaid","Isidro"]#NombresEnMemoria
apell=["Borge","Arellano","De Trinidad","Gomar","Carvajal","Martí","Sagot","Wolf","Salom","Vivas","Barrundia","Barquero","Bustillos","Pereira","Atencio","Urriola"]#ApellidoEnMemoria
centro=["Esc.La Mata","Esc.Los Boquerones","Esc.El Espino"]#Lista de los centro de votacion
repre=["Ismael Perez","Tomas Castro","Ricauter Gonzalez","Diana Montes"]#Candidatos a representante
cantidad=2000#Es numero votantes de la poblacion del corregimiento
votrandom=random.randint(1,(cantidad/2))#Indica la cantidad aleatoria de personas que asistiran a las urnas
def cargamatriz(f, a, b, c, d):#Funcion para cargar el padron electoral
    m=[]
    for j in range(f):
        m.append([])
        for i in range(1):
            m[j].append(b[j])
            m[j].append(a[j])
            m[j].append(c[j])
            m[j].append(d[j])
    return (m)
def imprecionmatriz(a,b,c):#Funcion para la imprecion de matriz
    for j in range(b):
        for i in range(c):
            print(" ",a[j][i],"  ",end=" ")
        print()
def creanomb(a,b,c):#Funcion para crear n cantidad nombres aleatorios
    t=[]
    for j in range(c):
        d=random.randint(0,len(a)-1)
        e = random.randint(0, len(b) - 1)
        t.append("  "+a[d]+' '+b[e])
    return (t)
def cedula(z): #Crea n cantidad de Cedulas aleatoriamente
    t=[]
    for j in range(z):
        a=random.randint(1,10)#N.Provincia
        b=random.randint(100,999)#Segundo numero
        c=random.randint(1,9999)#Tercer numero
        t.append(str(a)+"-"+str(b)+"-"+str(c))
    return (t)
def centrovot(a,b):#Gnera una lista con n cantidad de centro de votacion para los votantes
    t=[]
    for j in range(a):
        r=random.randint(0,len(b)-1)
        if b[r]=="Esc.La Mata":
            t.append("Esc.La Mata")
        else:
            if b[r]=="Esc.Los Boquerones":
                t.append("Esc.Los Boquerones")
            else:
                if b[r]=="Esc.El Espino":
                    t.append("Esc.El Espino")
    return (t)
def mesa(b,a): #Funcion que Depende del centro de votacion asignado da el numero de mesa
    t=[]
    for j in range(a):
        if b[j] == "Esc.La Mata":
            c = random.randint(1,2)
            t.append(c)
        else:
            if b[j] == "Esc.Los Boquerones":
                c = random.randint(3,4)
                t.append(c)
            else:
                if b[j] == "Esc.El Espino":
                    c = random.randint(5,6)
                    t.append(c)
    return (t)
def verifica(a,n,x):#Verifica cada indice para que no se repita
    i=0
    sw=0
    while (i<n and sw==0):
        if a[i]==x:
            sw=1
        i=i+1
    return (sw)
def cargamatrizdvotantes(a, b, c):#Carga una matriz para cada votante "No se pude usar la anterior por formato diferente al cargar los datos"
    m=[]
    for j in range(a):
        m.append([])
        for i in range(4):
            m[j].append(b[c[j]][i])
    return (m)
def genevotos():#Funcion que devuelve un valor que indica el candidato por el cual voto
    a=random.randint(0,4)
    return (a)
def concentro(a,b,c,d):#Da como resultado el total que votaron en x centro de votacion"Matriz"
    con=0
    for j in range(a):
        if b[j][d]==c:
            con=con+1
    return (con)
def contmesa(a,b,c):#Contador de voto por mesa "Nose puede utilizar la funcion anterior para las mesa porque las mesas es una lista"
    cont=0
    for j in range(a):
        if b[j]==c:
            cont=cont+1
    return (cont)
def canditogana(a):#Da la pocion del mayor en una lista "En este caso la pocion del ganador"
    mayor=0
    for j in range(len(a)):
        if a[j]>mayor:
            mayor=a[j]
            pos=j
    return (pos)
def porcentaje(a,b):#Porcentaje de voto
    c=(a/b)*100
    return (c)
b=cedula(cantidad)#Lista se cedulas
a=creanomb(nomb,apell,cantidad)#Lista de nombres
c=centrovot(cantidad,centro)#Lista de centro de votacion
d=mesa(c,cantidad)#Lista de mesas segun centro de votacion
print("PADRON ELECTORAL".center(65,"="))
print("      cedula             Nombre          Centro de Votacion   Mesa".upper())
padron=cargamatriz(cantidad, a, b, c, d)#Cargar matriz
imprecionmatriz(padron,cantidad,4)#Imprecion matriz
ind=[]#Indices aleatorios que votaran
i=0#Control de ciclo
while i<votrandom:
    x=random.randint(0,cantidad-1)
    if verifica(ind,i,x)==0:
        ind.append(x)
        i=i+1
print()
print("      cedula             Nombre          Centro de Votacion   Mesa".upper())
padronvotaron=cargamatrizdvotantes(votrandom, padron, ind)
imprecionmatriz(padronvotaron,votrandom,4)
print()
totalcen1=concentro(votrandom,padronvotaron,"Esc.La Mata",2)#Guarda el total de centro de votacion1
totalmesa1=concentro(votrandom,padronvotaron,1,3)#Guarda el total de votantes en la mesa 1
totalmesa2=concentro(votrandom,padronvotaron,2,3)#Guarda el total de votantes en la mesa 2
totalcen2=concentro(votrandom,padronvotaron,"Esc.Los Boquerones",2)#Guarda el total de centro de votacion2
totalmesa3=concentro(votrandom,padronvotaron,3,3)#Guarda el total de votantes en la mesa 3
totalmesa4=concentro(votrandom,padronvotaron,4,3)#Guarda el total de votantes en la mesa 4
totalcen3=concentro(votrandom,padronvotaron,"Esc.El Espino",2)#Guarda el total de centro de votacion3
totalmesa5=concentro(votrandom,padronvotaron,5,3)#Guarda el total de votantes en la mesa 5
totalmesa6=concentro(votrandom,padronvotaron,6,3)#Guarda el total de votantes en la mesa 6
print("Total del Corregimiento".upper(),votrandom)
print()
print("El total de votos emitidos por centro de votación".center(30,' ').upper())
print("Total Esc La mata",totalcen1)
print("Total Esc Los boquerlones",totalcen2)
print("Total Esc El espino",totalcen3)
print()
print("El total de votos emitidos por mesa".upper())
print("Total Mesa 1-",totalmesa1)
print("Total Mesa 2-",totalmesa2)
print("Total Mesa 3-",totalmesa3)
print("Total Mesa 4-",totalmesa4)
print("Total Mesa 5-",totalmesa5)
print("Total Mesa 6-",totalmesa6)
print()
votosrepre=[]#El voto de cada votante para los candidatos
for j in range(votrandom):#Ciclo para cargar los votos emitidos
    votosrepre.append(genevotos())
print("Total por candidato".upper())
cand1=contmesa(votrandom, votosrepre, 1)#Guarda el total del candidato 1
cand2=contmesa(votrandom, votosrepre, 2)#Guarda el total del candidato 2
cand3=contmesa(votrandom, votosrepre, 3)#Guarda el total del candidato 3
cand4=contmesa(votrandom, votosrepre, 4)#Guarda el total del candidato 4
print("Ismael Perez",cand1)
print("Tomas Castro",cand2)
print("Ricauter Gonzalez",cand3)
print("Diana Montes",cand4)
print()
nulo=contmesa(votrandom, votosrepre, 0)#Guarda el total de votos en blanco
print("Voto valido".upper(),votrandom-nulo)
print("Voto blanco".upper(),nulo)
print()
vototal=[]#Lista del total de votos para cada candidatos
for j in range(1):#se carga la lista con el total de votos por candidato
    vototal.append(cand1)
    vototal.append(cand2)
    vototal.append(cand3)
    vototal.append(cand4)
indrepre=canditogana(vototal)#Indice del ganador o del mayor votos
print("Candidato ganador",repre[indrepre].upper())#Se busca el indice en la lista cargada en memoria de los precandidatos a reprecentantes
print()
a1=porcentaje(cand1,votrandom)#Porcentaje de votos para le candidato 1
a2=porcentaje(cand2,votrandom)#Porcentaje de votos para le candidato 2
a3=porcentaje(cand3,votrandom)#Porcentaje de votos para le candidato 3
a4=porcentaje(cand4,votrandom)#Porcentaje de votos para le candidato 4
blanco=porcentaje(nulo,votrandom)#Porcentaje de votos en blanco
print("Porcentaje obtenido por cada candidato")
print('Ismael Perez','%.2f' %a1,'%')
print('Tomas Castro','%.2f' %a2,'%')
print('Ricauter Gonzalez','%.2f' %a3,'%')
print('Diana Montes','%.2f' %a4,'%')
print("Porcentaje de votos en blanco")
print('Votos en Blanco','%.2f' %blanco,'%')
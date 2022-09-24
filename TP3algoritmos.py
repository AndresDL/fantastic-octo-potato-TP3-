#Alejo,Rosso-Bautista/Ruiz Aldea/Julio,Vivas/Andres,De Luca-COM 106
#OPS = Array [0..7] of int / CONTPRODS = Array [0..3][0..4] of int / CAMS = Array [0..3][0..7] of int
#OPS2 = Array [0..6] of char/ OPS3 = Array [0..3] of char
#PRODS = Array [0..2] of string /HAB = Array [0..4] of string/HABMXMN = Array [0..1][0..4] of string/PATS = Array [0..2][0..7] of string
#elec,verif,verif2,verif3,c,contprod,recibidos,pb,tara,neto,taramax,taramin,pbmax,pbmin,netmax: integer
#elec2,elec3: char
#valid,patente,prod,ingprod,elim,mod: string
#ver1,ver2: bool
import os
import pickle
import os.path
import io

OPS2 = ["A","B","C","D","E","F","G"]
OPS3 = ["A","B","C","M"]
PRODS = [""]*3#Listadoactivo
CONTPRODS = [[0]*5,[0]*5,[0]*5,[40]*5]#Cantcamxprod-Netototalxprod-Netomaximoxprod-Netominimoxprod
HABMXMN = [[""]*5,[""]*5]#patMax-patMin
HAB = ["TRIGO","SOJA","MAIZ","GIRASOL","CEBADA"]#Productoshabilitados
CAMS = [[0]*8,[0]*8,[0]*8,[0]*8]#Cupo-Pesobruto-Tara-Pesoneto
PATS = [[""]*8,[""]*8,[""]*8]#Patente-Producto-Estado
taramax = 25
taramin = 13
pbmax = 53
pbmin = 30
netmax = 40 

class operaciones:
    def _init_(self):
        self.patente = ""
        self.codprod = 0
        self.fechacupo = 0
        self.estado = ""
        self.bruto = 0
        self.tara = 0

class productos:
    def _init_(self):
        self.cod = 0
        self.nomb = ""

class rubros:
    def _init_(self):
        self.cod = 0
        self.nombrubro = ""

class rubrosxprod:
    def _init_(self):
        self.codrubro = 0
        self.codprod = 0
        self.valorminad = 0.0
        self.valormaxad = 0.0

class silos:
    def _init_(self):
        self.codsilo = 0
        self.nombsilo = ""
        self.codprod = 0
        self.stock = 0   

def validarsientero(nro,min,max):
    try:
        int(nro)
        if int(nro) >= min and int(nro) <= max:
            return False
        else:
            os.system('cls')
            print("Usted ah ingresado un numero fuera del rango de opciones:",nro)
            print()
            print("Recuerde ingresar una de las opciones en pantalla.")
            print()
            input("Presione la tecla ENTER para continuar: ")
            return True
    except:
        os.system('cls')
        print("Usted ah ingresado una letra o un caracter especial:",nro)
        print()
        print("Recuerde ingresar una de las opciones en pantalla.")
        print()
        input("Presione la tecla ENTER para continuar: ")
        return True

def mainmenu():
    os.system('cls')
    print("------------------------")
    print("1-Administración")
    print("2-Entrega de cupos")
    print("3-Recepción")
    print("4-Registrar calidad")
    print("5-Registrar peso bruto")
    print("6-Registrar descarga")
    print("7-Registrar tara")
    print("8-Reportes")
    print("0-Fin del programa")
    print("------------------------")

def menu():
    global elec
    os.system('cls')
    mainmenu()
    elec = (input("Bienvenido a el menu principal. Ingrese una de las opciones con el teclado y presione la tecla ENTER: "))
    while elec != 0:
        while validarsientero(elec,0,8):
            mainmenu()
            elec = input("Ingrese una de las opciones en pantalla y presione la tecla ENTER: ")
        elec = int(elec)
        if elec == 1:
            os.system('cls')
            administraciones()
        elif elec == 2:
            entcupos()
        elif elec == 3:
            recepcion()
        elif elec == 4:
            os.system('cls')
            enconst()
        elif elec == 5:
            os.system('cls')
            pesobruto()
        elif elec == 6:
            os.system('cls')
            enconst()
        elif elec == 7:
            os.system('cls')
            regtara()
        elif elec == 8:
            reportes()
        mainmenu()
        elec = int(input("Bienvenido a el menu principal. Ingrese una de las opciones con el teclado y presione la tecla ENTER: "))
         
        
c = 0
def entcupos():
    global c
    global patente
    global ver1
    global ver2
    global valid
    os.system('cls')
    print("Opción seleccionada: Entrega de Cupos.")
    print()
    mostrarlistado()
    print("Aquí podrá ingresar la patente de un camión y luego se le entregara un numero de cupo al mismo (con un maximo de 8 cupos, se otorga un cupo por camion) y se le otorgara el estado: P-Pendiente.")
    print()
    print("Las patentes validas son las siguientes: LLLNNN y LLNNNLL. Siendo L letras y N numeros")
    print()
    patente = str(input("Ingrese la patente del camión o ingrese un * para volver al menu anterior. Para continuar presione la telca ENTER luego de ingresar los datos: "))
    patente = patente.upper()
    ver1 = patente[0:3].isalpha() and patente[4:6].isdigit()
    ver2 = patente[0:2].isalpha() and patente[3:5].isdigit() and patente[6:7].isalpha()
    while patente != "*":
        validarpatente(patente)
        if c > 7:
            os.system('cls')
            print("Ya se ah dado el maximo numero de 8 cupos.")
            print()
            print("Patentes en el listado: ",end="")
            for k in range(8):
                print(PATS[0][k],end=" ")
            print()
            print()
            input("Presione la tecla ENTER para continuar: ")
        else:
            k = 0
            while PATS[0][k] != valid and k < 7:
                k = k + 1
            if PATS[0][k] == valid:
                os.system('cls')
                print(valid)
                print()
                print("Esta patente ya se encuentra en listado activo. Por lo tanto no se le puede asignar un cupo adicional.")
                print()
                for k in range(8):
                    print(PATS[0][k],end=" ")
                print()
                print()
                input("Presiona la tecla ENTER para continuar: ")
            else:
                k = 0 
                while PATS[0][k] != "":
                    k = k + 1
                if PATS[0][k] == "":
                    PATS[0][c] = valid
                    PATS[2][c] = "P"
                    CAMS[0][c] = c + 1
                    c = c + 1
                    os.system('cls')
                    print(valid)
                    print()
                    input("Patente ingresada exitosamente! Presione la tecla ENTER para coninuar: ")
        os.system('cls')
        mostrarlistado()
        print()
        print()
        print("Recuerde que los formatos validos de patente son de forma LLLNNN y LLNNNLL siendo L letras y N numeros, entre 6 y 7 caracteres y alfanumericas.")
        print()
        patente = str(input("Ingrese un * para volver al menu anterior o para registrar otra patente ingresela, recuerde que hay un maximo de 8 patentes, y presione ENTER: "))
        patente = patente.upper()
        ver1 = patente[0:3].isalpha() and patente[4:6].isdigit()
        ver2 = patente[0:2].isalpha() and patente[3:5].isdigit() and patente[6:7].isalpha()

def mostrarlistado():
    if c > 0:
        print("A continuación se mostraran las pantentes en el listado activo de manera: Pantente-Producto-Estado")
        print()
        print("Patentes en el listado activo: ",end="")
        for k in range(8):
            print(PATS[0][k],end=" ")
            print(PATS[1][k],end=" ")
            print(PATS[2][k],end=" - ")
        print()
        print()

def listadoproductos():
    if contprod > 0: 
        print()
        print("Productos en el listado activo: ",end="")
        for i in range(3):
            print(PRODS[i],end=".")
        print()
        print()

def validarpatente(patente):
    global valid
    global ver1 
    global ver2
    while ((patente.isalnum() == False or (ver1 == False and ver2 == False)) or (len(patente) < 6 or len(patente) > 7)):
        if patente.isalnum() == False:
            os.system('cls')
            print(patente)
            print("La patente ingresada no es de formato alfanumerico.")
            print()
            print("Evite utilizar espacios, comas, puntos, guiones y/o caracteres especiales ($,%,&,#,@,etc)")
            print()
            input("Presione la tecla ENTER para volver a intentar: ")
        elif len(patente) < 6:
            os.system('cls')
            print(patente)
            print()
            print("Patente muy corta. Las patentes no deben contener menos de 6 caracteres alfanumericos.")
            print()
            input("Presione la tecla ENTER para volver a intentar: ")
        elif len(patente) > 7:
            os.system('cls')
            print(patente)
            print()
            print("Patente muy larga. Las patentes no deben contener mas de 7 caracters alfanumericos.")
            print()
            input("Presione la tecla ENTER para volver a intentar: ")
        elif ver1 == False and ver2 == False:
            os.system('cls')
            print(patente)
            print()
            print("Patente de formato invalido. Recuerde que los tipos de patente valido son LLLNNN y LLNNNLL siendo L letras y N numeros.")
            print()
            input("Presione la tecla ENTER para volver a intentar: ")
        os.system('cls')
        print("Recuerde que los formatos validos de patente son de forma LLLNNN y LLNNNLL siendo L letras y N numeros, entre 6 y 7 caracteres y alfanumericas.")
        print()
        mostrarlistado()
        patente = str(input("Ingrese una patente con formato correcto. Para continuar presione la tecla ENTER luego de ingresar los datos: "))
        patente = patente.upper()
        ver1 = patente[0:3].isalpha() and patente[4:6].isdigit()
        ver2 = patente[0:2].isalpha() and patente[3:5].isdigit() and patente[6:7].isalpha()
    valid = patente 

recibidos = 0
def recepcion():
    global recibidos
    global patente
    global valid
    global ver1
    global ver2
    global prod
    os.system('cls')
    if c == 0:
        print("Todavia no se han ingresado patentes para procesar. Dirigirse a la opción: 2-Entrega de cupos.")
        print()
        input("Presione la tecla ENTER para volver al menu anterior: ")
    else:
        print("Opcion seleccionada: Recepcion")
        print()
        if contprod == 0:
            print("Todavía no se han ingresado productos. Para ingresarlos, dirijase a la opción: 1-Administraciones -> B-Productos -> A-Alta.")
            print()
            input("Presione la tecla ENTER para continuar: ")
        else:
            print("Aquí podra ingresar el tipo de producto que esta transportando el camion. Solo podrá hacerlo con dichos camiones en estado: Pendiente-P. Luego del ingreso se le asignara el estado: En proceso-E.")
            print()
            mostrarlistado()
            print()
            patente = str(input("Ingrese una de las patentes del listado para procesar o un * para volver al menu anterior. Presione la tecla ENTER para continuar: "))
            patente = patente.upper()
            ver1 = patente[0:3].isalpha() and patente[4:6].isdigit()
            ver2 = patente[0:2].isalpha() and patente[3:5].isdigit() and patente[6:7].isalpha()
            print()
            while patente != "*":
                validarpatente(patente)
                i = 0
                while PATS[0][i] != valid and i < 7:
                    i = i + 1
                if PATS[0][i] != valid:
                    os.system('cls')
                    print("La patente ingresada ",valid," no se encuentra dentro del listado activo.")
                    print()
                    mostrarlistado()
                    input("Presione la tecla ENTER para volver a intentar: ")
                else:
                    if PATS[2][i] != "P":
                        os.system('cls')
                        print("El camion con patente ",patente,"no esta en estado: Pendiente. Recuerde que aqui se procesan las patentes con dicho estado.")
                        print()
                        input("Presione la tecla ENTER para volver a intentar: ")
                    else:
                        listadoproductos()
                        prod = str(input("Ingrese el nombre del producto transportado. El mismo debe estar dentro del listado activo: "))
                        prod = prod.upper()
                        k = 0
                        while PRODS[k] != prod and k < 2:
                            k = k + 1
                        if PRODS[k] != prod or prod == "":
                            os.system('cls')
                            print("El producto ingresado",prod," no se encuentra en el listado activo.")
                            listadoproductos()
                            print()
                            input("Presione la tecla ENTER para volver a intentar: ")
                        else:
                            PATS[1][i] = prod
                            PATS[2][i] = "E"
                            recibidos = recibidos + 1
                            k = 0
                            while prod != HAB[k] and k < 4:
                                k = k + 1
                            CONTPRODS[0][k] = CONTPRODS[0][k] + 1
                            os.system('cls')
                            print("El producto del camion se registro correctamente!")
                            print()
                            print("Camion: ",PATS[0][i]," Producto: ",prod)
                            print()
                            input("Presione la tecla ENTER para continuar: ")
                os.system('cls')
                print("Opción seleccionada: Recepcion")
                print()
                mostrarlistado()
                patente = str(input("Ingrese una de las patentes del listado para procesar o un * para volver al menu anterior. Para continuar presione la tecla ENTER: "))
                patente = patente.upper()
                ver1 = patente[0:3].isalpha() and patente[4:6].isdigit()
                ver2 = patente[0:2].isalpha() and patente[3:5].isdigit() and patente[6:7].isalpha()

def pesobruto():
    global patente
    global ver1
    global ver2
    global valid
    os.system('cls')
    print("Opción elegida: Registrar peso bruto")
    print()
    if c == 0:
        print("Todavia no se han ingresado patentes para procesar. Dirigirse a la opción: Entrega de cupos.")
        print()
        input("Presione la tecla ENTER para volver al menu anterior: ")
    else:
        mostrarlistado()
        print()
        patente = str(input("Ingrese la patente de uno de los caminones del listado o ingrese un * para volver al menu anterior. Para continuar presione la telca ENTER: "))
        patente = patente.upper()
        ver1 = patente[0:3].isalpha() and patente[4:6].isdigit()
        ver2 = patente[0:2].isalpha() and patente[3:5].isdigit() and patente[6:7].isalpha()
        while patente != "*":
                validarpatente(patente)
                i = 0
                while PATS[0][i] != valid and i < 7:
                    i = i + 1
                if PATS[0][i] != valid:
                    os.system('cls')
                    print("La patente ingresada ",valid," no se encuentra en el listado activo.")
                    print()
                    input("Presione la tecla ENTER para continuar: ")
                else:
                    if PATS[2][i] != "E":
                        os.system('cls')
                        print("El camion con patente ",PATS[0][i]," no esta en estado E-En proceso. Para darle el estado necesario dirijase a Recepción.")
                        print()
                        input("Presione la tecla ENTER para volver a intentar: ")
                    else:
                        if CAMS[1][i] > 0:
                            os.system('cls')
                            print("El camion con patente ",PATS[0][i]," ya tiene peso bruto registrado: ",CAMS[1][i],". Por lo tanto no se le puede asignar nuevamente.")
                            print()
                            input("Presione la tecla ENTER para volver a intentar: ")
                        else:    
                            os.system('cls')
                            print("Recuerde ingresar el peso bruto del camion en Toneladas-TN.")
                            print()
                            print("El peso bruto maximo permitido según FADEEAC (la Federación Argentina de Entidades Empresarias del Autotransporte de Carga) es de 53 TN. Y el minimo permitido es de 30 TN.")
                            print()
                            pb = int(input("Ingrese el peso bruto del camion con patente "+PATS[0][i]+" el cual transporta "+PATS[1][i]+": "))
                            while pb > pbmax or pb < pbmin:
                                if pb > pbmax:
                                    os.system('cls')
                                    print("El peso ingresado es mayor que el permitido. Peso ingresado: ",pb)
                                    print()
                                    print("Recuerde que el peso bruto maximo permitido es de 53 TN según la FADEEAC.")
                                    print()
                                    input("Presione la tecla ENTER para volver a intentar: ")
                                else:
                                    os.system('cls')
                                    print("El peso bruto ingresado es menor que el permitido. Peso ingresado: ",pb)
                                    print()
                                    print("Recuerde que el minimo permitido es de 30 TN.")
                                    print()
                                    input("Presione la tecla ENTER para volver a intentar: ")
                                os.system('cls')
                                print("Recuerde ingresar el peso bruto del camion en Toneladas-TN.")
                                print()
                                print("El peso bruto maximo permitido según FADEEAC (la Federación Argentina de Entidades Empresarias del Autotransporte de Carga) es de 53 TN. Y el minimo permitido es de 30 TN.")
                                print()
                                pb = int(input("Ingrese el peso bruto del camion con patente "+PATS[0][i]+" el cual transporta "+PATS[1][i]+": "))    
                            CAMS[1][i] = pb
                            os.system('cls')
                            print("Peso bruto ingresado exitosamente!")
                            print()
                            print("Camion con patente: ",PATS[0][i]," Estado: ",PATS[2][i], " Peso bruto: ",CAMS[1][i],"TN")
                            print()
                            input("Presione la tecla ENTER para continuar: ")
                os.system('cls')
                mostrarlistado()
                print()
                patente = str(input("Ingrese la patente de uno de los caminones del listado o ingrese un * para volver al menu anterior. Para continuar presione la telca ENTER: "))
                patente = patente.upper()
                ver1 = patente[0:3].isalpha() and patente[4:6].isdigit()
                ver2 = patente[0:2].isalpha() and patente[3:5].isdigit() and patente[6:7].isalpha()

def regtara():
    global patente
    global ver1
    global ver2
    global valid
    global i
    os.system('cls')
    print("Opción elegida: Registrar tara")
    print()
    print("Aquí podrá registrar la tara de los camiones.")
    print()
    if c == 0:
        print("Todavia no se han ingresado patentes para procesar. Dirigirse a la opción: Entrega de cupos.")
        print()
        input("Presione la tecla ENTER para volver al menu anterior: ")
    else:
        print("Recuerde ingresar la tara del camión en Toneladas-TN")
        mostrarlistado()
        print()
        patente = str(input("Ingrese la patente de uno de los caminones del listado o ingrese un * para volver al menu anterior. Para continuar presione la telca ENTER: "))
        patente = patente.upper()
        ver1 = patente[0:3].isalpha() and patente[4:6].isdigit()
        ver2 = patente[0:2].isalpha() and patente[3:5].isdigit() and patente[6:7].isalpha()
        while patente != "*":
            validarpatente(patente)
            i = 0
            while PATS[0][i] != valid and i < 7:
                    i = i + 1
            if PATS[0][i] != valid:
                os.system('cls')
                print("La patente ingresada ",valid," no se encuentra en el listado activo.")
                print()
                input("Presione la tecla ENTER para volver a intentar: ")
            else:
                if CAMS[2][i] > 0:
                    os.system('cls')
                    print("La patente ingresada ",PATS[0][i]," ya tiene una tara registrada: ",CAMS[2][i])
                    print()
                    input("Presione la tecla ENTER para volver a intentar: ")
                else: 
                    if CAMS[1][i] == 0:
                        os.system('cls')
                        print("La patente ingresada ",PATS[0][i]," no tiene un peso bruto registrado. Para registrar el peso bruto dirijase a la opción: 5-Registrar peso bruto")
                        print()
                        input("Presione la tecla ENTER para volver a intentar: ")
                    else:
                        if PATS[2][i] != "E": 
                            os.system('cls')
                            print("La patente ingresada",PATS[0][i]," no se encuentra en estado: En Proceso-E. Para adquirir dicho estado dirijase a la opción: 3-Recepción")
                            print()
                            input("Presione la tecla ENTER para volver a intentar: ")
                        else:
                            os.system('cls')
                            print("Recuerde ingresar la tara (peso del camion descargado) en Toneladas-TN.")
                            print()
                            print("La tara maxima admitida es de 25 TN (Promedio aproximado de diferentes tipos de camion ) y la minima de 13 TN")
                            print()
                            tara = int(input("Ingrese la tara del camion con patente "+PATS[0][i]+" el cual transporta "+PATS[1][i]+": "))
                            while tara < taramin or tara > taramax:
                                if tara < taramin:
                                    os.system('cls')
                                    print("La tara ingresada ",tara," es menor que lo habilitado. Recuerde que la tara minima habilitada es de 13 TN")
                                    print()
                                    input("Presione la tecla ENTER para volver a intentar: ")
                                else:
                                    os.system('cls')
                                    print("La tara ingresada ",tara," es mayor que lo habilitado. Recuerde que la tara máxima habilitada es de 25 TN")
                                    print() 
                                    input("Presione la tecla ENTER para volver a intentar: ")
                                os.system('cls')
                                print("La tara maxima admitida es de 25 TN (Promedio aproximado de diferentes tipos de camion ) y la minima de 13 TN")
                                print()
                                tara = int(input("Ingrese la tara del camion con patente "+PATS[0][i]+" el cual transporta "+PATS[1][i]+": "))
                            CAMS[2][i] = tara
                            PATS[2][i] = "C"
                            neto = CAMS[1][i] - CAMS[2][i]
                            CAMS[3][i] = neto
                            k = 0
                            while PATS[1][i] != HAB[k]:
                                k = k + 1
                            if HAB[k] == PATS[1][i]:
                                CONTPRODS[1][k] = CONTPRODS[1][k] + neto 
                            buscarmayor(i,neto)
                            buscarmenor(i,neto) 
                            os.system('cls')
                            print("Tara ingresada exitosamente!")
                            print()
                            print("Camion con patente: ",PATS[0][i]," Tara: ",CAMS[2][i],"TN")
                            print()
                            input("Presione la tecla ENTER para continuar: ")
            os.system('cls')
            print("Opción elegida: Registrar tara")
            print()
            mostrarlistado()
            patente = str(input("Ingrese la patente de uno de los caminones del listado o ingrese un * para volver al menu anterior. Para continuar presione la telca ENTER: "))
            patente = patente.upper()
            ver1 = patente[0:3].isalpha() and patente[4:6].isdigit()
            ver2 = patente[0:2].isalpha() and patente[3:5].isdigit() and patente[6:7].isalpha()
                
def menadministracion():
    os.system('cls')
    print("----------------------------------------")
    print("Opción seleccionada: Administración.")
    print()
    print("A-Titulares")
    print("B-Productos")
    print("C-Rubros")
    print("D-Rubros por producto")
    print("E-Silos")
    print("F-Sucursales")
    print("G-Producto por sucursales")
    print("V-Volver al menu principal")
    print("----------------------------------------")

def administraciones():
    global elec2
    os.system('cls')
    menadministracion()
    elec2 = str(input("Ingrese una de las opciones con el teclado y presione la tecla ENTER: "))
    elec2 = elec2.upper()
    while elec2 != "V":
        busquedaelec(elec2,OPS2,6)
        if verif > 0:
            if elec2 == "A":
                os.system('cls')
                print("Esta funcionalidad esta en construcción.\n")
                input("Presione la tecla ENTER para continuar: ")
            elif elec2 == "B":
                terciaro()
            elif elec2 == "C":
                terciaro()
            elif elec2 == "D":
                terciaro()
            elif elec2 == "E":
                terciaro()
            elif elec2 == "F":
                os.system('cls')
                print("Esta funcionalidad esta en construcción.\n")
                input("Presione la tecla ENTER para continuar: ")
            elif elec2 == "G":
                os.system('cls')
                print("Esta funcionalidad esta en construcción.\n")
                input("Presione la tecla ENTER para continuar: ")
            menadministracion()
            elec2 = str(input("Ingrese una de las opciones con el teclado y presione la tecla ENTER: "))
            elec2 = elec2.upper()
        else:
            print()
            elec2 = str(input("Opción invalida. Ingrese una de las opciones con el teclado y presione la tecla ENTER: "))
            elec2 = elec2.upper()
        
def busquedaelec(elec,OPS,tam):
    global verif
    i = 0
    while OPS[i] != elec and i < tam:
        i = i + 1
    if OPS [i] == elec:
        verif = 1
        return(verif)
    else:
        verif = 0
        return(verif)

def menterciario():
    os.system('cls')
    print("---------------------------------")
    print("Opcion seleccionada: ",elec2)
    print()
    print("A-Alta")
    print("B-Baja")
    print("C-Consulta")
    print("M-Modificación")
    print("V-Volver al menu anterior")
    print("---------------------------------")

def terciaro():
    global elec3
    menterciario()
    elec3 = str(input("Ingrese una de las opciones con el teclado y presione la tecla ENTER: "))
    elec3 = elec3.upper()
    while elec3 != "V":
        busquedaelec(elec3,OPS3,3)
        if verif > 0:
            if elec3 == "A":
                if elec2 == "B":
                    altaprod()

                else: 
                    enconst()
            elif elec3 == "B":
                if elec2 == "B":
                    bajaprod()
                else:
                    enconst()
            elif elec3 == "C":
                if elec2 == "B":
                    consprod()
                else:
                    enconst()
            elif elec3 == "M":
                if elec2 == "B":
                    modifprod()
                else:
                    enconst()
            menterciario()
            elec3 = str(input("Ingrese una de las opciones con el teclado y presione la tecla ENTER: "))
            elec3 = elec3.upper() 
        else:
            print()
            elec3 = str(input("Opcion invalida. Ingrese una opción o V para volver al menu anterior: "))
            elec3 = elec3.upper()

def enconst():
    os.system('cls')
    print("Esta funcionalidad esta en construcción.")
    print()
    input("Presione la tecla ENTER para volver al menu: ")

def buscarcod(cod,AL):
    t = os.path.getsize(AFP)
    AL.seek(0)
    while AL.tell() < t:
        pos = AL.tell()
        temp = pickle.load(AL)
        if temp.cod == cod:
            print(pos)
            input("ENTER")
            return pos
            
    return -1 
    
def buscarnomb(nomb,AL):
    
    t = os.path.getsize(AFP)
    AL.seek(0)
    while AL.tell() < t:
        pos = AL.tell()
        temp = pickle.load(AL)
        if temp.nomb == nomb:
            print(pos)
            input("ENTER")
            return pos
    return -1

AFP = "C:\\Users\\Andres\\OneDrive\\Escritorio\\AyED\\AYEDTP3\\Archivos\\PRODUCTOS.dat"

def altaprod():
    if not os.path.exists(AFP):
        ALP = open(AFP,"w+b")
    else:
        ALP = open(AFP,"r+b")
    prod = productos()
    os.system('cls')
    print("Opción seleccionada: Alta\n")
    print("Aquí podrá registrar el nombre de los productos con los cuales se trabajará y sus codigos.\n")
    codprod = int(input("Ingrese el codigo del producto a ingresar o un 0 para terminar. Se permitira digitar un codigo de 3 digitos desde el 001 al 999: "))
    while codprod != 0:
        while validarsientero(codprod,1,999):
            os.system('cls')
            codprod = input("Por favor ingrese un codigo dentro del rango valido (001 al 999): ")
        codprod = int(codprod)
        if buscarcod(codprod,ALP) == -1:
            os.system('cls')
            ingprod = input("Ingrese el nombre del producto a registrar o ingrese un * para volver al menu anterior. Luego de ingresar los datos presione la tecla ENTER para continuar: ")
            ingprod = ingprod.upper()
            i = 0
            if buscarnomb(ingprod,ALP) == -1:
                while HAB[i] != ingprod and i < 4:
                    i = i + 1
                if HAB[i] == ingprod:
                    prod.cod = codprod
                    prod.nomb = ingprod
                    pickle.dump(prod,ALP)
                    ALP.flush()
                    os.system('cls')
                    print("Datos ingresados exitosamente!\n")
                    input("Presione la tecla ENTER para continuar: ")
                else:
                    os.system('cls')
                    print("El producto ingresado no es valido.\n")
                    for i in range(5):
                        print(HAB[i],"\n")
                    input("Presione la tecla ENTER para continuar: ")
            else:
                os.system('cls')
                print("Este producto ya ah sido ingresado: ",ingprod)
                print()
                input("Presione la tecla ENTER para continuar: ")
        else:
            os.system('cls')
            print("Ya existe un producto con ese codigo: ",codprod)
            print()
            input("Presione la tecla ENTER para continuar: ")
        os.system('cls')
        print("Opción seleccionada: Alta\n")
        print("Aquí podrá registrar el nombre de los productos con los cuales se trabajará y sus codigos.\n")
        codprod = int(input("Ingrese el codigo del producto a ingresar o un 0 para terminar. Se permitira digitar un codigo de 3 digitos desde el 001 al 999: "))
    ALP.close()
        
    

def bajaprod():
    if not os.path.exists(AFP):
        ALP = open(AFP,"w+b")
    else:
        ALP = open(AFP,"r+b")
    t = os.path.getsize(AFP)
    if t == 0:
        os.system('cls')
        print("No hay se han ingresado productos todavía. Por lo tanto no hay productos para dar de baja.\n")
        print("Presione la tecla ENTER para volver al menu anterior: ")
    else:
        os.system('cls')
        print("Opción seleccionada: Baja")
        print()
        print("Aquí se le dara la posibilidad de eliminar elementos del listado activo de productos.")
        print()

    

def consprod():
    os.system('cls')
    print("Opción elegida: Consulta")
    print()
    if contprod == 0:
        print("No hay productos en el listado activo. Para ingresarlos dirijase a la opción: A-Alta")
        print()
        input("Presione la tecla ENTER para continuar: ")
    else:
        print("A continuación el listado activo de productos!")
        listadoproductos()    
        input("Presione la tecla ENTER para volver al menu anterior: ")

def modifprod():
    os.system('cls')
    print("Opción elegida: Modificación")
    print()
    if contprod == 0:
        print("No hay productos en el listado activo. Para ingresarlos dirijase a la opción: A-Alta")
        print()
        input("Presione la tecla ENTER para continuar al menu anterior: ")
    else: 
        print("A continuación podrá modificar el nombre de los productos del listado. Solo se permitira cambiar los nombres de los productos en el listado activo a otros que esten habilitados. No se permitira que se repitan productos.")
        print()
        print("Listado de productos validos: ",end="")
        for i in range(5):
            print(HAB[i],end=".")
        print()
        listadoproductos()
        mod = str(input("Ingrese cual de los productos del listado quiere modificar o ingrese un * para volver al menu anterior. Para continuar presione la tecla ENTER: "))
        mod = mod.upper()
        while mod != "*":
            i = 0
            while mod != PRODS[i] and i < 2:
                i = i + 1
            if mod != PRODS[i]:
                os.system('cls')
                print("El producto ingresado ", mod," no se encuentra dentro del listado activo de productos.")
                listadoproductos()
                input("Presione la tecla ENTER para continuar: ")
            else:
                print()
                print("Producto elegido: ",mod)
                print()
                mod = str(input("Ingrese nuevo nombre del producto: " ))
                mod = mod.upper()
                k = 0
                while mod != PRODS[k] and k < 2:
                    k = k + 1
                if mod == PRODS[k]:
                    os.system('cls')
                    print("La modificación no se puede realizar ya que el producto ",mod," ya existe dentro del listado. Recuerde que no se admite repetición de productos dentro del listado activo.")
                    print()
                    input("Presione la tecla ENTER para volver a intentar: ")
                else:
                    k = 0
                    while mod != HAB[k] and k < 4:
                        k = k + 1
                    if mod != HAB[k]:
                        os.system('cls')
                        print("No se puede realizar la modificación ya que el producto ingresado ",mod, " no corresponde al listado de productos habilitados o esta mal escrito.")
                        print()
                        print("Listado de productos validos: ",end="")
                        for i in range(5):
                            print(HAB[i],end=".")
                        print()
                        print()
                        input("Presione la tecla ENTER para volver a intentar: ")
                    else:
                        os.system('cls')
                        PRODS[i] = mod
                        print("Modificación exitosa!")
                        listadoproductos()
                        input("Presione la tecla ENTER para continuar: ")
            os.system('cls')
            print("Listado de productos validos: ",end="")
            for i in range(5):
                print(HAB[i],end=".")
            print()
            listadoproductos()
            mod = str(input("Ingrese cual de los productos del listado quiere modificar o ingrese un * para volver al menu anterior. Presione la tecla ENTER continuar: "))
            mod = mod.upper()        
              
def reportes():
    os.system('cls')
    print("A continuación un reporte de los datos ingresados hasta ahora: ")
    print()
    if c == 0:
        print("Todavia no hay patentes dentro del listado. Por lo tanto no hay datos para reportar. Para ingresar patentes dirijase a la opción: 2-Entrega de cupos")
        print()
        input("Presione la tecla ENTER para continuar al menu anterior: ")
    else:
        print("-----------------------------------------------------------------------------------")
        print("Cantidad de cupos otorgados: ",c)
        print("-----------------------------------------------------------------------------------")
        print()
        if recibidos == 0:
            print("Todavia no hay camiones que hallan pasado por recepción. Para procesarlos dirijase a la opción: 3-Recepción")
            print()
            input("Presione la tecla ENTER para continuar: ")
        else:
            print("-----------------------------------------------------------------------------------")
            print("Cantidad total de camiones recibidos: ",recibidos)
            print("-----------------------------------------------------------------------------------")
            print()
            if contprod == 0:
                print("Todavía no se han ingresado productos al listado activo. Para ingresarlos dirijase a la opción: 1-Administración -> B-Productos -> A-Alta")
                print()
                input("Presione la tecla ENTER para continuar: ")
            else:
                print("-----------------------------------------------------------------------------------")
                print("Cantidad total de camiones de cada producto: ")
                print("-----------------------------------------------------------------------------------")
                print()
                for i in range (5):
                    if  CONTPRODS[0][i] == 0:
                        print("No hay ingreso de camiones transportando ",HAB[i]," registrado.")
                    else:
                        print(HAB[i],": ",CONTPRODS[0][i])
                print()
                print("-----------------------------------------------------------------------------------")
                print("Peso neto total de cada producto: ")
                print("-----------------------------------------------------------------------------------")
                print()
                for i in range (5):
                    if  CONTPRODS[1][i] == 0:
                        print("No hay ingreso de camiones transportando ",HAB[i]," registrado.")
                    else:
                        print(HAB[i],": ",CONTPRODS[1][i])
                print()
                print("-----------------------------------------------------------------------------------")
                print("Promedio del peso neto de producto por camión de ese producto: ")
                print("-----------------------------------------------------------------------------------")
                print()
                for i in range (5):
                    if  CONTPRODS[0][i] == 0 or CONTPRODS[1][i] == 0:
                        print("No hay ingreso de camiones transportando ",HAB[i]," registrado.")
                    else:
                        print(HAB[i],": ",CONTPRODS[1][i]/CONTPRODS[0][i])
                print()
                print("-----------------------------------------------------------------------------------")
                print("Patente del camión de cada producto que mayor cantidad de dicho producto descargó: ")
                print("-----------------------------------------------------------------------------------")
                for i in range (5):
                    if  CONTPRODS[0][i] == 0 or CONTPRODS[1][i] == 0:
                        print("No hay ingreso de camiones transportando ",HAB[i]," registrado.")
                    else:
                        print(HAB[i],": ","Patente: ",HABMXMN[0][i]," Cantidad: ",CONTPRODS[2][i],"TN")
                print()
                print("-----------------------------------------------------------------------------------")
                print("Patente del camión de cada producto que menor cantidad de dicho producto descargó: ")
                print("-----------------------------------------------------------------------------------")
                for i in range (5):
                    if  CONTPRODS[0][i] == 0 or CONTPRODS[1][i] == 0:
                        print("No hay ingreso de camiones transportando ",HAB[i]," registrado.")
                    else:
                        print(HAB[i],": ","Patente: ",HABMXMN[1][i]," Cantidad: ",CONTPRODS[3][i],"TN")
                print()
                print("-----------------------------------------------------------------------------------")
                print("Listado descendiente de cantidades de peso neto descargado: ")
                print("-----------------------------------------------------------------------------------")
                ordenamiento()
                for i in range(8):
                    if PATS[0][i] != "" and PATS[1][i] != "" and CAMS[3][i] != 0:
                        print("Patente: ",PATS[0][i],"Producto: ",PATS[1][i],"Peso neto: ",CAMS[3][i])
                print()
                input("Presione la tecla ENTER para volver al menu anterior: ")

def buscarmayor(i,neto):
    k = 0
    while PATS[1][i] != HAB[k] and k < 4:
        k = k + 1
    if PATS[1][i] == HAB[k]:
        if CONTPRODS[2][k] < neto:
            CONTPRODS[2][k] = neto
            HABMXMN[0][k] = PATS[0][i]

def buscarmenor(i,neto):
    k = 0
    while PATS[1][i]!= HAB[k] and k < 4:
        k = k + 1
    if PATS[1][i] == HAB[k]:
        if CONTPRODS[3][k] > neto:
            CONTPRODS[3][k] = neto
            HABMXMN[1][k] = PATS[0][i]
    
def ordenamiento():
    for i in range(7):
        for k in range(i+1,8):
            if CAMS[3][i] < CAMS[3][k]:
                for r in range (3):
                    aux = PATS[r][i]
                    PATS[r][i] = PATS[r][k]
                    PATS[r][k] = aux
                    aux = CAMS[r][i]
                    CAMS[r][i] = CAMS[r][k]
                    CAMS[r][k] = aux
                aux = CAMS[3][i]
                CAMS[3][i] = CAMS[3][k]
                CAMS[3][k] = aux

menu()
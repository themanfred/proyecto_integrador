import random
from unidecode import unidecode #convierte stirngs en flotante
from fractions import Fraction #convierte fracciones en decimales

Puntos_Jugador1 = 0
Puntos_Jugador2 = 0
columnas = 0
filas = 0
tablero = []
orientacion_cartas=[]
jugador_turno = 1
par = False

def fila_string(fila):
  return str(fila).strip(']').strip('[').replace(' ','')


def GuardaArchivo(matriz, orientacion, nombre):
  print('\nGuardando en archivo\n')
  global filas, columnas
    
  # ... abre el archivo ...
  f = open("archivo"+nombre+".txt", 'w')
  f.write(str(filas))
  f.write('\n')
  # ... ciclo que guarda la matriz fila por fila ...
  for fila in matriz:
    # ... manda a llamar a fila_string para quitar los corchetes ...
    f.write(fila_string(fila)+'\n')
  for fila in orientacion_cartas:
    # ... manda a llamar a fila_string para quitar los corchetes ...
    f.write(fila_string(fila)+'\n')
  
  f.close()
    
  #print('\nArchivo guardado con éxito\n')
  #print('Hasta luego')

# ... Función que lee archivo ...
def LeeArchivo(f,tablero,orientacion):
    global Puntos_Jugador2, Puntos_Jugador1, jugador_turno
    matriz = []
    print('Leyendo contenido de archivo ...\n')
    
    # ... abre el archivo ...
    file = open(f, 'r')
    """
    Asigna el contenido del archivo.
    Lo que hace es leer la línea y elemento por elemento convirtiéndolo
    en número y separándole las comas.
    Se hace esto ya que cuando se guarda un valor en un archivo de texto, se
    guarda como texto, y como texto no permite agregarle valores a la matriz.
    """
    #matriz = [[num.strip('\n').strip('\'') for num in line.split(',')] for line in file]
    size=0
    numlinea=0 #contador de lineas
    tablero=[]
    orientacion=[]
    p1=0
    p2=0
    for line in file:
      linea=[]
      for num in line.split(','):
        num = num.strip('\n').strip('\'')
        if num == 'False':
          num = False
        elif num == 'True':
          num = True
        linea.append(num)
      if(numlinea==0):
        size=int(linea[0])
      if(numlinea>0 and numlinea<=size):
        tablero.append(linea)
      if(numlinea>size and numlinea <=size*2):
        orientacion.append(linea)
      if(numlinea==size*2+1):
        Puntos_Jugador1=int(linea)
      if(numlinea==size*2+2):
        Puntos_Jugador2=int(linea)
      numlinea+=1
      
    return tablero, orientacion
      
    
    '''
     size=int(matriz[0][0])
    nueva_matriz=[]
    for i in range(1,size+1):
      for j in range(size):
        nueva_matriz[i][j]=matriz[i][j]

    '''
    
    # ... cierra archivo ...
    file.close()
    


def generador_Fraccion(): 

  #Asigna una fraccion y que lo pueda imprimir como fraccion (n/t)
  #Asignalo de manara random como elemento con valor falso
  #Si el lugar asignado ya esta ocupado vuelva a hacerlo hasta que
  #encuentras un lugar desocupado

  '''
  esa misma fraccion multiplicalo por la dividsion equivalante a uno 
  que al final sea igual a la fraccion origial

  Asigna ese elemento a otro 'casillero' y usar una variable
  para contar la cantidad de pares que hay 

  Los pares siempre son positivos

  Repito el metodo de asignacion de la primera fraccion
  '''

  numerador=random.randint(1,10) #Generación números aleatorios para el numerador y denominador.
  denominador=random.randint(1,10) #Generación de números aletorios

  multiplicacion=random.randint(2,8) #Busca un número aleatorio para multiplicar la fraccion a una equivalencia

  fraccion=str(numerador)+'/'+str(denominador) #Convierte los numeros generadores en string
  equivalente=str(numerador*multiplicacion)+'/'+str(denominador*multiplicacion)#Convierte los numeros generadores en string 

  return fraccion,equivalente


def TurnoJugador():
  '''
  El programa debe controlar que
  le toque el turno a cada uno de los 2 jugadores
  de manera alternada, a menos de que un jugador
  encuentre un par correcto,
  en cuyo caso se mostrará un
  mensaje felicitando al jugador
  y el turno le seguirá tocando al mismo jugador.
  '''

  global jugador_turno, par,Puntos_Jugador1,Puntos_Jugador2, mul #Toma las variables globales
  
  if jugador_turno == 1: #si es el turno del jugado 1
    if par == True: # Y tuvo un pa
      #a quién le toca el siguiente turno.
      #mostrará un mensaje felicitando al jugador
      print("Es un par, ¡felicitaciones!!\nSigue siendo el turno del jugador 1")
      jugador_turno =1 #sigue siendo su turno
      Puntos_Jugador1 +=1 #y el jugador gana un punto
    else:
      #a quién le toca el siguiente turno.
      print("No hubo par, es el turno del jugador 2")
      jugador_turno =2 #si no es el turno del jugador 2

  elif jugador_turno == 2:#si es el turno del jugado 2
    if par == True: # Y tuvo un par
      #a quién le toca el siguiente turno.
      #mostrará un mensaje felicitando al jugador
      print("Es un par, ¡felicitaciones!!\nSigue siendo el turno del jugador 2")
      jugador_turno =2 #sigue siendo su turno
      Puntos_Jugador2 +=1 #y el jugador gana un punto
    else:
      #a quién le toca el siguiente turno.
      print("No hubo par, es el turno del jugador 1")
      jugador_turno =1 #si no es el turno del jugador 1

  ganador()  
  return jugador_turno, Puntos_Jugador1,Puntos_Jugador2
  
      

def parametrosjuego():  #Funcion que valida que el minimo de filas y columnas sea 8 y agrega los valores a la matriz
    global mul
    print(f'Digite el numero de filas y columnas del juego:')

    while True:
        '''
        Es necesario que se validen las reglas del juego. El programa deberá validar
        todos los datos que pida al usuario; es decir:
        i)  Que el número de renglón y columna de la posición a abrir exista. 
        '''

        global filas, columnas

        #asegurarme que no pasa nada si pongo un numero y que me pida denuevo
        while True:
          try:#Solo aceptar valores si son enteros
            filas = int(input("Digita la dimension de filas (min. 8): "))       
          except ValueError: #En caso de que digite cualquier otra cosa
            print("Minimo 8 filas")
            continue
          else:
            break 
        #asegurarme que no pasa nada si pongo un numero y que me pida denuevo
        
        while True:
          try:#Solo aceptar valores si son enteros
            columnas = int(input("Digita la dimension de columnas (min. 8): "))       
          except ValueError: #En caso de que digite cualquier otra cosa
            print("Minimo 8 columnas")
            continue
          else:
            break 
       
        #digita el numero de columnas
        mul = filas*columnas
        
        if mul % 2 == 0:
          if filas >= 2 and columnas >= 2:  #Si el numbero de filas y columnas es mayor a 8 rompe este ciclo
              break

          else:
              print("Rango no valido (min. 8)")#en caso que filas y/o colmnas es menor a 8
              
        else:
          print("El tablero no puede ser impar")
  
    
    lista_fracciones=[] 

    for i in range(int(mul/2)):#For que agrega los valores generados de fracciones a una lista

      fraccion,fraccion_equivalente=generador_Fraccion()

      lista_fracciones.append(fraccion)
      lista_fracciones.append(fraccion_equivalente)
    
    random.shuffle(lista_fracciones)

    '''
    Los datos del tablero deberán representarse mediante dos matrices,
    una para guardar los valores de las cartas y la otra para guardar valores que indiquen
    si la carta de esa posición está tapada o destapada.
    '''

    indice=0
    for i in range(filas): 
        renglon = []
        renglon2 = []
        
        for j in range(columnas):
            renglon.append(lista_fracciones[indice])
            indice+=1
   
            renglon2.append(False)#False Boca abajo
            
        orientacion_cartas.append(renglon2)
        tablero.append(renglon) 
    


def imprimir_tablero():  #Funcion que crea la matriz
  #Al mostrar la tabla, utilice formatos de manera que todos los números se muestren
  #con la misma cantidad de espacios y se vean alineados
    GuardaArchivo(tablero, orientacion_cartas, "partida") #prubea 
    for x in range(columnas):
        print("\t\t" + str(x), end=" ") #imprimir el numero de la columna
    print()

    for i in range(filas):
        print(str(i), end=" ") #imprimir numero de la fila

        for j in range(columnas):

            if orientacion_cartas[i][j] == False: #imprimir tablero
                print("\t\t*", end=" ")

            else:
                print(f"\t\t{tablero[i][j]}", end=" ")

        print()

    print("\nJugador 1:", Puntos_Jugador1, end="\t\t\t")
    print("Jugador 2:", Puntos_Jugador2)
    print("\nTurno: Jugador", jugador_turno)



def cartasEquivalentes(x1,x2,y1,y2): 

  ''' 
  Si las cartas de esas casillas están correctas porque están asociadas de alguna forma,
  se deben quedar a la vista, si no, se deben volver a “tapar” ambas
  casillas mostrando de nuevo el * (o la figura que se haya decidido). Además, se debe mostrar
  el puntaje de cada jugador y a quién le toca el siguiente turno.
  
  '''

  global par

  stingNum1=unidecode(tablero[x1][y1]).split()#convertir usando la libereia unicode y en split en una lista
  stringNum2=unidecode(tablero[x2][y2]).split()#convertir usando la libereia unicode y en split en una lista
  floatNum1 = float(Fraction(stingNum1[0]))#usar libreria fraccion y hacer que sea un float
  floatNum2= (float(Fraction(stringNum2[0])))#usar libreria fraccion y hacer que sea un float

  if  floatNum1 == floatNum2:
    
    #tener a las cartas abiertas y hacer que el jugador que hizo el print
    par = True
    TurnoJugador()

  else:

      #Las cartas nos son igulas
      orientacion_cartas[x1][y1] = False #dar la vuelta de regreso
      orientacion_cartas[x2][y2] = False# dar la vuelta de regreso
      #imprimir_tablero() #mostrar el tablero 
      #mostrar que es el turno del proximo jugador
      par = False
      TurnoJugador()



def voltear_cartas():  #Funcion que se encarga de cambiar los valores "voltear cartas", dentro de la matriz
    # Reglas del juego: 
    #Que no se pida destapar la misma casilla en el mismo turno.
    #Que no se pida destapar una casilla ya destapada.

    counterDeCartas=0 #cuenta cuantas carta se han dado la vuelta

    while True:

        print("\nPrimera Carta")
        x1 = 0
        
        while True:
          try:#Solo aceptar valores si son enteros
            x1 = int(input("Fila primera carta: "))       
          except ValueError: #En caso de que digite cualquier otra cosa
            print("Digita un numero en el rango valido")            
            continue
          else:
            break 
       
        while True:
            try:#Solo aceptar valores si son enteros
              y1 = int(input("Columna primera carta: "))       
            except ValueError: #En caso de que digite cualquier otra cosa
              print("Digita un numero en el rango valido")            
              continue
            else:
              break 

        #asegurarme que no pasa nada si pongo un numero y que me pida denuevo
        if x1 >= 0 and x1 < filas and y1 >= 0 and y1 < columnas: 
          if orientacion_cartas[x1][y1] == False:  
          
              orientacion_cartas[x1][y1] = True
              counterDeCartas+=1 #ya se decubrio una carta
              break
          else:
              print("Carta ya volteada")
              continue
        else:
          print("\nRango Invalido")
          continue

    imprimir_tablero()

    while True:

        print("Segunda Carta")
        while True:
          try:#Solo aceptar valores si son enteros
            x2 = int(input("Fila segunda carta: "))       
          except ValueError:#En caso de que digite cualquier otra cosa
            print("Digita un numero en el rango valido")            
            continue
          else:
            break 

        while True:
          try:#Solo aceptar valores si son enteros
            y2 = int(input("Columna segunda carta: "))       
          except ValueError:#En caso de que digite cualquier otra cosa
            print("Digita un numero en el rango valido")            
            continue
          else:
            break 
        #asegurarme que no pasa nada si pongo un numero y que me pida denuevo
        
        if x2 >= 0 and x2 < filas and y2 >= 0 and y2 < columnas :

          if orientacion_cartas[x2][y2] == False:

              orientacion_cartas[x2][y2] = True
              counterDeCartas+=1# y ahora la segunda carta tambien haciendo un par
              break

          else:
              print("\nCarta ya volteada")
              continue

        else:
          print("Rango invalido")
          continue
          
    imprimir_tablero()        
    if counterDeCartas == 2:
      cartasEquivalentes(x1,x2,y1,y2)
      #llamar una funcion que me va determinar si las dos cartas son iguales open y de esa funcion se va a determinar si el jugador sigue jugando en caso de que es par o es el turno del otro
      #En caso que no es igual se va a repetir esta eccion para darle la vuelta a las cartas
     
  

def ganador():  #Función que valida ganador e imprime mensaje de felicitaciones
  '''
  Debe mostrar un mensaje que indique que ya se terminó el juego, 
  , un mensaje indicando los puntos
  obtenidos por cada jugado
  '''

  global mul, Puntos_Jugador1,Puntos_Jugador2

  if Puntos_Jugador1 == Puntos_Jugador2 and (mul/2)==(Puntos_Jugador1 + Puntos_Jugador2):
      print('¡Termino el Juego es un empate!')
      #un mensaje indicando los puntos obtenidos por cada jugador
      print(f'El jugador 1 y 2  tuvieron {Puntos_Jugador1} puntos')
      print("EMPATE")
  elif (mul/2)==(Puntos_Jugador1 + Puntos_Jugador2) and Puntos_Jugador1> Puntos_Jugador2:
        
      print(f'''
          __^__                                      __^__
         ( ___ )------------------------------------( ___ )
          | / |                                      | \ |
          | / |        Felicidades Jugador 1         | \ |
          |___|                                      |___|
         (_____)------------------------------------(_____)

    ''')
     #un mensaje indicando los puntos obtenidos por cada jugador
      print(f'El jugador 1 tuvo {Puntos_Jugador1} puntos\nel jugador 2 tuvo {Puntos_Jugador2} puntos')

  elif (mul/2)==(Puntos_Jugador1 + Puntos_Jugador2) and Puntos_Jugador2> Puntos_Jugador1:
      print(f'''
          __^__                                      __^__
         ( ___ )------------------------------------( ___ )
          | / |                                      | \ |
          | / |        Felicidades Jugador 2         | \ |
          |___|                                      |___|
         (_____)------------------------------------(_____)

    ''')
    #un mensaje indicando los puntos obtenidos por cada jugador
      print(f'El jugador 2 tuvo {Puntos_Jugador2} puntos\nel jugador 1 tuvo {Puntos_Jugador1} puntos')


def guardar_partida(): #Función que va a guardar la partida en un archivo
  pass


'''
El programa debe de tener un menú para seleccionar si se desea iniciar el juego,
si se desea continuar con un juego anterior o si se desea terminar.
El menú debe de mostrarse al inicio y al terminar cada juego, hasta que se desee terminar.
'''
n = 0
while n != 3:
    print('''
                    MENU
    1)Empezar partida
    2)Continuar una partida guardada
    3)Salir

    ''')
    
    while True:
      try:#Solo aceptar valores si son enteros
        n = int(input("Digita la opcion: "))       
      except ValueError:#En caso de que digite cualquier otra cosa
        print("Digita un numero entero")
        continue
      else:
        break 

    if n == 1:
        resp = ''
        pregunta=''
        parametrosjuego()

        while resp != 'fin':  #Ciclo donde se une el tablero con el voltear cartas, permite jugar mientras no se escriba fin al termino de un turno

            imprimir_tablero()

            voltear_cartas()
            
            resp = input('¿Desea seguir jugando? (Escriba fin para terminar el juego? ')
        if resp == 'fin':
           pregunta = input('¿Desea guardar partida? ')
           if pregunta == 'si': #solo si la respuesta es si se guarda
            GuardaArchivo(tablero, orientacion_cartas, 'partida')


    elif n == 2:
        resp = ''
        if tablero ==[]:
          n=1
        else:
          tablero, orientacion_cartas=LeeArchivo('archivopartida.txt',tablero,orientacion_cartas)
          while resp != 'fin':  #Ciclo donde se une el tablero con el voltear cartas, permite jugar mientras no se escriba fin al termino de un turno

              imprimir_tablero()

              voltear_cartas()
              
              resp = input('¿Desea seguir jugando? (Escriba fin para terminar el juego? ')
              
          if resp == 'fin':
            pregunta = input('¿Desea guardar partida? ')
            if pregunta == 'si':
              GuardaArchivo(tablero, orientacion_cartas, 'partida')
          #GuardaArchivo(tablero,orientacion_cartas,'guardado')
    elif n == 3:
        print('''Hasta luego
             A____A
            |・ㅅ・|
            |っ　ｃ|
            |　　　|
            |　　　|
            |　　　|
            |　　　|
            |　　　|
             U￣￣U
        ''')
    else:
      print('Digite una opcion valida')
'''
-------------------------------------
Tarea 2
-------------------------------------
Jose Guillermo Perez Arana  201700388
-------------------------------------

'''
#Clase para representar la matriz
class matriz(object):
    #Constructor
    def __init__(self, mat = []):
        self.mat = mat
        if self.verificacion(): #primero verificamos si se ingreso correctamente
            pass
        else:                   #sino se levanta un error
            raise ErrorDeIngreso   

    #Funcion 'len' para el objeto matriz
    def __len__(self):
        return len(self.mat)
    
    #operacion de suma para el objeto matriz
    def __add__(self, sumando):
        if (self.equalFilas(sumando) and self.equalColumnas(sumando)):#Primero comprobamos las dimensiones
            x = []                                                    #de las matrices
            for i in range(len(self.mat)):                          
                y=[]                                                #creamos una lista para las filas de la matriz
                for j in range(len(self.mat[i])):                   #y se suma cada elemento correspondiente
                    y.append(self.mat[i][j] + sumando.mat[i][j])
                x.append(y)                                         #agregamos las filas a la matriz
            return matriz(x)
        else:                               #si la cantidad de columnas o filas no coincide
            raise ErrorDimensionalSumRes          #se levanta un error de dimensiones

    #operacion de resta para el objeto matriz        
    def __sub__(self, sumando):
        if (self.equalFilas(sumando) and self.equalColumnas(sumando)):#Primero comprobamos las dimensiones
            x = []                                                    #de las matrices
            for i in range(len(self.mat)):
                y=[]                                                #creamos una lista para las filas de la matriz
                for j in range(len(self.mat[i])):                   #y se resta cada elemento correspondiente
                    y.append(self.mat[i][j] - sumando.mat[i][j])
                x.append(y)                                         #agregamos las filas a la matriz
            return matriz(x)
        else:                               #si la cantidad de columnas o filas no coincide
            raise ErrorDimensionalSumRes          #se levanta un error de dimensiones    

    #operacion de multiplicacion para el objeto matriz
    def __mul__(self, MatrizoEscalar):
        if (type(MatrizoEscalar) == int or type(MatrizoEscalar) == float):
            x = []                                              #Comprobamos si es multiplicacion por un escalar
            for i in range(len(self.mat)):                      #o por otra matriz. Si es escalar se multiplica
                y=[]                                            #cada elemento por el numero
                for j in range(len(self.mat[i])):
                    y.append(self.mat[i][j] * MatrizoEscalar)
                x.append(y)  
            return matriz(x)

        elif (type(MatrizoEscalar) == matriz):              #Si es matriz por matriz primero verificamos que las
            if (self.equalFilasxColumnas(MatrizoEscalar)):  #las dimensiones son correctas
                x = []                                         
                for i in range(len(self.mat)):
                    y =[]
                    for j in range(len(MatrizoEscalar.mat[0])):
                        val = 0
                        for k in range(len(self.mat[0])):
                            val += self.mat[i][k] * MatrizoEscalar.mat[k][j]#multiplicamos fila por columna        
                        y.append(val)                                       #sucesivamente y vamos guardando
                    x.append(y)                                             #en otra matriz
                return matriz(x)    
            else:                               #si la cantidad de columnas o filas no coincide
                raise ErrorDimensionalMul          #se levanta un error de dimensiones 
    '''
    def determinante(self, matcopia=[]):
        if (self.matCuadrada(self)):
            # Copia CORRECTA de la matriz A en la de B.
            matcopia = [k[:] for k in self.mat]
            n = len(self.mat)
            suma = 0
            if n > 2: # Si el rango es mayor que 2
                for i in range(len(self.mat)):
                    factor = matcopia[0][i] # saca el factor de la primera fila i
                    signo = -2 * (i % 2) + 1 # calcula su signo
                    #print (signo)
                    matcopia.remove(matcopia[0]) # Borra la primera fila
                    for j in range(0,n-1):
                        # B[j].remove(B[j][i]). NO SE PUEDE PONER REMOVE porque lo que quita es el elemento de la primera posición
                        matcopia[j].pop(i) # Quita, de cada fila de B, el factor i, o sea, quita esa columna.
                    suma = suma + factor * signo * self.determinante(matcopia) # El determinante es la suma anterior más lo que calcule
                    matcopia = [k[:] for k in self.mat] # reconstruye la matriz B
                return suma # retorna la suma
            else:
                return (matcopia[0][0] * matcopia[1][1]) - (matcopia[0][1] * matcopia[1][0]) # devuelve el determinante del rango 2
        else:
            raise ErrorDimensional
    '''        
    #metodo para comprobar si la cantidad de columnas de la primer matriz
    #es igual a la cantidad de filas de la segunda matriz. Esto es requisito
    #para poder multiplicarlas
    def equalFilasxColumnas(self, nextMat):
        return len(self.mat[0]) == len(nextMat.mat)
    
#    def matCuadrada(self, Matriz):
#        return len(Matriz.mat) == len(Matriz.mat[0])

    #metodo para comprobar que dos matrices tienen la misma cantidad de filas
    def equalFilas(self, nextMat):
        return len(self)==len(nextMat)  #comparamos que las dos matrices tengan la misma cantidad de filas

    #metodo para comprobar que dos matrices tienen la misma cantidad de columnas
    def equalColumnas(self, nextMat):
        cont = 0
        for i in range(len(self.mat)):                  #comparamos que las dos matrices tengan
            if (len(self.mat[i])==len(nextMat.mat[i])): #la misma longitud de filas
                cont+=1
        return cont==len(self)

    #metodo para verificar si la matriz se ha ingresado correctamente
    def verificacion(self):
        cont = 0
        for i in range(1,len(self.mat)):            #comparamos que todas las filas tengan
            if len(self.mat[0])==len(self.mat[i]):  #la misma longitud
                cont+=1
        return cont==len(self.mat)-1

    #sobrecarga de string, convierte la lista en un solo string con los
    #datos de la matriz
    def __str__(self):
        x=''
        for i in range(len(self.mat)):      #creamos un string con los
            x+=str(str(self.mat[i])+'\n')   #elementos de la matriz y 
        return x                            #saltos de linea

    #representacion de la matriz
    def __repr__(self):
        return self.__str__()   #usamos la sobrecarga de string
    '''
    def determinante(self):
        if self.matCuadrada():
        # Copia CORRECTA de la matriz A en la de B.
            self.matcopia = [k[:] for k in self.mat]
            n = len(self.mat)
            suma = 0.0
            if n > 2: # Si el rango es mayor que 2
                for i in range(len(self.mat)):
                    factor = self.matcopia[0][i] # saca el factor de la primera fila i
                    signo = -2 * (i % 2) + 1 # calcula su signo
                    print (signo)
                    self.matcopia.remove(self.matcopia[0]) # Borra la primera fila
                    for j in range(len(self.mat)):
                        # B[j].remove(B[j][i]). NO SE PUEDE PONER REMOVE porque lo que quita es el elemento de la primera posición
                        self.matcopia[j].pop(i) # Quita, de cada fila de B, el factor i, o sea, quita esa columna.
                    suma = suma + factor * signo * self.determinante(self.matcopia) # El determinante es la suma anterior más lo que calcule
                    self.matcopia = [k[:] for k in self.mat] # reconstruye la matriz B
                return suma # retorna la suma
            else:
                return (self.matcopia[0][0] * self.matcopia[1][1]) - (self.matcopia[0][1] * self.matcopia[1][0]) # devuelve el determinante del rango 2    
   
    def determinante(self, copia):
        if (self.matCuadrada(self)):
            # Copia CORRECTA de la matriz A en la de B.
            matcopia = [k[:] for k in self.mat]
            n = len(self.mat)
            suma = 0.0
            if n > 2: # Si el rango es mayor que 2
                for i in range(len(self.mat)):
                    factor = matcopia[0][i] # saca el factor de la primera fila i
                    signo = -2 * (i % 2) + 1 # calcula su signo
                    print (signo)
                    matcopia.remove(matcopia[0]) # Borra la primera fila
                    for j in range(len(self.mat)):
                        # B[j].remove(B[j][i]). NO SE PUEDE PONER REMOVE porque lo que quita es el elemento de la primera posición
                        matcopia[j].pop(i) # Quita, de cada fila de B, el factor i, o sea, quita esa columna.
                    suma = suma + factor * signo * determinante(matcopia) # El determinante es la suma anterior más lo que calcule
                    matcopia = [k[:] for k in self.mat] # reconstruye la matriz B
                return suma # retorna la suma
            else:
                return (matcopia[0][0] * matcopia[1][1]) - (matcopia[0][1] * matcopia[1][0]) # devuelve el determinante del rango 2
        else:
            raise ErrorDimensional


        det = 0
        if len(mattmp) == 2:
            det = (mattmp[0][0]*mattmp[1][1])-(mattmp[1][0]*mattmp[0][1])
            return det
        else:
            aux=[]
            for i in range(len(mattmp)):
                y=[]
                for j in range(len(mattmp)):    
                    y.append(0)
                aux.append(y)
            for i in range(len(mattmp)):
                y=[]
                for j in range(len(mattmp)):
                    if i != j:
                        for k in range(1,len(mattmp)):
                            index =-1
                            if j < i:
                                index  =j
                            else:
                                index = j -1
                                aux[index][k-1]=mattmp[j][k]  
                if i%2 == 0:
                    det += mattmp[i][0] * self.determinante(aux)
                else:
                    det -= mattmp[i][0] * self.determinante(aux)
        return det                    
    def llamardet(self):
        if self.matCuadrada():
            valor = self.determinante(self.mat)
            print(valor)

    '''

#clase para cuando existe un error de dimensiones de la matriz
class ErrorDimensionalSumRes(Exception):
    #sobrecarga para mostrar cual es el error
    def __str__(self):
        return str("Las dimensiones de las matrices no son iguales")
    #representacion de la clase
    def __repr__(self):
        return self.__str__()   #usamos la sobrecarga de string

#clase para cuando existe un error de dimensiones de la matriz
class ErrorDimensionalMul(Exception):
    #sobrecarga para mostrar cual es el error
    def __str__(self):
        return str('El numero de columnas no es igual al numero de filas')
    #representacion de la clase
    def __repr__(self):
        return self.__str__()   #usamos la sobrecarga de string

#clase para cuando existe un error de mal ingreso de la matriz
class ErrorDeIngreso(Exception):
    #sobrecarga para mostrar cual es el error
    def __str__(self):
        return str("La matriz no fue ingresada correctamente")
    #representacion de la clase
    def __repr__(self):
        return self.__str__()   #usamos la sobrecarga de string
     
'''
a=matriz([[1,2],[3,4],[5,6]])
b=matriz([[1,2,3,4],[4,5,6,7]])

c=matriz([[1,3,5],[7,9,11],[2,7,4]])#96
'''






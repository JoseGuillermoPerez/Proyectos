"""
---------
|Problema 1|
---------

***************************************************

Encontrar los primeros N numeros perfectos
Como sugerencia, puede implementar una funcion que encuentre
los divisores propios de un numero, y devuelva una lista con estos
N es un numero que ingresa el usuario

***************************************************
"""
#Definimos una funcion para obtener una lista con los divisores propios

def divisores(num):                           
    div = []
    for i in range(1,num):
        if (num%i==0):
            div.append(i)
    return div

#Pedimos al usuario que ingrese un numero,
#depues de 4 numeros perfectos el proceso es mas lento
#porque el quinto numero perfecto es demasiado grande

N = input('Ingrese un numero entre 1 y 4: ')

#Declaramos variables

contador = 0
x=1

#Comprobamos que el numero ingresado sea correcto

if(N<5):
    while(contador < N):                #Ciclo while hasta que lleguemos al numero ingresado
        total = 0                       #Iniciamos la suma de los divisores
        divisorespropios = divisores(x) #Obtenemos los divisores
        for y in divisorespropios:      
            total += y                  #Sumamos cada divisor
        if (total == x):
            print total                 #Si la suma es igual al numero, se imprime el numero
            contador+=1                 #y se aumenta el contador
        x+=1                            #Siguiente numero

#Si el numero es muy grande se imprime el texto

else:
    print 'Numero incorrecto'           
    

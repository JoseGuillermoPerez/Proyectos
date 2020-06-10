"""
---------
|Problema 2|
---------

***************************************************

Encontrar los primeros N numeros amigos.
Debe preguntar al usuario el valor de N antes de iniciar.

***************************************************
"""
#Definimos una funcion para obtener la suma de los divisores propios

def sumadivisores(num):
    div = 0
    for i in range(1,num):
        if (num%i==0):
            div += i
    return div

#Pedimos al usuario que ingrese un numero,
#depues de 4 numeros perfectos el proceso es mas lento

N = int(input('Ingrese un numero entre 1 y 4: '))

#Declaramos variables

i=1
j=1
start=1
contador = 0

#Comprobamos que el numero ingresado sea correcto

if(N<5):
    while(contador < N):                                #Ciclo while hasta que lleguemos al numero ingresado
        divisoresi=sumadivisores(i)                     #Obtenemos la suma de los divisores del primer numero
        while(j<=i):                                    #Ciclo while para la suma de divisores del segundo numero
            divisoresj=sumadivisores(j)                 #Obtenemos la suma de los divisores del primer numero
            if (divisoresj==i and divisoresi==j and i!=j):
                print (i)                                 #Comparamos si los numeros son amigos. Si son amigos entonces 
                print (j)                                 #se imprimen los numeros y se aumenta el contador.
                contador+=1                             #Se cambia el valor de j para que no empiece de 1 sino que 
                start=i                                 #inicie desde el ultimo numero donde se quedo. Esto es
                j=i                                     #para acelerar un poco el proceso
            j+=1
        i+=1
        j=start

#Si el numero es muy grande se imprime el texto
        
else:
    print ('Numero incorrecto')

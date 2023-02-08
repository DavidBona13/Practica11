# Esta funcion compara dos numeros y saca por pantalla cual es el numero mas grande o mas pequeno
# Soporta equals

def CompareNumber(Num_1, Num_2):
    print("The biggest number is {}, the lower one is {}".format(Num_1, Num_2 if Num_1 > Num_2 else Num_2, Num_1)) if Num_1 != Num_2 else print("The numbers are equal!")

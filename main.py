import exercici1_A as Ex1
import exercici2_A as Ex2
import exercici3_A as Ex3
import exercici_B as ex1
import exercici2_B as ex2
import exercici3_B as ex3

#Desde el main executem tot, poses les dades en els inputs (quan fas el "run") i et surt el codi.
nGran = int(input("Esciu un número: "))
nPetit = int(input("Escriu un segon número: "))
print(ex1.exercici1(nGran, nPetit))

num = int(input("Escriu un número: "))
print(ex2.exercici2(num))

edat = int(input("Escriu una edat: "))
ingressos = int(input("Esciure els teus ingressos mensuals: "))
print(ex3.exercici3(edat, ingressos))

Ex1.CompareNumber(1, 2)
Ex2.IsOnTheList()
Secret = Ex3.SecretNumber()


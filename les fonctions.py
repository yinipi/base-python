
# importer le module ramdom pour la generation des nombres aleaoires
import random as rnd
#addition
def addition(nb1,nb2):
    return nb1 + nb2

#soustraction
def subtraction(c, d):
    return c-d

#multiplication
def multiplication(nb1,nb2):
    return nb1*nb2

#division entier
def division(nb1,nb2):
    return nb1/nb2

#fonction pour generer un nombre entre deux valeurs donner par l'utilisateur
def ramdom_number(n1,n2):
    return rnd.randint(n1,n2)


a = int(input("entrez le premier nombre : "))
b = int(input("entrez le second nombre : "))

resulat_addition = addition(a,b)
print(f"le resultat de addition : {resulat_addition}")

resul_subtraction = subtraction(a,b)
print(f"le resultat de subtraction : {resul_subtraction}")

resul_division = division(a,b)
print(f"le resultat de division : {resul_division}")

resul_mult = multiplication(a,b)
print(f"le resultat de multiplication : {resul_mult}")

print(f"un entier aleatoire compris entre {a} et {b} est : {ramdom_number(a,b)}")


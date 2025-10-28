
# creation d'une classe eleve

class eleve :

    #initialisation des attributs de la classe
    def   __init__(self,nom,prenom,age,classe):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.classe = classe

    #initialisation d'une methode de la classe eleve
    #methode pour afficher les informations des eleves
    def info_eleve(self):
        print(f" vous etes {self.nom} {self.prenom} et vous avez {self.age} ans et vous etes en {self.classe}")

    #creation de la methode d'incrementation de l'age de l'eleve
    def birthday(self):
        self.age += 1



#creons un objet eleve ainsi que ces aattributs propes a lui
eleve1 = eleve("yinipi","jospen",21,"IOT3")
eleve1.birthday()

#utilisation de la methode de la classe
eleve1.info_eleve()
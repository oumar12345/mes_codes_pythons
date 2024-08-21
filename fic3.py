class Personne():
    def __init__(self, nom):
        self.nom = nom

    def vous_faites_quoi(self):
        return f"{self.nom} ne fait rien."

    def comment_vous_vous_appelez(self):
        return f"Je m'appelle {self.nom}."

#----------NE MODIFIEZ PAS LE CODE AU DESSUS DE CETTE LIGNE, IL SERA REINITIALISE LORS DE l'EXECUTION----------
class Etudiant(Personne):
    def vous_faites_quoi(self):
        return f"{self.nom} fait son devoir."
    
Mary = Personne("Mary")
Betty = Etudiant("Betty")

print(Mary.vous_faites_quoi())
print(Mary.comment_vous_vous_appelez())
print("**"*30)
print(Betty.vous_faites_quoi())
print(Betty.comment_vous_vous_appelez())

vr = 123450
t = [1,2,3,4,5]
def rever(vr):
    inter = str(vr)
    rev = inter[::-1]
    return int(rev)

print(rever(vr))
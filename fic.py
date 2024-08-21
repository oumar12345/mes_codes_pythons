from collections import Counter
# x = int(input("Entrez un nombre : "))
# def facto (x) :
#     fact = 1
#     for i in range(1, x+1) :
#         fact = fact*i
#     return fact

# print(facto(x))

# t = input("Entrez une liste de races de chiens, séparés par des virgules : ")
# tab = t.split(",")
# for i in tab : 
#     print(i.strip().capitalize())
# print (tab)

# f = open("demofile.txt", "r")
# string = f.readlines()
# f.close()
# print(string)

# t = input("Entrez une liste de races de chiens, séparés par des virgules : ")
# t2 = t.split(",")
# tab = []
# for i in t2 :
#     tab.append(i.strip().capitalize())

# cpt = Counter(tab)
# print(cpt.most_common())
# print('**'*30)
# elt_max = max(cpt, key=lambda x : cpt[x])

# print(elt_max)

def trouver_elements_les_plus_courants(liste, n=None):
    # Étape 1: Compter les occurrences de chaque élément
    comptages = {}
    for element in liste:
        if element in comptages:
            comptages[element] += 1
        else:
            comptages[element] = 1
    
    # Étape 2: Trier les éléments par leur fréquence
    # Convertir le dictionnaire en liste de tuples (élément, fréquence)
    liste_triee = sorted(comptages.items(), key=lambda x: x[1], reverse=True)
    
    # Étape 3: Retourner les n éléments les plus courants (ou tous si n est None)
    if n is not None:
        return liste_triee[:n]
    else:
        return liste_triee

# Exemple de liste
liste = ['Husky', 'Corgi', 'Malinois', 'Husky', 'Pitbull', 'Husky', 'Corgi', 'Husky', 'Malinois']

# Trouver les éléments les plus courants
resultat = trouver_elements_les_plus_courants(liste, 2)

# Afficher le résultat
print(resultat)

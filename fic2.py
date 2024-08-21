# # nested_list = [['_'] * 3] * 3
# nested_list = [['_'] * 3 for el in range(3)]
# nested_list[1][2] = '99'
# print(nested_list)

# import time
# time.sleep(10)
# print("Temps écoulé !")

# class Rectangle :
#     def perimetre(self, largeur, longueur) :
#         return 2 * (largeur + longueur)
    
#     def surface(self, largeur, longueur) :
#         return largeur * longueur
    
# petit_rectangle = Rectangle()
# surface = petit_rectangle.surface(5, 10)
# perimetre = petit_rectangle.perimetre(5, 10)

# print("La surface du petit rectangle est de {} m2 et son perimetre est de {} m".format(surface, perimetre))

numb = [1, 2, 3]
letters = ['a', 'b', 'c']

tuple = list(zip(numb, letters))
dict = dict(tuple)
print("Tuple : ", tuple)
print("T1:", tuple[1])
print("Dictionnaire : ", dict)

def sum_length(param):
    sum = 0
    for i in param :
        sum = sum+i
    return sum

print(sum_length([1, 2, 3]))
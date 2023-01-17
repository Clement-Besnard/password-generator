import random;

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
list4 = ['?', '.', '!']
list5 = [list1, list2, list3, list4]
result = []
for i in range(16):
    result.append(random.choice(random.choice(list5)))
str = "".join(result)
Nom = input("Nom de l'application : ")
print(Nom, ' = ', str)
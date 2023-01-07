#   Permet de compter le nombre d'occurence de chaque element dans une liste de maniere consecutive


def count_occurence(list_to_count):
    occurences = []
    list_to_count.append('X')  # pour regler le probleme de liste out of range
    c = 1
    for i in range(0, len(list_to_count) - 1):
        if list_to_count[i] == list_to_count[i + 1]:
            c += 1
        else:
            occurences.append([list_to_count[i], c])
            c = 1
    return occurences


#   Exemples
list1 = [0, 2, 2, 5, 5, 9, 8, 7, 7, 7, 0, 0, 1]
list2 = [0, 4, 2, 8, 8, 9, 8, 2, 7, 7, 1, 1, 1, 1, 0, 1]
list3 = ['a', 'b', 'b', 'b', 'c', 'c', 'd']
list4 = [0, 2, 2, 5, 5, 9, 8, 7, 7, '7', '7', 0, 0, 1]

print(count_occurence(list1))
print(count_occurence(list2))
print(count_occurence(list3))
print(count_occurence(list4))

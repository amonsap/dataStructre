def bubblesort(list):
    for K in range(len(list) - 1, 0, -1):
        for idx in range(K):
            if list[idx] > list[idx + 1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp

def insertionsort(list):
    for i in range(1,len(list)):
        j = i - 1
        temp = list[i]
        while (list[j] > temp) and (j >= 0):
            list[j+1] = list[j]
            j = j-1
        list[j+1] = temp

def selectionsort(list):
    for i in range(len(list)):
        indMin = i
        for j in range(i + 1, len(list)):
            if list[indMin] > list[j]:
                indMin = j
        list[i], list[indMin] = list[indMin], list[i]

list = []
num = int(input("input Number: "))

for i in range(num):
    a = int(input("input data "))
    list.append(a)

menu = int(input('Menu\n  1:Bubble Sort\n  2:Insertion sort\n  3:Selection Sort\n  input  choice:'))

if menu == 1 :
    bubblesort(list)
    print('\nBubble Sort')
elif menu == 2 :
    insertionsort(list)
    print('\nInsertion sort')
elif menu == 3:
    selectionsort(list)
    print('\nSelection Sort')
else:
    print('\nErroe')

print('List')
print(list)
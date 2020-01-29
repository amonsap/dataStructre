hash_table = [[] for _ in range(10)]

def hashing_funcion(key):
    return key % len(hash_table)

def insert(hash_table,key,value):
    hash_key = hashing_funcion(key)
    key_exists = False
    bucket = hash_table[hash_key]
    for i , kv in enumerate(bucket):
        k , v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key,value))

#search method
def search(hash_table,key):
    hash_key = hashing_funcion(key)
    bucket = hash_table[hash_key]
    for i,kv in enumerate(bucket):
        k , v = kv
        if key == k:
            return  v

temp = True
while temp:
    menu = int(input('Menu\n  1:Insert\n  2:Search\n  3:Exit\n  input  choice:'))
    if menu == 1 :
        key = int(input('Input Key : '))
        value = input('Input value : ')
        insert(hash_table, key, value)
        print('Data : ',hash_table,key,value)
        print('\n')
    elif menu == 2 :
        key = int(input('Input Key : '))
        search(hash_table, key)
        print('Result : ',hash_table,key)
        print('\n')
    elif menu == 3 :
        temp = False
    else:
        print('Please check choice ')
        print('\n')


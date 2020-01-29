from array import *
arrsta = array('i',[])
top = -1
temp = True

while temp:
    menu = int(input('Menu\n  1:push\n  2:pop\n  3:exit\n  input your choice:'))
    if menu == 1:
        top = top+1
        data = int(input('input data : '))
        arrsta.insert(top,data)
    elif menu == 2:
        arrsta.remove(arrsta[top])
        top = top-1
    elif menu == 3:
        temp = False

    print('data in stack ')
    for n in arrsta:
        print(n)

    print('\n')



mid = input('Score mid : ')
final = input('Scorn final : ')

Score = int(mid)+int(final)

if Score >100 or Score <0:
    print('Score error')
elif Score >=80  :
    print('A')
elif Score >=70:
    print('B')
elif Score >=60:
    print('C')
elif Score >=50:
    print('D')
else:
    print('F')





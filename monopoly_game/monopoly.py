from msvcrt import getch

print('|--------------------------------------------------------------------|')
print('|                                                                    |')
print('|                           Monopoly game                            |')
print('|                                                                    |')
print('|                                                                    |')
print('|                  please press a to start the game                  |')
print('|                                                                    |')
print('|                                                                    |')
print('|                                                                    |')
print('|                                                                    |')
print('|                                                                    |')
print('|                                                                    |')
print('|                                                                    |')
print('|                                                                    |')
print('|                                                                    |')
print('|                                                                    |')
print('|                                                                    |')
print('|                                                                    |')
print('|                                                                    |')
print('|                                                                    |')
print('|                                                                    |')
print('|                                                                    |')
print('|                                                                    |')
print('|--------------------------------------------------------------------|')
item = getch()
item = item.decode()
while item != 'a':
    item = getch()
    item = item.decode()
#print(item)#only for debugging
while True:
    A = 0 #Max 17
    B = 0 #Max 17
    Whole_list = ['|--------------------------------------------------------------------|',
                  '|  press r for rolling the dice                                      |',
                  '|  press b for buy                                                   |',
                  '|  press n to skip the buy                                           |',
                  '|  Start (+$200)                       A B                           |',
                  '|  Västerlånggatan                                                   |',
                  '|  Hornsgatan                                                        |',
                  '|  Folkungagatan                                                     |',
                  '|  Götgatan                                                          |',
                  '|  Ringvägen                                                         |',
                  '|  S:t Eriksgatan                                                    |',
                  '|  Odengatan                                                         |',
                  '|  Vallhallavägen                                                    |',
                  '|  Eletric factory                                                   |',
                  '|  Sturegatan                                                        |',
                  '|  Karlavägen                                                        |',
                  '|  Narvavägen                                                        |',
                  '|  Gustav Aldofs torg                                                |',
                  '|  Drottninggatan                                                    |',
                  '|  Diplomatstaden                                                    |',
                  '|  Centrum                                                           |',
                  '|  Norrmalmstorg                                                     |',
                  '|  A: $1500        B: $1500                                          |',
                  '|--------------------------------------------------------------------|']
    # [38], [40]  Players status,  y =22,x = 7-10    y= 22 x= 23-26
    print(Whole_list)    
    break
# The code is ending here
while True:
    pass
from msvcrt import getch
from random import randint

A = 0 #Max 17
B = 0 #Max 17
A_own = {}
B_own = {}
Game_own = {'Västerlånggatan   ' : (2,4,20,40,80,160), 
            'Hornsgatan        ' : (4,8,40,80,160,320),
            'Folkungagatan     ' : (12,24,50,100,200,450),
            'Götgatan          ' : (12,24,50,100,200,450),
            'Ringvägen         ' : (14,28,60,120,240,540),
            'S:t Eriksgatan    ' : (17,36,72,144,288,648),
            'Odengatan         ' : (17,36,72,144,288,648),
            'Vallhallavägen    ' : (17,36,72,144,288,648),
            'Eletrical Factory ' : 'randint(1,6)*10',
            'Sturegatan        ' : (22,44,88,176,352,842),
            'Karlavägen        ' : (22,44,88,176,352,842),
            'Narvavägen        ' : (24,48,96,192,384,926),
            'Gustav Aldofs Torg' : (36,72,144,288,576,1389),
            'Drottninggatan    ' : (36,72,144,288,576,1389),
            'Diplomatstaden    ' : (40,80,160,320,640,2023),
            'Centrum           ' : (50,100,200,400,800,1500),
            'Norrmalmstorg     ' : (100,200,400,800,1600,3200)}
offset = 4

Whole_list = ['|--------------------------------------------------------------------|',
              '|  press r for rolling the dice                                      |',
              '|  press b for buy  (x to get the house)                             |',
              '|  press n to skip the buy  (n for give up)                          |',
              '|  Start (+$200)                       A B                           |',
              '|  Västerlånggatan                                 $60               |',
              '|  Hornsgatan                                      $60               |',
              '|  Folkungagatan                                   $100              |',
              '|  Götgatan                                        $100              |',
              '|  Ringvägen                                       $120              |',
              '|  S:t Eriksgatan                                  $140              |',
              '|  Odengatan                                       $140              |',
              '|  Vallhallavägen                                  $140              |',
              '|  Eletric factory                                 $150              |',
              '|  Sturegatan                                      $180              |',
              '|  Karlavägen                                      $180              |',
              '|  Narvavägen                                      $200              |',
              '|  Gustav Aldofs torg                              $300              |',
              '|  Drottninggatan                                  $300              |',
              '|  Diplomatstaden                                  $320              |',
              '|  Centrum                                         $350              |',
              '|  Norrmalmstorg                                   $400              |',
              '|  A: $1500        B: $1500                                          |',
              '|--------------------------------------------------------------------|']
def printer(list):
    for i in list:
        print(i)
'''
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
'''
while True:
    printer(Whole_list)
    item = getch().decode()
    while item != 'r':
        item = getch().decode()
    steps = randint(1,6)
    #print(steps)
    result_position = offset+A+steps
    x = offset + A
    Whole_list[x] = Whole_list[x][0:39] + ' ' + Whole_list[x][40:]
    Whole_list[result_position] = Whole_list[result_position][0:39] + 'A'+ Whole_list[result_position][40:]
    printer(Whole_list)
    A = result_position - offset
    #print(A)
    if int(Whole_list[22][7:11]) > int(Whole_list[offset + A][52:56]):
        item = getch().decode()
        while not item in ['b', 'n', 'x']:
            item = getch().decode()
        if item == 'b' and Whole_list[offset+A][3:21] in Game_own.keys():
            A_cash = str(int(Whole_list[22][7:11])-int(Whole_list[offset+A][52:55]))
            if len(A_cash) < 4:
                A_cash = A_cash + ' '*4-len(A_cash)
            Whole_list[22] = Whole_list[22][0:7]+A_cash+Whole_list[22][11:]
            A[Whole_list[offset+A][3:21]] = Game_own[Whole_list[offset+A][3:21]]
            del Game_own[Whole_list]
        print('a:',A_own,)
        print(Whole_list)
    # [39], [41]  Players status,  y =22,x = 7-10    y= 22 x= 23-26, players cash, 52-55, cost, 60-64,,3-20,name  
    break
# The code is ending here
while True:
    pass
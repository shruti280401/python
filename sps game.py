import random
while True:
    li1 = ['Rock', 'Paper', 'Scissor']
    li = ['Rock', 'Paper', 'Scissor']


    print(li1)
    cp1=0
    cp2=0
    x = input(" p1 enter ur choice from above list:")
    # y=input(" p2 enter ur choice from above list:",li2)
    p1 = x.capitalize()
    p2 = random.choice(li1)
    print("p2 choosed:",p2)
    # p2 = li2

    if p1 not in li1:
        print("oops! Invalid Entry")
    if p2 not in li1:
        print("oops! Invalid Entry")
    if p1 == li1[0] and p2 == li[0]:
        pass
    if p1 == li1[1] and p2 == li[1]:
        pass
    if p1 == li1[2] and p2 == li[2]:
        pass
    if p1 == li1[0] and p2 == li[1]:
        cp2+=1
    if p1 == li1[0] and p2 == li[2]:
        cp1+=1
    if p1 == li1[1] and p2 == li[0]:
        cp1+=1
    if p1 == li1[1] and p2 == li[2]:
        cp2+=1
    if p1 == li1[2] and p2 == li[0]:
        cp2+=1
    if p1 == li1[2] and p2 == li[1]:
        cp1+=1
    print("player 1 score:",cp1)
    print("player 2 score:",cp2)
    if cp1>cp2:
        print("player1(you) won")
    elif cp1<cp2:
        print("player 2 won")
    else:
        print("Tie")
    ask = int(input("press 1 for continue and 0 for exit"))
    if ask == 1:
        pass
    else:
        exit(0)







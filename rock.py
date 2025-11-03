import random as rd
def rock():
    s=['rock','paper','scissor']
    d=rd.choice(s)
    k = input('Enter the rock or paper or scissor').lower()
    if k not in ['rock','paper','scissor']:
        print('try again')
    elif k==d:
        print('game is tied try again')
    elif d=='rock' and k =='scissor':
        print('computer wins')
    elif d=='rock' and k=='paper':
        print('you win')
    elif d=='scissor' and k=='paper':
        print('computer wins')
    elif d=='scissor' and k=='rock':
        print('you wins')
    elif d=='paper' and k=='rock':
        print('computer wins')
    elif d=='paper' and k=='scissor':
        print('you wins')
def main():
    while True:
        f=input('enter you want to play:Y or exit N').upper()
        if f=='Y':
            rock()
        else:
            print('okk thank you')
            break
if __name__=='__main__':
    main()
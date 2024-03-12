import random
#三个‘’‘货“”“，换行输出
def menu():
    print('-'*7,'welconme to the game','-'*7)
#eval（）转换成实际数据类型
#choice=eval(input('please input:'))
#产生随机数
#a=random.randint(1,10)
#print(a)
#逻辑运算符：and==&&,or==||,!不等于
#循环 whilie True:
while True:
    #number_guess = eval(input('please input:'))
    true_number=random.randint(1,10)
    while True:
        number_guess = eval(input('please input:'))
        if number_guess ==true_number:
            print('true')
            break
        elif number_guess > true_number:
            print('guess wrong.big')
        else:
            print('guess wrong.small')
        choice = input('guess again?:yes/no:\n')
        if choice == 'yes':
            continue
        else:
            break
    Choice = input('play again?:yes/no:\n')
    if Choice == 'yes':
        continue
    else:
        break




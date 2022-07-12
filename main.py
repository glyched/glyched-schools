
homework_names = []
homework_desc =[]
print('what would you like to input(h for help):')
ans = input()
while True:
    if ans == 'h':
        print('homework or 1:   for homework')
    elif ans == ('homework'):
        x = int(input('how much homework you got today bud?'))
        for i in range(x):
            y = input('enter Homework title: ')
            z = input('enter homework description: ')
            homework_names.append(y)
            homework_desc.append(z)
        print('1.Enter more homework')
        print('2.go to menue')


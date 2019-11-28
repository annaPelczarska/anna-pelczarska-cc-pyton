repeat = True

while (repeat):
    n1 = input('Enter a number (or a letter to exit): ')

    if n1.isalpha():
        print('the end')
        repeat = False
        exit()

    operator = input('Enter an operation (+, -, *, /): ')
    n2 = input('Enter another number: ')

    num1 = float(n1)
    num2 = float(n2)

    if operator == '+':
        print('Result: {}'.format(num1 + num2))

    elif operator == '-':
        print('Result: {}'.format(num1 - num2))

    elif operator == '*':
        print('Result: {}'.format(num1 * num2))

    elif operator == '/' and num2 != 0:
        print('Result: {}'.format(num1 / num2))

    else:
        print('What are you trying to do?')

first_number = int(input('Введите первое число: '))
operation = input("Введите операцию: ")
second_number = int(input('Введите второе число: '))

if operation == '+':
    def add(first_number, second_number):
        result = first_number + second_number
        print(f'Ответ: {result}')
    add(first_number, second_number)


elif operation == '/':
    def divide(first_number, second_number):
        result = first_number // second_number
        print(f'Ответ: {result}')
    divide(first_number, second_number)


elif operation == '-':
    def add(first_number, second_number):
        result = first_number - second_number
        print(f'Ответ: {result}')
    add(first_number, second_number)


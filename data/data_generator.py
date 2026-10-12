import random


def massive_generator(): # 8
    try:
        while True:
            size=int(input('Введите размер массива: '))
            if size>0:
                break
            else:
                print('Ошибка: Размер должен быть больше нуля')
        pov=input('В массиве будут повторятся символы?(Yes/No): ')
        if pov in ['Yes','yes','Да','да']:
            while True:
                max=int(input('Введите введите максимально возможный эллемент массива: '))
                min=int(input('Введите введите минимально возможный эллемент массива: '))
                if min<=max:
                    break
                else:
                    print('Ошибка: Минимум не может быть больше максимума')
            data=[random.randint(min,max) for _ in range(size)]
            print('Новый массив сгенерирован\n')
            return data
        else:
            data=[int(x) for x in range(1,size+1)]
            print('Новый массив сгенерирован\n')
            return data
    except ValueError:
        print("Ошибка: Введите корректное число")
        return massive_generator() 
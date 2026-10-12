def straight_up_searth(data): # 1
    try:
        search_num=int(input(f'Введите число от {min(data)} до {max(data)-1}: '))
        sw=True
        for n in range(len(data)):
            if data[n]==search_num:
                sw=False
                print(f'Число {search_num} найдено за {n+1} шагов')
                input('Нажмите, чтобы продолжить\n')
                break
        if sw:
            input('Ошибка: Число вне списка\n')
    except ValueError:
        print("Ошибка: Введите корректное число")


def bin_search(data): # 2
    try:
        search_num=int(input(f'Введите число от {min(data)} до {max(data)-1}: '))
        if search_num in data:
            sorted(data); sw=0
            while len(data)>1:
                n=len(data)//2
                if data[n]>search_num:
                    data=data[:n]
                elif data[n]<search_num:
                    data=data[n+1:]
                elif data[n]==search_num:
                    sw=1
                    print(f'Число {search_num} найдено')
                    input('Нажмите, чтобы продолжить\n')
                    break
            if sw and data[0]==search_num:
                print(f'Число {search_num} найдено')
                input('Нажмите, чтобы продолжить\n')
            else:
                print('Ошибка: Число не найдено')
        else:
            input('Ошибка: Число вне списка\n')
    except ValueError:
        print('Ошибка: Число вне заданого отрезка')

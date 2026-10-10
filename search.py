import random
import time
import statistics

# 4 вида сортировки, +
# прогнать по разным длинам, +
# сделать график,
# сортировка текста (буквы и слова)

def sort_check(mass):
    return all([mass[n]<=mass[n+1] for n in range(len(mass)-1)])

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
            data.sort(); sw=0
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
        
def bubble_sort(data): # 3
    n=len(data)
    for i in range(n-1):
        swap=0
        for j in range(n-1-i):
            if data[j]>data[j+1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swap=1
        if not swap:
            break
    return data
        
        
def insertion_sort(data): # 4
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def sort_by_another_massive(data2): # 5
    data=data2.copy()
    sorted_massive=[]
    while data:
        m = max(data)
        sorted_massive.append(m)
        data.remove(m)
    return sorted_massive
    

def quick_sort(mass): # 6
    if len(mass)<=1:
        return mass
    pivot=mass[len(mass)//2]
    left=[x for x in mass if x<pivot]
    middle=[x for x in mass if x==pivot]
    right=[x for x in mass if x>pivot]
    return quick_sort(left) + middle + quick_sort(right)

def shell_sort(data): # 7
    n=len(data)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            tmp=data[i]
            while i>=gap and data[i-gap]>tmp:
                data[i]=data[i-gap]
                i-=gap
            data[i]=tmp
        gap//=2
    return data

def Massive_generator(): # 8
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
        return Massive_generator() 

def draw_grouped(data_list):

    names = list(data_list[0].keys())
    N=[10, 100 ,200, 1000, 3000, 5000, 10000]

    print(f"\n=== {"Сравнение сортировок"} ===")
    print("Размер   | " + " | ".join(f"{n:<25}" for n in names),"| ")
    print("-" * 149)

    for cnt,arr in enumerate(data_list):
        row = f"N={N[cnt]:<7}| "
        max_val = max(arr.values())
        for n in names:
            bar_len = max(1,round(arr[n] / max_val * 25)) if arr[n] > 0 else 0
            row += f"{'█'*bar_len:<25} | "
        print(row)

    print("-" * 149)
    print('\n=== (Скорость находится относительно самой медленной сортировки, чем меньше - тем лучше!) ===')

def speed_test(): # 11
    sorts = [bubble_sort, insertion_sort, sort_by_another_massive, quick_sort, shell_sort]
    slow_sorts=[bubble_sort, insertion_sort]
    all_results=[]

    for n in [10, 100 ,200, 1000, 3000, 5000, 10000]:
        base = [random.randint(0, 100000) for _ in range(n)]
        inputs = []
        for _ in range(3):
            random.shuffle(base)
            inputs.append(base.copy())

        for func in sorts:
            func(inputs[0].copy())

        result = {}
        for func in sorts:
            times = []
            if func in slow_sorts and n>=3000:
                data1 = inputs[0].copy()
                start = time.perf_counter()
                try:
                    func(data1)
                except Exception as e:
                    print(f'{func.__name__}: ошибка {e}')
                    break
                times.append(time.perf_counter() - start)

            else:
                for arr in inputs:
                    data1 = arr.copy()
                    start = time.perf_counter()
                    try:
                        func(data1)
                    except Exception as e:
                        print(f'{func.__name__}: ошибка {e}')
                        break
                    times.append(time.perf_counter() - start)
            if times:
                result[func.__name__] = statistics.median(times)
        
        all_results.append(result)
        print(f'--- n = {n} ---')
        for name, t in sorted(result.items(), key=lambda x: x[1]):
            print(f'{name:25} {t:13f}')
    draw_grouped(all_results)

def main():
    data=Massive_generator()
    while True:
        print('Выберите действие: \n'
              '1 — Последовательный поиск \n'
              '2 — Бинарный поиск \n'
              '3 — Bubble сортировка \n'
              '4 — Сортировка вставками \n'
              '5 — Сортировка выбором \n'
              '6 — Быстрая сортировка \n'
              '7 - Сортировка шелла \n'
              '8 - Изменить вид списка \n'
              '9 - перемешать список \n'
              '10 - показать текущий массив \n'
              '11 - Сравнить скорость сортировок(от 10 до 10000 элементов)\n'
              '0 — Выход')
        User_ansver=input()

        if User_ansver=='1': #Последовательный поиск 
            straight_up_searth(data)

        elif User_ansver=='2': #Бинарный поиск 
            bin_search(data)

        elif User_ansver=='3': #Пузырьковая сортировка 
            data=bubble_sort(data)
            if sort_check(data):    
                print(f'Массив отсортирован')
                input('Нажмите, чтобы продолжить\n')
            else:
                input('Ошибка\n')

        elif User_ansver=='4': #Сортировка вставками
            data=insertion_sort(data)
            if sort_check(data):    
                print(f'Массив отсортирован')
                input('Нажмите, чтобы продолжить\n')
            else:
                input('Ошибка\n')

        elif User_ansver=='5': #Сортировка дополнительный массивом
            data=sort_by_another_massive(data)
            if sort_check(data):    
                print(f'Массив отсортирован')
                input('Нажмите, чтобы продолжить\n')
            else:
                input('Ошибка\n')

        elif User_ansver=='6': #Быстрая сортировка
            data=quick_sort(data)
            if sort_check(data):    
                print(f'Массив отсортирован')
                input('Нажмите, чтобы продолжить\n')
            else:
                input('Ошибка\n')
                
            
        elif User_ansver=='7': #Сортировка шелла
            data=shell_sort(data)
            if sort_check(data):    
                print(f'Массив отсортирован')
                input('Нажмите, чтобы продолжить\n')
            else:
                input('Ошибка\n')

        elif User_ansver=='8': #Изменить вид списка
            data=Massive_generator()
            
        elif User_ansver=='9': #Перемешать список
            random.shuffle(data)
            print(f'Массив перемешан')
            
        elif User_ansver=='10': #Показать список
            print(data)
            input('Нажмите, чтобы продолжить\n')
            
        elif User_ansver=='11': #Сравнить скорость сортировок
            speed_test()
            input('Нажмите, чтобы продолжить\n')
        
        elif User_ansver=='0': #Выход
            break

        elif User_ansver:
            print('Ошибка: Введите корректное значение')

if __name__ == "__main__":
    main()
    


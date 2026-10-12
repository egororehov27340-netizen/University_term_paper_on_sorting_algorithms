import random
import time
import statistics
from data.data_generator import massive_generator
from algoritms.sorts import (
    sort_check,
    bubble_sort,
    insertion_sort,
    sort_by_another_massive,
    quick_sort,
    shell_sort,
)
from algoritms.search import straight_up_searth, bin_search

# 5 видов сортировки, +
# прогнать по разным длинам, +
# сделать график, +
# сортировка текста (буквы и слова)

class App:

    def __init__(self):
        self.data=massive_generator()
        self.commands={"1":self.cmd_straight_up_searth,
                       "2":self.cmd_bin_search,
                       "3":self.cmd_bubble,
                       "4":self.cmd_insert,
                       "5":self.cmd_another,
                       "6":self.cmd_quick,
                       "7":self.cmd_shell,
                       "8":self.cmd_change,
                       "9":self.cmd_shuffle,
                       "10":self.cmd_show,
                       "11":self.cmd_speed_test,
                       "0":self.cmd_exit
        }

    def show_menu(self):
        print('Выберите действие: \n'
              '1 — Последовательный поиск \n'
              '2 — Бинарный поиск \n'
              '3 — Bubble сортировка \n'
              '4 — Сортировка вставками \n'
              '5 — Сортировка дополнительным массивом \n'
              '6 — Быстрая сортировка \n'
              '7 - Сортировка шелла \n'
              '8 - Изменить вид списка \n'
              '9 - перемешать список \n'
              '10 - показать текущий массив \n'
              '11 - Сравнить скорость сортировок(от 10 до 10000 элементов)\n'
              '0 - Выход\n'
        )

    def cmd_straight_up_searth(self):
        straight_up_searth(self.data)

    def cmd_bin_search(self):
        bin_search(self.data)

    def cmd_bubble(self):
        self.data=menu_sorts(self.data,bubble_sort)

    def cmd_insert(self):
        self.data=menu_sorts(self.data,insertion_sort)

    def cmd_another(self):
        self.data=menu_sorts(self.data,sort_by_another_massive)

    def cmd_quick(self):
        self.data=menu_sorts(self.data,quick_sort)

    def cmd_shell(self):
        self.data=menu_sorts(self.data,shell_sort)

    def cmd_change(self):
        self.data=massive_generator()

    def cmd_shuffle(self):
        random.shuffle(self.data)
        print('Массив перемешан')
        input('Нажмите, чтобы продолжить\n')  

    def cmd_show(self):
        print(self.data,'\n')
        input('Нажмите, чтобы продолжить\n')  

    def cmd_speed_test(self):
        speed_test()
        input('Нажмите, чтобы продолжить\n')   

    def run(self):
        while True:
            self.show_menu()
            choice = input("> ").strip()
            action = self.commands.get(choice)
            if action:
                action()
            else:
                print("Неверный выбор")

    def cmd_exit(self):
        raise SystemExit


def menu_sorts(data,sort_func):
    start=time.perf_counter()
    data=sort_func(data)
    t=(time.perf_counter()-start)  
    if sort_check(data):
        print(f'Массив отсортирован за {t:.7f} секунд')
    else:
        print(f'Ошибка: {sort_func.__name__} не отсортировал!')
    input('Нажмите, чтобы продолжить\n')
    return data


def draw_grouped(data_list):

    names = list(data_list[0].keys())
    N=[10, 100 ,200, 1000, 3000, 5000, 10000]

    print("\n=== Сравнение сортировок ===")
    line="Размер   | " + " | ".join(f"{n:<25}" for n in names)+' |'
    print(line)
    print("-" * len(line))

    for cnt,arr in enumerate(data_list):
        row = f"N={N[cnt]:<7}| "
        max_val = max(arr.values())
        for n in names:
            bar_len = max(1,round(arr[n] / max_val * 25)) if arr[n] > 0 else 0
            row += f"{'█'*bar_len:<25} | "
        print(row)

    print("-" * len(line))
    print('\n=== (Скорость находится относительно самой медленной сортировки, чем меньше - тем лучше!) ===\n')


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


if __name__ == "__main__":
    menu=App()
    menu.run()
def sort_check(mass, reverse=False):
    lst = list(mass)
    return lst == sorted(lst, reverse=reverse)


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
        m = min(data)
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

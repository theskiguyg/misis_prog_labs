# ЛАБОРАТОРНАЯ РАБОТА №1 

# Загребин Егор Денисович БИВТ-25-4



# Задание №1

```python
name = input("What is your name? ")
age = int(input("What is your age? "))
print("Hello, " + name + "!" + "You'll be " + str(age + 1)  + " next year!")
```
![Вывод задание 1](./images/lab01/Задание1.png)


# Задание №2

```python
a = float(input('a:').replace(',', '.'))
b = float(input('b:').replace(',', '.'))
print(f"sum: {a + b}\navg: {(a + b) / 2}")
```
![Вывод задание 2](./images/lab01/Задание2.png)


# Задание №3

```python
price = float(input('Цена: '))
disc = float(input('Скидка: '))
vat = float(input('Налог: '))
base = price * (1 - disc/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base:.2f}')
print(f'НДС:               {vat_amount:.2f}')
print(f'Итого к оплате:    {total:.2f}')
```
![Вывод задание 3](./images/lab01/Задание3.png)


# Задание №4

```python
m = int(input("Минуты: "))
print(f"{m // 60:02d}:{m % 60:02d}")
```
![Вывод задание 4](./images/lab01/Задание4.png)


# Задание №5

```python
name = input('ФИО: ')
print(f'Инициалы: {''.join([i[0].upper() for i in name.split()])}.')
print(f'Длина (символов): {len(''.join(name.split())) + 2}')
```
![Вывод задание 5](./images/lab01/Задание5.png)


# ЛАБОРАТОРНАЯ РАБОТА №2


# Задание 1 -> arrays

# 1 min_max

```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        return ValueError
    mn = 9e6 
    mx = -9e6 
    for i in range(len(nums)):
        if nums[i] < mn:
            mn = nums[i]
        if nums[i] > mx:
            mx = nums[i]
    return tuple([mn, mx])
print(min_max())
```
![Вывод задание 1.1](./images/lab02/1.1.png)

# 2 unique_sorted

```python
def unique_sorted(nums1: list[float | int]) -> list[float | int]:
    unique_nums = set(nums1)
    return sorted(unique_nums)
print(unique_sorted())
```
![Вывод задание 1.2](./images/lab02/1.2.png)

# 3 flatten

```python
def flatten(mat: list[list | tuple]) -> list:
    arr = list()
    for a in mat:
        if not(isinstance(a, list) or isinstance(a, tuple)):
            return TypeError
        for el in a:
            arr.append(el)
    return arr 
print(flatten())
```
![Вывод задание 1.3](./images/lab02/1.3.png)


# Задание 2 -> matrix

# Вспомогательная функция 
## С ее помощью проверяю длину строк матрицы. Если длина строк разная, значит матрица - рваная, возвращаю ValueError.

```python
def dliny(mat):
    if any(len(mat[0]) != len(mat[s]) for s in range(len(mat))):
        return False
    return True
```

# 1 transpose

```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []
    if dliny(mat) == False:
        return ValueError
    newmat = [[0 for stro in range(len(mat))] for stol in range(len(mat[0]))]
    for strok in range(len(mat)):
        for stolb in range(len(mat[strok])):
            newmat[stolb][strok] = mat[strok][stolb]
    return newmat

print(transpose())
```
![Вывод задание 2.1](./images/lab02/2.1.png)

# 2 row_sums

```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    if dliny(mat) == False:
        return ValueError
    sums = []
    for i in mat:
        sums.append(sum(i))
    return sums

print(row_sums())
```
![Вывод задание 2.2](./images/lab02/2.2.png)

# 3 col_sums

```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if dliny(mat) == False:
        return ValueError
    return row_sums(transpose(mat))

print(col_sums())
```
![Вывод задание 2.3.1](./images/lab02/2.2.1.png)


# Задание 3 -> tuples

```python
def format_record(rec: tuple[str, str, float]) -> str:
    
    name_processing = rec[0].strip().split()
    final_name = ''
    if len(name_processing) == 1:
        final_name = f"{name_processing[0][0].upper()}{name_processing[0][1:]}"
    elif len(name_processing) == 2:
        final_name = f"{name_processing[0][0].upper()}{name_processing[0][1:]} {name_processing[1][0:1].upper()}."
    elif len(name_processing) == 3:
        final_name = f"{name_processing[0][0].upper()}{name_processing[0][1:]} {name_processing[1][0:1].upper()}. {name_processing[2][0:1].upper()}."
    else:
        return ValueError
    
    group = ''
    group_processing = rec[1].strip()
    if group_processing == '':
        return ValueError
    else:
        group = group_processing

    gpa = float(rec[2])
    if not(isinstance(gpa, float)):
        return TypeError
    
    return f"{final_name}, гр. {group}, GPA: {gpa:.2f}"   

print(format_record(()))
```
![Вывод задание 3](./images/lab02/3.png)




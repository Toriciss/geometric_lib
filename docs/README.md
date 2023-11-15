# Документация

## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (ah)/2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Общее описание решения
1. Функция получает число/числа (например, число а - являющееся длиной каких-либо элементов фигуры)
2. Далее выполняются математические операции над данным числом/числами (вычисление площади/объёма фигуры в зависимости от формул)
3. Программа возвращает результат

## Функции

### Circle 

**Programm:**

```python
import math
"""Модуль math предоставляет обширный функционал для работы с числами"""

def area(r):

    """
    Функция принимает число r (радиус круга)
    Далее возвращает r в квадрате, умноженное на число pi (т.е. возвращает площадь круга)
    """
    return math.pi * r * r


def perimeter(r):
    """Функция принимает число r (радиус круга)
    Далее возвращает удвоенное произведение r на pi (т.е. периметр круга)
    """

    return 2 * math.pi * r
```

***Пример вызова:***

*Input:* r = 7
*Output:* Площадь = 153.938040, Периметр = 43.982297


### Rectangle

**Programm:**

```python
def area(a, b):
    """
    Функция принимает 2 числа - a и b (стороны прямоугольника)
    Далее возвращает произведение a и b (т.е. площадь прямоугольника)
    """
    return a * b

def perimeter(a, b):
    """
    Функция принимает 2 числа - a и b (стороны прямоугольника)
    Далее возвращает удвоенную сумму a и b (т.е. периметр прямоугольника)
    """
    return 2*a + 2*b
```
***Пример вызова:***

*Input:* a = 2, b = 5
*Output:* Площадь = 10, Периметр = 14 


### Square

**Programm:**

```python
def area(a):
    """
    Функция принимает число a (сторону квадрата)
    Далее возвращает число a возведенное в квадрат (т.е. площадь квадрата)
    """
    return a * a


def perimeter(a):
    """
    Функция принимает число a (сторону квадрата)
    Далее возвращает число a умноженное на 4 (т.е. периметр квадрата)
    """
    return 4 * a
```
***Пример вызова:***

*Input:* a = 5
*Output:* Площадь = 25, Периметр = 20


### Triangle 

***Program:***

```python
def area(a, h):
    """
    Функция принимает 2 числа - a и h (a - сторона треугольника, h - высота треугольника)
    Функция возвращает произведения числа a на число h деленное на 2 (т.е. площадь треугольника)
    """
    return a * h / 2

def perimeter(a, b, c):
    """
    Функция принимает 3 числа - a, b, c (стороны треугольника)
    Далее возвращает сумму этих 3 чисел (т.е. периметр треугольника)
    """
    return a + b + c
```
***Пример вызова:***

*Input:* a = 3, b = 4, c = 5, h = 4
*Output:* Площадь = 6, Периметр = 12

## Commit history

commit ca6c8aa524725d5ce71397cfc995f81a6de9ad36
Author: Viktoria Obukhova <obu-viktoria@mail.ru>
Date:   Wed Oct 4 01:12:28 2023 +0300

    General description of the solution

commit 5731a99174e6dfd734f18cf303441e9f3682ab4a
Author: Viktoria Obukhova <obu-viktoria@mail.ru>
Date:   Wed Oct 4 00:32:10 2023 +0300

    adding documentation to triangle

commit 0064b7b1027fdef5c3a9e46aa505ae99183513a5
Author: Viktoria Obukhova <obu-viktoria@mail.ru>
Date:   Wed Oct 4 00:29:44 2023 +0300

    adding documentation to square

commit 618837b232d172f800912330993df2e01ecc9a1d
Author: Viktoria Obukhova <obu-viktoria@mail.ru>
Date:   Wed Oct 4 00:27:09 2023 +0300

    adding documentation to rectangle

commit be97c6e48e2ec9d1b082ff9e9939b029e3cf508a
Author: Viktoria Obukhova <obu-viktoria@mail.ru>
Date:   Wed Oct 4 00:24:34 2023 +0300

    adding documentation to circle

commit 6aa955811432b85e87c097edfda738dc67ff666f (origin/main, origin/HEAD, main)
Author: Viktoria Obukhova <obu-viktoria@mail.ru>
Date:   Mon Sep 18 06:01:58 2023 +0300

    Добавление файлов rectangle.py и triangle.py, и исправление ошибки в rectangle.py

commit 04f1bce7aedc73ae629ec2818ca81c14be8035b0
Author: Viktoria Obukhova <obu-viktoria@mail.ru>
Date:   Mon Sep 18 05:57:57 2023 +0300

    Исправлена ошибка при нахождении периметра в rectangle.py

commit 49f00509a8e3719bc996aa90c1c52a3876d1773b
Author: Viktoria Obukhova <obu-viktoria@mail.ru>
Date:   Mon Sep 18 05:56:53 2023 +0300

    Добавлен новый файл rectangle.py

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added

## UnitTest
### Rectangle.py
- area()
###### Correct tests
~~~
input: 5,8
output: 40
~~~
~~~
input: 5.5, 9.9
output: 54.45
~~~
~~~
input: 10, 0
output: 0
~~~
###### Incorrect tests
~~~
input: 8, -4
output: -32
expected: The sides of the rectangle cannot be negative
~~~
- perimeter()
###### Correct tests
~~~
input: 5,7
output: 24
~~~
~~~
input: 5.5, 6.6
output: 24.2
~~~
~~~
input: 5, 0
output: 10
~~~
###### Incorrect tests
~~~
input: 5, -6
output: -2
expected: The sides of the rectangle cannot be negative
~~~
### Triangle.py
- area()
###### Correct tests
~~~
input: 3,8
output: 12
~~~
~~~
input: 8.8, 6.6
output: 29.04
~~~
~~~
input: 8, 0
output: 0
~~~
###### Incorrect tests
~~~
input: 10, -8
output: -40
expected: The base and height cannot be negative
~~~
- perimeter()
###### Correct tests
~~~
input: 6, 7, 8
output: 21
~~~
~~~
input: 7.7, 2.5, 9
output: 19.2
~~~
~~~
input: 6, 4, 6.6
output: 16.6
~~~
###### Incorrect tests
~~~
input: 8, -3, 4
output: 9
expected: The base and height cannot be negative
~~~
### Circle.py
- area()
###### Correct tests
~~~
input: 3
output: 28.274333882308138
~~~
~~~
input: 3.3
output: 34.21194399759285
~~~
~~~
input: 0
output: 0
~~~
###### Incorrect tests
~~~
input: -3
output: -28.274333882308138
expected: The radius cannot be negative
~~~
- perimeter()
###### Correct tests
~~~
input: 3
output: 18.84955592153876
~~~
~~~
input: 3.3
output: 20.734511513692635
~~~
~~~
input: 0
output: 0
~~~
###### Incorrect tests
~~~
input: -3
output: -18.84955592153876
expected: The radius cannot be negative
~~~
### Square.py
- area()
###### Correct tests
~~~
input: 8
output: 64
~~~
~~~
input: 8.8
output: 77.44000000000001
~~~
~~~
input: 0
output: 0
~~~
###### Incorrect tests
~~~
input: -8
output: -64
expected: The side of the square cannot be negative
~~~
- perimeter()
###### Correct tests
~~~
input: 8
output: 32
~~~
~~~
input: 8.8
output: 35.2
~~~
~~~
input: 0
output: 0
~~~
###### Incorrect tests
~~~
input: -8
output: -32
expected: The side of the square cannot be negative
~~~

## Autotests succes:
~~~
- 32 - all tests;
- 8 - tests with errors;
- 24 - tests without errors;
~~~
- P with errors = 8/32 = 0,25
- P without errors = 24/32 = 0,75
~~~
- Tests with errors = 25%
- Tests without errors = 75%
~~~

## GIT LOG:
| Автор | Дата | Хэш | Комментарий |
|---|---|---| --- |
| Viktoria Obukhova |Wed Nov 15 22:43:23 2023 +0300 | 44c0a29b7a890ddf18b8b555c2a6cf6731aa26d8|test: added tests for rectangle|
| Viktoria Obukhova | Wed Nov 15 22:43:23 2023 +0300 | 552a9c79962213041df1d4e883980b9979f0555e |test: added tests for triangle|
| Viktoria Obukhova | Wed Nov 15 22:43:23 2023 +0300 | 671aaa9298059dc32ca03b0efc6e277fdf21d504 | test: added tests for circle|
| Viktoria Obukhova | Wed Nov 15 22:43:23 2023 +0300 | 2b2926eacefabe4c5334a0e727595729cae385e4 | test: added tests for square|
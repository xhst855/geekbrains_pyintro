"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в
переменные, выведите на экран.
"""

x = 5
y = 6
my_str = "string"

print(my_str)
print(x)
hello = input("Please, type word hello: ")
print(hello)

"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
import time

sec = int(input("Please, enter the time in seconds: "))
print(f"{int(sec/3600)}:{int(sec/60%60)}:{sec%60}")

# or

print(time.strftime('%H:%M:%S', time.gmtime(sec)))

"""
3.Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""

n = input("Please, type the number: ")
result = int(n) + int(n * 2) + int(n * 3)
print(result)

"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

n = int(input("Please, type the number: "))
max_n = 0
while n > 0:
    i = n % 10
    if max_n < i:
        max_n = i
    if max_n == 9:
        break
    n = n // 10
print(f"Maximum number is: {max_n}")

"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

revenue = int(input("Please, enter the company revenue: "))
costs = int(input("Please, enter the company costs: "))
if revenue > costs:
    print("The company makes a profit")
    roi = (revenue - costs) / revenue
    print(roi)
    employees_number = int(input("Please, enter the company employees number: "))
    print((revenue - costs) / employees_number)
else:
    print("The company is unprofitable")


"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

a = int(input("a: "))
b = int(input("b: "))
day = 1

while a <= b:
    print(f"{day}-й день: {a:.2f}")
    day += 1
    a = a * 1.1
print(f"{day}-й день: {a:.2f}")
print(f"на {day}-й день спортсмен достиг результата — не менее {int(a)} км.")
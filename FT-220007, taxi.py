from num2words import num2words

try:
    n = int(input("Введите количество сотрудников: "))
except ValueError:
    print('Введено, вероятно, не целое число')
    pass

while True:
    try:
        distances = list(map(int, input("\nВведите через пробел расстояние для каждого сотрудника(в километрах): ").split()))
        if len(distances) != n:
            print('Вы ввели расстояние до дома не для каждого сотрудника')
        else:
            break
    except ValueError:
        print('Введено, вероятно, не целое число')
        pass


while True:
    try:
        tariffs = list(map(int, input("\nВведите через пробел тарифы для каждого сотрудника(в рублях): ").split()))
        if len(tariffs) != n:
            print('Вы ввели тарифы не для каждого сотрудника')
        else:
            break
    except ValueError:
        print('Введено, вероятно, не целое число')
        pass


result = []

for distance in distances:
    min_cost = distance * tariffs[0]
    min_taxi = 1
    for i in range(1, n):
        cost = distance * tariffs[i]
        if cost < min_cost:
            min_cost = cost
            min_taxi = i + 1
    result.append(min_taxi)

print('\nВ следующем порядке соответственно следует заказывать такси для рабочих: ', *result)

total_cost = sum(distance * tariffs[result[i] - 1] for i, distance in enumerate(distances))

if total_cost % 10 == 1 and total_cost != 11:
    end = 'рубль'

elif (total_cost % 10 == 2 or total_cost % 10 == 3 or total_cost % 10 == 4) and (total_cost % 100 > 20 or total_cost < 10):
    end = 'рубля'

else:
    end = 'рублей'

print("Общая стоимость: ", total_cost, end)
print('Общая стоимость: ', num2words(total_cost, lang = 'ru'), end)
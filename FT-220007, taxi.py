from num2words import num2words

while True:
    try:
        N = int(input('Введите количество сотрудников компании: '))
        if N < 1 or N > 1000:
            print('Число должно быть в диапазоне от 1 до 1000')
        else:
            break
    except ValueError:
        print('Должно быть введено целое натуральное число')

def merge_sorting_down(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sorting_down(left)
        merge_sorting_down(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

def merge_sorting_up(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sorting_up(left)
        merge_sorting_up(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

array_distances = []
for i in range(1, N+1):
    while True:
        try:
            distances = int(input(f'Введите расстояние от дома до работы {i}-го сотрудника(целое натуральное число): '))
            if distances < 1:
                print('Недопустимое число')
            else:
                break
        except ValueError:
            print('Должно быть введено целое натуральное число')
    array_distances.append([distances + i / 10 ** len(str(i))])
merge_sorting_up(array_distances)

array_tariffs = []
for i in range(1, N+1):
    while True:
        try:
            tariffs = int(input(f'Введите тариф для {i+1}-го сотрудника(целое натуральное число): '))
            if tariffs < 1:
                print('Недопустимое число')
            else:
                break
        except ValueError:
            print('Должно быть введено целое натуральное число')
    array_tariffs.append([tariffs + i/10 ** len(str(i))])
merge_sorting_down(array_tariffs)

print('')

array_ride = []
for i in range(0, N):
    array_distances_split = str(array_distances[i][0]).split('.')
    array_tariffs_split = str(array_tariffs[i][0]).split('.')
    array_ride.append([array_distances_split[1] + '.' + array_tariffs_split[1] + '.' + str(int(array_distances_split[0
                                                ]) * int(array_tariffs_split[0]))])

merge_sorting_up((array_ride))

for i in range(0, N):
    array_ride_split = array_ride[i][0].split('.')
    print(f"Для {i+1} сотрудника такси под номером: {array_ride_split[1]}, ", end='')

total_cost = 0
for i in range(0, N):
    array_ride_split = array_ride[i][0].split('.')
    total_cost += int(array_ride_split[2])

if total_cost % 10 == 1 and total_cost != 11:
    ending = 'рубль'

elif (total_cost % 10 == 2 or total_cost % 10 == 3 or total_cost % 10 == 4) and (total_cost % 100 > 20 or total_cost < 10):
    ending = 'рубля'

else:
    ending = 'рублей'

print("\nОбщая стоимость: ", total_cost, ending)
print('Общая стоимость: ', num2words(total_cost, lang = 'ru'), ending)

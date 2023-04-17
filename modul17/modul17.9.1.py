def merge_sort(array_list):
    if len(array_list) < 2:
        return array_list[:]
    else:
        middle = len(array_list) // 2
        left = merge_sort(array_list[:middle])
        right = merge_sort(array_list[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def binary_search(array, number, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == number:
       return middle

    elif number < array[middle]:
       return binary_search(array, number, left, middle - 1)
    else:
        return binary_search(array, number, middle + 1, right)


num_sequence = input('Введите последовательность чисел через пробел: ')
try:
    num_sequence_list = list(map(int, num_sequence.split()))
except ValueError:
    print("Ошибка: Введите последовательность чисел")
    exit(1)

try:
    number = int(input('Введите любое число: '))
except ValueError:
    print("Ошибка: Введите число")
    exit(1)

if number > max(num_sequence_list):
    print('Число выходит за верхнюю границу списка, введите меньшее число.')
elif number-1 < min(num_sequence_list):
    print('Число выходит (или равно) за нижнюю границу списка, введите большее число.')
else:
    num_sequence_list_sorted = merge_sort(num_sequence_list)
    print(f'Упорядоченный по возрастанию список: {num_sequence_list_sorted}')

    if number not in num_sequence_list:
        num_sequence_list.append(number)
        num_sequence_list_sorted = merge_sort(num_sequence_list)

    number_position = binary_search(num_sequence_list_sorted, number, 0, len(num_sequence_list_sorted)) - 1

    print(f"Номер позиции элемента в упорядоченном списке: {number_position}")


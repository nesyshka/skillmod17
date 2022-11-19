def binary_search(ls, el, bg, en):
    while int(bg) <= int(en):
        tm = (bg + en) // 2
        if int(el) > int(ls[tm]):
            bg = tm + 1
        else:
            en = tm - 1
    return bg


def binary_sort(input_list: list) -> list:
    for i in range(0, len(input_list)):
        element = input_list[i]
        left, right = 0, i - 1
        ll = binary_search(input_list, element, left, right)
        for index in range(i, ll, -1):
            input_list[index] = input_list[index - 1]
        input_list[ll] = element
    return input_list


def find_position(input_list: list, search_element: int) -> int:
    assert search_element > input_list[0], "Число меньше минимально возможного"
    assert search_element <= input_list[-1], "Число больше максимально возможного"
    for index, element in enumerate(input_list[:-1]):
        if element < search_element and input_list[index + 1] >= search_element:
            return index


digits_line = input("Введите последовательность чисел через пробел:  ")
# digits_line = "10 5 4 8 7 -6"
digits = digits_line.split()
digits = [int(digit) for digit in digits]
sorted_digits = binary_sort(digits)
search_digit = int(input("Введите Ваше желаемое число: "))
# search_digit = 5
index = find_position(input_list=sorted_digits, search_element=search_digit)
print(f"Отсортированный список: {sorted_digits}")
print(f"Номер позиции элемента: {index}")
print()


# array = [i for i in range(1, 100)]  # 1,2,3,4,...
#
# # запускаем алгоритм на левой и правой границе
# print(binary_search(array, element, 0, 99))

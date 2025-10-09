def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    if len(nums) == 0:
        return "ValueError"

    minimum = nums[0]
    maximum = nums[0]
    
    for element in nums:
        if element < minimum:
            minimum = element
        if element > maximum:
            maximum = element

    return(maximum, minimum)

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([]))
print(([1.5, 2, 2.0, -3.1]))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    s = []
    for element in nums:
        if element not in s:
            s.append(element) # + елемент, если нет в списке
    
    s.sort() 
    return s

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))


def flatten(mat: list[list | tuple]) -> list:
    d = []
    for i, row in enumerate(mat):
        if not (isinstance(row, list) or isinstance(row, tuple)): # Список или кортеж
            if isinstance(row, str):
                return "TypeError"
            else:
                return "TypeError"
        # Проходим по элементам строки и просто добавляем их в result
        for elem in row:
            d.append(elem)
    
    return d

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))

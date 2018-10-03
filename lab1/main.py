import csv
from Zoo import Zoo
from InsertionSort import InsertionSort
import time
from datetime import timedelta


def read_data_from_file():
    zoo_list = []
    try:
        with open('printer_data.csv') as csvin:
            reader = csv.reader(csvin)
            for row in reader:
                new_printer = Zoo(row[0], int(row[1]), int(row[2]))
                zoo_list.append(new_printer)
    except FileNotFoundError:
        print("ERROR!")
    return zoo_list


def merge_sort(zoo_list):
    if len(zoo_list) > 1:
        mid = len(zoo_list) // 2
        left = zoo_list[:mid]
        right = zoo_list[mid:]

        merge_sort(left)
        merge_sort(right)

        l = 0
        r = 0
        sum = 0
        while l < len(left) and r < len(right):
            Zoo.compare_count()
            if left[l].visitors_for_year > right[r].visitors_for_year:
                zoo_list[sum] = left[l]
                l = l + 1
                Zoo.compare_count()
                Zoo.changes_count()
            else:
                zoo_list[sum] = right[r]
                r = r + 1
            sum = sum + 1
            Zoo.compare_count()
            Zoo.changes_count()

        while l < len(left):
            zoo_list[sum] = left[l]
            l = l + 1
            sum = sum + 1
            Zoo.compare_count()
            Zoo.changes_count()

        while r < len(right):
            zoo_list[sum] = right[r]
            r = r + 1
            sum = sum + 1
            Zoo.compare_count()
            Zoo.changes_count()

    return zoo_list


if __name__ == "__main__":
##read
    zoo_list = read_data_from_file()
    for index in range(0, len(zoo_list)):
        print(zoo_list[index])
    print('------')
#insertion
    start_time = time.monotonic()
    InsertionSort(zoo_list)
    end_time = time.monotonic()
#out-put
    print("compare",str(Zoo.compare),"changes",str(Zoo.changes))
    print('time of sort', timedelta(seconds=end_time - start_time))
    for index in range(0, len(zoo_list)):
        print(zoo_list[index])
    print('------')
    Zoo.count_reset()

    start_time = time.monotonic()
    zoo_list = merge_sort(zoo_list)
    end_time = time.monotonic()
    print("compare", str(Zoo.compare), "changes", str(Zoo.changes))
    print('time of sort', timedelta(seconds=end_time - start_time))
    for index in range(0, len(zoo_list)):

        print(zoo_list[index])
    print(str(Zoo.compare))
    print(str(Zoo.changes))

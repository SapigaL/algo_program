def insertion_sort(list_to_sort):
    for i in range(1, len(list_to_sort)):
        current = list_to_sort[i]
        position = i
        while position > 0 and current > list_to_sort[position - 1]:
            list_to_sort[position] = list_to_sort[position - 1]
            position -= 1
        list_to_sort[position] = current
    return list_to_sort


if __name__ == "__main__":
    sum = 0

    file = open('discnt_in')
    lines = [line.rstrip('\n') for line in file]
    all_prices = []
    for price in lines[0].split(" "):
        all_prices.append(int(price))

    discount = int(lines[1])
    discount_percent = int(lines[1])
    insertion_sort(all_prices)


    number = len(all_prices)
    number_of_cey = int(number / 3)
    for index in range(0, number_of_cey):
        all_prices[index] = all_prices[index] - all_prices[index] * (discount * 0.01)

    for index in range(0, len(all_prices)):
        sum = sum + all_prices[index]

    my_file = open("discnt_out", "w")
    my_file.write(str(sum))
    my_file.close()

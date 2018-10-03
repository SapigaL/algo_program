from Zoo import Zoo

def InsertionSort(list):

    for index in range(0, len(list)):
        Zoo.compare_count()

        currentvalue = list[index].number_of_animals
        position = index

        while position > 0 and list[position - 1].number_of_animals > currentvalue:
            Zoo.compare_count()
            Zoo.changes_count()

            list[position].number_of_animals = list[position - 1].number_of_animals
            position = position - 1

        list[position].number_of_animals = currentvalue

    return list



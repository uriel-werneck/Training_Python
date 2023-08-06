def recursive_binary_search(lst, number):
    if len(lst) == 0:  # if ths list is empty
        return False  # the searched number is not in the list

    mid = len(lst) // 2  # position of the middle element in the list

    if number == lst[mid]:  # if the searched number is equal to the mid number
        return True  # the searched number is in the list

    elif number > lst[mid]:  # if the searched number is greater than the mid number
        return recursive_binary_search(lst[mid + 1:], number)  # perform a new search in the right half of the list

    elif number < lst[mid]:  # if the searched number is smaller than the mid number
        return recursive_binary_search(lst[:mid], number)  # perform a new search in the left half of the list


list_to_search = [4, 13, 20, 25, 44, 50, 52]  # list, in ascending order
print('List:', list_to_search)  # displays the list

number = int(input('Choose a number: '))  # number to be searched in the list

result = recursive_binary_search(list_to_search, number)  # performs the recursive binary search
print('Result:', result)  # displays the result of the search

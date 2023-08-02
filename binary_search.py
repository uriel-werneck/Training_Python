sorted_list = [2, 5, 18, 22, 25, 32, 44, 50]  # sorted list in ascending order

print('List:', sorted_list)  # display the list

start = 0  # starting position of the list 
end = len(sorted_list) - 1  # ending position of the list 
mid = (start + end) // 2  # central position of the list

value = int(input('Choose a value: '))  # value to be searched in the list

while True:
    if value == sorted_list[mid]:  # if the searched value is at the center of the list
        print(f'{value} is in the list!')  # the value has been found
        break

    elif value > sorted_list[mid]:  # if the searched value is greater than the value at the center of the list
        start = mid + 1  # continue the search in the right half of the list
               
    elif value < sorted_list[mid]:  # if the searched value is less than the value at the center of the list
        end = mid - 1  # continue the search in the left half of the list

    if start > end:  # if the starting position is greater than the ending position
        print(f'{value} is not in the list!')  # the value is not in the list
        break

    mid = (start + end) // 2  # calculate the central position at each iteration

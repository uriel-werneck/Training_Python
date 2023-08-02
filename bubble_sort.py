my_list = [17, 4, 23, 8, 19, 12]

print('Unsorted list:', my_list)

flag = 1  # flag to start the while loop

while flag != 0:  # while flag is different from 0
    flag = 0  # if no values are swapped, the loop will be terminated
    for i in range(1, len(my_list)):  # check each element in the list starting from the second one
        if my_list[i] < my_list[i - 1]:  # if the value ahead is smaller than the value behing
            my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]  # swap the values
            flag = 1  # if any value is swapped, the loops restarts

print('Sorted list:', my_list)

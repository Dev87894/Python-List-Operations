# Find the average of all numbers in a list.
l = [2, 55, 11, 33, -7]
total = 0
length = 0
for number in l:
    total += number
    length += 1
average = total / length
print(average)


# Reverse a list without using reverse() or slicing [::-1].
l = [2, 55, 11, 33, -7]
l1 = []
for number in range(len(l)-1,-1,-1):
    l1.append(l[number])
print(l1)


l = ["devesh","raghu","rohit"]
l1=[]
for i in range(len(l)-1,-1,-1):
    l1.append(l[i][::-1])
print(l1)


# Find the second-largest number in a list.
l = [2333, 7, 91, 45, 12, 68, 34, 5, 87, 511]
largest_no = l[0]
second_largest_no = l[1]
for number in l:
    if number > largest_no:
        second_largest_no = largest_no
        largest_no = number
    elif number > second_largest_no and number != largest_no:
        second_largest_no = number
print("largest_no:", largest_no)
print("second_largest_no:", second_largest_no)


# Find the second-smallest number in a list.
l = [2, 70, 91, 45, 120, 680, 34, 50, -87, 51]
smallest_no = l[0]
second_smallest_no = l[1]
for number in l:
    if number < smallest_no:
        second_smallest_no = smallest_no
        smallest_no = number
    elif number < second_smallest_no and number != smallest_no:
        second_smallest_no = number
print("smallest_no:", smallest_no)
print("second_smallest_no:", second_smallest_no)


# Count how many times a particular element occurs in a list without using count().
l = [2, 7, 9, 2, 2, 6, 3, 7, 4, 5]
element = 2
frequency = {}
# frequency = 0
for number in l:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
# or,
# for number in l:
#     if number == element:
#         frequency += 1
print(frequency)


# Find the index of a particular element without using index().
l = [2, 7, 9, 2, 2, 6, 3, 7, 4, 5]
element = 2
print(l.index(2,5))
# or,
for i, number in enumerate(l):
    if number == element:
        print(i)


# Replace every negative number in a list with 0.
l = [2, 7, -9, 2, -2, 6, 3, -7, 4, 5]
for i,number in enumerate(l):
    if number < 0:
        l[i]=0
print(l)


# Multiply every element of a list by 2 and store the results in a new list.
l = [2, 7, -9, 2, -2, 6, 3, -7, 4, 5]
l1 = []
for number in l:
    l1.append(number * 2)
print(l1)
# or,
l1 = list(map(lambda x: x * 2, l))
print(l1)


# Find the elements that are present in the first list but not in the second list.
l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
unique = []
for element in l1:
    if element not in l2:
        unique.append(element)
print(unique)


# Combine two lists without using +.
l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
l1.extend(l2)
print("combination of two list:", l1)


# Find the union of two lists without duplicates.
l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
for number in l2:
    if number not in l1:
        l1.append(number)
print("union of two list:", l1)


# Find the intersection of two lists without using set().
l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
intersection = []
for number in l1:
    if number in l2:
        intersection.append(number)
print("intersection of two list:", intersection)


# Check whether a list is sorted in ascending order.
l1 = [1, 2, 3, 4, 5, 1]
is_sorted = True
for i in range(len(l1) - 1):
    if l1[i] > l1[i + 1]:
        is_sorted = False
        break
if is_sorted:
    print("list is sorted in ascending order")
else:
    print("list is not sorted in ascending order")


# Check whether a list is a palindrome.
l1 = [1, 2, 3, 2, 1, 3]
is_palindrome = False
if l1 == l1[::-1]:
    is_palindrome=True
if is_palindrome:
    print("list is palindrome")
else:
    print("list is not palindrome")
# or,
l2 = l1.copy()
l2.reverse()
if l1 == l2:
    print("list is palindrome")
else:
    print("list is not palindrome")


# Find all pairs of numbers whose sum is equal to a given number.
lst = [2, 4, 3, 5, 7, 8]
target = 10
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            print(f"{lst[i]} + {lst[j]} = {target}")


# Find the element that occurs most frequently in a list.
l = [8, 7, 7, 2, 2, 6, 2, 6, 5]
frequency = {}
for i in l:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print("frequency of element in the list:", frequency)
most_frequent_ele = l[0]
for value in frequency:
    if frequency[value] > frequency[most_frequent_ele]:
        most_frequent_ele = value
print("most frequent element in the list is:", most_frequent_ele)


# Move all zeros to the end of a list.
lst = [0, 0, 1]
for number in lst:
    if number == 0:
        lst.append(0)
        lst.remove(number)
print(lst)

# Find the third-largest unique number in a list.
lst = [51, 8, 92, 14, 6, 3, 81]
largest_no = 0
second_largest_no = 0
third_largest_no = 0
for number in lst:
    if number > largest_no:
        third_largest_no = second_largest_no
        second_largest_no = largest_no
        largest_no = number
    elif number > second_largest_no and number != largest_no:
        third_largest_no = second_largest_no
        second_largest_no = number
    elif (
        number > third_largest_no
        and number != second_largest_no
        and number != third_largest_no
    ):
        third_largest_no = number

print("largest_no:", largest_no)
print("second_largest_no:", second_largest_no)
print("third_largest_no:", third_largest_no)


# Find the missing number from a list containing numbers from 1 to n.
lst = [1, 2, 3, 5, 6]
for i in range(len(lst)):
    if (i + 1) != lst[i]:
        print(i + 1)
        break
# or,
n = len(lst) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(lst)
missing_number = expected_sum - actual_sum
print("missing number in the list is :", missing_number)


# Find all duplicate elements in a list.
lst = [1, 2, 3, 2, 4, 5, 1, 6, 3]
duplicate_elements = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            duplicate_elements.append(lst[i])
print("duplicate elements of the list are : ", duplicate_elements)


# Rotate a list to the right by k positions.
lst = [1, 2, 3, 4, 5]
print(lst)
k = 2
lst = lst[-k:] + lst[:-k]
print(lst)

# Flatten a nested list without using external libraries.
lst = [[1, 2], [3, 4], [5, 6]]
print("original list:\n",lst)
flatten_list=[]
for sublist in lst:
    for element in sublist:
        flatten_list.append(element)
print("Flatten list of the existing list:\n",flatten_list)

# Find the longest word in a list of words.
words = ["pomegranate", "banana", "kiwi", "watermelon"]
longest_word = words[0]
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("Longest word in the list is :", longest_word)


# Sort a list without using sort() or sorted().
lst = [1, 8, 92, 14, 6, 3, 81]
for i in range(len(lst)):
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)

# Find the maximum consecutive 1s in a list.
lst = [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1]
count = 0
max_count = 0
for number in lst:
    if number == 1:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0
print("maximum consecutive 1s in a list :", max_count)

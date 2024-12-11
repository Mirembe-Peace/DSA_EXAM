# initializing an empty array
array = []

#adding elements to the array
array.append(40)
array.append(89)
array.append(56)
array.append(92)
array.append(90)


#printing the array
print(f'the new array is: {array}')

#removing an element by its index
def remove_element(A, index):
    for i in range(len(A)):
        if index == A[i]:
            A.remove(i)
            print(A)
    return A

unwanted = int(input('Enter the position of the number that you want to remove from the array starts at 0:'))
reduced_array = remove_element(array, unwanted),
#printing the array without that element
print(reduced_array)

#displaying the lenth of the array
print(f'The array has {len(array)} elements')


#Checking if an element exists in the array
def linear_search(array,target):
    for i in range(len(array)):#loop through the array
        if array[i] == target: #check if the element at that index in the array matches the target
            return target      #if it matches the target return the element     

target = int(input('Enter a number: ')) # user input a number 
result = linear_search(array,target)
if result is not None:
    print('The target is found and it is: ',result)
else:
    print('The target is not found')
    


#sorting the arra in ascending order
def selection_sort(A):                         #selection sort that takes on the array as it's pararmeter
    for i in range(len(A)):                    #loop through all the elements
        smallest = i                           #let the smallest element be the one at hand
        for j in range(i + 1, len(A)):         #starting from the element after the first loop through the list
            if A[j] < A[smallest]:             #if there is an element smaller than the first smallest element
                smallest = j                    #let that new element now be our smallest element
        A[smallest], A[i] = A[i], A[smallest]   #Swap this element with the one we first had
    return A

sorted_array = selection_sort(array)
print(f'Here is the sorted array {sorted_array}')    #print the sorted array




#clearing all elements of the array
array.clear() 
print(f'the cleared array: {array}')


# DISCLAIMER!!!! even after the AI auto generate was disabled it was still showing up in my work but, i did not use it so it may appear in the screen shorts but i i did not use it
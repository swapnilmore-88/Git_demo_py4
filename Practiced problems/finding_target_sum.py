'''Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
Note: There will be one solution for each input and do not use the same element twice. Go to the editor
Input: numbers= [10,20,30,40,50,60,70], target=50
Output: 3, 4'''
class A:
    def __init__(self, list_1):
        k = 1
        for i in list_1:
            for j in list_1[k:]:
                if i+j == 50:
                    # print(list_1.index(i),list_1.index(j))
                    print(list_1.index(i),list_1.index(j))
            k += 1


a = A([10,20,30,40,50,60,70])

"jvdjfvvdsf"
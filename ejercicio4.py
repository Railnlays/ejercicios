import random

def merge(l_left: list[int], l_right: list[int]) -> list[int]:
    l: list[int] = []
    count_left = 0
    count_right = 0
    while count_left < len(l_left) or count_right < len(l_right):
        if count_left == len(l_left):
           return l + l_right[count_right:]
        if count_right == len(l_right):
           return l + l_left[count_left:]
        if l_left[count_left] < l_right[count_right]:
            l.append(l_left[count_left])
            count_left += 1
        else:
            l.append(l_right[count_right])
            count_right += 1
    return l

def mergesort(l: list[int]) -> list[int]:
    if len(l) == 1:
        return l
    pivote = len(l) // 2
    return merge(mergesort(l[:pivote]),mergesort(l[pivote:]))

def main():
    l_1: list[int] = [1,5,6]
    l_2: list[int] = [2,4,8]
    l: list[int] = [5,8,15,6,3,79]
    print(mergesort(l))
    l_random = [random.randint(1,100000) for _ in range(1000)]
    print(mergesort(l_random))

if __name__  == "__main__":
    main()
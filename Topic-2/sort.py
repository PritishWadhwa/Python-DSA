def selectionSort(arr):
    for i in range(len(arr)):
        minIdx = i
        for j in range(i+1, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    for i in arr:
        print(i, end=" ")
    print()


def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    for i in arr:
        print(i, end=" ")
    print()


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    for i in arr:
        print(i, end=" ")
    print()


def countSort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]

    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1

    for i in output_arr:
        print(i, end=" ")
    print()


arr = [1, 5, 5421, -454, 100, 0]
selArr = arr[:]
bubArr = arr[:]
insArr = arr[:]
countArr = arr[:]

selectionSort(selArr)
bubbleSort(bubArr)
insertionSort(insArr)
countSort(countArr)

for i in arr:
    print(i, end=" ")

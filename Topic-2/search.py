def linearSearch(arr, tgt):
    for i in arr:
        if i == tgt:
            print("Present")
            return
    print("Not Present")


def binarySearch(arr, tgt, s, e):
    if(s > e):
        print("Not Present")
        return
    else:
        mid = (s + e) // 2
        if arr[mid] == tgt:
            print("Present")
            return
        elif arr[mid] > tgt:
            return binarySearch(arr, tgt, s, mid - 1)
        return binarySearch(arr, tgt, mid + 1, e)


linArr = [4, 51, 0, 1, 2, 4, 2, 34, 1, 23, 1, 234]
binArr = [-1000, 1, 2, 3, 4, 6, 100, 10000]

linearSearch(linArr, 51)
linearSearch(linArr, 5000)

binarySearch(binArr, -1000, 0, len(binArr) - 1)
binarySearch(binArr, 10000, 0, len(binArr) - 1)

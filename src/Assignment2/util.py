def main(arr):
    arr.sort()
    arr1 = []
    for i in arr:
        if i not in arr1:
            arr1.append(i)
    print(arr1[-2])
    return(arr1[-2])

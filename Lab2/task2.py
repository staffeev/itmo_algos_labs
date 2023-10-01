def sort_bubble(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == '__main__':
    arr = list(map(float, input().split()))
    print(sort_bubble(arr))
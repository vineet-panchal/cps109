def faroShuffle(items, out):
    newList = []
    right = []
    left = []
    for i in range(0, int((len(items) / 2))):
        right.append(items[i])
    for i in range(int(len(items) / 2), len(items)):
        left.append(items[i])
    for i in range(0, len(right)):
        if out:
            newList.append(right[i])
            newList.append(left[i])
        else:
            newList.append(left[i])
            newList.append(right[i])
    return newList

if __name__ == "__main__":
    print(faroShuffle([1, 2, 3, 4, 5, 6, 7, 8], True))
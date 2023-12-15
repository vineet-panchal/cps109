def rlen(items):
    if items == []:
        return 0
    else:
        return 1 + rlen(items[1:])

if __name__ == "__main__":
    print(rlen([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
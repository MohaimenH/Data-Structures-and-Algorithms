def bubbleSort(items):

    passes = 0

    l = list(items)

    while (passes != len(l) - 1):

        passes = 0

        for x in range(1, len(l)):
            if l[x-1] > l[x]:
                l[x], l[x-1] = l[x-1], l[x]
            else:
                passes += 1

    return l

if __name__ == '__main__':
    data = [256,2,875,2,2,365,84,0,984,-1,568,52211,8792,3,4,65,98,1025,476]
    print(bubbleSort(data))
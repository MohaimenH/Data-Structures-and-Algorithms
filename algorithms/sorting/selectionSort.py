def selectionSort(items):

    l = list(items)
   
    for i in range(len(l) - 1):

        minimum = l[i]

        pos = i

        for x in range(i, len(l)):
            if l[x] < minimum:
               pos = x 
               minimum = l[x]
        

        l[i], l[pos] = minimum, l[i]
        
    return l

if __name__ == '__main__':
    data = [256,2,875,2,2,365,84,0,984,-1,568,52211,8792,3,4,65,98,1025,476]
    print(selectionSort(data))
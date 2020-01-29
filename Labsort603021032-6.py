def sublist(unsortlist):
    if len(unsortlist) == 1 :
        return unsortlist

    mid = len(unsortlist)//2
    left_list = unsortlist[:mid]
    right_list = unsortlist[mid:]

    left_list = sublist(left_list)
    right_list = sublist(right_list)

    return merge(left_list, right_list)

def merge(left_list,right_list):
    sort = []
    while len(left_list)!=0 and len(right_list)!=0:
        if left_list[0] > right_list[0]:
            sort.append(right_list[0])
            right_list.remove(right_list[0])
        else:
            sort.append(left_list[0])
            left_list.remove(left_list[0])

    if len(left_list) == 0:
        sort = sort + right_list
    else:
        sort = sort + left_list

    return sort

def shellsort(unsortlist):
    gap = len(unsortlist)//2
    while gap > 0:
        for index in range(len(unsortlist)):
            temp = unsortlist[index]
            subindex = index
            while subindex >= gap and unsortlist[subindex - gap] > temp:
                unsortlist[subindex] = unsortlist[subindex - gap]
                subindex = subindex - gap

            unsortlist[subindex] = temp
        gap = gap//2
    return unsortlist

unsortlist = [64,34,50,25,12,22,11]
print("Merge")
print(sublist(unsortlist))
print("shell")
print(shellsort(unsortlist))
def bubble_sort(l1):

    for i in range(len(l1)-1,0,-1):
        swa=True

        for j in range(0,i):
            if l1[j+1] < l1[j]:
                l1[j] , l1[j+1] = l1[j+1], l1[j]
                swa=False
        if swa:
            return


def insertion_sort(l2):
    #we start from 1 as the first element is considered trivially sorted
    
    for k in range(1,len(l2)):
        cur_value=l2[k]
        cur_pos=k

        while cur_pos>0 and l2[cur_pos-1] > cur_value:
            l2[cur_pos] = l2[cur_pos-1]
            cur_pos=cur_pos-1

        l2[cur_pos]=cur_value

def linear_search(l1,item):

    for i in range(len(l1)):
        if l1[i]==item:
            return i
    return -1

def binary_search(l1,item):
    low=0
    high=len(l1)-1

    while low<=high:
        mid = (low+high)//2
        if(l1[mid]==item):
            return mid
        elif(l1[mid]<item):
            low=mid+1
        else:
            high=mid-1

    return -1

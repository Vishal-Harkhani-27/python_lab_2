li = [12,35,9,56,24]

def myfun(li):
    size = len(li)

    #swaping
    tmp = li[0]
    li[0]=li[size-1]
    li[size-1]=tmp

    return li
print(myfun(li))
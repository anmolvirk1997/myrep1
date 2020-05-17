def sort(list):
    for i in range(len(list)-1):
        minpos=i
        for j in range(i+1,len(list)):
            if list[minpos]>list[j]:
                minpos=j
        list[i],list[minpos]=list[minpos],list[i]


list=[9,3,2,1,6,5,0,8]
sort(list)
print(list)

#

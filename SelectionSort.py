def SelectionSort(size,arr):

    for ind in range(size):
        # print("Outer loop index is "+str(ind))
        min_index=ind
        for j in range(ind+1,size):
            # print("inner loop index is "+str(j))
            if(arr[j]<arr[min_index]):
                # print("minimum element found is " +str(arr[j])+"at"+str(j))
                min_index=j
        (arr[ind],arr[min_index])=(arr[min_index],arr[ind])

arr=[2,3,4,8,13,5,673,3,6,53,54,-3]
size=len(arr)
SelectionSort(size,arr)
print(arr)

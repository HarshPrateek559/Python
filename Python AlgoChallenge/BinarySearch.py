def binarySearch(arr, x):
    #This function will calculate and return the position of the number in the given array
    high = len(arr)-1
    low = 0
    mid = 0

    while low<=high:
        mid = (low + high)//2
        
        if(arr[mid]<x):
            low = mid+1
        elif(arr[mid]>x):
            high = mid-1
        else:
            return mid
    
    return "The number is not present in the list"

arr = [66,4,244,6,9,99,24,7,3,23,677,34,55]

x = int(input("Enter the number that is to be searched: "))

print(binarySearch(arr, x))


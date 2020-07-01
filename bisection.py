def bisection_recr(n,arr,start,stop):
    if start > stop:
        return f"{n} not found in list"
    else:
        mid= (start+stop)//2

        if n == arr[mid]:
            return f"{n} found at index {mid}"
        elif n > arr[mid]:
            return bisection_recr(n,arr,mid+1,stop)
        else:
            return bisection_recr(n,arr,start,mid-1)



l=[1,2,3]
for num in range(5):
    print(bisection_recr(num,l,0,len(l)-1))

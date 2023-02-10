arr=[1,2,3,0,-6,6]
n=len(arr)
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k]==0:
                # print("("a[i]","a[j]","a[k]")")
                print(arr[i], arr[j], arr[k])

print(arr[i], arr[j], arr[k])
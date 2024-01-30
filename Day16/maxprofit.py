def maxprofit(arr):
    n=len(arr)
    maxprofit=0
    localmin=arr[0]
    for i in range(1, n):
        if arr[i] > localmin:
            profit=arr[i]-localmin
            maxprofit=max(maxprofit, profit)
        else:
            localmin=arr[i]
    return maxprofit

arr=[]
n=int(input("Enter the no of stock : "))
print("Enter prices : ")
for i in range(n):
    element=int(input())
    arr.append(element)
print("Stock Prices :", arr)

print("Max Profit :", maxprofit(arr))

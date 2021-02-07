print("Enter how many row you went to print: ")
Row = int(input())
k = 2 * Row - 2
for i in range(0,Row):
    for j in range(0,k):
        print(end=" ")
    k = k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
for i in range(Row,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k=k+1
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
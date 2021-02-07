print("Enter how many row you went to print: ")
Row = int(input())
c = 1
while c<=Row:
    print(c*"*")
    c+=1
while Row>0:
    print(Row*"*")
    Row=Row-1
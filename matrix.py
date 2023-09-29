first_multiple_input=input().rstrip().split()
n=int(first_multiple_input[0])
m=int(first_multiple_input[1])
matrix=[]
for i in range(n):
    matrix_item=input()
    matrix.append(matrix_item)

result = ""
flag = False
for j in range(m):
    for i in range(n):
        if matrix[i][j].isalnum():
            result=result+matrix[i][j]
            flag=False
        else:
            flag=True
            result += " "
print(result)

tenDem = input("Nhập tên đệm: ")
ten = input("Nhập tên: ")
name = tenDem + " " + ten

n = int(str(len(tenDem)) + str(len(ten)))

tmp = n
arr = []
sum = 0

while (tmp > 0):
    sum += tmp % 10
    arr.append(str(tmp % 10))
    tmp = int(tmp / 10)

arr.reverse()

print(name, "thi n = ", n, " = ", ' + '.join(arr), " = ", sum)
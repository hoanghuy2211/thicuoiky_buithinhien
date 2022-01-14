ho = input("Nhập họ: ")
tenDem = input("Nhập tên đệm: ")
ten = input("Nhập tên: ")
fullName = ho + " " + tenDem + " " + ten

n = int(str(len(ho)) + str(len(tenDem)) + str(len(ten)))

tmp = n
num = 0

while (tmp > 0):
    num = num * 10 + tmp % 10
    tmp = int(tmp / 10)

res = " là số thuận nghịch" if (n == num) else " Không là số thuận nghịch"

print(fullName, "thi n =", n, res)
ten = input("Nhập tên: ")

n = int(str(len(ten)))

d = dict()
for i in range(1, n + 1):
    d[i] = i * i

print(ten, "thi n = ", n)
print("Kết quả: ", d)
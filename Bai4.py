fullName = input("Nhập họ tên: ")
id = input("Nhập mã sinh viên: ")
values = input("Nhập chuỗi kí tự: ")

lst = values.split(",")
tup = tuple(lst)

print("Thông tin của bạn: ", fullName, id)
print("List: ", lst)
print("Tuple: ", tup)
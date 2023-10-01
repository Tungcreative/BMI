l = eval(input('Hãy lập ra một set cách nhau bởi dấu phẩy: '))
print('')
print('Bài 1:')
s = {l}
# Yêu cầu người dùng nhập vào số n
n = int(input("Nhập vào số n: "))
# Kiểm tra số n có trong set hay không
if n in l:
    print("Số", n, "đã có trong set.")
else:
    print("Số", n, "chưa có trong set.")
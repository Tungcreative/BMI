personal_info = {}
personal_info['name'] = input("Hãy nhập tên của bạn: ")
personal_info['age'] = int(input("Hãy nhập tuổi của bạn: "))
print("Thông tin cá nhân của bạn: ")
for key, value in personal_info.items():
    print(f"{key}: {value}")

print()

n = int(input('Hãy nhập số người cần điền: '))
people = []
print('Thông tin nhập theo cấu trúc như sau: tên/tuổi')
for i in range(1, n+1):
    info = input("Thông tin cá nhân của người thứ {} -> {}: ".format(i, n))
    people.append(info)
    print('Thông tin của các người đã điền là: ', info)
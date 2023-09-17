#Bài 3: Chữa
with open("../Bài tập về nhà/Văn bản/Data.txt", "r") as file:
    a = file.read().strip()
    text = a.split('\n')
    print(text)
    numbers = [ str(i) for i in text ]
    print(numbers)

#Bài 4: Chữa
ho_ten = input("Nhập họ và tên của bạn: ")
tuoi = input("Nhập tuổi của bạn: ")

with open("../Bài tập về nhà/Văn bản/Data.txt", "w") as file:
    file.write(f'Họ và tên: {ho_ten}\n')
    file.write(f'Tuổi: {tuoi}\n')
print("Thông tin đã được ghi vào Data.txt")
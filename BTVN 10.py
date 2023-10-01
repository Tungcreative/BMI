S = input("Nhập họ và tên đầy đủ: ")
# Xoá bỏ dấu khoảng trắng ở đầu và cuối xâu S
S = S.strip()
# Viết hoa từng chữ cái đầu mỗi từ
S = S.title()
# Xoá 2 dấu khoảng cách liên tiếp để chỉ còn 1 khoảng cách
while " " in S:
    S = S.replace(" ", " ")
    print(S)
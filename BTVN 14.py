#Bài 1:
name = input("Nhập họ và tên của bạn: ")
word_count = len(name.split())
print(f"Đáp án: {word_count} từ.")

#Bài 2:
def kiem_tra_CMND(cmnd):
    if len(cmnd) < 9 or len(cmnd) > 11:
        return False

    for char in cmnd:
        if not char.isdigit():
            return False

    return True


cmnd = input("Nhập số chứng minh nhân dân của bạn: ")

if kiem_tra_CMND(cmnd):
    print("Số CMND của bạn hợp lệ.")
else:
    print("Số CMND của bạn không hợp lệ.")

#Bài 3:
def validate_email(email):
    if email.count('@') != 1:
        return False

    parts = email.split('@')
    if len(parts) != 2:
        return False

    username, domain = parts[0], parts[1]

    if ' ' in email:
        return False

    if '.' not in domain or domain[-4:] != '.com':
        return False

    return True


email = input("Hãy nhập địa chỉ email của bạn: ")
if validate_email(email):
    print("Địa chỉ email của bạn hợp lệ.")
else:
    print("Địa chỉ email của bạn không hợp lệ.")
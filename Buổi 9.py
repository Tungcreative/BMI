n = 0

def kiem_tra_nam_nhuan_hay_khong(n):
    if n%4 == 0 and n%400 !=0:
        return True
    else:
        return False

nam = int(input('Hãy nhập năm mà bạn muốn kiểm tra: '))

if kiem_tra_nam_nhuan_hay_khong(nam) == True:
    print(f'Năm {nam} là năm nhuận.')
else:
    print(f'Năm {nam} là năm không nhuận.')

print()

def tinh_trung_binh_cong(danh_sach):
    if len(danh_sach) == 0:
        return 0
    else:
        return sum(danh_sach) / len(danh_sach)
day_so = eval(input('Hãy nhập một dãy số: '))
my_list = (day_so)
average = tinh_trung_binh_cong(my_list)
print(average)
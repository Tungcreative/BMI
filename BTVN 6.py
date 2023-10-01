from datetime import date

day_of_birth = int(input('NHập ngày sinh của bạn: '))
month_of_birth = int(input('NHập tháng sinh của bạn: '))
year_of_birth = int(input('Nhập năm sinh của bạn: '))
print(f'Ngày tháng năm sinh của bạn là: {day_of_birth}/{month_of_birth}/{year_of_birth}')

today_date = date.today().strftime('%Y')

print('Tuổi hiện tại của bạn là: ', int(today_date) - year_of_birth)
from datetime import date
dob = input("Nhập ngày tháng năm sinh của bạn (DD/MM/YYYY): ")
dob_date = date(int(dob[6:]), int(dob[3:5]), int(dob[0:2]))
current_date = date.today()
age = current_date - dob_date
print("Tuổi hiện tại của bạn là: ", age.days // 365,'tuổi.')
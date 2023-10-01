dien = float (input ('Hãy nhập số điện bạn dùng: '))
if dien >= 0:
    if 0 <= dien <= 50:
        tien = dien*1678
    if 51 <= dien <= 100:
        tien = 1678*50 + 1734*(dien-50)
    if 101 <= dien <= 200:
        tien = 1678*50 + 1734*50 + 2014*(dien-100)
    if 201 <= dien <= 300:
        tien = 1678*50 + 1734*50 + 2014*100 + 2536*(dien-200)
    if 301 <= dien <= 400:
        tien = 1678*50 + 1734*50 + 2014*100 + 2536*100 + 2834*(dien-300)
    if 401 <= dien:
        tien = 1678*50 + 1734*50 + 2014*100 + 2536*100 + 2834*100 + 2927*(dien-400)
print ('Số tiền điện phải trả là: ',tien,'đồng.')
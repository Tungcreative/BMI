
file=open('Văn bản/Sinh vien.txt', 'a', encoding='utf-8')
while True:
    maSV=input('Hãy nhập mã sinh viên: ')
    if (maSV==''):
        break
    tenSV=input('Hãy nhập tên sinh viên: ')
    lopSV=input('Hãy nhập lớp sinh viên: ')
    quequanSV=input('Hãy nhập quê quán sinh viên: ')
    file.write('\t'.join([maSV, tenSV, lopSV, quequanSV])+'\n')
file.close()
print('Danh sách sinh viên vừa nhập là: ')
print('\t'.join(['Mã', 'Họ tên', 'Lớp', 'Quê quán']))
file=open('Văn bản/Sinh vien.txt', 'r', encoding='utf-8')
for SV in file.readlines():
    print(SV.replace('\n', ''))
file.close()
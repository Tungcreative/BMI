my_tuple = eval(input('Hãy nhập các số: '))
unique_elements = set(my_tuple)
for element in unique_elements:
    count = my_tuple.count(element)
    print(f"số {element} xuất hiện {count} lần")
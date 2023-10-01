# Bài 1:
with open("Văn bản/Data.txt", "w") as file:
    for i in range(1, 11):
        file.write(str(i) + "\n")

# Bài 2:
with open("Văn bản/Data.txt", "r") as file:
    data = file.read()
    print(data)


# Bài 2:

def fomat_text(text):
    formatted_text = text.capitalize()
    words = formatted_text.split()
    formatted_text = ' '.join(words)
    return formatted_text

input_text = input('Hãy nhập câu bạn muốn chỉnh sửa lại: ')
formatted_text = fomat_text(input_text)
print(formatted_text)


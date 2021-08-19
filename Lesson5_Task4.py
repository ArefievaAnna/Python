"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
 Новый блок строк должен записываться в новый текстовый файл."""

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('test_4.txt', 'r', encoding="utf-8") as file_obj:

    #content = file_obj.read().split('\n')

    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

#in encode  return codecs.charmap_encode(input,self.errors,encoding_table)[0]
#UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-3:
# character maps to <undefined> - to solve it using encoding

with open('test_4_new.txt', 'w+', encoding="utf-8") as file_obj_2:
    file_obj_2.writelines(new_file)




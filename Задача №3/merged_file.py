files = ['1.txt', '2.txt', '3.txt']
file_contents = []

for file_name in files:
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_contents.append((file_name, len(lines), lines))

# Сортируем содержимое файлов по количеству строк
file_contents.sort(key=lambda x: x[1])

# Записываем отсортированное содержимое в новый файл
with open('merged_file.txt', 'w') as result_file:
    for file_name, num_lines, lines in file_contents:
        result_file.write(f'{file_name}\n{num_lines}\n')
        result_file.writelines(lines)
        result_file.write('\n')

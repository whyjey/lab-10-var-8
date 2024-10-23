with open('example.txt', 'w') as file:
    file.write('This is an example text with numbers like 123 and 456.')
# Відкрити файл example.txt для читання
with open('example.txt', 'r') as file:
    text = file.read()

# Ініціалізувати словник для підрахунку цифр
digit_count = {str(i): 0 for i in range(10)}

# Підрахувати частоту появи кожної цифри
for char in text:
    if char.isdigit():
        digit_count[char] += 1

# Записати результати у файл result.txt
with open('result.txt', 'w') as result_file:
    for digit, count in digit_count.items():
        result_file.write(f'{digit}: {count} у тексті\n')

print("Частота появи цифр записана у файл result.txt")
import os
import shutil

# Створити каталог WEST на диску D: (якщо він не існує)
west_dir = 'D:/WEST'  
if not os.path.exists(west_dir):
    os.makedirs(west_dir)

# Отримати список всіх файлів з поточного каталогу, що починаються з 'w'
current_dir = os.getcwd()
files_to_copy = [f for f in os.listdir(current_dir) if f.lower().startswith('w')]

# Копіювати файли до каталогу WEST
for file in files_to_copy:
    shutil.copy(os.path.join(current_dir, file), west_dir)

# Вивести кількість скопійованих файлів
print(f'Кількість файлів, які починаються з "w": {len(files_to_copy)}')

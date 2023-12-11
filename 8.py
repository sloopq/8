import csv
import random
import os

# Загрузка файла CSV
def load_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data

# Функция Show()
def show(file_name, output_type='top', rows=5, separator=','):
    data = load_csv(file_name)
    
    if output_type == 'bottom':
        data = data[-rows:]
    elif output_type == 'random':
        data = random.sample(data, min(rows, len(data)))
    else:
        data = data[:rows]

    for row in data:
        print(separator.join(row))

# Функция Info()
def info(file_name):
    data = load_csv(file_name)
    header = data[0]
    data = data[1:]

    num_rows = len(data)
    num_columns = len(header)

    print(f"Количество строк с данными (не считая заголовок): {num_rows}x{num_columns}")

    print("Список имен полей данных с количеством не пустых значений и типом значений:")
    for i, column_name in enumerate(header):
        non_empty_values = sum(1 for row in data if row[i])
        value_types = {type(row[i]).__name__ for row in data if row[i]}
        value_type = ', '.join(value_types) if value_types else 'empty'
        print(f"{column_name} {non_empty_values} {value_type}")


# Функция DelNaN()
def del_nan(file_name):
    data = load_csv(file_name)
    header = data[0]
    data = data[1:]

    cleaned_data = [header]
    for row in data:
        if all(row):
            cleaned_data.append(row)

    with open('cleaned_data.csv', 'w', newline='') as cleaned_file:
        writer = csv.writer(cleaned_file)
        writer.writerows(cleaned_data)

# Функция MakeDS()
def make_ds(file_name):
    data = load_csv(file_name)
    header = data[0]
    data = data[1:]

    random.shuffle(data)
    split_index = int(0.7 * len(data))

    learning_data = [header] + data[:split_index]
    testing_data = [header] + data[split_index:]

    os.makedirs('workdata/Learning', exist_ok=True)
    os.makedirs('workdata/Testing', exist_ok=True)

    with open('workdata/Learning/train.csv', 'w', newline='') as learning_file:
        writer = csv.writer(learning_file)
        writer.writerows(learning_data)

    with open('workdata/Testing/test.csv', 'w', newline='') as testing_file:
        writer = csv.writer(testing_file)
        writer.writerows(testing_data)

# Проверка функции Show()
show('data.csv', output_type='top', rows=5, separator=',')

# Проверка функции Info()
info('data.csv')

# Проверка функции DelNaN()
del_nan('data.csv')

# Проверка функции MakeDS()
make_ds('cleaned_data.csv')
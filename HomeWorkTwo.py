def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cat_info = {"id": cat_id, "name": name, "age": age}
                    cats_info.append(cat_info)
                except ValueError:
                    print("Невірний формат рядка: {}".format(line))

        return cats_info
    except FileNotFoundError:
        print("Файл не знайдено")
        return None

# Приклад використання:
cats_info = get_cats_info("path/to/cats_file.txt")
if cats_info is not None:
    print(cats_info)

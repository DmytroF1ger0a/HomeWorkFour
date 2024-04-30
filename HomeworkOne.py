def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary_str = line.strip().split(',')
                    salary = int(salary_str)
                    total_salary += salary
                    num_developers += 1
                except ValueError:
                    print("Невірний формат рядка: {}".format(line))

        if num_developers == 0:
            return 0, 0  # у випадку, якщо файл порожній

        average_salary = total_salary / num_developers
        return total_salary, average_salary
    except FileNotFoundError:
        print("Файл не знайдено")
        return None

# Виклик функції та виведення результату
total, average = total_salary("path/to/salary_file.txt")
if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

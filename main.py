import sys

def read_file(input_file):
    """
    Зчитує вміст файлу та повертає список рядків.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            return infile.readlines()
    except FileNotFoundError:
        print(f"Помилка: Файл '{input_file}' не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка під час зчитування файлу: {e}")
        return []

def filter_lines(lines, keyword):
    """
    Відбирає рядки з ключовим словом.
    """
    return [line for line in lines if keyword in line]

def write_to_file(output_file, lines):
    """
    Записує відфільтровані рядки у файл.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.writelines(lines)
        print(f"{len(lines)} рядків було записано у '{output_file}'")
    except Exception as e:
        print(f"Сталася помилка під час запису у файл: {e}")

def main():
    if len(sys.argv) != 3:
        print("Використання: python script.py <вхідний_файл> <ключове_слово>")
    else:
        _, input_file, keyword = sys.argv
        lines = read_file(input_file)
        filtered_lines = filter_lines(lines, keyword)
        write_to_file('filtered.txt', filtered_lines)

if __name__ == "__main__":
    main()

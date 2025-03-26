import sys

def filter_lines(input_file, keyword):
    """
    Зчитує вміст файлу, відбирає рядки з ключовим словом та записує їх у "filtered.txt"
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            filtered_lines = [line for line in infile if keyword in line]

        with open('filtered.txt', 'w', encoding='utf-8') as outfile:
            outfile.writelines(filtered_lines)

        print(f"{len(filtered_lines)} рядків було записано у 'filtered.txt'")

    except FileNotFoundError:
        print(f"Помилка: Файл '{input_file}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Використання: python script.py <вхідний_файл> <ключове_слово>")
    else:
        _, input_file, keyword = sys.argv
        filter_lines(input_file, keyword)

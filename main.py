def filter_lines(input_file, keyword, output_file):
    """Фільтрує рядки, що містять ключове слово, з вхідного файлу і записує їх у вихідний файл."""
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
        
        filtered_lines = [line for line in lines if keyword in line]

        with open(output_file, 'w') as outfile:
            outfile.writelines(filtered_lines)
        print(f"Збережено {len(filtered_lines)} рядків у файл {output_file}")
    except FileNotFoundError:
        print(f"Файл {input_file} не знайдений!")
    except Exception as e:
        print(f"Сталася помилка: {e}")

# Приклад використання функції
input_file = 'example.txt'
keyword = 'приколад'  # Ваше ключове слово
output_file = 'filtered.txt'

filter_lines(input_file, keyword, output_file)

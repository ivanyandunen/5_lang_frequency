import sys
import re
import collections

def load_data(filepath):
    with open(filepath) as input_file:
        return input_file.read().lower()


def get_most_frequent_words(file_content):
    words_list = re.findall(r'\w+', file_content)
    most_frequent_words = collections.Counter(words_list).most_common(10)
    return most_frequent_words


if __name__ == '__main__':
    try:
        file_content = load_data(sys.argv[1])
        most_frequent_words = get_most_frequent_words(file_content)
        for word, frequency in most_frequent_words:
            print(word, frequency)
    except (IndexError, FileNotFoundError):
        print('Input file is not specified or missed')
    except UnicodeDecodeError:
        print('Incorrect file')

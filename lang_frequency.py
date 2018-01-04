import sys

def load_data(filepath):
    words_count = {}
    with open(filepath) as input_file:
        for line in input_file:
            for word in line.split():
                words_count[word] = words_count.get(word, 0) + 1
    return words_count


def get_most_frequent_words(file_content):
    words_frequency = [(frequency, word) for word, frequency in file_content.items()]
    words_frequency.sort()
    words_frequency.reverse()
    words_frequency = [(word, frequency) for frequency, word in words_frequency]
    return words_frequency


def print_most_frequent_words(words_frequency):
    for word, frequency in words_frequency[:10]:
            print(word, frequency)


if __name__ == '__main__':
    try:
        file_content = load_data(sys.argv[1])
        words_frequency = get_most_frequent_words(file_content)
        print_most_frequent_words(words_frequency)
    except (IndexError, FileNotFoundError):
        print('Input file is not specified or missed')
    except UnicodeDecodeError:
        print('Incorrect file')

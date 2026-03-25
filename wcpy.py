import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Program to count number of words, lines, characters and bytes.'
    )

    parser.add_argument('-c', '--bytes', action='store_true',help='Counts the number of bytes.', dest='is_counting_bytes')
    parser.add_argument('-l', '--lines', action='store_true', help='Counts the number of lines.', dest='is_counting_lines')
    parser.add_argument('-w', '--words', action='store_true', help='Counts the number of words.', dest='is_counting_words')
    parser.add_argument('file', help='The file to read.')

    args = parser.parse_args()

    if args.is_counting_bytes:
        print(get_number_of_bytes(args.file), args.file)
    elif args.is_counting_lines:
        print(get_number_of_lines(args.file), args.file)
    elif args.is_counting_words:
        print(get_number_of_words(args.file), args.file)

def get_number_of_bytes(path_to_file):
    with open(path_to_file, 'rb') as file:
        data = file.read()
        return len(data)
    
def get_number_of_lines(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return len(lines)

def get_number_of_words(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file:
        total_words = 0

        # walrus operator - allows assignments to be done in expressions
        # we don't have to do `line = file.readline()` before the while loop to define what `line` is
        # and then `line = file.readline()` after the while loop
        while (line := file.readline()):
            total_words += len(line.split())
        return total_words

if __name__ == '__main__':
    main()
    
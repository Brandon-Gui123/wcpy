import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Program to count number of words, lines, characters and bytes.'
    )

    parser.add_argument('-c', '--bytes', action='store_true',help='Counts the number of bytes.', dest='is_counting_bytes')
    parser.add_argument('file', help='The file to read.')

    args = parser.parse_args()

    if args.is_counting_bytes:
        print(get_number_of_bytes(args.file), args.file)

def get_number_of_bytes(path_to_file):
    with open(path_to_file, 'rb') as file:
        data = file.read()
        return len(data)
    


if __name__ == '__main__':
    main()
    
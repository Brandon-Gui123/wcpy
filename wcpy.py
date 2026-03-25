import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Program to count number of words, lines, characters and bytes.'
    )

    parser.add_argument('-c', '--bytes', action='store_true',help='Counts the number of bytes.', dest='is_counting_bytes')
    parser.add_argument('-l', '--lines', action='store_true', help='Counts the number of lines.', dest='is_counting_lines')
    parser.add_argument('-w', '--words', action='store_true', help='Counts the number of words.', dest='is_counting_words')
    parser.add_argument('-m', '--chars', action='store_true', help='Counts the number of characters.', dest='is_counting_chars')
    parser.add_argument('file', help='The file to read.')

    args = parser.parse_args()

    file_stats = get_file_stats(args.file)
    stats_to_show = []

    # handle no flags given
    if not args.is_counting_lines and not args.is_counting_words and not args.is_counting_bytes:
        stats_to_show.append(file_stats['lines'])
        stats_to_show.append(file_stats['words'])
        stats_to_show.append(file_stats['bytes'])
    else:
        if args.is_counting_lines:
            stats_to_show.append(file_stats['lines'])
        
        if args.is_counting_words:
            stats_to_show.append(file_stats['words'])

        if args.is_counting_chars:
            stats_to_show.append(file_stats['chars'])

        if args.is_counting_bytes:
            stats_to_show.append(file_stats['bytes'])

    # need to convert each item in the array to a string so that after each string a space is added
    print(' '.join([str(value) for value in stats_to_show]), args.file)
    

def get_file_stats(path_to_file) -> dict[str, int]:
    byte_count = 0
    line_count = 0
    word_count = 0
    char_count = 0

    with open(path_to_file, 'rb') as file:
        for line in file:
            byte_count += len(line)

            # if we're in CR or LF, we won't find any CRLF, so we get the correct amount as usual
            # if we're in CRLF, inclusion-exclusion principle helps us get the correct amount
            line_count += line.count(b'\n') + line.count(b'\r') - line.count(b'\r\n')
            
            word_count += len(line.split())
            char_count += len(line.decode('utf-8', errors='ignore'))

    return {
        'bytes': byte_count,
        'lines': line_count,
        'words': word_count,
        'chars': char_count
    }

if __name__ == '__main__':
    main()
    
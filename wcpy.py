import argparse
import sys

from dataclasses import dataclass
from typing import BinaryIO

@dataclass 
class FileStats:
    bytes: int
    lines: int
    words: int
    chars: int

def main():
    parser = argparse.ArgumentParser(
        description='Program to count number of words, lines, characters and bytes.'
    )

    parser.add_argument('-c', '--bytes', action='store_true',help='Counts the number of bytes.', dest='is_counting_bytes')
    parser.add_argument('-l', '--lines', action='store_true', help='Counts the number of lines.', dest='is_counting_lines')
    parser.add_argument('-w', '--words', action='store_true', help='Counts the number of words.', dest='is_counting_words')
    parser.add_argument('-m', '--chars', action='store_true', help='Counts the number of characters.', dest='is_counting_chars')
    parser.add_argument('file', nargs='?', default='-', help='The file to read. If omitted or is "-", read from standard input.')

    args = parser.parse_args()

    if args.file == '-':
        stream = sys.stdin.buffer
        display_name = ''
        close_after = False
    else:
        stream = open(args.file, 'rb')
        display_name = args.file
        close_after = True

    try:    
        file_stats = get_file_stats(stream)
    finally:
        if close_after:
            stream.close()

    stats_to_show: list[str] = []

    flags = (args.is_counting_lines, args.is_counting_words, args.is_counting_bytes, args.is_counting_chars)
    if not any(flags):
        fields = ('lines', 'words', 'bytes')
    else:
        # iterates pairs and each time flag is True, this generator yields name
        fields = tuple(
            name for name, flag in (
                ('lines', args.is_counting_lines),
                ('words', args.is_counting_words),
                ('chars', args.is_counting_chars),
                ('bytes', args.is_counting_bytes)
            ) if flag
        )
    
    # using getattr to pull the value in the field with a specific name
    stats_to_show = [str(getattr(file_stats, field_name)) for field_name in fields]

    # need to convert each item in the array to a string so that after each string a space is added
    print(' '.join([str(value) for value in stats_to_show]), display_name)
    

def get_file_stats(stream: BinaryIO) -> FileStats:
    byte_count = 0
    line_count = 0
    word_count = 0
    char_count = 0

    for line in stream:
        byte_count += len(line)

        # if we're in CR or LF, we won't find any CRLF, so we get the correct amount as usual
        # if we're in CRLF, inclusion-exclusion principle helps us get the correct amount
        line_count += line.count(b'\n') + line.count(b'\r') - line.count(b'\r\n')
        
        word_count += len(line.split())
        char_count += len(line.decode('utf-8', errors='ignore'))

    return FileStats(byte_count, line_count, word_count, char_count)

if __name__ == '__main__':
    main()
    
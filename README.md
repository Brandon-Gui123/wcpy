# wcpy

A `wc`-like tool I made for the "[Build Your Own wc Tool](https://codingchallenges.fyi/challenges/challenge-wc)" coding challenge at [codingchallenges.fyi](https://codingchallenges.fyi/).

## Prerequisites

- Python 3.9+

## How to Use

- View help information

  ```bash
  python wcpy.py --help
  ```

- See lines, words and bytes count of a file

  ```bash
  python wcpy.py my_file.txt
  ```

- See lines, words and bytes count of the output of another program

  ```bash
  cat my_file.txt | python wcpy.py
  ```

- See just the character count of a file

  ```bash
  python wcpy.py -m my_file.txt
  ```

## Developer Notes

Learning Python was a bit of a struggle to me since I came from a C++/C# background but I started getting better during my university's Machine Learning module.

This coding challenge is great for me to put some of that Python knowledge to use and to explore more of it along the way.
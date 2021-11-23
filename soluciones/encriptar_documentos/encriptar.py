"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List


def _read_data(file: str) -> None:
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def _write_data(file: str, data: List[str]) -> None:
    with open(file, 'w', encoding="utf-8") as f:
        for line in data:
            f.write(line)
            f.write('\n')


def encriptar(data: List[str]) -> List[str]:
    return list(line[::-1] for line in data)[::-1]


def main():
    data = _read_data('input.txt')
    data = encriptar(data)
    _write_data('inv.txt', data)


if __name__ == '__main__':
    main()
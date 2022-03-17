import sqlite3
import os


def connect():
    return sqlite3.connect(os.path.dirname(__file__) + "/db/kaffe.db")


def print_error(msg):
    print(f"❗️\033[0;31m{msg}\033[0m")


def print_header(header):
    print("=" * len(header))
    print(header)
    print("=" * len(header))


def print_column_titles(*titles, width=15, widths=None):
    if widths is None:
        widths = [width] * len(titles)
    for i in range(len(titles)):
        if i < len(widths):
            widths.append(width)
    print_header(
        "\t".join(str(title).ljust(width) for title, width in zip(titles, widths))
    )


def get_placeholders(array):
    return ", ".join("?" for i in range(len(array)))

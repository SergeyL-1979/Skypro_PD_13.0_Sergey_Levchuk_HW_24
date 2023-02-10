from typing import Iterable
import re

def filter_query(value: str, data: Iterable[str]):
    return filter(lambda x: value in x, data)


def unique_query(data, *args, **kwargs):
    return set(data)


def limit_query(value, data):
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value, data):
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value, data):
    reverse = value == "desc"
    return sorted(data, reverse=reverse)

def regex_query(value: str, data: Iterable[str]):
    # data = read_file(LOG_FILE)
    regex = re.compile('images/\\w+\\.svg|png|jpg|jpeg')
    result = filter(lambda v: regex.search(v), data)
    print(''.join(result))
    return regex.findall(value)




from typing import Iterable
import re

def filter_query(value: str, data: Iterable[str]) -> Iterable[str]:
    return filter(lambda x: value in x, data)


def regex_query(value: str, data: Iterable[str]) -> Iterable[str]:
    return filter(lambda v: re.compile(value).search(v), data)


def unique_query(data: Iterable[str], *args: str, **kwargs: int) -> Iterable[str]:
    return set(data)


def limit_query(value: str, data: Iterable[str]) -> Iterable[str]:
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value: str, data: Iterable[str]) -> Iterable[str]:
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value: str, data: Iterable[str]) -> Iterable[str]:
    reverse = value == "desc"
    return sorted(data, reverse=reverse)

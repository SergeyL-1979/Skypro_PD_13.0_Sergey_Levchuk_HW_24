from typing import Iterable, Set, Iterator, List, Any, AnyStr
import re

def filter_query(value: str, data: Iterable[str]) -> Iterator[str]:
    """
    Функция позволяет делать фильтрацию по запросу: 'POST' или 'GET'
    """
    return filter(lambda x: value in x, data)


def regex_query(value: str, data: Iterable[str]) -> Iterable[str]:
    """
    Функция позволяет делать фильтрацию по регулярным выражениям
    """
    return filter(lambda v: re.compile(value).search(v), data)


def unique_query(data: Iterable[str], *args: AnyStr, **kwargs: Any) -> Set[str]:
    """
    Функция возвращает уникальное значение с помощью set()
    """
    return set(data)


def limit_query(value: str, data: Iterable[str]) -> Iterable[str]:
    """
    Функция ограничивает вывод запроса в параметре limit:
    """
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value: str, data: Iterable[str]) -> Iterable[str]:
    """
    Функция выполняет split по index в списке
    """
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value: str, data: Iterable[str]) -> List[str]:
    """
    Функция позволяет сортировать вывод данных
    """
    reverse = value == "desc"
    return sorted(data, reverse=reverse)

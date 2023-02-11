from typing import Optional, Iterable, Callable, Dict, List

from functions import filter_query, limit_query, map_query, sort_query, unique_query, regex_query


CMD_TO_FUNCTIONS: Dict[str, Callable] = {
    'filter': filter_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
    'unique': unique_query,
    'regex': regex_query
 }

def read_file(file_name: str) -> Iterable[str]:
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            yield line


def build_query(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]) -> List[str]:
    """
    Функция строит запрос для вывода данных по словарю CMD_TO_FUNCTIONS
    """
    if data is None:
        prepared_data: Iterable[str] = read_file(file_name)
    else:
        prepared_data = data

    return list(CMD_TO_FUNCTIONS[cmd](value=value, data=prepared_data))

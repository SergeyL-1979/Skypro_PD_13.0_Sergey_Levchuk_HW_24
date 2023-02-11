# Skypro_PD_13.0_Sergey_Levchuk_HW_24

## Задача

Усовершенствовать язык программирования и добавить команду — regex.

## Регулярные выражения

Допустим, у вас есть лог-файл работы веб-сервера:

```python
1.181.2.178 [17/May/2015:20:05:36] "GET / HTTP/1.1" 200
1.125.2.148 [17/May/2015:20:05:19] "GET /?flav=rss20 HTTP/1.1" 200
1.170.2.204 [17/May/2015:20:05:03] "POST /?flav=atom HTTP/1.1" 200
1.163.30.77 [17/May/2015:20:05:36] "GET /images/gle.png HTTP/1.1" 200
1.163.30.77 [17/May/2015:20:05:37] "GET /blog/dot.html HTTP/1.1" 200
```

Рассмотрим команду **cmd1=regex value1=<regex>**

Команда regex принимает в качестве аргумента регулярное выражение, по которой нужно будет фильтровать строки входных данных. В результате выполнения команды **cmd1=regex value1=images\/\w+\.png** (запросы в виде images/*.png, то есть получить запросы на картинки png) должно быть выведено:

```python
1.163.30.77 [17/May/2015:20:05:36] "GET /images/gle.png HTTP/1.1" 200
```

## Типизация

После выполнения предыдущего пункта нужно внедрить типизацию в ваш проект. Необходимо добиться, чтобы команда mypy выполнялась без ошибок.

Исходное состояние проекта при запуске mypy:

```python
lesson24_project_solution % mypy app.py
app.py:12: error: Function is missing a type annotation
app.py:37: error: Function is missing a return type annotation
Found 2 errors in 1 file (checked 1 source file)
```

Исходное состояние:

```python
lesson24_project_solution % mypy app.py
app.py:12: error: Function is missing a type annotation
app.py:37: error: Function is missing a return type annotation
Found 2 errors in 1 file (checked 1 source file)
```

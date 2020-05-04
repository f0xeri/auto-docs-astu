# auto-docs-astu
Генерация отчётов и таблиц для дисциплины «Программирование и информатика»

## Установка

Способов два:
1. Скачать из репозитория auto-docs-astu.exe
2. Запустить самому из исходника, но потребуется библиотека [python-docx](https://github.com/python-openxml/python-docx):

```bash
pip install python-docx
```

## Подготовка исходника для генерации таблицы функций
Для правильной генерации таблицы с описанием функций, достаточно написать комментарий с описанием прямо над функцией.
Не смотря на то, что синтаксически необходимо использовать многострочный комментарий (```/* ... */```), программа будет работать верно, только если комментарий написан в одну строку. Следующая за комментарием строка считается заголовком функции и вносится в таблицу.

#### Пример:
```cpp
/*func Добавляет новый элемент в список */
void push(List &list, float value)
{
    list.top = new Node(value, list.top);
}
```
#### Результат:
![Результат работы](https://i.imgur.com/7ML55VG.png)

## Использование

При первом запуске будет создан файл ```config.ini``` (если Вы его не скачали сразу).
Пример заполнения:
```
[Параметры]
номер лабы = 6
номер варианта = 9
автор = Иванов И.И.
преподаватель - Иванова.И.И.
имя исходника = lab6.cpp
```
Файл с исходным кодом (в примере - ```lab6.cpp```, (любой текстовый формат, главное чтобы комментарии в коде были верно написаны) должен находиться в директории с программой.
Если ```config.ini``` уже существует, будет сгенерирован docx документ с названием исходника (в примере - ```lab6.docx```).
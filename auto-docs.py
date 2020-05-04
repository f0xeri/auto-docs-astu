import configparser
import os

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, Cm

lab_names = [
    "Знакомство с интегрированной средой Code::Blocks",
    "Организация циклов в С++",
    "Функции. Передача параметра по значению. Перегрузка",
    "Функции. Передача параметра по ссылке",
    "Обработка числовых последовательностей с использованием текстовых файлов",
    "Списки, массивы, векторы",
    "Матрицы",
    "Строки. Процедурная и объектно-ориентированная библиотеки. Широкие строки.",
    "Бинарные файлы",
    "Структуры и файлы",
    "Многомодульные проекты",
    "Обработка строк, хранящихся в файле",
    "Множества",
    "Рекурсивные функции",
    "Обработка исключений. Функции, генерирующие исключения",
    "Указатели на функции",
    "Реализация стека и очереди на базе списка, на базе вектора и на базе динамического массива",
    "Длинная арифметика",
    "Динамические структуры данных и файлы",
    "Структура-пара",
    "Функции с переменным числом параметров",
    "Объединения. Перечисления. Типы, определяемые пользователем",
    "Поразрядные операции и битовые поля",
    "Шаблоны функций"
]

purposes = [
    "Получение первичных навыков работы в интегрированной среде Code::Blocks",
    "выработка навыков программирования циклических вычислительных процессов;\nпорядок работы с вложенными циклами;\nформатированный вывод данных.",
    "закрепление навыков в организации итерационных и арифметических циклов, использования вспомогательных алгоритмов (функций с передачей параметров по значению).",
    "выработка навыков передачи параметров в функцию по ссылке.",
    "\nприобретение навыков работы с текстовыми файлами;\nзакрепление навыков в организации итерационных и арифметических циклов, использования вспомогательных алгоритмов (функций с передачей параметров по значению). ",
    "Знакомство с динамическими информационными структурами на примере одно- и двунаправленных списков, динамических массивов и векторов",
    "выработка навыков реализации матриц в языке C++ различными способами и закрепление навыков реализации типовых алгоритмов (классификация, поиск, сортировка).",
    "Получить практические навыки работы с библиотеками cstring, string, а также работы с широкими строками и символами wstring.",
    "выработка навыков работы с бинарными файлами",
    "1. Получить практические навыки работы со структурами и файлами.\n2. Получить практические навыки организации массивов/векторов с элементами сложной структуры.",
    None,
    None,
    "Изучить правила описания и использования контейнера Set из стандартной библиотеки шаблонов. Получить навыки в решении практических задач и ребусов с использованием теории множеств.",
    "Получить практические навыки работы с рекурсивными функциями.",
    None,
    None,
    "1.Изучить алгоритмы формирования и просмотра динамической структуры данных – «стек». Научиться программировать различные действия над его элементами\n2.Изучить алгоритмы формирования и просмотра динамической структуры данных «очередь». Научиться программировать различные действия над ее элементами.",
    None,
    None,
    "закрепление навыков использования структур.",
    "Приобрести практические навыки работы с функциями с переменным числом параметров и закрепить использование указателей на функции.",
    "изучить синтаксис и правила работы с объединениями, перечислениями и типами, определяемые пользователем",
    "изучить теорию и научиться программировать поразрядные операции и битовые поля.",
    "научиться создавать шаблоны функций для работы с любыми типами данных без переписывания кода программы."
]


def set_func_table(tab):
    row_cells = tab.row_cells(0)
    tab.cell(0, 0).paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    tab.cell(0, 1).paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    func = row_cells[0].paragraphs[0].add_run('Функция')
    desc = row_cells[1].paragraphs[0].add_run('Назначение')
    func.bold = True
    desc.bold = True


def get_funcs_from_cpp(path):
    funcs_list = []
    with open(path) as src:
        for line in src:
            if line.startswith('/*func'):
                description = line
                description = description.rstrip()
                description = description.replace('/*func ', '')
                description = description.replace('*/', '')
                if '*/' not in line:
                    for line in src:
                        if '*/' in line:
                            break
                code = next(src).rstrip()
                funcs_list.append((code, description))
    return funcs_list


def fill_table(tab, funcs):
    for i in range(len(funcs)):
        new_row = tab.add_row()
        new_row.cells[0].paragraphs[0].text = funcs[i][0]
        new_row.cells[1].paragraphs[0].text = funcs[i][1]


def set_table_style(tab):
    tab.allow_autofit = False
    for row in tab.rows:
        for cell in row.cells:
            paragraphs = cell.paragraphs
            cell.width = Cm(8.74)
            for paragraph in paragraphs:
                paragraph.paragraph_format.line_spacing = 1.5
                for run in paragraph.runs:
                    run.font.name = 'Times New Roman'
                    font = run.font
                    font.size = Pt(12)


def set_p_style(p, font_size, is_bold):
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = 0
    for run in p.runs:
        run.font.name = 'Times New Roman'
        run.bold = is_bold
        font = run.font
        font.size = Pt(font_size)


def create_config(path):
    config = configparser.ConfigParser()
    config.add_section("Параметры")
    config.set("Параметры", "Номер лабы", "")
    config.set("Параметры", "Номер варианта", "")
    config.set("Параметры", "Автор", "")
    config.set("Параметры", "Преподаватель", "")
    config.set("Параметры", "Имя исходника", "")

    with open(path, "w") as config_file:
        config.write(config_file)


def read_config(path):
    config = configparser.ConfigParser()
    config.read(path)
    cfg = []
    cfg.append(config.get("Параметры", "Номер лабы"))
    cfg.append(config.get("Параметры", "Номер варианта"))
    cfg.append(config.get("Параметры", "Автор"))
    cfg.append(config.get("Параметры", "Преподаватель"))
    cfg.append(config.get("Параметры", "Имя исходника"))
    return cfg


path = "config.ini"
if not os.path.exists(path):
    create_config(path)
    print("config.ini создан.")
    exit(0)

cfg = read_config(path)
lab_number = cfg[0]
if lab_number != '':
    lab_number = int(lab_number)
var = cfg[1]
if var != '':
    var = int(var)
author_name = cfg[2]
teacher_name = cfg[3]
cpp_path = cfg[4]

output_filename = cpp_path.split(".")[0] + '.docx'

funcs = get_funcs_from_cpp(cpp_path)

document = Document()
document._body.clear_content()

if lab_number != '' and var != '':
    header_ = document.add_paragraph()
    header_.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = header_.add_run()
    r.font.size = Pt(18)
    r.bold = True
    r.font.name = 'Times New Roman'

    r2 = header_.add_run()
    r2.font.size = Pt(14)
    r2.bold = True
    r2.font.name = 'Times New Roman'

    r.text = 'Отчёт\xa0по\xa0лабораторной\xa0работе\xa0№\xa0{lab} Вариант\xa0{var}\n'.format(lab=lab_number, var=var)
    r2.text = 'Дисциплина\xa0«Программирование\xa0и\xa0информатика», 2\xa0семестр\n«' + lab_names[lab_number - 1] + '»'

    author = document.add_paragraph()
    author.paragraph_format.line_spacing = 1.5
    author_r1 = author.add_run()
    author_r1.text = 'Выполнил \n'
    author_r1.bold = True
    author_r1.font.size = Pt(12)
    author_r1.font.name = 'Times New Roman'

    author_r2 = author.add_run()
    author_r2.text = 'студент группы ДИПРб11 ____________ {author_name} «____»__________ 2020\n'.format(
        author_name=author_name)
    author_r2.font.name = 'Times New Roman'
    author_r2.font.size = Pt(12)

    author_r3 = author.add_run()
    author_r3.text = 'Проверила \n'
    author_r3.bold = True
    author_r3.font.name = 'Times New Roman'
    author_r3.font.size = Pt(12)

    author_r4 = author.add_run()
    author_r4.text = 'ст. преп. кафедры АСОИУ ____________ {teacher_name} «____»__________ 2020'.format(
        teacher_name=teacher_name)
    author_r4.font.name = 'Times New Roman'
    author_r4.font.size = Pt(12)

    if purposes[lab_number - 1] is not None:
        purpose = document.add_paragraph()
        purpose_r1 = purpose.add_run()
        purpose_r1.text = "Цель работы: "
        purpose_r1.font.name = 'Times New Roman'
        purpose_r1.font.size = Pt(12)
        purpose_r1.bold = True

        purpose_r2 = purpose.add_run()
        purpose_r2.text = purposes[lab_number - 1]
        purpose_r2.font.name = 'Times New Roman'
        purpose_r2.font.size = Pt(12)

func_label = document.add_paragraph('Таблица X.X - Функции, обеспечивающие работу программы')
set_p_style(func_label, font_size=12, is_bold=False)

func_tab = document.add_table(1, 2, 'TableGrid')
set_func_table(func_tab)
fill_table(func_tab, funcs)
set_table_style(func_tab)

# tab2_label = document.add_paragraph('Таблица X.X - Важнейшие переменные программы')

document.save(output_filename)

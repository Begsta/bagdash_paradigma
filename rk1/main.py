from functions import func1, func2, func3
from data import *


def main():
    # Связь один-ко-многим
    one_to_many = [(op.name, lang.title)
                   for lang in langs
                   for op in ops
                   if op.lang_id == lang.id]

    # Связь многие-ко-многим
    many_to_many_temp = [(ol.op_id, ol.lang_id) for ol in ops_langs]
    many_to_many = [(op.name, lang.title)
                    for op_id, lang_id in many_to_many_temp
                    for op in ops if op.id == op_id
                    for lang in langs if lang.id == lang_id]
    print(f"Б1: {func1(one_to_many)}\nБ2: {func2(one_to_many, langs)}\nБ3: {func3(many_to_many)}")

if __name__ == '__main__':
    main()

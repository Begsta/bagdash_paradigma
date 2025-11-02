# Функция для Б1
def func1(one_to_many : list) -> list:
    return sorted(one_to_many, key=lambda x: x[1])

# Функция для Б2
def func2(one_to_many : list, langs : list) -> list:
    res_b2_unsorted = []
    for lang in langs:
        ops_count = len([x for x in one_to_many if x[1] == lang.title])
        if ops_count > 0:
            res_b2_unsorted.append((lang.title, ops_count))
    res_b2 = sorted(res_b2_unsorted, key=lambda x: x[1], reverse=True)
    return res_b2

# Фунция для Б3
def func3(many_to_many : list) -> list:
    return [(op_name, lang_title) for op_name, lang_title in many_to_many if op_name.endswith("ov")]
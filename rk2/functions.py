

def get_one_to_many(languages, operators):
    return [(op.name, lang.title)
            for lang in languages
            for op in operators
            if op.lang_id == lang.id]

def get_many_to_many(operators, languages, ops_langs):
    temp = [(ol.op_id, ol.lang_id) for ol in ops_langs]
    return [(op.name, lang.title)
            for op_id, lang_id in temp
            for op in operators if op.id == op_id
            for lang in languages if lang.id == lang_id]

def func1(one_to_many):
    return sorted(one_to_many, key=lambda x: x[0])

def func2(one_to_many, languages):
    res = []
    for lang in languages:
        ops_count = len([x for x in one_to_many if x[1] == lang.title])
        if ops_count > 0:
            res.append((lang.title, ops_count))
    return sorted(res, key=lambda x: x[1], reverse=True)

def func3(many_to_many, suffix):
    return [(op_name, lang_title) for op_name, lang_title in many_to_many if op_name.endswith(suffix)]

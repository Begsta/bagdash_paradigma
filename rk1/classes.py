# Операторы(if, else, ...)
class Operator:
    def __init__(self, id, name, lang_id):
        self.id = id
        self.name = name
        self.lang_id = lang_id


# Языки программирования
class Language:
    def __init__(self, id, title):
        self.id = id
        self.title = title


# Для связи многие-ко-многим
class OperatorLanguage:
    def __init__(self, op_id, lang_id):
        self.op_id = op_id
        self.lang_id = lang_id
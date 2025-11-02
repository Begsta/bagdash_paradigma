from classes import *

# Языки программирования
langs = [
    Language(1, "Python"),
    Language(2, "C++"),
    Language(3, "Java"),
]

# Операторы
ops = [
    Operator(1, "print", 1),
    Operator(2, "cout", 2),
    Operator(3, "for", 1),
    Operator(4, "if", 3),
    Operator(5, "breakov", 2), # пример фамилии/оператора на "ов"
]

# Связи многие-ко-многим, у одного оператора может быть много языков программирования 
ops_langs = [
    OperatorLanguage(1, 1),
    OperatorLanguage(2, 2),
    OperatorLanguage(3, 1),
    OperatorLanguage(4, 3),
    OperatorLanguage(5, 2),
    OperatorLanguage(5, 3),
]
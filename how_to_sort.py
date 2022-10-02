_test_dict = {
    'string1': 3,
    'string22': 2,
    'string333': 1
}


def sort_by_func(*args):
    print(args)
    return args[0][1]


print(sorted(_test_dict.items(), key=sort_by_func))

# каждый проход по _test_dict.items() возвращает кортеж из (key, value),
# указание x[1] означает, что мы будет сортировать именно по value
print(sorted(_test_dict.items(), key=lambda x: x[1]))

# например, мы можем также отсортировать по длине ключа, используя другую функцию
# чтобы более длинные ключи шли раньше
print(sorted(_test_dict, key=lambda x: len(x), reverse=True))

# выше я указал только _test_dict, что значит, что вернутся только отсортированные ключи
# чтобы вернулось сразу все, надо сделать вот так
print(sorted(_test_dict.items(), key=lambda x: len(x[0]), reverse=True))

# имеет смысл потренироваться в сортировке по разным признакам, это будет полезно.
# например, если вы сортируете объекты, вы можете их сортировать по атрибуту вида
# sorted(object_list, key=lambda x: x.attribute)
# 1. Разобрать домашнее задание по файлам
# 2. Рассказать про linux
# 3. Рассказать про циклы
# 4. Расскажать про .get
# 5. Рассказать про функции (лямбда функции, например при поиске)
# 6. Про импорты (перекрестные), если успеем


homework_file = open('q4_urls.txt', 'r')
_dict = {}

for _string in homework_file.readlines():
    if _string not in _dict:
        _dict[_string] = 0
    _dict[_string] += 1

homework_file.close()

# я специально использовал тут open без with, чтобы четко отметить последовательность
# (открыть файл, записать в файл, закрыть файл)

new_file = open('sorted_strings', 'w')

for key, value in sorted(_dict.items(), key=lambda x: x[1], reverse=True):
    new_file.write(f'{value} {key}')

new_file.close()

print('*' * 100)

a = [1, 2, 3]
# как выглядит for, через while. Это тождественно, но через for меньше кода
a_iter = iter(a)
while True:
    try:
        print(next(a_iter))
    except StopIteration:
        # print('Stop Iteration')
        break
# в принципе это две идентичные инструкции (за исключением print(StopIteration))
for i in a:
    print(i)

# цикл for это эквивалент раздачи листовок, которые вам выдали на подработку
# пока не раздаст все листовки, или не бросите это дело в исключительном случае,
# он будет работать пока не исчерпается итератор
fatigue = 0
for i in range(1, 100):
    fatigue += 20
    print('отдал листовку')
    if fatigue >= 100:
        print('ну нафиг')
        break

# цикл while это конвеер, который работает независимо от состояния итератора
count = 0
while True:
    print('привез деталь')
    count += 1
    if count > 5:
        break


# генератор, это итератор, который не занимает оперативную память и хранит там только текущее состояние
# эквивалент - дозатор салфеток в уборной, берете столько, сколько нужно, и когда нужно.
# к нему обращаются только тогда, когда в этом есть необходимость
def func_gen():
    for x in range(1, 10):
        yield x


print('*' * 100)

url = 'https://mailru.ru/?ref=1234&utm=dtf&browser=true'
url2 = 'https://mailru.ru/?ref=1234&utm=dtf'

url_dict = {
    'ref': 1234,
    'utm': 'dtf',
    'browser': True
}

url2_dict = {
    'ref': 1234,
    'utm': 'dtf'
}
# в словарях при доступе к элементам используйте get.
# используйте квадратные скобки, когда вам ТОЧНО нужно взять оттуда элемент, так вы отследите ошибку
print(url_dict.get('browser'))
print(url2_dict.get('browser', False))

for key, value in url_dict.items():
    print(f'{key}: {value}')

print('*' * 100)


def _func(x):
    return x * 2


print(_func(10))


def func1(x):
    return x * 2


def func2(x):
    return x + 100500


# используйте лямбда функции, чтобы сократить количество кода, например в такой ситуации
func_dict = {
    True: lambda x: x * 2,
    False: func2
}

print(func_dict[True](10))
print(func_dict[False](10))

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

new_file = open('sorted_strings', 'w')

for key, value in sorted(_dict.items(), key=lambda x: x[1], reverse=True):
    new_file.write(f'{value} {key}')

new_file.close()

print('*' * 100)

a = [1, 2, 3]

a_iter = iter(a)

# циклы


while True:
    try:
        print(next(a_iter))
    except StopIteration:
        print('Stop Iteration')
        break

fatigue = 0
for i in range(1, 100):
    fatigue += 20
    print('отдал листовку')
    if fatigue >= 100:
        print('ну нафиг')
        break

count = 0
while True:
    print('привез деталь')
    count += 1
    if count > 5:
        break


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


func_dict = {
    True: lambda x: x * 2,
    False: func2
}

print(func_dict[True](10))
print(func_dict[False](10))

while True:
    break

# for


class A:
    def save(self):
        print(f'SAVE FROM A')
        super().save()


class B:
    def save(self):
        print(f'SAVE FROM B')


class C:
    def save(self):
        print(f'SAVE FROM C')


class D:
    def save(self):
        print(f'SAVE FROM D')
        super().save()


class Test1(A, B, C, D):
    def save(self):
        print('save from TEST1')


class Test2(A, B, C, D):
    def save(self):
        print('save from TEST2')
        super().save()


if __name__ == '__main__':
    test1 = Test1()
    test1.save()

    test2 = Test2()
    test2.save()

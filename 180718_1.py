class Person(object):
    def __init__(self, year, month, day, sex):
        self.year = year
        self.month = month
        self.day = day
        self.sex = sex

    def __str__(self):
        return '{}년 {}월 {}일생 {}입니다.'.format(self.year, self.month, self.day, self.sex)

    @classmethod
    def ssn_constructor(cls, ssn):
        front, back = ssn.split('-')
        sex = back[0]

        if sex == '1' or sex == '2':
            year = '19' + front[:2]
        else:
            year = '20' + front[:2]

        if (int(sex) % 2) == 0:
            sex = '여성'
        else: 
            sex = '남성'

        month = front[2:4]
        day = front[4:6]

        return cls(year, month, day, sex)

ssn_1 = '900829-1034356'
ssn_2 = '051224-4061569'

person_1 = Person.ssn_constructor(ssn_1)
print(person_1)

person_2 = Person.ssn_constructor(ssn_2)
print(person_2)


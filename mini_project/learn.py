
class Person:

    def __init__(factors, name, color, age, sex):

        factors.name = name
        factors.sex = sex
        factors.age = age
        factors.color = color

    def __str__(factors):
        return f'{factors.name}, {factors.color}, {factors.age}, {factors.sex}'

    def cus_name(info):
        print('customer details are' + info.name + info.color + str(info.age))

print(Person('Akin', 'fair', 31, 'male'))


Person('Akin', 'fair', 31, 'male').cus_name()








# 考虑 Student 对象
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


# 建立一组Student对象
students = [
    Student('jane', 'B', 12),
    Student('john', 'A', 12),
    Student('dave', 'B', 10),
]




from operator import itemgetter, attrgetter

# 对students按照年龄排序
print(sorted(students, key=attrgetter('age')))
# 其等价于
print(sorted(students, key=lambda o: o.age))
# 输出: >>> [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# 亦可以按多个key排序, 先按age再按grade排序
print(sorted(students, key=attrgetter('age', 'grade')))
# 输出: >>> [('dave', 'B', 10), ('john', 'A', 12), ('jane', 'B', 12)]


data = list(*map(itemgetter("id", 'name'), [{'id': "121212", "name": "121fafdasd"}]))
print(data)
keys = {"name": "1212"}.keys()
print(keys)

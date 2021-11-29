class Student:
    # name = 'Backbull'
    group_name = 'SCA20'
    is_tired = True

    def __init__(self, new_name):
        print('Object initialized')
        self.name = new_name

    def print_my_name(self):
        print()
        

    def calculate(self, num, num1):
        return num + num1 

obj1 = Student('Backbull')
obj1.print_my_name()
# print('Name:', obj1.name)
# obj1.name = "Shukur"
# print('Name:', obj1.name)
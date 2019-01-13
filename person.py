class gender:
    name = "null"
    def __init__(self,name):
        self.name = name

male = gender('male')
female = gender('female')


class person:
    name = "null"
    age = -1
    country = "null"
    money = -1
    gender = 0


    def __init__(self,name,gender,age):
        self.name = name
        self.age = age
        self.gender = gender
    

    
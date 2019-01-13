class gender:
    name = "null"
    def __init__(self,name):
        self.name = name

class country:
    def __init__(self,name,code):
        self.name = name
        self.code = code

class family:
  
    def __init__(self,name,culture, founders):
        self.name = name
        self.culture = culture
        self.MemberList = founders

    def addMember(self,person):
        self.MemberList.append(person)
    
    def removeMember(self,person):
        self.MemberList.remove(person)
    def getName(self):
        return str(self.name)

    


male = gender('male')
female = gender('female')


class person:

    emailAccount = ('email@address.com','12345')
    #photoFile = Null



    def __init__(self,name,gender,age, country):
        self.name = name
        self.age = age
        self.gender = gender
        self.county = country

    def getName(self):
        return str(self.name)
    
    

    
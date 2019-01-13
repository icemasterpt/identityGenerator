import identityGenerator
import dbmanager
from person import gender
male = gender('male')
female = gender('female')

def main():
    #create sample person.
    print("Generating a family...")
    person1 = identityGenerator.generatePerson()
    person2 = identityGenerator.generatePerson(female)
    family1 = identityGenerator.generateFamily("en",[person1,person2])
    print("Family " + str(family1.getName()) + " generated with members:\n")
    print("Male founder: "+ str(family1.MemberList[0].getName()) + "\n")
    print("Female founder: "+ str(family1.MemberList[1].getName()) + "\n")
    print("adding new member to family "+ family1.getName()+ "\n")
    person3 = identityGenerator.generatePerson()
    family1.addMember(person3)
    print("added new member with name "+person3.name)

dbmanager.wipeAllPeoplebyGender(1)
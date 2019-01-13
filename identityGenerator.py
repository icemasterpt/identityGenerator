
from person import *

import dbmanager
import config

#first thing: are we using a local db?
isLocal = config.uselocalDB



def db_getCountry(country = 'random'):
    if country == 'random':
        #get random country from DB
        connect = dbmanager.db_connect()
        cursor = connect.cursor()
        res = cursor.execute('SELECT name FROM ' + config.db_countries + ' ORDER BY RANDOM() LIMIT 1')
        
        #print('log: getting ' +str(res.fetchone()) + ' from db')
        connect.close()
        return str(res.fetchone())
    else:
        #get specific country from DB
        connect = dbmanager.db_connect()
        cursor = connect.cursor()
        res = cursor.execute('SELECT name FROM ' + config.db_countries + ' WHERE textIndex = "'+country+'" ORDER BY RANDOM() LIMIT 1') 

        s = res.fetchone()
        countryName = tuple(s)
        #print('log: getting ' +str(res.fetchone()) + ' from db')
        connect.close()
        return countryName[0]

def db_getMaleName(culture = 'en'):
        connect = dbmanager.db_connect()
        cursor = connect.cursor()
        res = cursor.execute('SELECT name FROM ' + config.db_nameTable + ' WHERE culturecode = "'+culture+'" ORDER BY RANDOM() LIMIT 1')

        s = res.fetchone()
        finalName = tuple(s)
        
        return finalName[0]


def db_getFemaleName(culture = 'en'):
        connect = dbmanager.db_connect()
        cursor = connect.cursor()
        res = cursor.execute('SELECT name FROM ' + config.db_nameTableFemale + ' WHERE culturecode = "'+culture+'" ORDER BY RANDOM() LIMIT 1')

        s = res.fetchone()
        finalName = tuple(s)
        
        return finalName[0]

def db_getFamilyName(culture = 'en'):
        connect = dbmanager.db_connect()
        cursor = connect.cursor()
        res = cursor.execute('SELECT name FROM ' + config.db_lastname + ' WHERE culturecode = "'+culture+'" ORDER BY RANDOM() LIMIT 1')

        s = res.fetchone()
        finalName = tuple(s)
        
        return finalName[0]

#GENERATORS!!!!


def generatePerson(gender = male, age = 18 , culture = "en"):
    name = "null"
    if gender == male:
        name = db_getMaleName(culture)
    else:
        name = db_getFemaleName(culture)
    pessoa = person(name,gender,age,country)
    return pessoa




adam = generatePerson()
eve = generatePerson(female,16)




def generateFamily(culture = "en", founders = [adam,eve]):
    fam = family(db_getFamilyName(culture), culture,founders)
    return fam

    

#for testing purposes

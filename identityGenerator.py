
from person import *

import dbmanager
import config

#first thing: are we using a local db?
isLocal = config.uselocalDB

def generatePerson(gender = male, age = 18 ):
    pass

def db_getCountry(country = 'random'):
    if country == 'random':
        #get random country from DB
        connect = dbmanager.db_connect()
        cursor = connect.cursor()
        res = cursor.execute('SELECT name FROM ' + config.db_countries + ' ORDER BY RANDOM() LIMIT 1')
        
        #print('log: getting ' +str(res.fetchone()) + ' from db')
        return str(res.fetchone())
    else:
        #get specific country from DB
        pass


a = db_getCountry()
print(a)
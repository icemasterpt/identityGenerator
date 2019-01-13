import sqlite3
import config




def db_connect(isLocal = True):
    if isLocal:
        return sqlite3.connect(config.localdb_filename)
    else:
        print 'remote mysql is still not implemented!'


def wipeAllPeoplebyGender(genderInt,isLocal = True ):
    #genderINT 0 male , 1 female
    if isLocal:
        conn = db_connect()
        sql = 'DELETE FROM '+config.db_person
        cur = conn.cursor()
        cur.execute(sql)
    else:
        pass
        


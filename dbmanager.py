import sqlite3
import config




def db_connect(isLocal = True):
    if isLocal:
        return sqlite3.connect(config.localdb_filename)
    else:
        print 'remote mysql is still not implemented!'



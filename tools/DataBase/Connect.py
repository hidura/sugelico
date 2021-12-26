'''
Created on Jun 23, 2013

@author: hidura
'''

from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from mongoengine import connect


class conection:
    def conORM(self):
        return create_engine("postgresql+pypostgresql://username:password"
                             "@hostname:portname/dbname",poolclass=NullPool)


    def conODM(self):

        return connect(db='dbname', alias='default', username='username',
                       password='password', port=port, host='hostname')



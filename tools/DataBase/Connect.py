'''
Created on Jun 23, 2013

@author: hidura
'''

from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from mongoengine import connect


class conection:
    def conORM(self):
        return create_engine("postgresql+pypostgresql://sugelico:vgi3se1fq7k4fhox"
                             "@web1-bmsuiteio-do-user-4013959-0.db.ondigitalocean.com:25060/sugelico?sslmode=require",poolclass=NullPool)


    def conODM(self):

        return connect(db='sugelico_erp_test', alias='default', username='sugelico',
                       password='#GbUsa1776@', port=29642, host='209.97.153.183')



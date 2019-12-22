#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from sqlalchemy import Column, BIGINT, ForeignKey, Text, String, Time, DECIMAL, MetaData, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.sqltypes import BOOLEAN

from tools.DataBase.Definition.Base import Base
from tools.DataBase.Definition.Status import Status

from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Type import Type


class User(Base):
    """This is the base class of the users in the system
    here the system store all the users, without discrimination,
    if is an user client or an user of a commerce, will be determine
    by the column usrtype, that is connected to the type table."""
    __tablename__="user_reg"
    __table_args__ = {"useexisting": True}

    id = Column("id",BIGINT, primary_key=True)
    username = Column("username",Text)
    passwd = Column("passwd",Text)
    status = Column("status",BIGINT, ForeignKey(Status.code), nullable=False, default=12)
    #client or a company or user-company.
    code = Column("code", BIGINT, unique=True)
    avatar = Column("avatar", Text, nullable=True)
    contact = Column('contact', BIGINT, nullable=True)
    usrtype = Column('usrtype', BIGINT, nullable=True)
    branch = Column('branch', BIGINT, nullable=True)
    owner = Column('owner', BOOLEAN, nullable=True, default=False)


    #Relationship
    sta_user_rel = relationship(Status,  backref=backref("User"))



    metadata = MetaData()


    user_tbl = Table(__tablename__, metadata,id,username, passwd,
                     status,code, avatar, contact, usrtype, owner,branch)

    def __repr__(self):
        return "<User (id='%s', username='%s', passwd='%s', " \
               "status='%s',code='%s'" \
               "avatar='%s', contact='%s', usrtype='%s', owner='%s', branch='%s')>"%(self.id, self.username,
        self.passwd, self.status,
        self.code,self.avatar, self.contact, self.usrtype, self.owner,self.branch)


    def __Publish__(self):
        data={}
        for column in self.__table__.columns.keys():
            value=self.__dict__[self.__table__.columns[column].name]
            if self.__table__.columns[column].type =="BIGINT":
                data[self.__table__.columns[column].name]=int(value)
            elif self.__table__.columns[column].type =="Integer":
                data[self.__table__.columns[column].name]=int(value)

            elif self.__table__.columns[column].type=="NUMERIC":
                data[self.__table__.columns[column].name] = float(value)
            elif self.__table__.columns[column].type=="Decimal":
                data[self.__table__.columns[column].name] = float(value)

            elif self.__table__.columns[column].type=="time":
                data[self.__table__.columns[column].name] = str(value.strftime('%H:%M:%S'))
            elif self.__table__.columns[column].type=="datetime":
                data[self.__table__.columns[column].name] = str(value.strftime('%H:%M:%S'))
            else:
                data[self.__table__.columns[column].name] = str(value)
        return data

if __name__ == '__main__':
    User()

__author__ = 'hidura'

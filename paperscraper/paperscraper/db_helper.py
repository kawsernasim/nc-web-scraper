import sqlalchemy
from sqlalchemy import Table, Column, Integer, Unicode, MetaData, create_engine, UnicodeText
from sqlalchemy.exc import IntegrityError, InvalidRequestError, NoSuchTableError, ArgumentError
from sqlalchemy.orm import mapper, create_session, clear_mappers
from sqlalchemy.ext.declarative import declarative_base
import datetime
import logging



class Word(object):
    def __getitem__(self, item): 
            return getattr(self, item)
    def __setitem__(self, item, value):
        return setattr(self, item, value)


class DBHelper():
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:Armstrong785!@localhost:5432/paper_scraper_db')
        self.meta = MetaData()
        self.meta.reflect(bind=self.engine)
        self.session = create_session(bind=self.engine, autocommit=False, autoflush=True)
        try:
            self.table = Table('scraped_data_master', self.meta, autoload=True, autoload_with=self.engine)
            mapper(Word, self.table)
        except NoSuchTableError:
            pass
        except ArgumentError:
            self.table = Table('scraped_data_master', self.meta, autoload=True, autoload_with=self.engine)
            mapper(Word, self.table, non_primary=True)
    
    def __del__(self):
        self.session.commit()

    def create_table(self, columns):
        try:
            self.table = Table('scraped_data_master', self.meta,
                Column('id', Unicode(255), primary_key = True),
                Column('board', Unicode(255)),
                Column('qualification', Unicode(255)),
                Column('subject', Unicode(255)),
                Column('year', Unicode(255)),
                Column('session', Unicode(255)),
                Column('paper_type', Unicode(255)),
                Column('link', Unicode(255)),          
            )

            self.meta.create_all(self.engine)
            mapper(Word, self.table)
        except InvalidRequestError:
            pass
    
    def add_paper(self, id, board, qualification, subject, year, session, paper_type, link):
        try:
            w = Word()
            w.id = id
            w.board = board
            w.qualification = qualification
            w.subject = subject
            w.year = year
            w.session = session
            w.paper_type = paper_type
            w.link = link

            self.session.add(w)
            self.session.commit()
            return True
        except IntegrityError:
            self.session.rollback()
            return False
    
    
    def commit(self):
        clear_mappers()
        self.session.close()
        self.session.commit()




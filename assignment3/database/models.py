import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()

class Links(DeclarativeBase):
    __tablename__ = "urls"
    
    url = Column('url', String, primary_key=True)
    protocol = Column('protocol', String)
    domain = Column('domain', String)
    path = Column('path', String)
    page = Column('page', String)
    get_params = Column('get_params', String)
    scrape_date = Column('scrape_date', DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return "<URL ({})>".format(self.url)

class Forms(DeclarativeBase):
    __tablename__ = "forms"

    url = Column('url', String, primary_key=True)
    id_attr = Column('id_attr', String, primary_key=True)
    scrape_date = Column('scrape_date', DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return "<URL ({})>    <ID ({})>".format(self.url, self.id_attr)

class Inputs(DeclarativeBase):
    __tablename__ = "inputs"

    # ID to uniquely identify inputs. Generated by database
    input_id = Column('input_id', Integer, primary_key=True)
    url = Column('url', Integer)
    form_id = Column('form_id', String)
    complete = Column('complete', String)
    type_attr = Column('type_attr', String)
    scrape_date = Column('scrape_date', DateTime, default=datetime.datetime.now)
    # Foreign keys to associate input and form
    ForeignKeyConstraint(['url', 'form_id'], ['forms.url', 'forms.id_attr'])

    def __repr__(self):
        return "<Complete Input ({})>".format(self.complete)

class Vulnerabilities(DeclarativeBase):
    __tablename__ = "vulnerabilities"
    
    url = Column('url', String, primary_key=True)
    vulnerability_type = Column('vulnerability_type', String, primary_key=True)
    value = Column('value', String)
    scan_date = Column('scan_date', DateTime, default=datetime.datetime.now)

    # def __repr__(self):
    #     return "<Vulnerability ({})>".format(self.url)